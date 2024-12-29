# Copyright (c) 2022-2024, The ORBIT Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

"""Common functions that can be used to enable different randomizations.

Randomization includes anything related to altering the simulation state. This includes changing the physics
materials, applying external forces, and resetting the state of the asset.

The functions can be passed to the :class:`omni.isaac.lab.managers.RandomizationTermCfg` object to enable
the randomization introduced by the function.
"""

from __future__ import annotations
import os

import torch
from typing import TYPE_CHECKING

from omni.isaac.lab.assets import Articulation, RigidObject
from omni.isaac.lab.managers import SceneEntityCfg
from omni.isaac.lab.utils.math import quat_from_euler_xyz, sample_uniform
from omni.isaac.lab_tasks.manager_based.manipulation.lift import DEFAULT_QPOS_7DIM, CollectEpsBuf, HisQposBuf
from VFCNet.yolo_process_data import YoloCollectData
# import source/extensions/omni.isaac.lab_tasks/omni/isaac/orbit_tasks/utils
from omni.isaac.lab_tasks.utils.data_collector.cobot_data_collect import save_data, push_tensor_obs_action_to_buf, \
    save_data_v4
from omni.isaac.lab_tasks.manager_based.manipulation.lift import object_pos, apple_to_tablecloth_height_diff


from collections import deque
import argparse
import statistics
import random


if TYPE_CHECKING:
    from omni.isaac.lab.envs import ManagerBasedRLEnv
    
def reset_root_state_uniform_object_over_platform(
    env: ManagerBasedRLEnv,
    env_ids: torch.Tensor,
    pose_range: dict[str, tuple[float, float]],
    velocity_range: dict[str, tuple[float, float]],
    asset_cfg: SceneEntityCfg = SceneEntityCfg("object"),
):
    """Reset the asset root state to a random position and velocity uniformly within the given ranges.

    This function randomizes the root position and velocity of the asset.

    * It samples the root position from the given ranges and adds them to the default root position, before setting
      them into the physics simulation.
    * It samples the root orientation from the given ranges and sets them into the physics simulation.
    * It samples the root velocity from the given ranges and sets them into the physics simulation.

    The function takes a dictionary of position and velocity ranges for each axis and rotation. The keys of the
    dictionary are ``x``, ``y``, ``z``, ``roll``, ``pitch``, and ``yaw``. The values are tuples of the form
    ``(min, max)``. If the dictionary does not contain a key, the position or velocity is set to zero for that axis.
    """
    # extract the used quantities (to enable type-hinting)
    asset: RigidObject | Articulation = env.scene[asset_cfg.name]
    # get default root state
    root_states = asset.data.default_root_state[env_ids].clone()

    # positions
    pos_offset = torch.zeros_like(root_states[:, 0:3])
    # modify the z position to be above the platform
    platform: RigidObject | Articulation = env.scene["platform"]
    init_object_z = platform.data.root_pos_w[env_ids, 2] + apple_to_tablecloth_height_diff
    platform_xy = platform.data.root_pos_w[env_ids, 0:2]
    
    pos_offset[:, 0].uniform_(*pose_range.get("x", (0.0, 0.0)))
    pos_offset[:, 1].uniform_(*pose_range.get("y", (0.0, 0.0)))
    pos_offset[:, 2].uniform_(*pose_range.get("z", (0.0, 0.0)))
    
    positions = root_states[:, 0:3] + env.scene.env_origins[env_ids] + pos_offset
    # object is above the platform
    positions[:, 0:2] = platform_xy + pos_offset[:, 0:2]  
    # platform_xy already contains env.scene.env_origins[env_ids, 0:2]
    positions[:, 2] = init_object_z + env.scene.env_origins[env_ids, 2] + pos_offset[:, 2]
    # set the z position to be above the platform
    
    # orientations
    euler_angles = torch.zeros_like(positions)
    euler_angles[:, 0].uniform_(*pose_range.get("roll", (0.0, 0.0)))
    euler_angles[:, 1].uniform_(*pose_range.get("pitch", (0.0, 0.0)))
    euler_angles[:, 2].uniform_(*pose_range.get("yaw", (0.0, 0.0)))
    orientations = quat_from_euler_xyz(euler_angles[:, 0], euler_angles[:, 1], euler_angles[:, 2])
    # velocities
    velocities = root_states[:, 7:13]
    velocities[:, 0].uniform_(*velocity_range.get("x", (0.0, 0.0)))
    velocities[:, 1].uniform_(*velocity_range.get("y", (0.0, 0.0)))
    velocities[:, 2].uniform_(*velocity_range.get("z", (0.0, 0.0)))
    velocities[:, 3].uniform_(*velocity_range.get("roll", (0.0, 0.0)))
    velocities[:, 4].uniform_(*velocity_range.get("pitch", (0.0, 0.0)))
    velocities[:, 5].uniform_(*velocity_range.get("yaw", (0.0, 0.0)))

    # print object debug info
    # if asset_cfg.name == "object":
    #     print(f"asset_name: {asset_cfg.name}, positions: {positions}, orientations: {orientations}, velocities: {velocities}, root_states: {root_states}, pos_offset: {pos_offset}, euler_angles: {euler_angles}, pose_range: {pose_range}")
    
    # set into the physics simulation
    asset.write_root_pose_to_sim(torch.cat([positions, orientations], dim=-1), env_ids=env_ids)
    asset.write_root_velocity_to_sim(velocities, env_ids=env_ids)


