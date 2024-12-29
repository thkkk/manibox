# Copyright (c) 2022-2024, The ORBIT Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause


from __future__ import annotations

from dataclasses import MISSING

from omni.isaac.lab.assets.random_rigid_object.random_rigid_object_cfg import RandomRigidObjectCfg
import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.assets import ArticulationCfg, AssetBaseCfg, RigidObjectCfg
from omni.isaac.lab.envs import ManagerBasedRLEnvCfg
from omni.isaac.lab.managers import CurriculumTermCfg as CurrTerm
from omni.isaac.lab.managers import ObservationGroupCfg as ObsGroup
from omni.isaac.lab.managers import ObservationTermCfg as ObsTerm
from omni.isaac.lab.managers import EventTermCfg as EventTerm
from omni.isaac.lab.managers import RewardTermCfg as RewTerm
from omni.isaac.lab.managers import SceneEntityCfg
from omni.isaac.lab.managers import TerminationTermCfg as DoneTerm
from omni.isaac.lab.scene import InteractiveSceneCfg
from omni.isaac.lab.sensors.frame_transformer.frame_transformer_cfg import FrameTransformerCfg
from omni.isaac.lab.sim.spawners.from_files.from_files_cfg import GroundPlaneCfg, RandomUsdFileCfg, UsdFileCfg
from omni.isaac.lab.utils import configclass
from omni.isaac.lab.utils.assets import ISAAC_NUCLEUS_DIR
from omni.isaac.lab.sim.schemas.schemas_cfg import RigidBodyPropertiesCfg
from omni.isaac.lab.markers import VisualizationMarkersCfg, VisualizationMarkers
from omni.isaac.lab_assets.mobile_aloha import OP_LEFT_FINGER_JOINT_NAMES

# from omni.isaac.lab.sensors import CameraCfg
# from omni.isaac.lab.scene import LiftSceneCfg

from omni.isaac.lab_tasks.manager_based.manipulation.lift import x_scene_object_offset, y_scene_object_offset, object_pos, \
    object_quat, table_pos, table_quat, rigid_asset_names, reset_object_pose_range, LiftTgtObjects, \
        command_reset_range, reset_platform_range, front_command_reset_range
from omni.isaac.lab.sim import schemas
from omni.isaac.lab.utils.noise import AdditiveUniformNoiseCfg as Unoise

import os
import json
import torch


from . import mdp

##
# Scene definition
##

from dataclasses import MISSING

from omni.isaac.lab.assets import ArticulationCfg, AssetBaseCfg, RigidObjectCfg
from omni.isaac.lab.scene import InteractiveSceneCfg
from omni.isaac.lab.sensors.frame_transformer.frame_transformer_cfg import FrameTransformerCfg
from omni.isaac.lab.utils import configclass
from omni.isaac.lab.sensors.contact_sensor import ContactSensor, ContactSensorCfg
from omni.isaac.lab.sensors import CameraCfg

tableCls = RigidObjectCfg if "platform" in rigid_asset_names else AssetBaseCfg

@configclass
class LiftSceneCfg(InteractiveSceneCfg):
    """Configuration for the lift scene with a robot and a object.
    This is the abstract base implementation, the exact scene is defined in the derived classes
    which need to set the target object, robot and end-effector frames
    """

    # robots: will be populated by agent env cfg
    robot: ArticulationCfg = MISSING
    # end-effector sensor: will be populated by agent env cfg
    ee_frame: FrameTransformerCfg = MISSING
    # target object: will be populated by agent env cfg
    object: RigidObjectCfg = MISSING

    contact_forces: ContactSensorCfg | None = None
    
    cam_high: CameraCfg | None = None
    cam_left_wrist: CameraCfg | None = None
    cam_right_wrist: CameraCfg | None = None

    # fingers contact forces filter object
    fingers_contact_forces: ContactSensorCfg | None = None
    
    background: AssetBaseCfg | None = None


