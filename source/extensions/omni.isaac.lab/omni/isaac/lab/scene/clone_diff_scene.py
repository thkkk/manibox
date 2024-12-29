from __future__ import annotations

import builtins

from omni.isaac.lab.scene.interactive_scene_cfg import InteractiveSceneCfg
import torch
from collections.abc import Sequence
from typing import Any

import carb
import omni.usd
from omni.isaac.cloner import GridCloner
from omni.isaac.core.prims import XFormPrimView
from pxr import PhysxSchema

import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.assets import Articulation, ArticulationCfg, AssetBaseCfg, RigidObject, RigidObjectCfg
from omni.isaac.lab.assets.random_rigid_object import random_rigid_object_cfg
# from omni.isaac.lab.assets.random_rigid_object.random_rigid_object_cfg import RandomRigidObjectCfg
from omni.isaac.lab.sensors import FrameTransformerCfg, SensorBase, SensorBaseCfg
from omni.isaac.lab.terrains import TerrainImporter, TerrainImporterCfg

from .clone_diff_scene_cfg import CloneDiffSceneCfg
from .interactive_scene import InteractiveScene



class CloneDiffScene(InteractiveScene):
    def __init__(self, cfg: CloneDiffSceneCfg):
        # store inputs
        self.cfg = cfg
        # obtain the current stage
        self.stage = omni.usd.get_context().get_stage()
        
        self._articulations = dict()
        self._sensors = dict()
        self._rigid_objects = dict()
        self._extras = dict()
        self._terrain = None
        
        # prepare cloner for environment replication
        self.cloner = GridCloner(spacing=self.cfg.env_spacing)
        self.cloner.define_base_env(self.env_ns)
        self.env_prim_paths = self.cloner.generate_paths(f"{self.env_ns}/env", self.cfg.num_envs)
        # create source prim
        self.stage.DefinePrim(self.env_prim_paths[0], "Xform")
        # clone the env xform
        env_origins = self.cloner.clone(
            source_prim_path=self.env_prim_paths[0],
            prim_paths=self.env_prim_paths,
            replicate_physics=False,
            copy_from_source=True,
        )
        self._default_env_origins = torch.tensor(env_origins, device=self.device, dtype=torch.float32)
        # add entities from config
        self._add_entities_from_cfg()
        self._add_randomized_entities_from_cfg()
        # replicate physics if we have more than one environment
        # this is done to make scene initialization faster at play time
        if self.cfg.replicate_physics and self.cfg.num_envs > 1:
            self.cloner.replicate_physics(
                source_prim_path=self.env_prim_paths[0],
                prim_paths=self.env_prim_paths,
                base_env_path=self.env_ns,
                root_path=self.env_regex_ns.replace(".*", ""),
            )
        
        # add objects to the scene
        # self._add_randomized_entities_from_cfg()
        
        # obtain the current physics scene
        physics_scene_prim_path = None
        for prim in self.stage.Traverse():
            if prim.HasAPI(PhysxSchema.PhysxSceneAPI):
                physics_scene_prim_path = prim.GetPrimPath()
                carb.log_info(f"Physics scene prim path: {physics_scene_prim_path}")
                break
        # filter collisions within each environment instance
        self.cloner.filter_collisions(
            physics_scene_prim_path,
            "/World/collisions",
            self.env_prim_paths,
            global_paths=self._global_prim_paths,
        )
        
    """
    Internal methods.
    """
    
    def _add_entities_from_cfg(self):
        """Add scene entities from the config."""
        # store paths that are in global collision filter
        self._global_prim_paths = list()
        # parse the entire scene config and resolve regex
        for asset_name, asset_cfg in self.cfg.__dict__.items():
            # skip keywords
            # note: easier than writing a list of keywords: [num_envs, env_spacing, lazy_sensor_update]
            if asset_name in CloneDiffSceneCfg.__dataclass_fields__ or asset_cfg is None:
                continue
            # skip RandomRigidObjectCfg since they are handled separately
            if isinstance(asset_cfg, random_rigid_object_cfg.RandomRigidObjectCfg):
                continue
            # resolve regex
            asset_cfg.prim_path = asset_cfg.prim_path.format(ENV_REGEX_NS=self.env_regex_ns)
            # create asset
            if isinstance(asset_cfg, TerrainImporterCfg):
                # terrains are special entities since they define environment origins
                asset_cfg.num_envs = self.cfg.num_envs
                asset_cfg.env_spacing = self.cfg.env_spacing
                self.terrain = asset_cfg.class_type(asset_cfg)
            elif isinstance(asset_cfg, ArticulationCfg):
                self.articulations[asset_name] = asset_cfg.class_type(asset_cfg)
            elif isinstance(asset_cfg, RigidObjectCfg):
                self.rigid_objects[asset_name] = asset_cfg.class_type(asset_cfg)
            elif isinstance(asset_cfg, SensorBaseCfg):
                # Update target frame path(s)' regex name space for FrameTransformer
                if isinstance(asset_cfg, FrameTransformerCfg):
                    updated_target_frames = []
                    for target_frame in asset_cfg.target_frames:
                        target_frame.prim_path = target_frame.prim_path.format(ENV_REGEX_NS=self.env_regex_ns)
                        updated_target_frames.append(target_frame)
                    asset_cfg.target_frames = updated_target_frames

                self.sensors[asset_name] = asset_cfg.class_type(asset_cfg)
            elif isinstance(asset_cfg, AssetBaseCfg):
                # manually spawn asset
                if asset_cfg.spawn is not None:
                    asset_cfg.spawn.func(
                        asset_cfg.prim_path,
                        asset_cfg.spawn,
                        translation=asset_cfg.init_state.pos,
                        orientation=asset_cfg.init_state.rot,
                    )
                # store xform prim view corresponding to this asset
                # all prims in the scene are Xform prims (i.e. have a transform component)
                self.extras[asset_name] = XFormPrimView(asset_cfg.prim_path, reset_xform_properties=False)
            else:
                raise ValueError(f"Unknown asset config type for {asset_name}: {asset_cfg}")
            # store global collision paths
            if hasattr(asset_cfg, "collision_group") and asset_cfg.collision_group == -1:
                asset_paths = sim_utils.find_matching_prim_paths(asset_cfg.prim_path)
                self._global_prim_paths += asset_paths
    
    
    def _add_randomized_entities_from_cfg(self):
        for asset_name, asset_cfg in self.cfg.__dict__.items():
            if asset_name in CloneDiffSceneCfg.__dataclass_fields__ or asset_cfg is None:
                continue
            # resolve regex
            asset_cfg.prim_path = asset_cfg.prim_path.format(ENV_REGEX_NS=self.env_regex_ns)
            # create asset
            if isinstance(asset_cfg, random_rigid_object_cfg.RandomRigidObjectCfg):
                self.rigid_objects[asset_name] = asset_cfg.class_type(asset_cfg, self.num_envs)

            # store global collision paths
            if hasattr(asset_cfg, "collision_group") and asset_cfg.collision_group == -1:
                asset_paths = sim_utils.find_matching_prim_paths(asset_cfg.prim_path)
                self._global_prim_paths += asset_paths
