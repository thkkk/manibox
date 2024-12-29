# Copyright (c) 2022-2024, The ORBIT Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from omni.isaac.lab.assets import AssetBase
from omni.isaac.lab.assets import RigidObjectCfg
from omni.isaac.lab.sensors import FrameTransformerCfg
from omni.isaac.lab.sensors.frame_transformer.frame_transformer_cfg import OffsetCfg
from omni.isaac.lab.sim.schemas.schemas_cfg import RigidBodyPropertiesCfg, MassPropertiesCfg, CollisionPropertiesCfg, \
    ArticulationRootPropertiesCfg
from omni.isaac.lab.sim.spawners.from_files.from_files_cfg import UsdFileCfg
from omni.isaac.lab.utils import configclass
from omni.isaac.lab.utils.assets import ISAAC_NUCLEUS_DIR

from omni.isaac.lab_tasks.manager_based.manipulation.lift import mdp, x_scene_object_offset, y_scene_object_offset, \
    object_pos, ee_offset, object_quat, table_pos, rigid_asset_names, object_history_length, ObjectHisPosBuf, \
    object_torsional_patch_radius, LiftTgtObjects, CollectEpsBuf
from VFCNet.yolo_process_data import YoloCollectData
from omni.isaac.lab_tasks.manager_based.manipulation.lift.lift_env_cfg import LiftEnvCfg, ActionsCfg, EventCfg
from omni.isaac.lab.assets import ArticulationCfg, AssetBaseCfg, RigidObjectCfg
from omni.isaac.lab.envs.mdp.actions.actions_cfg import JointPositionActionCfg, SyncedJointPositionActionCfg
from omni.isaac.lab.sensors.contact_sensor import ContactSensor, ContactSensorCfg
import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.markers.visualization_markers import VisualizationMarkersCfg


from omni.isaac.lab.omnigibson import beechwood0IntquickSceneCfg, beechwood0IntfullSceneCfg, beechwood1IntquickSceneCfg, beechwood1IntfullSceneCfg, benevolence1IntquickSceneCfg, benevolence1IntfullSceneCfg, benevolence2IntquickSceneCfg, benevolence2IntfullSceneCfg, houseDoubleFloorLowerquickSceneCfg, houseDoubleFloorLowerfullSceneCfg, houseDoubleFloorUpperquickSceneCfg, houseDoubleFloorUpperfullSceneCfg, ihlen0IntquickSceneCfg, ihlen0IntfullSceneCfg, ihlen1IntquickSceneCfg, ihlen1IntfullSceneCfg, merom0IntquickSceneCfg, merom0IntfullSceneCfg, merom1IntquickSceneCfg, merom1IntfullSceneCfg, officeLargequickSceneCfg, officeLargefullSceneCfg, pomaria0IntquickSceneCfg, pomaria0IntfullSceneCfg, pomaria1IntquickSceneCfg, pomaria1IntfullSceneCfg, pomaria2IntquickSceneCfg, pomaria2IntfullSceneCfg, rsIntquickSceneCfg, rsIntfullSceneCfg, groceryStoreCafequickSceneCfg, groceryStoreCafefullSceneCfg, houseSingleFloorquickSceneCfg, houseSingleFloorfullSceneCfg, restaurantBrunchquickSceneCfg, restaurantBrunchfullSceneCfg, wainscott0IntquickSceneCfg, wainscott0IntfullSceneCfg, wainscott1IntquickSceneCfg, wainscott1IntfullSceneCfg
from omni.isaac.lab.sensors import CameraCfg

import os
import math
import torch
from collections import deque

from omni.isaac.lab.utils.math import quat_mul


##
# Pre-defined configs
##
from omni.isaac.lab.markers.config import FRAME_MARKER_CFG  # isort: skip
from omni.isaac.lab_assets.mobile_aloha import MOBILEALOHA_CFG, OP_LEFT_ARM_JOINT_NAMES, \
    OP_LEFT_FINGER_JOINT_NAMES, WHEEL_JOINT_NAMES  # isort: skip


grasp_object = "apple" # apple cube
objectCls = RigidObjectCfg if "object" in rigid_asset_names else AssetBaseCfg