@configclass
class ObjectTableSceneCfg(LiftSceneCfg):
    """Configuration for the lift scene with a robot and a object.
    This is the abstract base implementation, the exact scene is defined in the derived classes
    which need to set the target object, robot and end-effector frames
    """
    replicate_physics: bool = False
    
    object = RandomRigidObjectCfg(
        prim_path="{ENV_REGEX_NS}/Object",
        init_state=RandomRigidObjectCfg.InitialStateCfg(),
        spawn=RandomUsdFileCfg(
            usd_paths=[os.path.expanduser("~/og_dataset/og_objects/apple/agveuv/usd/green_apple.usd")],
            scale_mode="uniform",
            visual_material_paths=["materials"],
            # scales=((0.75,0.85), (0.75,0.85), (0.85,0.95)),
            scales=((0.77,0.82), (0.77,0.82), (0.77,0.82)),
            # scales=((0.70,0.90), (0.70,0.80), (0.80,1.0)),
            # scales=((0.8,0.8), (0.8,0.8), (0.9,0.9)),
            activate_contact_sensors=True,
            rigid_props=RigidBodyPropertiesCfg(
                disable_gravity=True,
            )
            # rigid_props=RigidBodyPropertiesCfg(
            #     disable_gravity=True,
            #     linear_damping=5000,
            #     angular_damping=5000,
            # ),
        ),
    )
    
    
    # isaac sim table
    # table = AssetBaseCfg(
    #     prim_path="{ENV_REGEX_NS}/Table",
    #     init_state=AssetBaseCfg.InitialStateCfg(pos=(0.35+x_scene_object_offset, -0.3+y_scene_object_offset, 0.80), rot=(0.707, 0, 0, 0.707)),
    #     spawn=UsdFileCfg(usd_path=f"{ISAAC_NUCLEUS_DIR}/Props/Mounts/ThorlabsTable/table_instanceable.usd"),
    # )
    
    platform = RigidObjectCfg(
        prim_path="{ENV_REGEX_NS}/TableCloth",
        init_state=RigidObjectCfg.InitialStateCfg(
            # pos=(0.50, 0.0041, 0.53), 
            pos=(0.40, 0.0041, 0.42),  # 0.32~0.52
            # pos = table_pos, # (0.4010, 0.0041, 0.5058) # 会有碰撞问题
            rot=table_quat),
        spawn=UsdFileCfg(
            # usd_path=os.path.expanduser("~/og_dataset/og_objects/tablecloth/egtqpa/usd/egtqpa.usd"), # 白色圆桌布
            # usd_path=os.path.expanduser("~/og_dataset/og_objects/tablecloth/gwgbkq/usd/gwgbkq.usd"), # 白色圆桌布
            # usd_path=os.path.expanduser("~/og_dataset/og_objects/tablecloth/sgmepr/usd/sgmepr.usd"), # 白色方长桌布
            # usd_path=os.path.expanduser("~/og_dataset/og_objects/tablecloth/shgmwu/usd/shgmwu.usd"), # 白色方短桌布
            # usd_path=os.path.expanduser("~/og_dataset/og_objects/tablecloth/shgmwu/usd/orange_tablecloth.usd"), # 橙色方短桌布
            usd_path=os.path.expanduser("~/og_dataset/og_objects/tablecloth/shgmwu/usd/orange_tablecloth_without_ref_tem.usd"), # 无反光橙色方短桌布
            scale=(0.96, 0.53, 0.7), # (y, x, z)
            rigid_props=RigidBodyPropertiesCfg(
                disable_gravity=True,
                kinematic_enabled=True,
            ),
            mass_props=schemas.schemas_cfg.MassPropertiesCfg(
                density=10000,
            )
        )
    )
    # platform = tableCls(
    #     prim_path="{ENV_REGEX_NS}/Table",
    #     init_state=tableCls.InitialStateCfg(pos=table_pos, rot=table_quat),
    #     spawn=UsdFileCfg(
    #         usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
    #         visual_material_path="materials",
    #         scale=(0.7, 1.2, 1.3),  # notice the first-dim corresponds to the length of y-axis 
    #         # activate_contact_sensors=True,
    #         rigid_props=RigidBodyPropertiesCfg(
    #             kinematic_enabled=True,
    #         ) if "table" in rigid_asset_names else None,
    #         # mass_props=schemas.schemas_cfg.MassPropertiesCfg(
    #         #     density=1000,
    #         # ) if "table" in rigid_asset_names else None,
    #     ),
    # )
    
    # Add some random object to the scene
    
    # Plant
    # plant = AssetBaseCfg(
    #     prim_path="{ENV_REGEX_NS}/Plant",
    #     init_state=AssetBaseCfg.InitialStateCfg(pos=[0.5461+x_scene_object_offset, -0.269+y_scene_object_offset, 0.8], rot=[0.707, 0, 0, 0.707]),
        
    #     spawn=UsdFileCfg(
    #         usd_path=os.path.expanduser("~/isaac_sim-assets-2023.1.1/Assets/Isaac/2023.1.1/NVIDIA/Assets/ArchVis/Residential/Plants/Plant_Succulent_01.usd"),
    #         scale=[0.01, 0.01, 0.01],
    #         # rigid_props=RigidBodyPropertiesCfg(
    #         #     solver_position_iteration_count=16,
    #         #     solver_velocity_iteration_count=1,
    #         #     max_angular_velocity=1000.0,
    #         #     max_linear_velocity=1000.0,
    #         #     max_depenetration_velocity=5.0,
    #         #     disable_gravity=False,
    #         # ),
    #     ),
    # )

    
    
    # black_table_lamp
    # black_table_lamp = AssetBaseCfg(
    #     prim_path="{ENV_REGEX_NS}/Black_table_lamp",
    #     init_state=AssetBaseCfg.InitialStateCfg(pos=(0.273+x_scene_object_offset, -0.327+y_scene_object_offset, 0.8), rot=(0.707, 0, 0, 0.707)),
    #     spawn=UsdFileCfg(
    #         usd_path=os.path.expanduser("~/isaac_sim-assets-2023.1.1/Assets/Isaac/2023.1.1/NVIDIA/Assets/ArchVis/Residential/Lighting/Table Lamps/BlackTableLamp.usd"),
    #         scale=(0.008, 0.008, 0.008)
    #     ),
    # )
    
    # plane
    plane = AssetBaseCfg(
        prim_path="/World/GroundPlane",
        # init_state=AssetBaseCfg.InitialStateCfg(pos=[0+scene_object_offset, 0, -1.05]),
        init_state=AssetBaseCfg.InitialStateCfg(pos=(0+x_scene_object_offset, 0+y_scene_object_offset, 0)),
        spawn=GroundPlaneCfg(
            # color=(255, 255, 255),   # this is grey plane
        ),
        # spawn=UsdFileCfg(
        #     usd_path=os.path.expanduser("~/og_dataset/og_scenes/office_large/usd/Beechwood_0_int_quick.usd"),
        # )
    )
    
    # # Set camera
    # camera = CameraCfg(
    #     prim_path="{ENV_REGEX_NS}/Robot/panda_link7/front_cam",
    #     update_period=0.1,
    #     height=120,
    #     width=120,
    #     data_types=["rgb", "distance_to_image_plane"], 
    #     spawn=sim_utils.PinholeCameraCfg(
    #         focal_length=4.0, focus_distance=400.0, horizontal_aperture=20.955, clipping_range=(0.1, 1.0e5)
    #     ),
    #     # offset=CameraCfg.OffsetCfg(pos=(0.510, 0.0, 0.015), rot=(0.5, -0.5, 0.5, -0.5), convention="ros"),
    #     # offset=CameraCfg.OffsetCfg(pos=(0.0, 0.0, 0.08), rot=(0.6533, 0.2706, -0.2706, 0.6533), convention="ros"),
    #     offset=CameraCfg.OffsetCfg(pos=(0.0, 0.0, 0.08), rot=(0.7071, 0.0, 0.0, 0.7071), convention="ros"),
    # )

    # lights
    light = AssetBaseCfg(
        prim_path="/World/light",
        spawn=sim_utils.DomeLightCfg(color=(0.75, 0.75, 0.75), intensity=3000.0),
    )
    # background = None  # such as wall
    # background = RigidObjectCfg(
    #     prim_path="{ENV_REGEX_NS}/Background",
    #     init_state=RigidObjectCfg.InitialStateCfg(
    #         pos=(1.0+x_scene_object_offset, 0.0+y_scene_object_offset, 1.105), 
    #         rot=(1, 0, 0, 0)
    #     ),
    #     spawn=UsdFileCfg(
    #         usd_path=f"{ISAAC_NUCLEUS_DIR}/Props/Blocks/DexCube/dex_cube_instanceable.usd",
    #         scale=(0.1, 4.0, 2.0),
    #     ),
    # ),


