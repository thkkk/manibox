# def object_is_lifted(
#     env: ManagerBasedRLEnv, minimal_height: float, object_cfg: SceneEntityCfg = SceneEntityCfg("object")
# ) -> torch.Tensor:
#     """Reward the agent for lifting the object above the minimal height."""
#     object: RigidObject = env.scene[object_cfg.name]
#     return torch.where(object.data.root_pos_w[:, 2] > minimal_height, 1.0, 0.0)
# Copyright (c) 2022-2024, The ORBIT Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

import torch
from typing import TYPE_CHECKING

from omni.isaac.lab.assets import RigidObject
from omni.isaac.lab.managers import SceneEntityCfg
from omni.isaac.lab.sensors import FrameTransformer
from omni.isaac.lab.utils.math import combine_frame_transforms, quat_apply, quat_inv
from omni.isaac.lab.sensors.contact_sensor import ContactSensor, ContactSensorCfg
from omni.isaac.lab.assets import Articulation, RigidObject
from omni.isaac.lab_tasks.manager_based.manipulation.lift import ObjectHisPosBuf, LiftTgtObjects, ObjectChoice
from omni.isaac.lab.markers import VisualizationMarkers, VisualizationMarkersCfg
import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab_tasks.manager_based.manipulation.lift import object_pos, apple_to_tablecloth_height_diff

from collections import deque

if TYPE_CHECKING:
    from omni.isaac.lab.envs import ManagerBasedRLEnv

min_height = None
def object_is_lifted(
    env: ManagerBasedRLEnv, minimal_height: float, object_cfg: SceneEntityCfg = SceneEntityCfg("object")
) -> torch.Tensor:
    """Reward the agent for lifting the object above the minimal height."""
    object: RigidObject = env.scene[object_cfg.name]
    # print(f"object height: {object.data.root_pos_w[:, 2]}") # 0.82
    
    platform: RigidObject | Articulation = env.scene["platform"]
    init_object_z = platform.data.root_pos_w[:, 2] + apple_to_tablecloth_height_diff
    # print("platform height", platform.data.root_pos_w[:, 2])
    
    # global min_height
    # if min_height is None:
    #     min_height = object.data.root_pos_w[:, 2]
    # else:
    #     min_height = torch.min(min_height, object.data.root_pos_w[:, 2])
    # print(min_height, object.data.root_state_w[:, 2])
    # return (torch.clamp(object.data.root_pos_w[:, 2] - (init_object_z + minimal_height), 0.0, 0.2) / 0.2 + 1) *\
    #     (object.data.root_pos_w[:, 2] > (init_object_z + minimal_height))
    object_over_init_height = object.data.root_pos_w[:, 2] - init_object_z
    # init_object_z = platform + 0.307 (actually it is 0.3047~0.3065) 

    object_drop_penalty = (object_over_init_height < -minimal_height) * \
        (torch.clamp(object_over_init_height, -1.0, 0.0) * 2.5)
    object_fly_penalty = (object_over_init_height > 0.5) * (-2.5)
    return (torch.clamp(object_over_init_height -  minimal_height, 0.0, 0.2) / 0.2 + 1) *\
        (object_over_init_height > minimal_height) + object_drop_penalty + object_fly_penalty


def ee_is_lifted(
    env: ManagerBasedRLEnv, ee_frame_cfg: SceneEntityCfg = SceneEntityCfg("ee_frame")
) -> torch.Tensor:
    ee_frame: FrameTransformer = env.scene[ee_frame_cfg.name]
    ee_w = ee_frame.data.target_pos_w[..., 0, :]
    return torch.clamp(ee_w[:, 2] - 0.6, 0.0, 0.3) / 0.3 * (grasp_force(env) > 0.5)

