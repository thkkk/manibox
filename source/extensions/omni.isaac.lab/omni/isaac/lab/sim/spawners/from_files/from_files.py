# Copyright (c) 2022-2024, The Isaac Lab Project Developers.
# All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause

from __future__ import annotations

from typing import TYPE_CHECKING

import os
import random
import carb
import omni.isaac.core.utils.prims as prim_utils
import omni.isaac.core.utils.stage as stage_utils
import omni.kit.commands
from pxr import Gf, Sdf, Usd

from omni.isaac.lab.sim import converters, schemas
from omni.isaac.lab.sim.utils import bind_physics_material, bind_visual_material, clone, select_usd_variants
from omni.isaac.lab.utils.assets import check_file_path

if TYPE_CHECKING:
    from . import from_files_cfg


@clone
def spawn_from_usd(
    prim_path: str,
    cfg: from_files_cfg.UsdFileCfg,
    translation: tuple[float, float, float] | None = None,
    orientation: tuple[float, float, float, float] | None = None,
) -> Usd.Prim:
    """Spawn an asset from a USD file and override the settings with the given config.

    In the case of a USD file, the asset is spawned at the default prim specified in the USD file.
    If a default prim is not specified, then the asset is spawned at the root prim.

    In case a prim already exists at the given prim path, then the function does not create a new prim
    or throw an error that the prim already exists. Instead, it just takes the existing prim and overrides
    the settings with the given config.

    .. note::
        This function is decorated with :func:`clone` that resolves prim path into list of paths
        if the input prim path is a regex pattern. This is done to support spawning multiple assets
        from a single and cloning the USD prim at the given path expression.

    Args:
        prim_path: The prim path or pattern to spawn the asset at. If the prim path is a regex pattern,
            then the asset is spawned at all the matching prim paths.
        cfg: The configuration instance.
        translation: The translation to apply to the prim w.r.t. its parent prim. Defaults to None, in which
            case the translation specified in the USD file is used.
        orientation: The orientation in (w, x, y, z) to apply to the prim w.r.t. its parent prim. Defaults to None,
            in which case the orientation specified in the USD file is used.

    Returns:
        The prim of the spawned asset.

    Raises:
        FileNotFoundError: If the USD file does not exist at the given path.
    """
    # spawn asset from the given usd file
    return _spawn_from_usd_file(prim_path, cfg.usd_path, cfg, translation, orientation)


# @clone
def spawn_from_random_usd(
    # chosen_index: int,
    prim_path: str,
    cfg: from_files_cfg.RandomUsdFileCfg,
    translation: tuple[float, float, float] | None = None,
    orientation: tuple[float, float, float, float] | None = None,
    chosen_index: int | None = None,
) -> tuple[Usd.Prim, dict[str, any]]:
    # generate chosen index
    if chosen_index is None:
        chosen_index = random.randint(0, len(cfg.usd_paths) - 1)
    # generate usd path
    chosen_usd_path = os.path.expanduser(cfg.usd_paths[chosen_index])
    # generate scale
    if cfg.scales is None:
        chosen_scale = (1.0, 1.0, 1.0)
    elif cfg.scale_mode == "discret":
        chosen_scale = cfg.scales[chosen_index]
    elif cfg.scale_mode == "uniform":
        chosen_scale = (random.uniform(*cfg.scales[0]), random.uniform(*cfg.scales[1]), random.uniform(*cfg.scales[2]))
    else:
        raise ValueError(f"Invalid scale mode: '{cfg.scale_mode}'.")
    # generate visual material path
    chosen_visual_material_path = "material" if cfg.visual_material_paths is None else cfg.visual_material_paths[chosen_index]
    
    # check file path exists
    if not check_file_path(chosen_usd_path):
        raise FileNotFoundError(f"USD file not found at path: '{chosen_usd_path}'.")
    # spawn asset if it doesn't exist.
    if not prim_utils.is_prim_path_valid(prim_path):
        # add prim as reference to stage
        
        # def print_all_primPaths():
        #     paths = [prims_utils.get_prim_path(prim) for prim in stage_utils.traverse_stage()]
        #     return paths
        # print(print_all_primPaths())
        # print(prim_path)
        # exit(0)
        
        # print(f"haha333: {prim_path}")
        # exit(0)
        
        prim_utils.create_prim(
            prim_path,
            usd_path=chosen_usd_path,
            translation=translation,
            orientation=orientation,
            scale=chosen_scale,
        )
    else:
        carb.log_warn(f"A prim already exists at prim path: '{prim_path}'.")

    # modify rigid body properties
    if cfg.rigid_props is not None:
        schemas.modify_rigid_body_properties(prim_path, cfg.rigid_props)
    # modify collision properties
    if cfg.collision_props is not None:
        schemas.modify_collision_properties(prim_path, cfg.collision_props)
    # modify mass properties
    if cfg.mass_props is not None:
        schemas.modify_mass_properties(prim_path, cfg.mass_props)
    # modify articulation root properties
    if cfg.articulation_props is not None:
        schemas.modify_articulation_root_properties(prim_path, cfg.articulation_props)

    # apply visual material
    if cfg.visual_material is not None:
        if not chosen_visual_material_path.startswith("/"):
            material_path = f"{prim_path}/{chosen_visual_material_path}"
        else:
            material_path = chosen_visual_material_path
        # create material
        cfg.visual_material.func(material_path, cfg.visual_material)
        # apply material
        bind_visual_material(prim_path, material_path)

    # extra info
    extras = {
        "chosen_index": chosen_index,
        "chosen_usd_path": chosen_usd_path,
        "chosen_scale": chosen_scale,
        "chosen_visual_material_path": chosen_visual_material_path,
    }

    # return the prim
    return prim_utils.get_prim_at_path(prim_path), extras