##
# MDP settings
##

@configclass
class CommandsCfg:
    """Command terms for the MDP."""

    object_pose = mdp.UniformPoseCommandCfg(
        asset_name="robot",
        body_name=MISSING,  # will be set by agent env cfg
        resampling_time_range=(5.0, 5.0),
        # debug_vis=True,
        debug_vis=False,
        ranges=mdp.UniformPoseCommandCfg.Ranges(
            # gripper: object_pos+(0.34, 0.24, 0.23)
            pos_x=command_reset_range['x'], 
            pos_y=command_reset_range['y'], 
            pos_z=command_reset_range['z'], 
            roll=(0.0, 0.0), 
            pitch=(0.0, 0.0), 
            yaw=(0.0, 0.0)
        ),
    )


@configclass
class ActionsCfg:
    """Action specifications for the MDP."""

    # will be set by agent env cfg
    body_joint_pos: mdp.JointPositionActionCfg = MISSING
    finger_joint_pos: mdp.SyncedJointPositionActionCfg = MISSING
    pass


INF = 10.0
@configclass
class ObservationsCfg():
    """Observation specifications for the MDP."""

    @configclass
    class PolicyCfg(ObsGroup):
        """Observations for policy group."""

        contact_forces = ObsTerm(
            func=mdp.contact_forces_clipped,
            params={
                "clip": 10,
                "contact_sensors_cfg": SceneEntityCfg("contact_forces"),
            },
        )
        joint_pos = ObsTerm(func=mdp.joint_pos_rel, noise=Unoise(n_min=-0.001, n_max=0.001))
        joint_vel = ObsTerm(func=mdp.joint_vel_rel)  # , noise=Unoise(n_min=-0.002, n_max=0.002)
        object_position = ObsTerm(func=mdp.object_position_in_robot_root_frame)
        target_object_position = ObsTerm(func=mdp.generated_commands, params={"command_name": "object_pose"})
        actions = ObsTerm(func=mdp.last_action)
        
        # # Add camera input
        # image = ObsTerm(func=mdp.get_image)

    # observation groups
    policy: PolicyCfg = PolicyCfg(enable_corruption=True, concatenate_terms=True)
    student: PolicyCfg = PolicyCfg(
        contact_forces=None, object_position=None, target_object_position=None, 
        enable_corruption=True, concatenate_terms=True)  # without priviledged info, you can put vision info here
    # here concatenate_terms=False will cause error...
    # student PolicyCfg always puts joint_pos first in the concatenated array! it will affect the data collection


