# Copyright (c) 2022-2024, The ORBIT Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from omni.isaac.lab.controllers.differential_ik_cfg import DifferentialIKControllerCfg
from omni.isaac.lab.envs.mdp.actions.actions_cfg import DifferentialInverseKinematicsActionCfg, NonHolonomicActionCfg
from omni.isaac.lab.utils import configclass
from omni.isaac.lab.assets import ArticulationCfg

from . import joint_pos_env_cfg

##
# Pre-defined configs
##
from omni.isaac.lab_assets.mobile_aloha import MOBILEALOHA_CFG, OP_LEFT_ARM_JOINT_NAMES, \
    OP_LEFT_FINGER_JOINT_NAMES, OP_LEFT_ARM_HAND_LINK, WHEEL_JOINT_NAMES  # isort: skip
from omni.isaac.lab.envs.mdp.actions.actions_cfg import JointPositionActionCfg, SyncedJointPositionActionCfg
from omni.isaac.lab_tasks.manager_based.manipulation.lift import x_scene_object_offset, y_scene_object_offset, object_pos, \
    ee_offset, ENV_SPACING


@configclass
class MobileAlohaCubeLiftEnvCfg(joint_pos_env_cfg.MobileAlohaCubeLiftEnvCfg):
    def __post_init__(self):
        if not hasattr(self, 'observe_room'):
            self.observe_room = False
        # post init of parent 
        super().__post_init__()
        
        if (hasattr(self, 'observe_room') and self.observe_room) or (hasattr(self, 'collect_dataset') and self.collect_dataset == True):
            self.scene.env_spacing = ENV_SPACING * 3
        else:
            self.scene.env_spacing = ENV_SPACING
        
        # Set actions for the specific robot type (mobile aloha)
        # self.actions.body_joint_pos = DifferentialInverseKinematicsActionCfg(
        #     asset_name="robot",
        #     joint_names=[*OP_LEFT_ARM_JOINT_NAMES],
        #     body_name="fl_link6",
        #     controller=DifferentialIKControllerCfg(command_type="pose", use_relative_mode=False, ik_method="dls"),
        #     body_offset=DifferentialInverseKinematicsActionCfg.OffsetCfg(pos=ee_offset),
        #     scale=100,
        # )
        self.actions.body_joint_pos = JointPositionActionCfg(
            asset_name="robot",
            joint_names=[*OP_LEFT_ARM_JOINT_NAMES],
            scale=1,
            # use_default_offset=False,  # default offset is 0
        )
        self.actions.finger_joint_pos = SyncedJointPositionActionCfg(
            asset_name="robot",
            joint_names=OP_LEFT_FINGER_JOINT_NAMES,
            # scale=0.01,
            scale=0.1,
            use_default_offset=False,
        )
        
# ps: Our current training and inference do not use this class
@configclass
class MobileAlohaCubeLiftEnvCfg_PLAY(MobileAlohaCubeLiftEnvCfg):
    def __post_init__(self):
        self.collect_dataset = True
        # post init of parent
        super().__post_init__()
        # # make a smaller scene for play
        # self.scene.num_envs = 50
        # self.scene.env_spacing = ENV_SPACING
        # # disable randomization for play
        # self.observations.policy.enable_corruption = False


@configclass
class MobileAlohaCubeLiftEnvCfg_ROOM(MobileAlohaCubeLiftEnvCfg):
    def __post_init__(self):
        self.observe_room = True
        # post init of parent
        super().__post_init__()