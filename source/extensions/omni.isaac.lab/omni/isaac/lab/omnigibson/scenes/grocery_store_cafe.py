from __future__ import annotations

from dataclasses import MISSING

# import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.assets import ArticulationCfg, AssetBaseCfg, RigidObjectCfg, OmniGibsonObjectCfg
# from omni.isaac.lab.envs import RLTaskEnvCfg
# from omni.isaac.lab.managers import CurriculumTermCfg as CurrTerm
# from omni.isaac.lab.managers import ObservationGroupCfg as ObsGroup
# from omni.isaac.lab.managers import ObservationTermCfg as ObsTerm
# from omni.isaac.lab.managers import RandomizationTermCfg as RandTerm
# from omni.isaac.lab.managers import RewardTermCfg as RewTerm
# from omni.isaac.lab.managers import SceneEntityCfg
# from omni.isaac.lab.managers import TerminationTermCfg as DoneTerm
from omni.isaac.lab.scene import InteractiveSceneCfg
from omni.isaac.lab.sensors.frame_transformer.frame_transformer_cfg import FrameTransformerCfg
from omni.isaac.lab.sim.spawners.from_files.from_files_cfg import GroundPlaneCfg, UsdFileCfg, OmniGibsonUsdFileCfg
from omni.isaac.lab.utils import configclass
# from omni.isaac.lab.utils.assets import ISAAC_NUCLEUS_DIR
from omni.isaac.lab.sim.schemas.schemas_cfg import RigidBodyPropertiesCfg

# from omni.isaac.lab.sensors import CameraCfg
# from omni.isaac.lab.scene import InteractiveScene

# from omni.isaac.lab_tasks.manipulation.lift import x_scene_object_offset, y_scene_object_offset

import os
import json
@configclass
class groceryStoreCafequickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/grocery_store_cafe/usd/grocery_store_cafe_quick.usd"),
        )
    )