def object_lift_continuous_his_diff(
    env: ManagerBasedRLEnv, 
    valid_maximal_distance: float,
    object_cfg: SceneEntityCfg = SceneEntityCfg("object"),
    ee_frame_cfg: SceneEntityCfg = SceneEntityCfg("ee_frame"),
) -> torch.Tensor:
    '''deprecated'''
    
    # get history
    his_pos_deque: deque = ObjectHisPosBuf.data
    
    # Env episode length
    # eplen = env.episode_length_buf
    
    ee_frame: FrameTransformer = env.scene[ee_frame_cfg.name]
    # End-effector position: (num_envs, 3)
    ee_w = ee_frame.data.target_pos_w[..., 0, :]
    
    object: RigidObject = env.scene[object_cfg.name]
    # Target object position: (num_envs, 3)
    object_pos_w = object.data.root_pos_w
    # object_default_pos_w = object.data.default_root_state
    
    # distance between end-effector and object
    distance: torch.Tensor = torch.norm(object_pos_w - ee_w, dim=1)
    
    if len(his_pos_deque) < 1:
        lift_continuous_rew = torch.zeros(env.num_envs, device=env.device)
    else:
        last_object_pow_w = his_pos_deque[-1]
        lift_continuous_rew = (distance < valid_maximal_distance).float() * (object_pos_w[:, 2] - last_object_pow_w[:, 2])
        # lift_continuous_rew = (1 - torch.tanh(distance / std)) * (object_pos_w[:, 2] - object_default_pos_w[:, 2] + 1)
    
    his_pos_deque.append(object_pos_w)
    
    return lift_continuous_rew

def object_lift_continuous(
    env: ManagerBasedRLEnv, 
    valid_maximal_distance: float,
    height_offset: float = 0.44,
    object_cfg: SceneEntityCfg = SceneEntityCfg("object"),
    robot_cfg: SceneEntityCfg = SceneEntityCfg("robot"),
    ee_frame_cfg: SceneEntityCfg = SceneEntityCfg("ee_frame"),
) -> torch.Tensor:
    '''
    Args
        height_offset: float
            height offset relative to the fl_base_link, e.g. 1.21 - 0.77 = 0.44
    '''
    object: RigidObject = env.scene[object_cfg.name]
    rel_height = object.data.root_pos_w[:, 2] - object.data.default_root_state[:, 2]
    return (rel_height > 0.02) * (torch.clamp(rel_height - 0.02, max=0.1) + 1)
    # robot: Articulation = env.scene[robot_cfg.name]
    # robot_body_pos = robot.data.body_pos_w
    # fl_base_link_height = robot_body_pos[:, robot.body_names.index("fl_base_link"), 2] # height 0.77
    
    # ee_frame: FrameTransformer = env.scene[ee_frame_cfg.name]
    # # End-effector position: (num_envs, 3)
    # ee_w = ee_frame.data.target_pos_w[..., 0, :]
    
    # object: RigidObject = env.scene[object_cfg.name]
    # # Target object position: (num_envs, 3)
    # object_pos_w = object.data.root_pos_w
    # # object_default_pos_w = object.data.default_root_state
    
    # # distance between end-effector and object
    # distance: torch.Tensor = torch.norm(object_pos_w - ee_w, dim=1)

    # lift_continuous_rew = (distance < valid_maximal_distance).float() * \
    #     (fl_base_link_height + height_offset - object_pos_w[:, 2])
    
    # return lift_continuous_rew

def dummy_test(
    env: ManagerBasedRLEnv, 
    objects_cfg: SceneEntityCfg = SceneEntityCfg("objects"),
):
    tgt_object_names = LiftTgtObjects.tgt_object_names
    for tgt_object_name in tgt_object_names:
        tgt_object = SceneEntityCfg(tgt_object_name)
        

def open_finger(
    env: ManagerBasedRLEnv, 
    std: float,
    object_cfg: SceneEntityCfg = SceneEntityCfg("object"),
    robot_cfg: SceneEntityCfg = SceneEntityCfg("robot"),
    ee_frame_cfg: SceneEntityCfg = SceneEntityCfg("ee_frame"),
):
    robot: Articulation = env.scene[robot_cfg.name]
    # finger joint position: (num_envs, 2)
    robot_finger_pos: torch.Tensor = robot.data.joint_pos[:, -2:]
    
    ee_frame: FrameTransformer = env.scene[ee_frame_cfg.name]
    # End-effector position: (num_envs, 3)
    ee_w = ee_frame.data.target_pos_w[..., 0, :]
    
    object: RigidObject = env.scene[object_cfg.name]
    # Target object position: (num_envs, 3)
    cube_pos_w = object.data.root_pos_w
    
    # distance between end-effector and object
    distance = torch.norm(cube_pos_w - ee_w, dim=1)
    
    # finger distance
    finger_distance = torch.sum(robot_finger_pos, dim=1)
    
    return torch.tanh(distance / std) * finger_distance

