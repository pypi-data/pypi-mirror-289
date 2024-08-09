# adpated from https://github.com/huggingface/diffusers/blob/v0.27.2/src/diffusers/schedulers/scheduling_ddpm.py

import torch
from typing import Union, Tuple, Optional
from diffusers.schedulers.scheduling_ddpm import (
    DDPMScheduler, 
    DDPMSchedulerOutput,
)

from pipefuser.utils import DistriConfig
from pipefuser.logger import init_logger

logger = init_logger(__name__)
class DDPMSchedulerPiP(DDPMScheduler):
    def init(self, distri_config: DistriConfig):
        self.distri_config = distri_config

    def step(
        self,
        *args,
        **kwargs
    ) -> Union[DDPMSchedulerOutput, Tuple]:
        batch_idx = kwargs.pop("batch_idx", None)
        return super().step(*args, **kwargs)