@configclass
class EventCfg:
    """Configuration for randomization."""

    reset_all = EventTerm(
        func=mdp.reset_scene_to_default, 
        mode="reset",
    )
    
    # reset_dummy_append_new_traj = EventTerm(
    #     func=mdp.reset_dummy_save_traj, 
    #     mode="reset",
    # )
    
    reset_joints = EventTerm(
        func=mdp.reset_joints_by_offset,
        mode="reset",
        params={
            "position_range": (0, 0),
            "velocity_range": (0, 0),
            "asset_cfg": SceneEntityCfg("robot"),
        },
    )
    
    reset_robot = EventTerm(
        func=mdp.reset_root_state_uniform,
        mode="reset",
        params={
            "pose_range": {},
            "velocity_range": {},
            "asset_cfg": SceneEntityCfg("robot"),
        },
    )
    
    reset_tablecloth_range = EventTerm(
        func=mdp.reset_pose_uniform,
        mode="reset",
        params={
            "pose_range": reset_platform_range[3],
            "asset_cfg": SceneEntityCfg("platform"),
        }
    )
    
    reset_object_position = EventTerm(
        func=mdp.reset_root_state_uniform_object_over_platform,
        mode="reset",
        params={
            "pose_range": reset_object_pose_range[3],
            "velocity_range": {},
            "asset_cfg": SceneEntityCfg("object"),
        },
    )
    
    set_hands_grippers_physics_material = EventTerm(
        func=mdp.randomize_rigid_body_material,
        mode="startup",
        params={
            "asset_cfg": SceneEntityCfg("robot", body_names=["fl_link7", "fl_link8"]), # ".*" will failed, don't know why
            "static_friction_range": (1, 1),
            "dynamic_friction_range": (1, 1),
            "restitution_range": (0.0, 0.0),
            "num_buckets": 64,
        },
    )

