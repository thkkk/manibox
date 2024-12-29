from __future__ import annotations

from dataclasses import MISSING

from omni.isaac.lab.assets import ArticulationCfg, AssetBaseCfg, RigidObjectCfg
from omni.isaac.lab.scene import InteractiveSceneCfg
from omni.isaac.lab.sensors.frame_transformer.frame_transformer_cfg import FrameTransformerCfg
from omni.isaac.lab.utils import configclass
from omni.isaac.lab.sensors.contact_sensor import ContactSensor, ContactSensorCfg
from omni.isaac.lab.sensors import CameraCfg

##
# Scene definition
##

# to add sensors on robot, refer to source/standalone/tutorials/04_sensors/add_sensors_on_robot.py
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