@clone
def spawn_from_urdf(
    prim_path: str,
    cfg: from_files_cfg.UrdfFileCfg,
    translation: tuple[float, float, float] | None = None,
    orientation: tuple[float, float, float, float] | None = None,
) -> Usd.Prim:
    """Spawn an asset from a URDF file and override the settings with the given config.

    It uses the :class:`UrdfConverter` class to create a USD file from URDF. This file is then imported
    at the specified prim path.

    In case a prim already exists at the given prim path, then the function does not create a new prim
    or throw an error that the prim already exists. Instead, it just takes the existing prim and overrides
    the settings with the given config.

    .. note::
        This function is decorated with :func:`clone` that resolves prim path into list of paths
        if the input prim path is a regex pattern. This is done to support spawning multiple assets
        from a single and cloning the USD prim at the given path expression.

    Args:
        prim_path: The prim path or pattern to spawn the asset at. If the prim path is a regex pattern,
            then the asset is spawned at all the matching prim paths.
        cfg: The configuration instance.
        translation: The translation to apply to the prim w.r.t. its parent prim. Defaults to None, in which
            case the translation specified in the generated USD file is used.
        orientation: The orientation in (w, x, y, z) to apply to the prim w.r.t. its parent prim. Defaults to None,
            in which case the orientation specified in the generated USD file is used.

    Returns:
        The prim of the spawned asset.

    Raises:
        FileNotFoundError: If the URDF file does not exist at the given path.
    """
    # urdf loader to convert urdf to usd
    urdf_loader = converters.UrdfConverter(cfg)
    # spawn asset from the generated usd file
    return _spawn_from_usd_file(prim_path, urdf_loader.usd_path, cfg, translation, orientation)


def spawn_ground_plane(
    prim_path: str,
    cfg: from_files_cfg.GroundPlaneCfg,
    translation: tuple[float, float, float] | None = None,
    orientation: tuple[float, float, float, float] | None = None,
) -> Usd.Prim:
    """Spawns a ground plane into the scene.

    This function loads the USD file containing the grid plane asset from Isaac Sim. It may
    not work with other assets for ground planes. In those cases, please use the `spawn_from_usd`
    function.

    Note:
        This function takes keyword arguments to be compatible with other spawners. However, it does not
        use any of the kwargs.

    Args:
        prim_path: The path to spawn the asset at.
        cfg: The configuration instance.
        translation: The translation to apply to the prim w.r.t. its parent prim. Defaults to None, in which
            case the translation specified in the USD file is used.
        orientation: The orientation in (w, x, y, z) to apply to the prim w.r.t. its parent prim. Defaults to None,
            in which case the orientation specified in the USD file is used.

    Returns:
        The prim of the spawned asset.

    Raises:
        ValueError: If the prim path already exists.
    """
    # Spawn Ground-plane
    if not prim_utils.is_prim_path_valid(prim_path):
        prim_utils.create_prim(prim_path, usd_path=cfg.usd_path, translation=translation, orientation=orientation)
    else:
        raise ValueError(f"A prim already exists at path: '{prim_path}'.")

    # Create physics material
    if cfg.physics_material is not None:
        cfg.physics_material.func(f"{prim_path}/physicsMaterial", cfg.physics_material)
        # Apply physics material to ground plane
        collision_prim_path = prim_utils.get_prim_path(
            prim_utils.get_first_matching_child_prim(
                prim_path, predicate=lambda x: prim_utils.get_prim_type_name(x) == "Plane"
            )
        )
        bind_physics_material(collision_prim_path, f"{prim_path}/physicsMaterial")

    # Scale only the mesh
    # Warning: This is specific to the default grid plane asset.
    if prim_utils.is_prim_path_valid(f"{prim_path}/Enviroment"):
        # compute scale from size
        scale = (cfg.size[0] / 100.0, cfg.size[1] / 100.0, 1.0)
        # apply scale to the mesh
        omni.kit.commands.execute(
            "ChangeProperty",
            prop_path=Sdf.Path(f"{prim_path}/Enviroment.xformOp:scale"),
            value=scale,
            prev=None,
        )

    # Change the color of the plane
    # Warning: This is specific to the default grid plane asset.
    if cfg.color is not None:
        prop_path = f"{prim_path}/Looks/theGrid/Shader.inputs:diffuse_tint"
        # change the color
        omni.kit.commands.execute(
            "ChangePropertyCommand",
            prop_path=Sdf.Path(prop_path),
            value=Gf.Vec3f(*cfg.color),
            prev=None,
            type_to_create_if_not_exist=Sdf.ValueTypeNames.Color3f,
        )
    # Remove the light from the ground plane
    # It isn't bright enough and messes up with the user's lighting settings
    omni.kit.commands.execute("ToggleVisibilitySelectedPrims", selected_paths=[f"{prim_path}/SphereLight"])

    # return the prim
    return prim_utils.get_prim_at_path(prim_path)