object_minimal_height = 0.9 # default is 0.82

@configclass
class RewardsCfg:
    """Reward terms for the MDP."""

    # grasping
    # dummy_test = RewTerm(
    #     func=mdp.dummy_test, 
    #     params={
    #     },
    #     weight=0,
    # )
    
    # open fingers before reaching
    # priority lower than reaching
    fingers_open = RewTerm(
        func=mdp.open_finger, 
        params={
            "std": 0.1,
            "object_cfg": SceneEntityCfg("object"),
            "robot_cfg": SceneEntityCfg("robot"),
            "ee_frame_cfg": SceneEntityCfg("ee_frame"),
        },
        weight=5.0,
    )

    # reaching
    reaching_object = RewTerm(
        func=mdp.object_ee_distance, 
        params={
            "std": 0.2,
        }, 
        weight=15.0
    )

    # lifting
    # lifting_object = RewTerm(
    #     func=mdp.object_lift_continuous, 
    #     params={
    #         "valid_maximal_distance": 0.05,
    #         "height_offset": 0.44,
    #         "object_cfg": SceneEntityCfg("object"),
    #         "ee_frame_cfg": SceneEntityCfg("ee_frame"),
    #     }, 
    #     weight=5000.0
    # )
    object_goal_tracking = RewTerm(
        func=mdp.object_goal_distance,
        params={
            "std": 0.3, 
            "minimal_height": 0.02, 
            "command_name": "object_pose",
        },
        weight=80.0,
    )
    object_goal_tracking_fine_grained = RewTerm(
        func=mdp.object_goal_distance,
        params={
            "std": 0.05, 
            "minimal_height": 0.02,   # in reward.py: object.data.root_pos_w[:, 2] > init_object_height + minimal_height
            "command_name": "object_pose"
        },
        weight=70.0,
    )

    # action penalty
    action_rate = RewTerm(
        func=mdp.action_rate_l2, 
        weight=-1e-4,
    )

    joint_vel = RewTerm(
        func=mdp.joint_vel_l2,
        weight=-1e-4,
        params={"asset_cfg": SceneEntityCfg("robot")},
    )
    
    # grasp
    contact_forces = RewTerm(
        func=mdp.grasp_force,
        weight=10,
        params={
            "object_cfg": SceneEntityCfg("object"),
            "ee_frame_cfg": SceneEntityCfg("ee_frame"),
        },
    )
    
    # lift
    close_fingers = RewTerm(
        func=mdp.close_fingers_2,
        weight=100,
    )

    lift_ee = RewTerm(
        func=mdp.ee_is_lifted,
        weight=20,
    )

    lift_reward = RewTerm(
        func=mdp.object_is_lifted,
        weight=100,
        params={
            "minimal_height": 0.02,
            "object_cfg": SceneEntityCfg("object"),
        }
    )

@configclass
class TerminationsCfg:
    """Termination terms for the MDP."""

    time_out = DoneTerm(func=mdp.time_out, time_out=True)

    # object_dropping = DoneTerm(
    #     func=mdp.base_height, params={"minimum_height": -0.05, "asset_cfg": SceneEntityCfg("object")}
    # )
    
    state_out_of_bounds = DoneTerm(
        func=mdp.state_out_of_bound, params={"lower_bounds": -100, "upper_bounds": 100}
    )
    
    # termination_dummy_append_step_and_get_img = DoneTerm(
    #     func=mdp.get_image_and_save_step,
    #     # params={"termination": time_out, "out_of_bound": state_out_of_bounds.time_out}
    # ) 
    
    # object_fly = DoneTerm(
    #     func=mdp.object_fly, params={"fly_radius": 0.5}
    # )
    
    # last_action_out_of_bounds = DoneTerm(
    #     func=mdp.last_action_out_of_bound, 
    #     params={
    #         # "last_action_start": -8,
    #         # "last_action_end": None,
    #         "lower_bounds": -1000, 
    #         "upper_bounds": 1000,
    #     }
    # )