def close_finger(
    env: ManagerBasedRLEnv, 
    std: float,
    object_cfg: SceneEntityCfg = SceneEntityCfg("object"),
    robot_cfg: SceneEntityCfg = SceneEntityCfg("robot"),
    ee_frame_cfg: SceneEntityCfg = SceneEntityCfg("ee_frame"),
):
    # NOTE: this function is not used in the current training, we use close_fingers instead
    robot: Articulation = env.scene[robot_cfg.name]
    # finger joint position: (num_envs, 2)
    robot_finger_pos: torch.Tensor = robot.data.joint_pos[:, -2:]
    
    ee_frame: FrameTransformer = env.scene[ee_frame_cfg.name]
    # End-effector position: (num_envs, 3)
    ee_w = ee_frame.data.target_pos_w[..., 0, :]
    
    object: RigidObject = env.scene[object_cfg.name]
    # Target object position: (num_envs, 3)
    cube_pos_w = object.data.root_pos_w
    
    # distance between end-effector and object
    distance = torch.norm(cube_pos_w - ee_w, dim=1)
    
    # finger distance
    finger_distance = torch.sum(robot_finger_pos, dim=1) # print finger_distance max 0.08?
    # left/right finger qpos: [0, 0.042], 0 means close, 0.042 means open
    return (1 - torch.tanh(distance / std)) * (0.1 - finger_distance)

def object_ee_distance(
    env: ManagerBasedRLEnv,
    std: float,
    object_cfg: SceneEntityCfg = SceneEntityCfg("object"),
    ee_frame_cfg: SceneEntityCfg = SceneEntityCfg("ee_frame"),
) -> torch.Tensor:
    """Reward the agent for reaching the object using tanh-kernel."""
    # extract the used quantities (to enable type-hinting)
    object: RigidObject = env.scene[object_cfg.name]
    ee_frame: FrameTransformer = env.scene[ee_frame_cfg.name]
    # Target object position: (num_envs, 3)
    cube_pos_w = object.data.root_pos_w
    # End-effector position: (num_envs, 3)
    ee_w = ee_frame.data.target_pos_w[..., 0, :]
    # print(cube_pos_w, ee_w)
    # Distance of the end-effector to the object: (num_envs,)
    object_ee_distance = torch.norm(cube_pos_w - ee_w, dim=1)

    return (1 - torch.tanh(object_ee_distance / std)) + (1 - torch.tanh(object_ee_distance / (std / 4)))

def object_quat_similar(
    env: ManagerBasedRLEnv,
    std: float,
    object_cfg: SceneEntityCfg = SceneEntityCfg("object"),
    ee_frame_cfg: SceneEntityCfg = SceneEntityCfg("ee_frame"),
) -> torch.Tensor:
    # extract the used quantities (to enable type-hinting)
    object: RigidObject = env.scene[object_cfg.name]
    ee_frame: FrameTransformer = env.scene[ee_frame_cfg.name]
    # Target object position: (num_envs, 3)
    object_pos_w = object.data.root_pos_w
    # End-effector position: (num_envs, 3)
    ee_pw = ee_frame.data.target_pos_w[..., 0, :]
    # End-effector quaternion: (num_envs, 4) wxyz
    ee_qw = ee_frame.data.target_quat_w[..., 0, :]
    
    # 从end-effector到object的向量要跟end-effector的朝向一致
    # 代表end-effector的朝向跟object的朝向一致
    object_ee_vec = object_pos_w - ee_pw
    object_ee_vec /= torch.norm(object_ee_vec, dim=1, keepdim=True)
    # End-effector quaternion: (num_envs, 4) wxyz
    object_ee_quat = torch.cat([torch.zeros_like(ee_qw[:, :1]), object_ee_vec], dim=1)
    # 计算end-effector的朝向与object的朝向的cosine
    cos_sim = torch.sum(ee_qw * object_ee_quat, dim=1)
    return (1 - torch.tanh(cos_sim / std))


