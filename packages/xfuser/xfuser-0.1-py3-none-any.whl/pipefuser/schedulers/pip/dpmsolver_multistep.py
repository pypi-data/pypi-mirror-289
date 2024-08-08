# adpated from https://github.com/huggingface/diffusers/blob/v0.27.2/src/diffusers/schedulers/scheduling_dpmsolver_multistep.py

import torch
from typing import Union, Tuple, Optional
from diffusers.schedulers.scheduling_dpmsolver_multistep import (
    DPMSolverMultistepScheduler,
    SchedulerOutput,
)

from pipefuser.utils import DistriConfig
from pipefuser.logger import init_logger

logger = init_logger(__name__)


class DPMSolverMultistepSchedulerPiP(DPMSolverMultistepScheduler):
    def init(self, distri_config: DistriConfig):
        self.distri_config = distri_config

    def step(
        self,
        model_output: torch.FloatTensor,
        timestep: int,
        sample: torch.FloatTensor,
        generator=None,
        variance_noise: Optional[torch.FloatTensor] = None,
        return_dict: bool = True,
        batch_idx: Union[int] = None,
    ) -> Union[SchedulerOutput, Tuple]:
        distri_config = self.distri_config

        if self.num_inference_steps is None:
            raise ValueError(
                "Number of inference steps is 'None', you need to run 'set_timesteps' after creating the scheduler"
            )

        if self.step_index is None:
            self._init_step_index(timestep)

        # Improve numerical stability for small number of steps
        lower_order_final = (self.step_index == len(self.timesteps) - 1) and (
            self.config.euler_at_final
            or (self.config.lower_order_final and len(self.timesteps) < 15)
            or self.config.final_sigmas_type == "zero"
        )
        lower_order_second = (
            (self.step_index == len(self.timesteps) - 2)
            and self.config.lower_order_final
            and len(self.timesteps) < 15
        )

        model_output = self.convert_model_output(model_output, sample=sample)
        if batch_idx is None or batch_idx == 0:
            for i in range(self.config.solver_order - 1):
                self.model_outputs[i] = self.model_outputs[i + 1]

        _, _, c, _ = model_output.shape

        if batch_idx == 0:
            assert len(self.model_outputs) >= 2
            self.model_outputs[-1] = torch.zeros_like(self.model_outputs[-2])
        if batch_idx is not None:
            self.model_outputs[-1][
                :, :, c * batch_idx : c * (batch_idx + 1), :
            ] = model_output
        else:
            self.model_outputs[-1] = model_output

        # Upcast to avoid precision issues when computing prev_sample
        sample = sample.to(torch.float32)
        if (
            self.config.algorithm_type in ["sde-dpmsolver", "sde-dpmsolver++"]
            and variance_noise is None
        ):
            noise = randn_tensor(
                model_output.shape,
                generator=generator,
                device=model_output.device,
                dtype=torch.float32,
            )
        elif self.config.algorithm_type in ["sde-dpmsolver", "sde-dpmsolver++"]:
            noise = variance_noise.to(device=model_output.device, dtype=torch.float32)
        else:
            noise = None

        # logger.info(f"batch_idx {batch_idx}")

        if batch_idx is not None:
            model_outputs = []
            for output in self.model_outputs:
                model_outputs.append(
                    output[:, :, c * batch_idx : c * (batch_idx + 1), :]
                )
        else:
            model_outputs = self.model_outputs

        if (
            self.config.solver_order == 1
            or self.lower_order_nums < 1
            or lower_order_final
        ):
            prev_sample = self.dpm_solver_first_order_update(
                model_output, sample=sample, noise=noise
            )
        elif (
            self.config.solver_order == 2
            or self.lower_order_nums < 2
            or lower_order_second
        ):
            prev_sample = self.multistep_dpm_solver_second_order_update(
                model_outputs, sample=sample, noise=noise
            )
        else:
            prev_sample = self.multistep_dpm_solver_third_order_update(
                model_outputs, sample=sample
            )

        if self.lower_order_nums < self.config.solver_order:
            self.lower_order_nums += 1

        # Cast sample back to expected dtype
        prev_sample = prev_sample.to(model_output.dtype)

        # upon completion increase step index by one
        if batch_idx is None or batch_idx == distri_config.pp_num_patch - 1:
            self._step_index += 1

        if not return_dict:
            return (prev_sample,)

        return SchedulerOutput(prev_sample=prev_sample)