stage_iteration = [0, 1000, 2000, 3000]
@configclass
class CurriculumCfg:
    """Curriculum terms for the MDP."""

    action_rate = CurrTerm(
        func=mdp.modify_reward_weight, params={"term_name": "action_rate", "weight": -1e-2, "num_steps": 10000}
    )

    joint_vel = CurrTerm(
        func=mdp.modify_reward_weight, params={"term_name": "joint_vel", "weight": -1e-2, "num_steps": 10000}
    )
    
    # z_level_1 = CurrTerm(
    #     func=mdp.modify_event_params, 
    #     params={"term_name": "reset_tablecloth_range", "param_name": "pose_range", "value": reset_platform_range[1],
    #             "num_steps": 24 * stage_iteration[1]}
    # )
    # xy_level_1 = CurrTerm(
    #     func=mdp.modify_event_params, 
    #     params={"term_name": "reset_object_position", "param_name": "pose_range", "value": reset_object_pose_range[1],
    #             "num_steps": 24 * stage_iteration[1]}
    # )
    
    # z_level_2 = CurrTerm(
    #     func=mdp.modify_event_params, 
    #     params={"term_name": "reset_tablecloth_range", "param_name": "pose_range", "value": reset_platform_range[2],
    #             "num_steps": 24 * stage_iteration[2]}
    # )
    # xy_level_2 = CurrTerm(
    #     func=mdp.modify_event_params, 
    #     params={"term_name": "reset_object_position", "param_name": "pose_range", "value": reset_object_pose_range[2],
    #             "num_steps": 24 * stage_iteration[2]}
    # )
    
    # z_level_3 = CurrTerm(
    #     func=mdp.modify_event_params, 
    #     params={"term_name": "reset_tablecloth_range", "param_name": "pose_range", "value": reset_platform_range[3],
    #             "num_steps": 24 * stage_iteration[3]}
    # )
    # xy_level_3 = CurrTerm(
    #     func=mdp.modify_event_params, 
    #     params={"term_name": "reset_object_position", "param_name": "pose_range", "value": reset_object_pose_range[3],
    #             "num_steps": 24 * stage_iteration[3]}
    # )
    
    # reset_tablecloth_range = EventTerm(
    #     func=mdp.reset_pose_uniform,
    #     mode="reset",
    #     params={
    #         "pose_range": reset_platform_range,
    #         "asset_cfg": SceneEntityCfg("platform"),
    #     }
    # )
    
    # reset_object_position = EventTerm(
    #     func=mdp.reset_root_state_uniform_object_over_platform,
    #     mode="reset",
    #     params={
    #         "pose_range": reset_object_pose_range,
    #         "velocity_range": {},
    #         "asset_cfg": SceneEntityCfg("object"),
    #     },
    # )
    # TODO: modify_event
    # object_goal_tracking = CurrTerm(
    #     func=mdp.modify_reward_weight, 
    #     params={"term_name": "object_goal_tracking", "weight": 80.0, "num_steps": 2 * 300 * 24}
    #     # * 24 is the number of steps in one iterations
    #     # if we use MultiActorCritic, it will take effect in 750 iterations
    # )
    
    # object_goal_tracking_fine_grained = CurrTerm(
    #     func=mdp.modify_reward_weight, 
    #     params={"term_name": "object_goal_tracking_fine_grained", "weight": 70.0, "num_steps": 2 * 300 * 24}
    # )


##
# Environment configuration
##


