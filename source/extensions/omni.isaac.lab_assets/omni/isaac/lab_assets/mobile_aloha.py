"""Configuration for the Tiago robot."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import MISSING
import os

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.actuators import ImplicitActuatorCfg
from omni.isaac.lab.assets import ArticulationCfg
from omni.isaac.lab.utils.assets import ISAAC_NUCLEUS_DIR
from omni.isaac.lab.utils import configclass
from omni.isaac.lab.sim.utils import clone
from omni.isaac.lab_tasks.manager_based.manipulation.lift import robot_torsional_patch_radius
from omni.isaac.lab.sim.schemas.schemas_cfg import RigidBodyPropertiesCfg, MassPropertiesCfg, CollisionPropertiesCfg, \
    ArticulationRootPropertiesCfg

import os

# Mobile Aloha
# full joints
# ARX5USDPath = os.path.expanduser(f"~/GES_robots/mobile_aloha/arx5_description.usd")
# ARX5USDPath = os.path.expanduser(f"~/GES_robots/mobile_aloha/arx5_description_only_fl.usd")
# ARX5USDPath = os.path.expanduser(f"~/GES_robots/mobile_aloha/Links_all_Joints_fl.usd")
ARX5USDPath = os.path.expanduser(f"~/GES_robots/mobile_aloha/Links_allFront_Joints_fl.usd")  

# left teleoperation arms
TELEOP_LEFT_ARM_JOINT_NAMES = [
    "lr_joint1", 
    "lr_joint2", 
    "lr_joint3", 
    "lr_joint4", 
    "lr_joint5", 
    "lr_joint6",
]

# right teleoperation arms
TELEOP_RIGHT_ARM_JOINT_NAMES = [
    "rr_joint1", 
    "rr_joint2", 
    "rr_joint3", 
    "rr_joint4", 
    "rr_joint5", 
    "rr_joint6", 
]

# all teleoperation arms
TELEOP_ARM_JOINT_NAMES = [
    *TELEOP_LEFT_ARM_JOINT_NAMES,
    *TELEOP_RIGHT_ARM_JOINT_NAMES,
]

# left operation arms
OP_LEFT_ARM_JOINT1 = ["fl_joint1"]
OP_LEFT_ARM_JOINT2 = ["fl_joint2"]
OP_LEFT_ARM_JOINT3 = ["fl_joint3"]
OP_LEFT_ARM_JOINT4 = ["fl_joint4"]
OP_LEFT_ARM_JOINT5 = ["fl_joint5"]
OP_LEFT_ARM_JOINT6 = ["fl_joint6"]
OP_LEFT_ARM_JOINT_NAMES = [
    *OP_LEFT_ARM_JOINT1,
    *OP_LEFT_ARM_JOINT2,
    *OP_LEFT_ARM_JOINT3,
    *OP_LEFT_ARM_JOINT4,
    *OP_LEFT_ARM_JOINT5,
    *OP_LEFT_ARM_JOINT6,
]

OP_LEFT_ARM_JOINT_forearm = [
    "fl_joint3", 
    "fl_joint4", 
    "fl_joint5", 
    "fl_joint6", 
]

OP_LEFT_ARM_JOINT_shoulder = [
    "fl_joint1", 
    "fl_joint2", 
]

# right operation arms
OP_RIGHT_ARM_JOINT_NAMES = [
    "fr_joint1", 
    "fr_joint2", 
    "fr_joint3", 
    "fr_joint4", 
    "fr_joint5", 
    "fr_joint6", 
]

# all operation arms
OP_ARM_JOINT_NAMES = [
    *OP_LEFT_ARM_JOINT_NAMES,
    *OP_RIGHT_ARM_JOINT_NAMES,
]

# all arms
ALL_ARM_JOINT_NAMES = [
    *TELEOP_ARM_JOINT_NAMES,
    *OP_ARM_JOINT_NAMES,
]

# left teleoperation fingers
TELEOP_LEFT_FINGER_JOINT_NAMES = [
    "lr_joint7", 
    "lr_joint8", 

]

# right teleoperation fingers
TELEOP_RIGHT_FINGER_JOINT_NAMES = [
    "rr_joint7", 
    "rr_joint8", 
]

# all teleoperation fingers
TELEOP_FINGER_JOINT_NAMES = [
    *TELEOP_LEFT_FINGER_JOINT_NAMES,
    *TELEOP_RIGHT_FINGER_JOINT_NAMES,
]

# left operation fingers
OP_LEFT_FINGER_JOINT_NAMES = [
    "fl_joint7", 
    "fl_joint8", 
]

# right operation fingers
OP_RIGHT_FINGER_JOINT_NAMES = [
    "fr_joint7", 
    "fr_joint8", 
]

# all operation fingers
OP_FINGER_JOINT_NAMES = [
    *OP_LEFT_FINGER_JOINT_NAMES,
    *OP_RIGHT_FINGER_JOINT_NAMES,
]

# all fingers
ALL_FINGER_JOINT_NAMES = [
    *TELEOP_FINGER_JOINT_NAMES,
    *OP_FINGER_JOINT_NAMES,
]

# right teleoperation joints
TELEOP_RIGHT_JOINT_NAMES = [
    *TELEOP_RIGHT_ARM_JOINT_NAMES,
    *TELEOP_RIGHT_FINGER_JOINT_NAMES,
]

# left teleoperation joints
TELEOP_LEFT_JOINT_NAMES = [
    *TELEOP_LEFT_ARM_JOINT_NAMES,
    *TELEOP_LEFT_FINGER_JOINT_NAMES,
]

# right operation joints
OP_RIGHT_JOINT_NAMES = [
    *OP_RIGHT_ARM_JOINT_NAMES,
    *OP_RIGHT_FINGER_JOINT_NAMES,
]

# left operation joints
OP_LEFT_JOINT_NAMES = [
    *OP_LEFT_ARM_JOINT_NAMES,
    *OP_LEFT_FINGER_JOINT_NAMES,
]

# teleoperation joints
TELE_JOINT_NAMES = [
    *TELEOP_ARM_JOINT_NAMES,
    *TELEOP_FINGER_JOINT_NAMES,
]

# operation joints
OP_JOINT_NAMES = [
    *OP_ARM_JOINT_NAMES,
    *OP_FINGER_JOINT_NAMES,
]

WHEEL_JOINT_NAMES = [
    'left_wheel', # Driving wheel
    'right_wheel', 
    # 'fl_wheel', # driven wheel
    # 'fr_wheel',
    # 'rl_wheel',
    # 'rr_wheel',
    # 'fl_castor_wheel', 
    # 'fr_castor_wheel', 
    # 'rl_castor_wheel',
    # 'rr_castor_wheel',
]

# all mobile aloha joints
MOBILEALOHA_JOINT_NAMES = [
    *ALL_ARM_JOINT_NAMES,
    *ALL_FINGER_JOINT_NAMES,
    *WHEEL_JOINT_NAMES,
]

# arm hand links connecting to fingers directly like franka's panda hand
OP_LEFT_ARM_HAND_LINK = "fl_link6"
OP_RIGHT_ARM_HAND_LINK = "fr_link6"
TELEOP_LEFT_ARM_HAND_LINK = "lr_link6"
TELEOP_RIGHT_ARM_HAND_LINK = "rr_link6"



from pxr import Gf, Sdf, Usd

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from omni.isaac.lab.sim import from_files_cfg
import omni.isaac.core.utils.prims as prims_utils


@clone
def spawn_mobile_aloha(
    prim_path: str,
    cfg: MobileAlohaCfg,
    translation: tuple[float, float, float] | None = None,
    orientation: tuple[float, float, float, float] | None = None,
) -> Usd.Prim:
    
    mobile_aloha_prim: Usd.Prim = sim_utils.from_files.spawn_from_usd(
        prim_path=prim_path,
        cfg=cfg,
        translation=translation,
        orientation=orientation,
    )
    
    # print(f"spawn_mobile_aloha's prim_path: {prim_path}")
    
    # # TODO: failed be reference can not be deleted
    # # remove joints we want to fix
    # ignore_joints = cfg.ignore_joints
    # if ignore_joints is not None:
    #     for ignore_joint in ignore_joints:
    #         to_remove_prim_paths = prims_utils.find_matching_prim_paths(f"{prim_path}/.*/{ignore_joint}")
    #         for to_remove_prim_path in to_remove_prim_paths:
    #             print(f"is_prim_ancestral: {prims_utils.is_prim_ancestral(to_remove_prim_path)}")
    #             print(f"is_prim_no_delete: {prims_utils.is_prim_no_delete(to_remove_prim_path)}")
    #             print(f"remove prim path: {to_remove_prim_path}")
    #             prims_utils.delete_prim(to_remove_prim_path)
    
    return mobile_aloha_prim

@configclass
class MobileAlohaCfg(sim_utils.UsdFileCfg):
    """USD file to spawn asset from.

    See :meth:`spawn_from_usd` for more information.

    .. note::
        The configuration parameters include various properties. If not `None`, these properties
        are modified on the spawned prim in a nested manner.
    """

    func: Callable = spawn_mobile_aloha

    ignore_joints: list[str] | None = None
    """Joints we want to fix."""
    


MOBILEALOHA_CFG = ArticulationCfg(
    spawn=MobileAlohaCfg(
        usd_path=ARX5USDPath,
        activate_contact_sensors=True,
        rigid_props=RigidBodyPropertiesCfg(
            rigid_body_enabled=True,
            max_linear_velocity=1000.0, max_angular_velocity=1000.0, max_depenetration_velocity=1.0,
            # max_linear_velocity=1, max_angular_velocity=1, max_depenetration_velocity=1,
            # enable_gyroscopic_forces=True,
        ),
        articulation_props=ArticulationRootPropertiesCfg(
            enabled_self_collisions=True,  # could be False?
            solver_position_iteration_count=16,  # 32 of mk
            solver_velocity_iteration_count=0,  # 32 of mk
            sleep_threshold=0.005,
            stabilization_threshold=0.001
        ),
        # mass_props=MassPropertiesCfg(
        #     density=1000,
        # ),
        # collision_props=CollisionPropertiesCfg(
        #     collision_enabled=True,
        #     torsional_patch_radius=robot_torsional_patch_radius,
        # ),
        # ignore_joints=[*TELE_JOINT_NAMES, *OP_RIGHT_JOINT_NAMES, *WHEEL_JOINT_NAMES]
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        pos=(0.0, 0.0, 0.0), # the robot will fly if height is 1.0
        # joint_pos={k: 0.0 for k in MOBILEALOHA_JOINT_NAMES},
    ),
    
    actuators={
        # 1800 stiffness, 300 damping is more reasonable (arm action: scale=1)
        **{f"{joint_name}_actuator": ImplicitActuatorCfg(
            joint_names_expr=[joint_name],
            effort_limit=15.0,
            velocity_limit=3.0,
            stiffness=1800,
            damping=300,
        ) for joint_name in OP_LEFT_ARM_JOINT_NAMES},

        # single joint
        # **{f"{joint_name}_actuator": ImplicitActuatorCfg(
        #     joint_names_expr=[joint_name],
        #     effort_limit=15.0,
        #     velocity_limit=3.0,
        #     stiffness=5,
        #     damping=600,
        # ) for joint_name in OP_LEFT_ARM_JOINT1},
        
        # **{f"{joint_name}_actuator": ImplicitActuatorCfg(
        #     joint_names_expr=[joint_name],
        #     effort_limit=15.0,
        #     velocity_limit=3.0,
        #     stiffness=5.,
        #     damping=10,
        # ) for joint_name in OP_LEFT_ARM_JOINT2},
        
        # **{f"{joint_name}_actuator": ImplicitActuatorCfg(
        #     joint_names_expr=[joint_name],
        #     effort_limit=15.0,
        #     velocity_limit=3.0,
        #     stiffness=5.,
        #     damping=40.,
        # ) for joint_name in OP_LEFT_ARM_JOINT3},
        
        # **{f"{joint_name}_actuator": ImplicitActuatorCfg(
        #     joint_names_expr=[joint_name],
        #     effort_limit=15.0,
        #     velocity_limit=3.0,
        #     stiffness=4.,
        #     damping=400.,
        # ) for joint_name in OP_LEFT_ARM_JOINT4},
        
        # **{f"{joint_name}_actuator": ImplicitActuatorCfg(
        #     joint_names_expr=[joint_name],
        #     effort_limit=15.0,
        #     velocity_limit=3.0,
        #     stiffness=3.,
        #     damping=300.,
        # ) for joint_name in OP_LEFT_ARM_JOINT5},
        
        # **{f"{joint_name}_actuator": ImplicitActuatorCfg(
        #     joint_names_expr=[joint_name],
        #     effort_limit=15.0,
        #     velocity_limit=3.0,
        #     stiffness=2.,
        #     damping=70.,
        # ) for joint_name in OP_LEFT_ARM_JOINT6},
        
        # fingers
        **{f"{joint_name}_actuator": ImplicitActuatorCfg(
            joint_names_expr=[joint_name],
            effort_limit=15.0,
            velocity_limit=3.0,
            stiffness=1800,
            damping=300, # fix stiffness, adjust damping
        ) for joint_name in OP_LEFT_FINGER_JOINT_NAMES},
        
        # # Distable other arm's action
        # **{f"{joint_name}_actuator": ImplicitActuatorCfg(
        #     joint_names_expr=[joint_name],
        #     effort_limit=15.0,
        #     velocity_limit=3.0,
        #     stiffness=1e10,
        #     damping=80,
        # ) for joint_name in OP_RIGHT_ARM_JOINT_NAMES},
        
        # **{f"{joint_name}_actuator": ImplicitActuatorCfg(
        #     joint_names_expr=[joint_name],
        #     effort_limit=15.0,
        #     velocity_limit=3.0,
        #     stiffness=1e10,
        #     damping=100,
        # ) for joint_name in OP_RIGHT_FINGER_JOINT_NAMES},
        
        # **{f"{joint_name}_actuator": ImplicitActuatorCfg(
        #     joint_names_expr=[joint_name],
        #     effort_limit=15.0,
        #     velocity_limit=3.0,
        #     stiffness=1e10,
        #     damping=80,
        # ) for joint_name in TELEOP_LEFT_ARM_JOINT_NAMES},
        
        # **{f"{joint_name}_actuator": ImplicitActuatorCfg(
        #     joint_names_expr=[joint_name],
        #     effort_limit=15.0,
        #     velocity_limit=3.0,
        #     stiffness=1e10,
        #     damping=100,
        # ) for joint_name in TELEOP_LEFT_FINGER_JOINT_NAMES},
        
        # **{f"{joint_name}_actuator": ImplicitActuatorCfg(
        #     joint_names_expr=[joint_name],
        #     effort_limit=15.0,
        #     velocity_limit=3.0,
        #     stiffness=1e10,
        #     damping=80,
        # ) for joint_name in TELEOP_RIGHT_ARM_JOINT_NAMES},
        
        # **{f"{joint_name}_actuator": ImplicitActuatorCfg(
        #     joint_names_expr=[joint_name],
        #     effort_limit=15.0,
        #     velocity_limit=3.0,
        #     stiffness=1e10,
        #     damping=100,
        # ) for joint_name in TELEOP_RIGHT_FINGER_JOINT_NAMES},
        
        # **{f"{joint_name}_actuator": ImplicitActuatorCfg(
        #     joint_names_expr=[joint_name],
        #     effort_limit=15.0,
        #     velocity_limit=3.0,
        #     stiffness=0.0,
        #     damping=10.0,
        # ) for joint_name in WHEEL_JOINT_NAMES},
    }
)