def object_goal_distance(
    env: ManagerBasedRLEnv,
    std: float,
    minimal_height: float,
    command_name: str,
    robot_cfg: SceneEntityCfg = SceneEntityCfg("robot"),
    object_cfg: SceneEntityCfg = SceneEntityCfg("object"),
) -> torch.Tensor:
    """Reward the agent for tracking the goal pose using tanh-kernel."""
    # extract the used quantities (to enable type-hinting)
    robot: RigidObject = env.scene[robot_cfg.name]
    object: RigidObject = env.scene[object_cfg.name]
    command = env.command_manager.get_command(command_name)
    # compute the desired position in the world frame
    des_pos_b = command[:, :3]
    des_pos_w, _ = combine_frame_transforms(robot.data.root_state_w[:, :3], robot.data.root_state_w[:, 3:7], des_pos_b)
    # distance of the end-effector to the object: (num_envs,)
    distance = torch.norm(des_pos_w - object.data.root_pos_w[:, :3], dim=1)
    # rewarded if the object is lifted above the threshold
    
    platform: RigidObject | Articulation = env.scene["platform"]
    init_object_z = platform.data.root_pos_w[:, 2] + apple_to_tablecloth_height_diff
    return (object.data.root_pos_w[:, 2] > init_object_z + minimal_height) * (1 - torch.tanh(distance / std))

def arm_contact_forces_l2(
    env: ManagerBasedRLEnv, 
    contact_sensors_cfg: SceneEntityCfg = SceneEntityCfg("contact_forces"),
) -> torch.Tensor:
    """Penalty for the contact forces between the arm and env using L2-kernel."""
    contact_sensors: ContactSensor = env.scene[contact_sensors_cfg.name]
    # print(f"contact forces shape: {contact_sensors.data.net_forces_w.shape}") # num_envs sensors_per_env 3-Dforce
    contact_forces_rew = torch.sum(torch.sum(torch.square(contact_sensors.data.net_forces_w), dim=-1), dim=-1)
    assert contact_forces_rew.numel() == env.num_envs, f"contact_forces_rew size is {contact_forces_rew.numel()}, not the correct size"
    return contact_forces_rew

def arm_contact_forces_abs_max(
    env: ManagerBasedRLEnv, 
    contact_sensors_cfg: SceneEntityCfg = SceneEntityCfg("contact_forces"),
) -> torch.Tensor:
    """Penalty for the contact forces between the arm and env using Max-kernel."""
    contact_sensors: ContactSensor = env.scene[contact_sensors_cfg.name]
    # hand_fingers_force = contact_sensors.data.net_forces_w[:, -3:, :]
    contact_forces: torch.Tensor = contact_sensors.data.force_matrix_w # only contains the forces of the filtered bodies
    if torch.count_nonzero(contact_forces) > 0:
        print("contact_forces:", contact_forces)
    # print(f"finger_force: {hand_fingers_force[:, -2:, :, :]}")
    # print(f"force_matrix_w: {contact_sensors.data.force_matrix_w}")
    # print(f"contact forces shape: {contact_sensors.data.net_forces_w.shape}") # num_envs sensors_per_env 3-Dforce
    contact_forces_rew = torch.max(torch.max(torch.max(torch.abs(contact_forces), dim=-1)[0], dim=-1)[0], dim=-1)[0]
    assert contact_forces_rew.numel() == env.num_envs, f"contact_forces_rew size is {contact_forces_rew.numel()}, not the correct size"
    return contact_forces_rew

def arm_contact_forces_exist(
    env: ManagerBasedRLEnv, 
    contact_sensors_cfg: SceneEntityCfg = SceneEntityCfg("contact_forces"),
) -> torch.Tensor:
    """Penalty for the contact forces between the arm and env using Max-kernel."""
    contact_sensors: ContactSensor = env.scene[contact_sensors_cfg.name]
    # hand_fingers_force = contact_sensors.data.net_forces_w[:, -3:, :]
    contact_forces: torch.Tensor = contact_sensors.data.force_matrix_w # only contains the forces of the filtered bodies
    non_zeros_cnt = torch.count_nonzero(contact_forces.view(contact_forces.size(0), -1), dim=1)
    if torch.count_nonzero(contact_forces) > 0:
        print("contact_forces:", contact_forces)
    contact_forces_rew = (non_zeros_cnt > 0).float()
    assert contact_forces_rew.numel() == env.num_envs, f"contact_forces_rew size is {contact_forces_rew.numel()}, not the correct size"
    return contact_forces_rew