def reset_pose_uniform(
    env: ManagerBasedRLEnv,
    env_ids: torch.Tensor,
    pose_range: dict[str, tuple[float, float]],
    asset_cfg: SceneEntityCfg = SceneEntityCfg("platform"),
):
    """Reset the asset root state to a random position and velocity uniformly within the given ranges.
    This function randomizes the root position and velocity of the asset.
    * It samples the root position from the given ranges and adds them to the default root position, before setting
      them into the physics simulation.
    * It samples the root orientation from the given ranges and sets them into the physics simulation.
    * It samples the root velocity from the given ranges and sets them into the physics simulation.
    The function takes a dictionary of position and velocity ranges for each axis and rotation. The keys of the
    dictionary are ``x``, ``y``, ``z``, ``roll``, ``pitch``, and ``yaw``. The values are tuples of the form
    ``(min, max)``. If the dictionary does not contain a key, the position or velocity is set to zero for that axis.
    """
    # extract the used quantities (to enable type-hinting)
    asset: RigidObject | Articulation = env.scene[asset_cfg.name]
    # get default root state
    root_states = asset.data.default_root_state[env_ids].clone()

    # import pdb;pdb.set_trace()

    # positions
    pos_offset = torch.zeros_like(root_states[:, 0:3])
    pos_offset[:, 0].uniform_(*pose_range.get("x", (0.0, 0.0)))
    pos_offset[:, 1].uniform_(*pose_range.get("y", (0.0, 0.0)))
    pos_offset[:, 2].uniform_(*pose_range.get("z", (0.0, 0.0)))
    positions = root_states[:, 0:3] + env.scene.env_origins[env_ids] + pos_offset

    # orientations
    orientations = root_states[:, 3:7].clone()

    # euler_angles = torch.zeros_like(positions)
    # euler_angles[:, 0].uniform_(*height_range.get("roll", (0.0, 0.0)))
    # euler_angles[:, 1].uniform_(*height_range.get("pitch", (0.0, 0.0)))
    # euler_angles[:, 2].uniform_(*height_range.get("yaw", (0.0, 0.0)))
    # orientations = quat_from_euler_xyz(euler_angles[:, 0], euler_angles[:, 1], euler_angles[:, 2])

    # set into the physics simulation
    asset.write_root_pose_to_sim(torch.cat([positions, orientations], dim=-1), env_ids=env_ids)


def reset_joints_by_offset_with_probability(
    env: ManagerBasedRLEnv,
    env_ids: torch.Tensor,
    position_range: tuple[float, float],
    velocity_range: tuple[float, float],
    asset_cfg: SceneEntityCfg = SceneEntityCfg("robot"),
):
    """Reset the robot joints with offsets around the default position and velocity by the given ranges.

    This function samples random values from the given ranges and biases the default joint positions and velocities
    by these values. The biased values are then set into the physics simulation.
    TODO: both in reset_scene_to_default() and reset_joints_by_offset(), robot is reset to default state 
    """
    #  each env in env_ids will be skipped with 50% probability
    # skipper = torch.rand(env_ids.shape[0], device=env_ids.device) < 0.5
    # env_ids = env_ids[skipper]
    
    # extract the used quantities (to enable type-hinting)
    asset: Articulation = env.scene[asset_cfg.name]

    # get default joint state
    joint_pos = asset.data.default_joint_pos[env_ids].clone()
    joint_vel = asset.data.default_joint_vel[env_ids].clone()
    # bias these values randomly
    joint_pos += sample_uniform(*position_range, joint_pos.shape, joint_pos.device)
    joint_vel += sample_uniform(*velocity_range, joint_vel.shape, joint_vel.device)
    # clamp joint pos to limits
    joint_pos_limits = asset.data.soft_joint_pos_limits[env_ids]
    joint_pos = joint_pos.clamp_(joint_pos_limits[..., 0], joint_pos_limits[..., 1])

    # set into the physics simulation
    asset.write_joint_state_to_sim(joint_pos, joint_vel, env_ids=env_ids)


def reset_history_qpos_buf(env: ManagerBasedRLEnv, env_ids: torch.Tensor):
    if HisQposBuf.data == None:
        HisQposBuf.data = DEFAULT_QPOS_7DIM.repeat(env_ids.shape[0], 1)
        # we will not modify data
    else:
        HisQposBuf.data[env_ids] = DEFAULT_QPOS_7DIM
            