@configclass
class groceryStoreCafefullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/grocery_store_cafe/usd/grocery_store_cafe_quick.usd"),
        )
    )
    barCowjqr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/barCowjqr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.4260557143032244, 10.351090560715573, 0.5310068173052981),
            rot=(0.015697935546163153, -0.706932482854399, 0.7069325424590431, 0.015697767908100332),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bar/cowjqr/usd/cowjqr.usd"),
            visual_material_path="materials",
            scale=(1.0000262310876002, 0.9999967685142693, 0.9999898806214165),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    displayCaseDyiufq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/displayCaseDyiufq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.5653307299430839, 10.222230384280369, 0.9343723773736489),
            rot=(1.75892913173918e-06, -0.707106542765839, 0.7071070196030053, -1.6746362522140827e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/display_case/dyiufq/usd/dyiufq.usd"),
            visual_material_path="materials",
            scale=(0.9999967358147597, 0.9999996498228346, 1.0000001021794014),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    groceryShelfDylnro0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/groceryShelfDylnro0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.21315192484755, 12.086264969172683, 0.9901734130652069),
            rot=(-1.9949600365537016e-07, -0.7071067215818712, 0.7071068407911626, 1.9949604630472038e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grocery_shelf/dylnro/usd/dylnro.usd"),
            visual_material_path="materials",
            scale=(0.9999730017901151, 1.0000080608840696, 0.999997741689856),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    groceryShelfLdvnrg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/groceryShelfLdvnrg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-11.424585390780782, 5.469220944027207, 0.9755837046245586),
            rot=(-1.1920927527869391e-07, 0.9999999999999521, -2.821299744937143e-07, 4.37114238066289e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grocery_shelf/ldvnrg/usd/ldvnrg.usd"),
            visual_material_path="materials",
            scale=(1.0000386298875044, 0.9999980894487617, 1.000000272656146),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    groceryShelfPrtqlw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/groceryShelfPrtqlw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.520279171368649, 3.1467706895412, 0.4796381151652741),
            rot=(-0.7071067215818997, 0.0, 0.0, 0.7071068407911903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grocery_shelf/prtqlw/usd/prtqlw.usd"),
            visual_material_path="materials",
            scale=(0.9999810915215531, 1.0000012019053177, 0.999999944980331),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    groceryShelfPrtqlw1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/groceryShelfPrtqlw1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.52027917136869, 9.142730162196079, 0.479638115165274),
            rot=(-0.7071067215818997, 0.0, 0.0, 0.7071068407911903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grocery_shelf/prtqlw/usd/prtqlw.usd"),
            visual_material_path="materials",
            scale=(0.9999810915215531, 1.0000012019053177, 0.999999944980331),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    groceryShelfPrtqlw2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/groceryShelfPrtqlw2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.520279095421231, 6.138495787196159, 0.47963749813788426),
            rot=(-0.7071067215818186, 3.371747596654026e-07, -3.3717481650882253e-07, 0.7071068407911106),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grocery_shelf/prtqlw/usd/prtqlw.usd"),
            visual_material_path="materials",
            scale=(0.9999810915215531, 1.0000012019053177, 0.999999944980331),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    groceryShelfRowulr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/groceryShelfRowulr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.917296261726873, 6.7824864257897115, 0.4096471905708313),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grocery_shelf/rowulr/usd/rowulr.usd"),
            visual_material_path="materials",
            scale=(0.9999996870757129, 0.999999985098839, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    groceryShelfRowulr1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/groceryShelfRowulr1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.1172961396568724, 6.7824864257897115, 0.4096471905708313),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grocery_shelf/rowulr/usd/rowulr.usd"),
            visual_material_path="materials",
            scale=(0.9999996870757129, 0.999999985098839, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    groceryShelfRowulr2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/groceryShelfRowulr2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.917296167612517, 5.982486433240298, 0.4096471905708313),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grocery_shelf/rowulr/usd/rowulr.usd"),
            visual_material_path="materials",
            scale=(0.9999996870757129, 0.999999985098839, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    groceryShelfRowulr3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/groceryShelfRowulr3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.1172961396568724, 5.982486425789711, 0.4096471905708313),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grocery_shelf/rowulr/usd/rowulr.usd"),
            visual_material_path="materials",
            scale=(0.9999996870757129, 0.999999985098839, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    groceryShelfRowulr4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/groceryShelfRowulr4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.917296167612517, 8.982486433240295, 0.4096471905708313),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grocery_shelf/rowulr/usd/rowulr.usd"),
            visual_material_path="materials",
            scale=(0.9999996870757129, 0.999999985098839, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    groceryShelfRowulr5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/groceryShelfRowulr5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.1172961396568724, 9.78248642578971, 0.4096471905708313),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grocery_shelf/rowulr/usd/rowulr.usd"),
            visual_material_path="materials",
            scale=(0.9999996870757129, 0.999999985098839, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    groceryShelfRowulr6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/groceryShelfRowulr6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.917296167612517, 9.782486433240296, 0.4096471905708313),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grocery_shelf/rowulr/usd/rowulr.usd"),
            visual_material_path="materials",
            scale=(0.9999996870757129, 0.999999985098839, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    groceryShelfRowulr7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/groceryShelfRowulr7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.117296139656873, 8.982486425789709, 0.4096471905708313),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grocery_shelf/rowulr/usd/rowulr.usd"),
            visual_material_path="materials",
            scale=(0.9999996870757129, 0.999999985098839, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    groceryShelfSjmdri0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/groceryShelfSjmdri0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.6018940913648985, 9.116924359141326, 0.7032134387509448),
            rot=(-0.4999997615813941, -0.49999994039532863, 0.5000001788139076, 0.5000001192092631),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grocery_shelf/sjmdri/usd/sjmdri.usd"),
            visual_material_path="materials",
            scale=(0.9999993297711308, 1.000001083485969, 0.9999995628994627),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    groceryShelfSjmdri1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/groceryShelfSjmdri1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.601894091364974, 6.1005238509012445, 0.7032134387509599),
            rot=(-0.4999997615813941, -0.49999994039532863, 0.5000001788139076, 0.5000001192092631),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grocery_shelf/sjmdri/usd/sjmdri.usd"),
            visual_material_path="materials",
            scale=(0.9999993297711308, 1.000001083485969, 0.9999995628994627),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    groceryShelfTfjzen0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/groceryShelfTfjzen0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.150397466378458, 12.087259360912073, 0.9868018573645863),
            rot=(-1.7167825782583437e-06, -0.7071067215798152, 0.7071068407891067, 1.7167829194451338e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grocery_shelf/tfjzen/usd/tfjzen.usd"),
            visual_material_path="materials",
            scale=(0.9999725447742382, 0.9999963854522438, 0.9999979471248233),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    groceryShelfWranvj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/groceryShelfWranvj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(11.610276886175434, 7.966192909100773, 0.7548406243324279),
            rot=(3.023943691061739e-06, 0.0, 0.0, 0.9999999999954279),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grocery_shelf/wranvj/usd/wranvj.usd"),
            visual_material_path="materials",
            scale=(0.9999984701497912, 1.0000000596046483, 0.9999999602635717),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    groceryShelfWranvj1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/groceryShelfWranvj1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(11.610276886176173, 2.5641924208207727, 0.7548404412274279),
            rot=(3.023943691061739e-06, 0.0, 0.0, 0.9999999999954279),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grocery_shelf/wranvj/usd/wranvj.usd"),
            visual_material_path="materials",
            scale=(0.9999984701497912, 1.0000000596046483, 0.9999999602635717),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    groceryShelfXngcbz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/groceryShelfXngcbz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(7.601000002215045, 3.519901564541604, 0.5887967652699323),
            rot=(-0.707106721581898, -4.214683791125238e-08, 4.214683779425277e-08, 0.7071068407911895),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/grocery_shelf/xngcbz/usd/xngcbz.usd"),
            visual_material_path="materials",
            scale=(1.000000435373247, 1.000000953675226, 0.9999983146928842),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfIwziew0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfIwziew0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.983494685189911, 12.27774643224481, 1.8137823067185306),
            rot=(-1.7167825782583437e-06, -0.7071067215798151, 0.7071068407891068, 1.7167829194451342e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/iwziew/usd/iwziew.usd"),
            visual_material_path="materials",
            scale=(0.9999997497395011, 1.00000117719312, 1.0000004172326875),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swingNppayh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swingNppayh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.914318745197129, -0.10644701295454213, 1.2557283058157127),
            rot=(0.7071067811865477, 0.0, 0.0, -0.7071067811865474),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swing/nppayh/usd/nppayh.usd"),
            visual_material_path="materials",
            scale=(0.9999893697678726, 1.0000279858870826, 0.9999935483878514),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swingUjsdou0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swingUjsdou0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.600361435623827, 0.3201863825991503, 1.2781091356283714),
            rot=(0.7071067811865477, 0.0, 0.0, -0.7071067811865474),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swing/ujsdou/usd/ujsdou.usd"),
            visual_material_path="materials",
            scale=(0.9999745023285149, 0.9999801692423654, 1.000009608000892),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfYursyw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfYursyw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.040995044708681636, 12.091280710440767, 1.6539923009268578),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/yursyw/usd/yursyw.usd"),
            visual_material_path="materials",
            scale=(0.999941886384222, 1.0000153371943143, 0.9999997615814777),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableYlykeh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableYlykeh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.684901237487793, 0.7362388968467712, 0.7437606453895569),
            rot=(2.8638169169425964e-07, -2.7474015951156616e-08, 6.964137355680577e-08, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/ylykeh/usd/ylykeh.usd"),
            visual_material_path="materials",
            scale=(0.9999998807907247, 0.9999999205271466, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    cashRegisterTggwud0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/cashRegisterTggwud0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.6297755241394043, 10.2805814743042, 1.366830825805664),
            rot=(0.01229931227862835, 0.7071084976196289, 0.7068973183631897, -0.011941030621528625),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/cash_register/tggwud/usd/tggwud.usd"),
            visual_material_path="materials",
            scale=(0.9999967699227582, 1.0000460252695587, 1.0000151542619713),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    packingBoxCjhskr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/packingBoxCjhskr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.072515487670898, 0.27089354395866394, 0.33681416511535645),
            rot=(-0.6235007643699646, 0.0, 0.0, 0.7818227410316467),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/packing_box/cjhskr/usd/cjhskr.usd"),
            visual_material_path="materials",
            scale=(1.000068926214066, 1.0000062618142134, 0.9998622314658653),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    packingBoxCjhskr1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/packingBoxCjhskr1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.061773300170898, 0.27089354395866394, 0.11288293451070786),
            rot=(0.8515264391899109, 0.0, 0.0, -0.5243116617202759),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/packing_box/cjhskr/usd/cjhskr.usd"),
            visual_material_path="materials",
            scale=(1.000068926214066, 1.0000062618142134, 0.9998622314658653),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    packingBoxCjhskr2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/packingBoxCjhskr2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.734023571014404, 0.2717587947845459, 0.11288293451070786),
            rot=(-0.7071065902709961, 0.0, 0.0, 0.7071069478988647),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/packing_box/cjhskr/usd/cjhskr.usd"),
            visual_material_path="materials",
            scale=(1.000068926214066, 1.0000062618142134, 0.9998622314658653),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTableXrrhik0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTableXrrhik0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.33553168177604675, 6.394808769226074, 0.44556617736816406),
            rot=(4.030012496514246e-05, 0.9659258127212524, 0.2588193416595459, 0.00020366569515317678),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/xrrhik/usd/xrrhik.usd"),
            visual_material_path="materials",
            scale=(1.000064065523322, 0.9999942644189586, 0.999933348126097),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTableXrrhik1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTableXrrhik1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.3355315923690796, 8.093823432922363, 0.4455665349960327),
            rot=(4.0380487916991115e-05, 0.9659258127212524, 0.2588191330432892, 0.00020396651234477758),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/xrrhik/usd/xrrhik.usd"),
            visual_material_path="materials",
            scale=(1.000064065523322, 0.9999942644189586, 0.999933348126097),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTableXrrhik2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTableXrrhik2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.6301164627075195, 8.09382438659668, 0.44556736946105957),
            rot=(4.1502018575556576e-05, 0.9659258723258972, 0.2588191032409668, 0.00020442105596885085),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/xrrhik/usd/xrrhik.usd"),
            visual_material_path="materials",
            scale=(1.000064065523322, 0.9999942644189586, 0.999933348126097),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pedestalTableXrrhik3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pedestalTableXrrhik3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.6301164627075195, 6.394808769226074, 0.4455662667751312),
            rot=(4.030057607451454e-05, 0.9659258723258972, 0.2588195204734802, 0.00020374107407405972),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pedestal_table/xrrhik/usd/xrrhik.usd"),
            visual_material_path="materials",
            scale=(0.9999359014754527, 0.9999942644189586, 0.999933348126097),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shoppingCartKmgltg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shoppingCartKmgltg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6244696378707886, -0.5779556035995483, 0.4379855990409851),
            rot=(1.2665987014770508e-06, 0.0011845678091049194, -0.00021306611597537994, 0.9999992847442627),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shopping_cart/kmgltg/usd/kmgltg.usd"),
            visual_material_path="materials",
            scale=(1.0000341312129981, 0.9999587690185842, 0.9999457110695145),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shoppingCartKmgltg1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shoppingCartKmgltg1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.3914425373077393, -0.5583587288856506, 0.4379788935184479),
            rot=(0.9999991059303284, -0.0004619522951543331, -0.0013412516564130783, -1.4081597328186035e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shopping_cart/kmgltg/usd/kmgltg.usd"),
            visual_material_path="materials",
            scale=(1.0000341312129981, 0.9999587690185842, 0.9999457110695145),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shoppingCartKmgltg2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shoppingCartKmgltg2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.8341083526611328, -0.558358371257782, 0.43797892332077026),
            rot=(0.9999990463256836, -0.000462227500975132, -0.0013413371052592993, -1.4416873455047607e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shopping_cart/kmgltg/usd/kmgltg.usd"),
            visual_material_path="materials",
            scale=(1.0000341312129981, 0.9999587690185842, 0.9999457110695145),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shoppingCartKmgltg3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shoppingCartKmgltg3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.5969724655151367, -0.5583585500717163, 0.4379788637161255),
            rot=(0.9999991059303284, -0.00046198349446058273, -0.0013412483967840672, -1.2069940567016602e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shopping_cart/kmgltg/usd/kmgltg.usd"),
            visual_material_path="materials",
            scale=(1.0000341312129981, 0.9999587690185842, 0.9999457110695145),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shoppingCartKmgltg4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shoppingCartKmgltg4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.3360209465026855, -0.5779557228088379, 0.4379854202270508),
            rot=(1.2498348951339722e-06, 0.0011846721172332764, -0.00021359045058488846, 0.9999993443489075),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shopping_cart/kmgltg/usd/kmgltg.usd"),
            visual_material_path="materials",
            scale=(1.0000341312129981, 0.9999587690185842, 0.9999457110695145),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shoppingCartKmgltg5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shoppingCartKmgltg5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.469583034515381, -0.5779567360877991, 0.43798547983169556),
            rot=(1.125037670135498e-06, 0.001184716820716858, -0.0002135755494236946, 0.9999994039535522),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shopping_cart/kmgltg/usd/kmgltg.usd"),
            visual_material_path="materials",
            scale=(1.0000341312129981, 0.9999587690185842, 0.9999457110695145),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairQnjtxe0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairQnjtxe0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.295574426651001, 6.035500526428223, 0.4499833583831787),
            rot=(2.0693987607955933e-06, 0.969759464263916, 0.24406281113624573, 5.364418029785156e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/qnjtxe/usd/qnjtxe.usd"),
            visual_material_path="materials",
            scale=(0.9999284666561642, 1.000044737495996, 1.000025495458633),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairQnjtxe1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairQnjtxe1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.3499508798122406, 8.831679344177246, 0.44998258352279663),
            rot=(2.237968146800995e-06, -0.6852208375930786, 0.7283353805541992, -7.934868335723877e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/qnjtxe/usd/qnjtxe.usd"),
            visual_material_path="materials",
            scale=(0.9999284666561642, 1.000044737495996, 1.000025495458633),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairQnjtxe10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairQnjtxe10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.34995052218437195, 7.132666110992432, 0.4499827027320862),
            rot=(2.555549144744873e-06, -0.6852206587791443, 0.7283354997634888, -8.866190910339355e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/qnjtxe/usd/qnjtxe.usd"),
            visual_material_path="materials",
            scale=(0.9999284666561642, 1.000044737495996, 1.000025495458633),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairQnjtxe11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairQnjtxe11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.973761260509491, 6.027653217315674, 0.44998183846473694),
            rot=(6.909249350428581e-07, 0.2731769382953644, 0.9619637727737427, -1.1920928955078125e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/qnjtxe/usd/qnjtxe.usd"),
            visual_material_path="materials",
            scale=(0.9999284666561642, 1.000044737495996, 1.000025495458633),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairQnjtxe2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairQnjtxe2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.9737622141838074, 7.726666450500488, 0.4499826729297638),
            rot=(-1.4505349099636078e-06, 0.2731770873069763, 0.9619638323783875, 1.7136335372924805e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/qnjtxe/usd/qnjtxe.usd"),
            visual_material_path="materials",
            scale=(0.9999284666561642, 1.000044737495996, 1.000025495458633),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairQnjtxe3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairQnjtxe3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.2955735921859741, 7.734514236450195, 0.4499830901622772),
            rot=(2.6384368538856506e-06, 0.969759464263916, 0.2440631240606308, -3.6694109439849854e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/qnjtxe/usd/qnjtxe.usd"),
            visual_material_path="materials",
            scale=(0.9999284666561642, 1.000044737495996, 1.000025495458633),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairQnjtxe4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairQnjtxe4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.6445364952087402, 8.831679344177246, 0.4499826431274414),
            rot=(2.1960586309432983e-06, -0.6852208375930786, 0.728335440158844, -9.015202522277832e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/qnjtxe/usd/qnjtxe.usd"),
            visual_material_path="materials",
            scale=(0.9999284666561642, 1.000044737495996, 1.000025495458633),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairQnjtxe5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairQnjtxe5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.2683472633361816, 7.726666450500488, 0.4499826729297638),
            rot=(-1.5097903087735176e-06, 0.2731771469116211, 0.9619638323783875, 1.7210841178894043e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/qnjtxe/usd/qnjtxe.usd"),
            visual_material_path="materials",
            scale=(0.9999284666561642, 1.000044737495996, 1.000025495458633),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairQnjtxe6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairQnjtxe6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.9990110397338867, 7.734516143798828, 0.4499833285808563),
            rot=(2.175569534301758e-06, 0.9697593450546265, 0.24406331777572632, 6.277114152908325e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/qnjtxe/usd/qnjtxe.usd"),
            visual_material_path="materials",
            scale=(0.9999284666561642, 1.000044737495996, 1.000025495458633),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairQnjtxe7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairQnjtxe7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.6445353031158447, 7.132666110992432, 0.44998273253440857),
            rot=(2.6402994990348816e-06, -0.6852205991744995, 0.7283356785774231, -6.966292858123779e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/qnjtxe/usd/qnjtxe.usd"),
            visual_material_path="materials",
            scale=(0.9999284666561642, 1.000044737495996, 1.000025495458633),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairQnjtxe8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairQnjtxe8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.2683465480804443, 6.027653694152832, 0.44998180866241455),
            rot=(6.016343832015991e-07, 0.2731770873069763, 0.9619636535644531, -5.960464477539063e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/qnjtxe/usd/qnjtxe.usd"),
            visual_material_path="materials",
            scale=(0.9999284666561642, 1.000044737495996, 1.000025495458633),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairQnjtxe9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairQnjtxe9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.9990110397338867, 6.035500526428223, 0.4499833285808563),
            rot=(2.066604793071747e-06, 0.969759464263916, 0.2440629005432129, 6.202608346939087e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/qnjtxe/usd/qnjtxe.usd"),
            visual_material_path="materials",
            scale=(0.9999284666561642, 1.000044737495996, 1.000025495458633),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetFnoifb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetFnoifb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.9741452167813933, 12.081647594737115, 0.43018215848214825),
            rot=(-9.026351371326977e-08, 0.7071066023725725, 0.7071069600004474, -1.8509401262054125e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/fnoifb/usd/fnoifb.usd"),
            visual_material_path="materials",
            scale=(0.9999930614730963, 0.9999991678853888, 0.999998612065198),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    checkoutCounterHhvxxr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/checkoutCounterHhvxxr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.734999891869509, 2.117414654072434, 0.4490759941379728),
            rot=(4.371138834797026e-08, 0.0, 0.0, 0.9999999999999992),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/checkout_counter/hhvxxr/usd/hhvxxr.usd"),
            visual_material_path="materials",
            scale=(1.0000079784663969, 0.9999928774802358, 0.9999877068643198),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    checkoutCounterSckdal0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/checkoutCounterSckdal0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7368888761418364, 2.0660888102035844, 0.5243021984952884),
            rot=(6.123233995736766e-17, 1.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/checkout_counter/sckdal/usd/sckdal.usd"),
            visual_material_path="materials",
            scale=(0.9999941471065901, 0.999996844934082, 1.0000304632069597),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    receptionDeskVxombm0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/receptionDeskVxombm0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.003446639222281008, 4.434006052207308, 0.4042887441813946),
            rot=(0.7071069003958291, 0.0, 0.0, 0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/reception_desk/vxombm/usd/vxombm.usd"),
            visual_material_path="materials",
            scale=(1.000000953675226, 1.0000015055714422, 0.999999985098839),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorAbghjg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorAbghjg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.024998664855957, 12.530658721923828, 1.3039690256118774),
            rot=(-0.7071067690849304, -1.58033799380064e-08, 1.5856947754855355e-08, 0.70710688829422),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/abghjg/usd/abghjg.usd"),
            visual_material_path="materials",
            scale=(0.9999900488326513, 0.9999990803863262, 0.9999985140445522),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railFenceMnegtc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railFenceMnegtc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.7275244918457189, 1.8677903963173772, 0.42540095555704194),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/rail_fence/mnegtc/usd/mnegtc.usd"),
            visual_material_path="materials",
            scale=(0.9994786022586628, 1.0000236619042746, 1.0000311494723941),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railFenceMnegtc1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railFenceMnegtc1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.6967756895538477, 1.8638053301868418, 0.5029120955474109),
            rot=(-2.9047344016110615e-06, 0.0, 0.0, 0.9999999999957813),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/rail_fence/mnegtc/usd/mnegtc.usd"),
            visual_material_path="materials",
            scale=(1.1839618022082758, 1.2324406814785307, 1.1837077406759595),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureChfljy0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureChfljy0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.2266791794341712, 12.422077641706547, 1.6116569572531394),
            rot=(-0.7071066023725865, 1.754979704783613e-14, 6.181723324469579e-08, 0.7071069600004608),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/chfljy/usd/chfljy.usd"),
            visual_material_path="materials",
            scale=(0.9999880782818514, 1.0000008543339716, 1.000001947088854),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pillarXnxycq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pillarXnxycq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.000001716915601, 5.265190414068546, 1.565444772451491),
            rot=(0.9999999999963279, 0.0, 0.0, -2.7100046693468865e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pillar/xnxycq/usd/xnxycq.usd"),
            visual_material_path="materials",
            scale=(0.9999978268780014, 0.9999993902741694, 1.0000000307636887),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pillarXnxycq1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pillarXnxycq1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.9999996258593145, 5.265190414074251, 1.5654447724514913),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pillar/xnxycq/usd/xnxycq.usd"),
            visual_material_path="materials",
            scale=(0.9999978268780014, 0.9999993902741694, 1.0000000307636887),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.703593382741006, 1.5644550701347242, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.547557249931007, 1.564455070134724, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.547557249931007, 10.829359733219723, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.703593382741006, 10.829359733219725, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.860358397391006, 1.5644550701347242, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.704322874931006, 1.564455070134724, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.704322874931006, 3.4024223552897244, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd15 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd15",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.860358397391006, 3.4024223552897244, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd16 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd16",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.704322874931006, 5.309673942204725, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd17 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd17",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.860358397391006, 5.309673942204725, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd18 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd18",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.704322874931006, 7.147641227359725, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd19 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd19",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.860358397391006, 7.147641227359724, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.547557249931007, 3.4024223552897244, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd20 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd20",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.704322874931006, 8.991392936344726, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd21 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd21",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.860358397391006, 8.991392936344726, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd22 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd22",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.704322874931006, 10.829359733219725, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd23 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd23",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.860358397391006, 10.829359733219723, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd24 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd24",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.078101044748994, 1.5644550701347242, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd25 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd25",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7658632802060059, 1.5644550701347242, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd26 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd26",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.765863280206006, 3.4024223552897244, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd27 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd27",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.078101044748994, 3.4024223552897244, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd28 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd28",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7658632802060059, 5.309673942204724, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd29 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd29",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.078101044748994, 5.309673942204725, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.703593382741006, 3.4024223552897244, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd30 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd30",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7658632802060059, 7.147641227359725, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd31 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd31",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.078101044748994, 7.147641227359724, 2.697934585569726),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd32 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd32",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7658632802060059, 8.991392936344726, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd33 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd33",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.078101044748994, 8.991392936344726, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd34 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd34",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.765863280206006, 10.829359733219723, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd35 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd35",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.078101044748994, 10.829359733219725, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd36 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd36",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.642228882883995, 1.564455070134724, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd37 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd37",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.798264039133994, 1.5644550701347242, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd38 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd38",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.798264039133994, 3.4024223552897244, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd39 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd39",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.642228882883995, 3.4024223552897244, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.547557249931005, 5.309673942204724, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd40 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd40",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.798264039133994, 5.309673942204724, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd41 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd41",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.642228882883995, 5.309673942204724, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd42 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd42",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.798264039133994, 7.147641227359724, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd43 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd43",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.642228882883995, 7.147641227359725, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd44 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd44",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.798264039133994, 8.991392936344724, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd45 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd45",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.642228882883995, 8.991392936344726, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd46 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd46",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.798264039133994, 10.829359733219725, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd47 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd47",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.642228882883995, 10.829359733219723, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd48 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd48",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.089174317453994, 3.4024223552897244, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd49 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd49",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.089174317453994, 1.564455070134724, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.703593382741006, 5.309673942204725, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd50 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd50",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.933138550848994, 1.5644550701347242, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd51 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd51",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.933138550848994, 3.4024223552897244, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd52 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd52",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.089174317453994, 7.147641227359724, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd53 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd53",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.089174317453994, 5.309673942204725, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd54 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd54",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.933138550848994, 5.309673942204724, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd55 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd55",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.933138550848994, 7.147641227359725, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd56 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd56",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.089174317453994, 10.829359733219723, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd57 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd57",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.089174317453994, 8.991392936344726, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd58 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd58",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.933138550848994, 8.991392936344724, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd59 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd59",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.933138550848994, 10.829359733219725, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.547557249931005, 7.147641227359724, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.703593382741006, 7.147641227359724, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(8.547557249931007, 8.991392936344724, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightBypxxd9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightBypxxd9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.703593382741006, 8.991392936344724, 2.6979345855697265),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/bypxxd/usd/bypxxd.usd"),
            visual_material_path="materials",
            scale=(0.9999282653924013, 1.0000402994004833, 0.9999819699712769),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    structuralElementKebons0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/structuralElementKebons0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.6148886539716407, 10.887137280953384, 2.6008203773482914),
            rot=(-0.7071067215818997, 0.0, 0.0, 0.7071068407911903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/structural_element/kebons/usd/kebons.usd"),
            visual_material_path="materials",
            scale=(1.0000072452242998, 0.9999961754077703, 0.999999805690244),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    turnstileUzrfpq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/turnstileUzrfpq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.2026588916778564, 1.8661035299301147, 0.4511481523513794),
            rot=(-3.7023710319772363e-07, -0.7071067690849304, 0.7071069478988647, 3.688037395477295e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/turnstile/uzrfpq/usd/uzrfpq.usd"),
            visual_material_path="materials",
            scale=(1.0000013808151857, 0.9999733006043264, 0.9999796901510342),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    turnstileUzrfpq1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/turnstileUzrfpq1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.118455410003662, 1.8658101558685303, 0.45114806294441223),
            rot=(-1.6986086848191917e-07, -0.7071067690849304, 0.7071069478988647, 2.3096799850463867e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/turnstile/uzrfpq/usd/uzrfpq.usd"),
            visual_material_path="materials",
            scale=(1.0000013808151857, 0.9999733006043264, 0.9999796901510342),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfIruewm0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfIruewm0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.51023261945157, 12.127748720320579, 1.6537037548251592),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/iruewm/usd/iruewm.usd"),
            visual_material_path="materials",
            scale=(0.9999998360872537, 1.0000000031683531, 0.9999938756602571),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvNmquap0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvNmquap0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7053757353030531, 10.413991998805734, 2.1657780105346585),
            rot=(-0.7034215991846587, -0.07209684766110867, -0.07209704882678661, 0.7034217183939492),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/nmquap/usd/nmquap.usd"),
            visual_material_path="materials",
            scale=(1.000480149397019, 1.0000228809027405, 0.9999515387246224),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvNmquap1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvNmquap1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.6324279183204224, 10.413938437201242, 2.166035232821326),
            rot=(0.07209740991418198, -0.7034215006410912, 0.7034217986643013, 0.07209666485615666),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/nmquap/usd/nmquap.usd"),
            visual_material_path="materials",
            scale=(1.000480149397019, 1.0000228809027405, 0.9999515387246224),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvNmquap2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvNmquap2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.5627335844230927, 10.413992007706051, 2.165777789153679),
            rot=(-0.7034215991846587, -0.07209684766110867, -0.07209704882678661, 0.7034217183939492),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/nmquap/usd/nmquap.usd"),
            visual_material_path="materials",
            scale=(1.000480149397019, 1.0000228809027405, 0.9999515387246224),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