# objectCfg = {
#     "apple": objectCls(
#         prim_path="{ENV_REGEX_NS}/Object",
#         # init_state=objectCls.InitialStateCfg(pos=object_pos, rot=object_quat),
#         # init_state=AssetBaseCfg.InitialStateCfg(),
#         spawn=UsdFileCfg(
#             # usd_path=os.path.expanduser("~/isaac_sim-assets-2023.1.1/Assets/Isaac/2023.1.1/NVIDIA/Assets/ArchVis/Residential/Food/Fruit/Apple.usd"),
#             usd_path=os.path.expanduser("~/og_dataset/og_objects/apple/agveuv/usd/green_apple.usd"),
#             visual_material_path="materials",
#             scale=(0.9, 0.9, 0.8),
#             # rigid_props=RigidBodyPropertiesCfg(
#             #     solver_position_iteration_count=16,
#             #     solver_velocity_iteration_count=1,
#             #     max_angular_velocity=1000.0,
#             #     max_linear_velocity=1000.0,
#             #     max_depenetration_velocity=5.0,
#             #     disable_gravity=False,
#             # ),
#             # rigid_props=RigidBodyPropertiesCfg(
#             #     # disable_gravity=True,
#             #     # kinematic_enabled=True,
#             # ) if "apple" in rigid_asset_names else None, 
#             # mass_props=MassPropertiesCfg(
#             #     density=1000,
#             # ) if "apple" in rigid_asset_names else None,   # NOTE: it causes training failure
#             rigid_props=None,
#             mass_props=None,
#             collision_props=CollisionPropertiesCfg(
#                 torsional_patch_radius=object_torsional_patch_radius,            
#             ),
#             activate_contact_sensors=True,
#         ),
#     ),
    # "cube": objectCls(
    #     prim_path="{ENV_REGEX_NS}/Object",
    #     init_state=objectCls.InitialStateCfg(pos=(0.4+x_scene_object_offset, 0+y_scene_object_offset, 1.105), rot=(1, 0, 0, 0)),
    #     spawn=UsdFileCfg(
    #         usd_path=f"{ISAAC_NUCLEUS_DIR}/Props/Blocks/DexCube/dex_cube_instanceable.usd",
    #         scale=(0.8, 0.8, 0.8),
    #         rigid_props=RigidBodyPropertiesCfg(
    #             solver_position_iteration_count=16,
    #             solver_velocity_iteration_count=1,
    #             max_angular_velocity=1000.0,
    #             max_linear_velocity=1000.0,
    #             max_depenetration_velocity=5.0,
    #             disable_gravity=False,
    #         ),
    #     ),
    # ),
# }