def arm_contact_forces_clipped_l2(
    env: ManagerBasedRLEnv, 
    clip: float,
    contact_sensors_cfg: SceneEntityCfg = SceneEntityCfg("contact_forces"),
) -> torch.Tensor:
    contact_sensors: ContactSensor = env.scene[contact_sensors_cfg.name]
    contact_forces: torch.Tensor = contact_sensors.data.net_forces_w
    # if torch.count_nonzero(contact_forces) > 0:
    #     print("contact_forces:", contact_forces)
    contact_forces_rew = torch.sum(torch.sum(torch.square(torch.clamp(contact_forces, max=clip, min=-clip)), dim=-1), dim=-1)
    assert contact_forces_rew.numel() == env.num_envs, f"contact_forces_rew size is {contact_forces_rew.numel()}, not the correct size"
    return contact_forces_rew


def contact_forces_clipped(
    env: ManagerBasedRLEnv, 
    clip: float,
    contact_sensors_cfg: SceneEntityCfg = SceneEntityCfg("contact_forces"),
) -> torch.Tensor:
    contact_sensors: ContactSensor = env.scene[contact_sensors_cfg.name]
    contact_forces: torch.Tensor = contact_sensors.data.net_forces_w
    contact_forces = torch.clamp(contact_forces, -clip, clip)
    # print("contact_forces_clipped", contact_forces.view((env.num_envs, -1)).shape)
    return contact_forces.view((env.num_envs, -1))


def finger_contact_forces_y(
    env: ManagerBasedRLEnv, 
    contact_sensors_cfg: SceneEntityCfg = SceneEntityCfg("fingers_contact_forces"),
) -> torch.Tensor:
    """Penalty for the contact forces between the arm and env using Max-kernel."""
    contact_sensors: ContactSensor = env.scene[contact_sensors_cfg.name]
    # hand_fingers_force = contact_sensors.data.net_forces_w[:, -3:, :]
    contact_forces: torch.Tensor = contact_sensors.data.force_matrix_w[:, :, :, 1] # (N, B, M, 3)
    # print(f"finger_force: {hand_fingers_force[:, -2:, :, :]}")
    # print(f"force_matrix_w: {contact_sensors.data.force_matrix_w}")
    # print(f"contact forces shape: {contact_sensors.data.net_forces_w.shape}") # num_envs sensors_per_env 3-Dforce
    contact_forces_rew = torch.sum(torch.sum(contact_forces, dim=-1), dim=-1)
    assert contact_forces_rew.numel() == env.num_envs, f"contact_forces_rew size is {contact_forces_rew.numel()}, not the correct size"
    return contact_forces_rew

def finger_contact_forces_x(
    env: ManagerBasedRLEnv, 
    contact_sensors_cfg: SceneEntityCfg = SceneEntityCfg("fingers_contact_forces"),
) -> torch.Tensor:
    """Penalty for the contact forces between the arm and env using Max-kernel."""
    contact_sensors: ContactSensor = env.scene[contact_sensors_cfg.name]
    # hand_fingers_force = contact_sensors.data.net_forces_w[:, -3:, :]
    contact_forces: torch.Tensor = contact_sensors.data.force_matrix_w[:, :, :, 0] # (N, B, M, 3)
    # print(f"finger_force: {hand_fingers_force[:, -2:, :, :]}")
    # print(f"force_matrix_w: {contact_sensors.data.force_matrix_w}")
    # print(f"contact forces shape: {contact_sensors.data.net_forces_w.shape}") # num_envs sensors_per_env 3-Dforce
    contact_forces_rew = torch.sum(torch.sum(torch.square(contact_forces), dim=-1), dim=-1)
    assert contact_forces_rew.numel() == env.num_envs, f"contact_forces_rew size is {contact_forces_rew.numel()}, not the correct size"
    return contact_forces_rew

def finger_contact_forces_z(
    env: ManagerBasedRLEnv, 
    contact_sensors_cfg: SceneEntityCfg = SceneEntityCfg("fingers_contact_forces"),
) -> torch.Tensor:
    """Penalty for the contact forces between the arm and env using Max-kernel."""
    contact_sensors: ContactSensor = env.scene[contact_sensors_cfg.name]
    # hand_fingers_force = contact_sensors.data.net_forces_w[:, -3:, :]
    contact_forces: torch.Tensor = contact_sensors.data.force_matrix_w[:, :, :, 2] # (N, B, M, 3)
    # print(f"finger_force: {hand_fingers_force[:, -2:, :, :]}")
    # print(f"force_matrix_w: {contact_sensors.data.force_matrix_w}")
    # print(f"contact forces shape: {contact_sensors.data.net_forces_w.shape}") # num_envs sensors_per_env 3-Dforce
    contact_forces_rew = torch.sum(torch.sum(torch.square(contact_forces), dim=-1), dim=-1)
    assert contact_forces_rew.numel() == env.num_envs, f"contact_forces_rew size is {contact_forces_rew.numel()}, not the correct size"
    return contact_forces_rew


