from __future__ import annotations

from dataclasses import MISSING

from omni.isaac.lab.utils import configclass

from ..rigid_object.rigid_object_cfg import RigidObjectCfg


@configclass
class OmniGibsonObjectCfg(RigidObjectCfg):
    """Configuration parameters for an object in the OmniGibson environment."""

    fixed_base: bool = False
    category: str = MISSING
    model_name: str = MISSING