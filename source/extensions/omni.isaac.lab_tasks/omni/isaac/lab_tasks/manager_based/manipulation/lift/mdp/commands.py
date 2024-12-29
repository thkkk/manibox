from __future__ import annotations

import torch
from typing import TYPE_CHECKING

from omni.isaac.lab.assets import RigidObject
from omni.isaac.lab.managers import SceneEntityCfg
from omni.isaac.lab.utils.math import subtract_frame_transforms
from omni.isaac.lab.markers import VisualizationMarkers, VisualizationMarkersCfg
import omni.isaac.lab.sim as sim_utils

if TYPE_CHECKING:
    from omni.isaac.lab.envs import ManagerBasedRLEnv

from .. import reset_object_pose_range, object_pos

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

def reset_object_target_position(
    env: ManagerBasedRLEnv,
    env_ids: torch.Tensor,
):
    if "object_target_position" not in env.extras:
        env.extras["object_target_position"] = torch.zeros((env.num_envs, 3), device=env.device)
    object_target_position: torch.Tensor = env.extras["object_target_position"]
    num_reset = env_ids.shape[0]
    object_target_position[env_ids, 0] = torch.rand(num_reset, device=env.device) * (reset_object_pose_range["x"][1] - reset_object_pose_range["x"][0])\
        + reset_object_pose_range["x"][0]
    object_target_position[env_ids, 1] = torch.rand(num_reset, device=env.device) * (reset_object_pose_range["y"][1] - reset_object_pose_range["y"][0])\
        + reset_object_pose_range["y"][0]
    object_target_position[env_ids, 2] = object_pos[2]

    global sphere_vis
    if sphere_vis is None:
        sphere_vis = VisualizationMarkers(sphere_vis_cfg)
    sphere_vis.visualize(object_target_position)