"""
Helper functions.
"""


def _spawn_from_usd_file(
    prim_path: str,
    usd_path: str,
    cfg: from_files_cfg.FileCfg,
    translation: tuple[float, float, float] | None = None,
    orientation: tuple[float, float, float, float] | None = None,
) -> Usd.Prim:
    """Spawn an asset from a USD file and override the settings with the given config.

    In case a prim already exists at the given prim path, then the function does not create a new prim
    or throw an error that the prim already exists. Instead, it just takes the existing prim and overrides
    the settings with the given config.

    Args:
        prim_path: The prim path or pattern to spawn the asset at. If the prim path is a regex pattern,
            then the asset is spawned at all the matching prim paths.
        usd_path: The path to the USD file to spawn the asset from.
        cfg: The configuration instance.
        translation: The translation to apply to the prim w.r.t. its parent prim. Defaults to None, in which
            case the translation specified in the generated USD file is used.
        orientation: The orientation in (w, x, y, z) to apply to the prim w.r.t. its parent prim. Defaults to None,
            in which case the orientation specified in the generated USD file is used.

    Returns:
        The prim of the spawned asset.

    Raises:
        FileNotFoundError: If the USD file does not exist at the given path.
    """
    # check file path exists
    stage: Usd.Stage = stage_utils.get_current_stage()
    if not stage.ResolveIdentifierToEditTarget(usd_path):
        raise FileNotFoundError(f"USD file not found at path: '{usd_path}'.")
    # spawn asset if it doesn't exist.
    if not prim_utils.is_prim_path_valid(prim_path):
        # add prim as reference to stage
        prim_utils.create_prim(
            prim_path,
            usd_path=usd_path,
            translation=translation,
            orientation=orientation,
            scale=cfg.scale,
        )
    else:
        carb.log_warn(f"A prim already exists at prim path: '{prim_path}'.")

    # modify variants
    if hasattr(cfg, "variants") and cfg.variants is not None:
        select_usd_variants(prim_path, cfg.variants)

    # modify rigid body properties
    if cfg.rigid_props is not None:
        schemas.modify_rigid_body_properties(prim_path, cfg.rigid_props)
    # modify collision properties
    if cfg.collision_props is not None:
        schemas.modify_collision_properties(prim_path, cfg.collision_props)
    # modify mass properties
    if cfg.mass_props is not None:
        schemas.modify_mass_properties(prim_path, cfg.mass_props)
    # modify articulation root properties
    if cfg.articulation_props is not None:
        schemas.modify_articulation_root_properties(prim_path, cfg.articulation_props)
    # modify tendon properties
    if cfg.fixed_tendons_props is not None:
        schemas.modify_fixed_tendon_properties(prim_path, cfg.fixed_tendons_props)

    # define drive API on the joints
    # note: these are only for setting low-level simulation properties. all others should be set or are
    #  and overridden by the articulation/actuator properties.
    if cfg.joint_drive_props is not None:
        schemas.modify_joint_drive_properties(prim_path, cfg.joint_drive_props)

    # apply visual material
    if cfg.visual_material is not None:
        if not cfg.visual_material_path.startswith("/"):
            material_path = f"{prim_path}/{cfg.visual_material_path}"
        else:
            material_path = cfg.visual_material_path
        # create material
        cfg.visual_material.func(material_path, cfg.visual_material)
        # apply material
        bind_visual_material(prim_path, material_path)

    # return the prim
    return prim_utils.get_prim_at_path(prim_path)


def spawn_from_omnigibson_usd(
    prim_path: str,
    cfg: from_files_cfg.OmniGibsonUsdFileCfg,
    translation: tuple[float, float, float] | None = None,
    orientation: tuple[float, float, float, float] | None = None,
) -> Usd.Prim:
    usd_prim = spawn_from_usd(prim_path, cfg, translation, orientation)
    
    # Get the category, model, and fixed_base from the configuration
    omnigibson_attr: from_files_cfg.OmniGibsonUsdFileCfg.OmniGibsonAttrCfg = cfg.omnigibson_attr
    category = omnigibson_attr.category
    model = omnigibson_attr.model
    fixed_base = omnigibson_attr.fixed_base
    
    
    
    return usd_prim