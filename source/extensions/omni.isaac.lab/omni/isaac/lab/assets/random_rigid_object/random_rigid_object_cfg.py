from typing import Literal

from ..rigid_object import RigidObjectCfg

from dataclasses import MISSING

from omni.isaac.lab.utils import configclass
from omni.isaac.lab.assets import AssetBase
from omni.isaac.lab.sim import SpawnerCfg
from omni.isaac.lab.sim.spawners.from_files.from_files_cfg import RandomUsdFileCfg

from . import random_rigid_object


@configclass
class RandomRigidObjectCfg(RigidObjectCfg):
    @configclass
    class InitialStateCfg:
        """Initial state of the rigid body."""
        pos: tuple[float, float, float] = (0.0, 0.0, 0.0)
        """Position of the root in simulation world frame. Defaults to (0.0, 0.0, 0.0)."""
        rot: tuple[float, float, float, float] = (1.0, 0.0, 0.0, 0.0)

        lin_vel: tuple[float, float, float] = (0.0, 0.0, 0.0)
        """Linear velocity of the root in simulation world frame. Defaults to (0.0, 0.0, 0.0)."""
        ang_vel: tuple[float, float, float] = (0.0, 0.0, 0.0)
        """Angular velocity of the root in simulation world frame. Defaults to (0.0, 0.0, 0.0)."""
    
    init_state: InitialStateCfg = InitialStateCfg()
    
    class_type: type[random_rigid_object.RandomRigidObject] = random_rigid_object.RandomRigidObject

    spawn: RandomUsdFileCfg | None = None
    
    root_physx_view: any = None
    device: str = None

# @configclass
# class RandomRigidObjectCfg:
    
#     @configclass
#     class InitialStateCfg:
#         pos: tuple[float, float, float] = (0.0, 0.0, 0.0)
#         """Position of the root in simulation world frame. Defaults to (0.0, 0.0, 0.0)."""
#         rot: tuple[float, float, float, float] = (1.0, 0.0, 0.0, 0.0)
#         """Quaternion rotation (w, x, y, z) of the root in simulation world frame.
#         Defaults to (1.0, 0.0, 0.0, 0.0).
#         """
#         lin_vel: tuple[float, float, float] = (0.0, 0.0, 0.0)
#         """Linear velocity of the root in simulation world frame. Defaults to (0.0, 0.0, 0.0)."""
#         ang_vel: tuple[float, float, float] = (0.0, 0.0, 0.0)
#         """Angular velocity of the root in simulation world frame. Defaults to (0.0, 0.0, 0.0)."""

#     class_type: type[RandomRigidObject] = RandomRigidObject

#     spawn: SpawnerCfg | None = None
#     """Spawn configuration for the asset. Defaults to None.

#     If None, then no prims are spawned by the asset class. Instead, it is assumed that the
#     asset is already present in the scene.
#     """

#     init_state: InitialStateCfg = InitialStateCfg()
#     """Initial state of the rigid object. Defaults to identity pose."""

#     collision_group: Literal[0, -1] = 0
#     """Collision group of the asset. Defaults to ``0``.

#     * ``-1``: global collision group (collides with all assets in the scene).
#     * ``0``: local collision group (collides with other assets in the same environment).
#     """

#     debug_vis: bool = False
#     """Whether to enable debug visualization for the asset. Defaults to ``False``."""

    
#     prim_paths: list[str] = MISSING