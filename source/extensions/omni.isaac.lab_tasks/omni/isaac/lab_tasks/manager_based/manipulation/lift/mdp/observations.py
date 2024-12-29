# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.

# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

import torch
from typing import TYPE_CHECKING

from omni.isaac.lab.assets import RigidObject
from omni.isaac.lab.managers import SceneEntityCfg
from omni.isaac.lab.utils.math import subtract_frame_transforms
from omni.isaac.lab.sensors import Camera

if TYPE_CHECKING:
    from omni.isaac.lab.envs import ManagerBasedRLEnv


def object_position_in_robot_root_frame(
    env: ManagerBasedRLEnv,
    robot_cfg: SceneEntityCfg = SceneEntityCfg("robot"),
    object_cfg: SceneEntityCfg = SceneEntityCfg("object"),
) -> torch.Tensor:
    """The position of the object in the robot's root frame."""
    robot: RigidObject = env.scene[robot_cfg.name]
    object: RigidObject = env.scene[object_cfg.name]
    object_pos_w = object.data.root_pos_w
    object_quat_w = object.data.root_quat_w
    object_pos_b, object_quat_b = subtract_frame_transforms(
        robot.data.root_state_w[:, :3], robot.data.root_state_w[:, 3:7], object_pos_w, object_quat_w
    )
    return torch.cat([object_pos_b, object_quat_b], dim=-1)


def object_target_position_in_robot_root_frame(
    env: ManagerBasedRLEnv,
    robot_cfg: SceneEntityCfg = SceneEntityCfg("robot"),
) -> torch.Tensor:
    if hasattr(env, "extras"):
        robot: RigidObject = env.scene[robot_cfg.name]
        object_pos_w = env.extras["object_target_position"]
        object_pos_b, object_quat_b = subtract_frame_transforms(
            robot.data.root_state_w[:, :3], robot.data.root_state_w[:, 3:7], object_pos_w
        )
        return torch.cat([object_pos_b, object_quat_b], dim=-1)
    return torch.zeros((env.num_envs, 7), device=env.device)
