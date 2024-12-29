"""Configurations for the object lift environments."""
import torch
from collections import deque

# We leave this file empty since we don't want to expose any configs in this package directly.
# We still need this file to import the "config" module in the parent package.

ENV_SPACING = 2.5

x_scene_object_offset = 0.0
y_scene_object_offset = 0.0

# object_pos = (
#     0.1 + x_scene_object_offset,
#     0.1154 + y_scene_object_offset,
#     0.68
# )
# object_quat = (
#     1, 0, 0, 0
# )

# init_object_height = 0.6758  # for table, scale_z = 1.3
# 0.6758 < 0.678 (real init height)
# init_object_height = 0.677  # for tablecloth, pos_z = 0.32, scale_z = 0.832
# init_object_height = 1.0
object_pos = (
    0.12, 0.0611, 0.677  # init_object_height
) 
# the object_pos is no use, because we will set the object height based on apple_to_tablecloth_height_diff
# in function reset_root_state_uniform_object_over_platform()

# NOTE: For TABLE, when the apple is placed flat on the table, since it will roll, 
# apple's maximum height - minimum height = 0.007
# for example, minimum height=0.673, maximum height=0.683
apple_to_tablecloth_height_diff = 0.307  # only works for tablecloth scale_z=0.7
# 0.292
# platform_z + apple_to_tablecloth_height_diff = apple init_object_height

object_quat = (
    0.6884,  0.6993, -0.1925,  0.0065
)

# use the third range (i.e. reset_platform_range[3], reset_object_pose_range[3]) by default
reset_platform_range = [
    {
        "z": (-0.00, 0.00)
    },
    {
        "z": (-0.07, 0.03)
    },
    {
        "z": (-0.1, 0.1), 
    },
    {
        "z": (-0.13, 0.15), 
    },
    {
        "z": (0.15, 0.15), 
    },
]
# reset_platform_range = {
#     # "x": (-0.15, 0.00),
#     # "z": (-0.1, 0.15 ) # tablecloth: [0.32, 0.52]
    
#     # "z": (-0.0, 0.00),
#     # "z": (-0.07, 0.03) # tablecloth: [0.32, 0.52]
#     # "z": (-0.1, 0.1), 
#     "z": (-0.1, 0.1), 
#     # "z": (0.15, 0.15), 
# },

reset_object_pose_range = [
    {
        "x": (-0.0, 0.0),
        "y": (-0.0, 0.0),
    },
    {
        "x": (-0.05, 0.05),
        "y": (-0.05, 0.05),
    },
    {
        "x": (-0.1, 0.1),
        "y": (-0.05, 0.15),
    },
    {
        "x": (-0.22, 0.08),
        "y": (-0.05, 0.36),
    },
    {
        "x": (-0.2, -0.2),
        "y": (0.00, 0.00),
    },
]
# reset_object_pose_range = {
#     # "x": (-0.20, 0.10),
#     # "y": (-0.05, 0.28),
    
#     # "x": (-0.0, 0.0),
#     # "y": (-0.0, 0.0),
#     # "x": (-0.05, 0.05),
#     # "y": (-0.05, 0.05),
#     # "x": (-0.1, 0.1),
#     # "y": (-0.05, 0.15),
#     "x": (-0.22, 0.08),
#     "y": (-0.05, 0.36),
# }
front_command_reset_range = {
    "x": (0.41, 0.41),
    "y": (-0.01, -0.01),
    "z": (0.75, 0.75),
}  # in front of cam_high
command_reset_range = {
    "x": (0.36, 0.48),
    "y": (-0.11, 0.09),
    "z": (0.6, 0.8),
}

robot_torsional_patch_radius: float = 0.02

# table_pos = (
#     0.35+x_scene_object_offset, 0.0+y_scene_object_offset, 0.40
# )
table_pos = (
    # 0.3510, 0.0041, 0.5058
    0.4010, 0.0041, 0.5058
)
table_quat = (
    0.707, 0, 0, 0.707
)

qpos_max_change = torch.tensor([0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 4.4], device="cuda")
# # was used in termination checking of qpos change, but we don't use it now
DEFAULT_QPOS_7DIM = torch.tensor([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.14160313], device="cuda")
# the first qpos in trajectory is DEFAULT_QPOS_7DIM

ee_offset = (0.11, 0.0, 0.0)

rigid_asset_names = [
    "object",
    "platform",
]
object_history_length = 1

class ObjectHisPosBuf:
    data: deque | None = None

class CollectEpsBuf:
    timesteps: list[list] | None = None  # states
    actions: list[list] | None = None   # actions
    rewards: list[list] | None = None # rewards
    infos: list[list] | None = None  # infos, includes key of "object_pos_z"
    # internal list contains the data of each step in the episode
    # external list contains the trajectories of all environments
    dataset_path = "./data/mobile_aloha"
    images_path = "./data/images/"
    trajectory_num = 0  # 648
    is_compress = True
    use_yolo_sync_process = True
    data_limit = 7000  # valid only when use_yolo_sync_process = False


class HisQposBuf:
    # was used in termination checking of qpos change, but we don't use it now
    data: torch.Tensor | None = None

class LiftTgtObjects:
    tgt_object_names: list[str] | None = None

class ObjectChoice:
    object_choices: torch.Tensor| None = None

object_torsional_patch_radius = 0.02
robot_torsional_patch_radius = 0.02

def each_env_choose_object(
    object_datas: list[torch.Tensor],
    object_choices: torch.Tensor,
):
    '''
    Args
        object_datas: list of torch.Tensor, each tensor is of shape (num_envs, ...)
        object_choices: 
    '''
    pass