@configclass
class LiftEnvCfg(ManagerBasedRLEnvCfg):
    """Configuration for the lifting environment."""

    # Scene settings
    scene: ObjectTableSceneCfg = ObjectTableSceneCfg(num_envs=4096, env_spacing=1.5, replicate_physics=False)
    
    # import pdb;pdb.set_trace()
    # Basic settings
    observations: ObservationsCfg = ObservationsCfg()
    actions: ActionsCfg = ActionsCfg()
    commands: CommandsCfg = CommandsCfg()
    # MDP settings
    rewards: RewardsCfg = RewardsCfg()
    terminations: TerminationsCfg = TerminationsCfg()
    randomization: EventCfg = EventCfg()
    curriculum: CurriculumCfg = CurriculumCfg()

    def __post_init__(self):
        """Post initialization."""
        # general settings
        self.decimation = 2
        # (env.cfg.sim.dt * env.cfg.decimation) is control frequency of model
        # env.cfg.sim.dt is PID control frequency
        sim_acc_coef = 4.0  # sim acceleration coefficient (compare to real world)
        self.sim.render_interval = self.decimation
        
        # NOTE: if sim_acc_coef <= 2, you should enlarge the lift_reward or reduce the close_finger reward
        # because we find that in the sim, robot action is too fast, so we need to slow down the sim
        if hasattr(self, 'collect_dataset') and self.collect_dataset:   # data collection
            print("***************************************collect_dataset mode")
            # when collecting dataset, we use the fixed command
            self.commands.object_pose = mdp.UniformPoseCommandCfg(
                asset_name="robot",
                body_name=MISSING,  # will be set by agent env cfg
                resampling_time_range=(5.0, 5.0),
                # debug_vis=True,
                debug_vis=False,
                ranges=mdp.UniformPoseCommandCfg.Ranges(
                    # gripper: object_pos+(0.34, 0.24, 0.23)
                    pos_x=front_command_reset_range['x'],   # TODO: still nedd to be modified
                    pos_y=front_command_reset_range['y'], 
                    pos_z=front_command_reset_range['z'], 
                    roll=(0.0, 0.0), 
                    pitch=(0.0, 0.0), 
                    yaw=(0.0, 0.0)
                ),
            )
            # self.observations.policy.joint_pos = ObsTerm(func=mdp.joint_pos_rel, noise=Unoise(n_min=-0.001, n_max=0.001))
            self.observations.policy.joint_pos = ObsTerm(func=mdp.joint_pos_rel)
            self.observations.policy.joint_vel = ObsTerm(func=mdp.joint_vel_rel)  # , noise=Unoise(n_min=-0.002, n_max=0.002)
            
            self.episode_length_s = 4.0 / sim_acc_coef * 0.75
            self.sim.dt = 1 / (30.0 * self.decimation * sim_acc_coef)
        elif hasattr(self, 'observe_room') and self.observe_room:
            print("***************************************observe_room mode")
            # this is also for sim2real vision-based policy inference
            self.commands.object_pose = mdp.UniformPoseCommandCfg(
                asset_name="robot",
                body_name=MISSING,  # will be set by agent env cfg
                resampling_time_range=(5.0, 5.0),
                # debug_vis=True,
                debug_vis=False,
                ranges=mdp.UniformPoseCommandCfg.Ranges(
                    # gripper: object_pos+(0.34, 0.24, 0.23)
                    pos_x=front_command_reset_range['x'],   # TODO: still nedd to be modified
                    pos_y=front_command_reset_range['y'], 
                    pos_z=front_command_reset_range['z'], 
                    roll=(0.0, 0.0), 
                    pitch=(0.0, 0.0), 
                    yaw=(0.0, 0.0)
                ),
            )
            self.observations.policy.joint_pos = ObsTerm(func=mdp.joint_pos_rel)
            self.observations.policy.joint_vel = ObsTerm(func=mdp.joint_vel_rel)
            
            self.episode_length_s = 4.0 / sim_acc_coef * 0.75
            self.sim.dt = 1 / (30.0 * self.decimation * sim_acc_coef)
        else:  # training
            # simulation settings
            # 100Hz/50Hz: 
            # self.episode_length_s = 4.0
            # self.sim.dt = 0.01  
            # 60Hz/30Hz
            # self.episode_length_s = 7.0
            self.episode_length_s = 4.0 / sim_acc_coef  # maybe we can * 0.8
            self.sim.dt = 1 / (30.0 * self.decimation * sim_acc_coef)
            # 120Hz for PID, 60Hz for control
            # self.episode_length_s = 3.0
            # self.sim.dt = 0.0083
            # 45/90 Hz
            # self.episode_length_s = 4.0
            # self.sim.dt = 0.011

        self.sim.physx.bounce_threshold_velocity = 0.2
        self.sim.physx.bounce_threshold_velocity = 0.01
        # Increase the size of the buffer
        self.sim.physx.gpu_found_lost_aggregate_pairs_capacity = 2**22
        self.sim.physx.gpu_total_aggregate_pairs_capacity = 16 * 1024
        self.sim.physx.friction_correlation_distance = 0.00625
        self.sim.physx.gpu_total_aggregate_pairs_capacity = 2 ** 24