sphere_vis_cfg = VisualizationMarkersCfg(
    prim_path="/Visuals/myMarkers",
    markers={
        "sphere": sim_utils.SphereCfg(
            radius=0.02,
            visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=(0.0, 1.0, 0.0)),
        ),
    }
)
sphere_vis = None

def grasp_force(
    env: ManagerBasedRLEnv,
    object_cfg: SceneEntityCfg = SceneEntityCfg("object"),
    ee_frame_cfg: SceneEntityCfg = SceneEntityCfg("ee_frame"),
) -> torch.Tensor:
    ee_frame: FrameTransformer = env.scene[ee_frame_cfg.name]
    finger_top_pos = ee_frame.data.target_pos_w[..., 0, :]
    finger_bottom_pos = ee_frame.data.target_pos_w[..., 1, :]
    left_finger_pos = ee_frame.data.target_pos_w[..., 2, :]
    right_finger_pos = ee_frame.data.target_pos_w[..., 3, :]

    object: RigidObject = env.scene[object_cfg.name]
    object_pos = object.data.root_pos_w
    
    org_vec = left_finger_pos - right_finger_pos
    org_vec[:, :2] = quat_apply(quat_inv(object.data.root_quat_w), org_vec)[:, :2]
    # print(org_vec[0], (left_finger_pos - right_finger_pos)[0], object.data.root_quat_w[0])
    org_vec /= torch.norm(org_vec, dim=1, keepdim=True)
    finger_dist = torch.norm(left_finger_pos - right_finger_pos, dim=1)
    proj_len = torch.sum((object_pos - left_finger_pos) * (right_finger_pos - left_finger_pos), dim=1) / finger_dist
    object_dist = torch.norm(torch.cross(object_pos - finger_bottom_pos, finger_top_pos - finger_bottom_pos, dim=1), dim=1) / 0.11 # finger dist

    # global sphere_vis
    # if sphere_vis is None:
    #     sphere_vis = VisualizationMarkers(sphere_vis_cfg)
    # sphere_vis.visualize(torch.cat([object_pos, left_finger_pos, right_finger_pos], dim=0))

    # print(object_pos[0], finger_top_pos[0], (left_finger_pos[0] + right_finger_pos[0]) / 2)
    reward = (((finger_dist / 4 < proj_len) & (proj_len < finger_dist / 1.25)) + 0.2) *\
        (1.2 - torch.tanh(object_dist / 0.2)) * (torch.norm(object_pos - finger_top_pos, dim=1) < 0.1) * \
        (1 - torch.tanh(torch.norm(org_vec - torch.tensor([0, 1, 0], device=org_vec.device, dtype=org_vec.dtype), dim=1) / 0.3))
    return reward

def table_force(
    env: ManagerBasedRLEnv,
    object_cfg: SceneEntityCfg = SceneEntityCfg("object"),
):
    object: RigidObject = env.scene[object_cfg.name]
    
    platform: RigidObject | Articulation = env.scene["platform"]
    init_object_z = platform.data.root_pos_w[:, 2] + apple_to_tablecloth_height_diff
    return (object.data.root_pos_w[:, 2] < init_object_z).float()

def close_fingers_2(
    env: ManagerBasedRLEnv,
    robot_cfg: SceneEntityCfg = SceneEntityCfg("robot"),
):
    robot: Articulation = env.scene[robot_cfg.name]
    finger_pos = robot.data.joint_pos[:, -2:]
    finger_distance = torch.sum(finger_pos, dim=1)
    grasp = grasp_force(env)
    return (grasp > 0.5) * (1 - torch.tanh(finger_distance / 0.1))

def object_target_distance(
    env: ManagerBasedRLEnv,
    std: float = 0.2,
    object_cfg: SceneEntityCfg = SceneEntityCfg("object"),
):
    object: RigidObject = env.scene[object_cfg.name]
    dist = torch.norm(object.data.root_pos_w - env.extras["object_target_position"], dim=1)
    return 1 - torch.tanh(dist / std) + 1 - torch.tanh(dist / (std / 4))
