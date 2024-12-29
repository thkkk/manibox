# Copyright (c) 2022-2024, The ORBIT Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Common functions that can be used to activate certain terminations.

The functions can be passed to the :class:`omni.isaac.lab.managers.TerminationTermCfg` object to enable
the termination introduced by the function.
"""

from __future__ import annotations

import torch
import numpy as np
from typing import TYPE_CHECKING

from omni.isaac.lab.assets import Articulation, RigidObject
from omni.isaac.lab.managers import SceneEntityCfg
from omni.isaac.lab.sensors import ContactSensor
from omni.isaac.lab_tasks.manager_based.manipulation.lift import HisQposBuf, ObjectHisPosBuf, CollectEpsBuf
from omni.isaac.lab_tasks.utils.data_collector.cobot_data_collect import project_to_rotation, push_tensor_obs_action_to_buf, \
    transfer_sim_image_to_standard_img_tensor

if TYPE_CHECKING:
    from omni.isaac.lab.envs import ManagerBasedRLEnv
    from omni.isaac.lab.managers.command_manager import CommandTerm

from VFCNet.yolo_process_data import YoloCollectData

import dm_env

"""
MDP terminations.
"""


def state_out_of_bound(env: ManagerBasedRLEnv, lower_bounds: float, upper_bounds: float) -> torch.Tensor:
    """Terminate the episode when the state is outside of the specified bounds."""
    state: torch.Tensor = env.observation_manager.compute()["policy"]
    return torch.any(
        torch.logical_or(state  < lower_bounds, state > upper_bounds),
        dim=1,
    )


def qpos_changes_too_much(env: ManagerBasedRLEnv, max_change: torch.Tensor) -> torch.Tensor:
    """Terminate the episode when the qpos changes too much. abs(qpos - last_qpos) must <= max_change
    """
    obs_tensor: torch.Tensor = env.observation_manager.compute()["policy"]
    
    qpos = obs_tensor[:, 3:9]  # left arm
    left_gripper_qpos = obs_tensor[:, 9:11]
    
    # left_gripper_qpos_mean: (num_envs, 1)
    left_gripper_qpos_mean = project_to_rotation(torch.mean(left_gripper_qpos, dim=1, keepdim=True))
    # concat left gripper
    qpos = torch.cat([qpos, left_gripper_qpos_mean], dim=-1)    # concat left gripper
    
    if HisQposBuf.data == None:
        # HisQposBuf.data = torch.zeros_like(qpos, device=qpos.device)  # TODO: default
        HisQposBuf.data = qpos
        return torch.zeros(qpos.shape[0], device=env.device, dtype=torch.bool)
    
    # last_qpos: qpos in the last step
    last_qpos = HisQposBuf.data
    # for env i, not termination requires abs(qpos[i] - last_qpos[i]) must <= max_change or len <= 2
    result = torch.logical_or(
        torch.all(torch.abs(qpos - last_qpos) <= max_change, dim=1),
        env.episode_length_buf <= 4
    )
    result = ~result
    HisQposBuf.data = qpos
    return result