ENV_SPACING = 5
contact_sensor_radius = 0.04 # default 0.02
@configclass
class MobileAlohaCubeLiftEnvCfg(LiftEnvCfg):
    # scene: beechwood0IntquickSceneCfg = beechwood0IntquickSceneCfg(num_envs=4096, env_spacing=40, replicate_physics=False)
    # scene: beechwood0IntfullSceneCfg = beechwood0IntfullSceneCfg(num_envs=4096, env_spacing=2.5, replicate_physics=False)
    
    def __post_init__(self):
        # post init of parent
        super().__post_init__()
        # filter collision for omnigibson objects[cellings, walls, floors]
        # self.filter_collision_omnigibson()
        
        # The cfg of robot will be overwritten in ik_abs_env_cfg
        self.scene.robot = MOBILEALOHA_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")
        if (hasattr(self, 'observe_room') and self.observe_room) or (hasattr(self, 'collect_dataset') and self.collect_dataset):
            room_floor_height = 0.06
            self.scene.robot.init_state.pos = (-0.40, 0.0, 0.14 + room_floor_height)  # 0.06 is room height
            self.scene.platform.init_state.pos = (0.40, 0.0041, 0.42 + room_floor_height) 
        else:
            self.scene.robot.init_state.pos = (-0.40, 0.0, 0.14)
            self.scene.platform.init_state.pos = (0.40, 0.0041, 0.42) 
        # 0.14 makes the robot not shake up and down during initialization
        self.scene.robot.init_state.rot = (1.0, 0.0, 0.0, 0.0)

        # set contact sensors
        self.scene.contact_forces = ContactSensorCfg(
            # prim_path="{ENV_REGEX_NS}/Robot/fl_link.*", 
            # prim_path="{ENV_REGEX_NS}/Object/base_link",
            prim_path="{ENV_REGEX_NS}/Robot/fl_link[1-8]", 
            update_period=0.0, 
            # history_length=6, 
            debug_vis=False,
            # filter_prim_paths_expr=["{ENV_REGEX_NS}/Robot/fl_link[1-5]"],
            # filter_prim_paths_expr=["{ENV_REGEX_NS}/Table"], # BUGS !!!!!!!!!!!!!!!!!!!!!!!
            # filter_prim_paths_expr=["/World/envs/env_0/Table"],
        )
        self.scene.contact_forces.visualizer_cfg = VisualizationMarkersCfg(
            prim_path="/Visuals/ContactSensor",
            markers={
                "contact": sim_utils.SphereCfg(
                    radius=contact_sensor_radius,
                    visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=(1.0, 0.0, 0.0)),
                ),
                "no_contact": sim_utils.SphereCfg(
                    radius=contact_sensor_radius,
                    visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=(0.0, 1.0, 0.0)),
                    visible=False,
                ),
            },
        )
        
        print("***************************************hassattr", hasattr(self, 'collect_dataset'))
        if hasattr(self, 'collect_dataset'):
            print("***************************************self.collect_dataset", self.collect_dataset)
        if (hasattr(self, 'observe_room') and self.observe_room) or (hasattr(self, 'collect_dataset') and self.collect_dataset): 
            cam_update_period = 0  # self.sim.dt * self.decimation
            self.scene.cam_high = CameraCfg(
                prim_path="{ENV_REGEX_NS}/Robot/fr_link6/cam_high",
                update_period=cam_update_period,  # TODO
                height=480,
                width=640,
                data_types=["rgb"],  #, "distance_to_image_plane", "semantic_segmentation", "instance_segmentation_fast", "instance_id_segmentation_fast"
                # data_types=["rgb", "distance_to_image_plane"], 
                spawn=sim_utils.PinholeCameraCfg(
                    focal_length=2.86, focus_distance=0.7, horizontal_aperture=3.84, 
                    clipping_range=(0.1, 1e10),
                    lock_camera=False,
                    f_stop=0,
                    horizontal_aperture_offset=-0.062,
                    vertical_aperture_offset=-0.102,
                ),
                # this is the obs coordinates
                offset=CameraCfg.OffsetCfg(
                                        # from Songling
                                        # pos=(-0.1668, 0.29248, -0.0621),
                                        # rot=(1.0, 0.0, 0.0, 0.0),
                                        # # Approximation_
                                        # pos=(-0.1665, 0.29248, -0.0121),
                                        # rot=(0.9996573, 0, 0.02617695, 0), # 3
                                        
                                        # pos=(-0.1618, 0.29248, -0.0171),
                                        # rot=(math.cos(math.pi * 0.7 / 360), 0, math.sin(math.pi * 0.7 / 360), 0), # 0.7 bottom at the same height
                                        # rot=(math.cos(math.pi * 0.5 / 360), 0, math.sin(math.pi * 0.5 / 360), 0), # 0.5 bbox center the same
                                        
                                        pos=(-0.1618, 0.29248, 0.0021),
                                        rot=(0.9997014897, 0, 0.02443217, 0), # 2.8
                                        # pos=(0.28359, 0.0135, 0.7174),
                                        # rot=(0.9993908, 0, 0.03489950, 0), # 4
                                        # rot=(0.9990482, 0, 0.04361939, 0), # 5
                                        # rot=(0.9961947, 0, 0.08715574, 0), # 10
                                        convention="world"),      
            )


            self.scene.cam_left_wrist = CameraCfg(
                prim_path="{ENV_REGEX_NS}/Robot/fl_link6/cam_left_wrist",
                update_period=cam_update_period,
                height=480,
                width=640,
                data_types=["rgb"],    
                spawn=sim_utils.PinholeCameraCfg(
                    focal_length=2.86, focus_distance=0.7, horizontal_aperture=3.84, clipping_range=(0.1, 1.0e5),
                    lock_camera=False,
                    f_stop=0.0,
                    horizontal_aperture_offset=-0.062,
                    vertical_aperture_offset=-0.102,
                ),
                offset=CameraCfg.OffsetCfg(
                                        # from Songling
                                        # pos=(0.03, -0.03, 0.07035),
                                        # rot=(0.9780309147241483, 0.0, 0.20845989984609956, 0.0),
                                        
                                        # pos=(0.0482, 0, 0.105), 
                                        # rot=(math.cos(math.pi * 23 / 360), 0, math.sin(math.pi * 23 / 360), 0),
                                        
                                        # Approximation2
                                        pos=(0.0382, -0.018, 0.10315), 
                                        rot=tuple(quat_mul(
                                        torch.tensor([math.cos(math.pi * 21.6 / 360), 0, math.sin(math.pi * 21.6 / 360), 0]),
                                        torch.tensor([math.cos(math.pi * 2.6 / 360), 0, 0, math.sin(math.pi * 2.6 / 360)]),
                                        ).tolist()),
                                        
                                        # pos=(0.0682, 0, 0.11), 
                                        # rot=(math.cos(math.pi * 30.5 / 360), 0, math.sin(math.pi * 30.5 / 360), 0),
            
                                        # Approximation
                                        # pos=(0.04, 0, 0.12), 
                                        # rot=(0.96592583, 0, 0.25881905, 0), # 30
                                        convention="world"),  
            )

            self.scene.cam_right_wrist = CameraCfg(
                prim_path="{ENV_REGEX_NS}/Robot/fr_link6/cam_right_wrist",
                update_period=cam_update_period,
                height=480,
                width=640,
                data_types=["rgb"],  #, "distance_to_image_plane", "semantic_segmentation", "instance_segmentation_fast", "instance_id_segmentation_fast"
                # data_types=["rgb", "distance_to_image_plane"], 
                spawn=sim_utils.PinholeCameraCfg(
                    focal_length=2.86, focus_distance=0.7, horizontal_aperture=3.84, clipping_range=(0.1, 1.0e5),
                    lock_camera=False,
                    f_stop=0.0,
                    horizontal_aperture_offset=-0.062,
                    vertical_aperture_offset=-0.102,
                ),
                offset=CameraCfg.OffsetCfg(
                                        # from Songling
                                        # pos=(0.0482, 0, 0.07035),
                                        # rot=(0.9747941070689433, 0.0, 0.22310636213174545, 0.0),
                                        
                                        
                                        # pos=(0.0682, 0, 0.11), 
                                        # rot=(math.cos(math.pi * 30.5 / 360), 0, math.sin(math.pi * 30.5 / 360), 0),
                                        # Approximation
                                        pos=(0.0482, 0, 0.11), 
                                        rot=(math.cos(math.pi * 26.8 / 360), 0, math.sin(math.pi * 26.8 / 360), 0),
                                        # rot=(0.96592583, 0, 0.25881905, 0), # 30
                                        convention="world"),      
            )
            
            # wall and floor
            self.scene.background = AssetBaseCfg(
                prim_path="{ENV_REGEX_NS}/CubeRoom",
                init_state=AssetBaseCfg.InitialStateCfg(
                    # pos=(0.50, 0.0041, 0.53), 
                    pos=(-0.75, 0.0, 0.0)
                ),
                spawn=UsdFileCfg(
                    usd_path=os.path.expanduser("~/og_dataset/og_scenes/Beechwood_0_int/usd/CubeRoom.usda"),
                    scale=(0.7, 0.7, 1.0),
                )
            )
        
        # set fingers contact sensors
        # self.scene.fingers_contact_forces = ContactSensorCfg(
        #     prim_path="{ENV_REGEX_NS}/Robot/fl_link[7-8]", 
        #     update_period=0.0, 
        #     # history_length=6, 
        #     debug_vis=True,
        #     # filter_prim_paths_expr=["{ENV_REGEX_NS}/Robot/fl_link[1-5]"],
        #     # filter_prim_paths_expr=["{ENV_REGEX_NS}/Object"],
        #     # filter_prim_paths_expr=["/World/envs/env_0/Object"],
        # )
        # self.scene.fingers_contact_forces.visualizer_cfg = VisualizationMarkersCfg(
        #     prim_path="/Visuals/ContactSensor",
        #     markers={
        #         "contact": sim_utils.SphereCfg(
        #             radius=contact_sensor_radius,
        #             visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=(1.0, 0.0, 0.0)),
        #         ),
        #         "no_contact": sim_utils.SphereCfg(
        #             radius=contact_sensor_radius,
        #             visual_material=sim_utils.PreviewSurfaceCfg(diffuse_color=(0.0, 1.0, 0.0)),
        #             visible=False,
        #         ),
        #     },
        # )

        # Set Franka as robot
        # self.scene.robot = MOBILEALOHA_CFG.replace(prim_path="{ENV_REGEX_NS}/Robot")

        # Set actions for the specific robot type (mobile_aloha)
        # self.actions.body_joint_pos = mdp.JointPositionActionCfg(
        #     asset_name="robot", joint_names=OP_LEFT_ARM_JOINT_NAMES, scale=0.5, use_default_offset=True
        # )
        
        # # left finger joint actions
        # self.actions.finger_joint_pos = mdp.BinaryJointPositionActionCfg(
        #     asset_name="robot",
        #     joint_names=OP_LEFT_FINGER_JOINT_NAMES,
        #     open_command_expr={"fl_joint7": 0.0425, "fl_joint8": 0.0425}, 
        #     close_command_expr={"fl_joint7": 0.0, "fl_joint8": 0.0}, 
        # )

        
        # wheel joint actions
        # self.actions.wheel_joint_pos = mdp.BinaryJointPositionActionCfg(
        #     asset_name="robot",
        #     joint_names=OP_LEFT_FINGER_JOINT_NAMES,
        #     open_command_expr={"fl_joint7": 0.04, "fl_joint8": 0.04}, # TODO: why 0.04 instead of 0.05
        #     close_command_expr={"fl_joint7": 0.0, "fl_joint8": 0.0}, # Temporal setting wit no finger joint
        # )
        # Set the body name for the end effector
        self.commands.object_pose.body_name = "fl_base_link" # Temporal setting

        # # Set Cube as object
        # self.scene.object = objectCfg[grasp_object]
        # if "object" in rigid_asset_names:
        #     self.scene.object.replace(
        #         history_length=object_history_length
        #     )
        
        # init object history buffer
        print(f"ObjectHisPosBuf inited with history length: {object_history_length}")
        ObjectHisPosBuf.data = deque(maxlen=object_history_length)
        
        print(f"CollectEpsBuf inited with history length: {object_history_length}")
        # CollectEpsBuf.timesteps = []
        # CollectEpsBuf.actions = []
        # CollectEpsBuf.rewards = []
        # CollectEpsBuf.infos = []
        # YoloCollectData.init(1)
        
        # multi objects
        print(f"LiftTgtObjects inited")
        LiftTgtObjects.tgt_object_names = ["table"]

        # Listens to the required transforms
        marker_cfg = FRAME_MARKER_CFG.copy()
        marker_cfg.markers["frame"].scale = (0.1, 0.1, 0.1)
        marker_cfg.prim_path = "/Visuals/FrameTransformer"
        
        self.scene.ee_frame = FrameTransformerCfg(
            prim_path="{ENV_REGEX_NS}/Robot/fl_base_link", # temoral setting for left
            # debug_vis=True,
            debug_vis=False,
            visualizer_cfg=marker_cfg,
            target_frames=[
                FrameTransformerCfg.FrameCfg(
                    prim_path="{ENV_REGEX_NS}/Robot/fl_link6",
                    name="hand_top",
                    offset=OffsetCfg(
                        pos=ee_offset, # TODO: may need to adjust
                    ),
                ),
                FrameTransformerCfg.FrameCfg(
                    prim_path="{ENV_REGEX_NS}/Robot/fl_link6",
                    name="hand_bottom",
                    offset=OffsetCfg(
                        pos=(0.0, 0.0, 0.0), # original position
                    ),
                ),
                FrameTransformerCfg.FrameCfg(
                    prim_path="{ENV_REGEX_NS}/Robot/fl_link7",
                    name="left_hand_link",
                    offset=OffsetCfg(
                        pos=ee_offset, # original position
                    ),
                ),
                FrameTransformerCfg.FrameCfg(
                    prim_path="{ENV_REGEX_NS}/Robot/fl_link8",
                    name="right_hand_link",
                    offset=OffsetCfg(
                        pos=ee_offset, # original position
                    ),
                ),
            ],
        )
    
    # def filter_collision_omnigibson(self):
    #     """filter collision for omnigibson objects[cellings, walls, floors]"""
    #     for k, v in self.scene.to_dict().items():
    #         print(f"k: {k}, v: {v}")
    #     exit(0)


@configclass
class MobileAlohaCubeLiftEnvCfg_PLAY(MobileAlohaCubeLiftEnvCfg):
    def __post_init__(self):
        # post init of parent
        super().__post_init__()
        # make a smaller scene for play
        self.scene.num_envs = 50
        self.scene.env_spacing = 2.5
        # disable randomization for play
        self.observations.policy.enable_corruption = False
        
        if hasattr(self.randomization, "random_ep_len_buf"):
            delattr(self.randomization, "random_ep_len_buf")


