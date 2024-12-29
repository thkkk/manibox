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
class benevolence2IntquickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Benevolence_2_int/usd/Benevolence_2_int_quick.usd"),
        )
    )
@configclass
class benevolence2IntfullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Benevolence_2_int/usd/Benevolence_2_int_quick.usd"),
        )
    )
    bottomCabinetBamfsz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.3673605918884277, -2.9734790325164795, 0.42897626757621765),
            rot=(0.7071068286895752, -6.593763828277588e-07, -5.42087946087122e-07, 0.7071068286895752),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.2690678248176637, 1.1508304476875855, 1.5467592120410023),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetJrhgeu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetJrhgeu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6803845167160034, -7.555323123931885, 0.5088873505592346),
            rot=(-1.4469027519226074e-05, 6.604939699172974e-06, -0.004678572993725538, 0.9999891519546509),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jrhgeu/usd/jrhgeu.usd"),
            visual_material_path="materials",
            scale=(1.2244818390638017, 1.4381301502438182, 1.4452692361744237),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetSlgzfc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetSlgzfc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.3530765771865845, -4.654350280761719, 0.424114465713501),
            rot=(0.7071069478988647, 4.6566128730773926e-08, -2.8976501198485494e-09, 0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/slgzfc/usd/slgzfc.usd"),
            visual_material_path="materials",
            scale=(2.247565819216118, 1.255912990004733, 1.5467576823431897),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableBmnubh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableBmnubh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.1350035667419434, 0.04397040605545044, 0.6453919410705566),
            rot=(-0.7044896483421326, -2.3283064365386963e-10, -2.7284841053187847e-10, 0.7097142934799194),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/bmnubh/usd/bmnubh.usd"),
            visual_material_path="materials",
            scale=(0.7550673401417789, 1.0773668911812606, 2.005665789182146),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    floorLampVdxlda0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/floorLampVdxlda0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.1698062419891357, -8.035165786743164, 1.0358933210372925),
            rot=(1.0, 0.00010601545363897458, -0.00014064366405364126, 3.154629212076543e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/vdxlda/usd/vdxlda.usd"),
            visual_material_path="materials",
            scale=(1.2883684408352385, 1.2503327861695646, 1.7299901176842694),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfOwvfik0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfOwvfik0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.320040225982666, -7.472720146179199, 0.4841166138648987),
            rot=(4.7497451305389404e-07, -2.2691558115184307e-05, -3.6373148759594187e-07, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(0.637932143468125, 1.8656000899917624, 2.2632040264102398),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairMhsjfu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairMhsjfu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.8093909025192261, 0.28153830766677856, 0.493746817111969),
            rot=(0.8455113172531128, -0.00033321414957754314, -0.00046771529014222324, 0.5339571833610535),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/mhsjfu/usd/mhsjfu.usd"),
            visual_material_path="materials",
            scale=(0.5134375114762227, 0.6300129208160357, 0.9487983109567828),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    trashCanZotrbg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/trashCanZotrbg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.3002175092697144, 0.5861706137657166, 0.17370650172233582),
            rot=(0.999993085861206, -0.0036694626323878765, 0.0007017404423095286, 9.732840226206463e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/trash_can/zotrbg/usd/zotrbg.usd"),
            visual_material_path="materials",
            scale=(0.6181211160210752, 0.42125984319754445, 0.7855449201192258),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    trashCanZotrbg1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/trashCanZotrbg1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.779934048652649, 1.6504050493240356, 0.1737099587917328),
            rot=(0.9999975562095642, -0.0020633323583751917, 0.0007443894282914698, 2.2367870769812725e-05),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/trash_can/zotrbg/usd/zotrbg.usd"),
            visual_material_path="materials",
            scale=(0.6181211160210752, 0.7303149618050887, 0.7855449201192258),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bathtubFdjykf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bathtubFdjykf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.650359034538269, -2.265313148498535, 0.15093444287776947),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bathtub/fdjykf/usd/fdjykf.usd"),
            visual_material_path="materials",
            scale=(1.3524015915300742, 0.8893624825225251, 0.8909744240257157),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bedFnzxxr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bedFnzxxr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.6722397964994818, 1.2630189508633691, 0.15446391570898405),
            rot=(0.7074708718016787, 0.0, 0.0, 0.7067425030038683),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/fnzxxr/usd/fnzxxr.usd"),
            visual_material_path="materials",
            scale=(0.6861443926612606, 0.970373984779227, 0.9530489588900595),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bedZrumze0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bedZrumze0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.47128812138418497, -6.541559984405713, 0.34492716657938005),
            rot=(-0.7062953651758864, 0.0, 0.0, 0.7079172671513679),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/zrumze/usd/zrumze.usd"),
            visual_material_path="materials",
            scale=(1.0495472888637387, 1.027116108952594, 1.2101913027179412),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopTpuwys0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopTpuwys0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7499963836650001, -3.935244628905, 1.6206307983400001),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.1321846286851573, 0.4098085160826456, 1.1748032499552672),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopTpuwys1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopTpuwys1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.3046747437712314, 1.0750015929062222, 1.425788635255),
            rot=(0.7087804610942684, 0.0, 0.0, -0.7054291303674638),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.0848022369615415, 0.5428212670319406, 1.467716660802023),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    cribOimydv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/cribOimydv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.027818762351552, -4.8448807277241785, 0.45570249044935274),
            rot=(0.7085140444357364, 0.0, 0.0, -0.7056967116526159),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/crib/oimydv/usd/oimydv.usd"),
            visual_material_path="materials",
            scale=(0.9432039227490988, 1.0699937973336122, 1.1290669624244722),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6200453042984009, -0.6055794358253479, 1.151099443435669),
            rot=(0.7071068286895752, -2.9103830456733704e-11, 9.745093620949774e-12, 0.7071068286895752),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.8582767578492083, 2.2877593139877095, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6199514865875244, 0.40525147318840027, 1.151099443435669),
            rot=(-0.7039709687232971, 2.9103830456733704e-11, -2.19912976717751e-11, 0.7102287411689758),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.650008444839447, 2.2877593139877095, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6199582815170288, -1.4886837005615234, 1.151099443435669),
            rot=(0.708427906036377, 0.0, -1.0464518140906875e-11, -0.7057833075523376),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(2.9582601194855953, 2.2877593139877095, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.0901191234588623, -5.669933319091797, 1.151099443435669),
            rot=(1.0, 4.405364961712621e-13, -7.831624238008317e-12, -0.00036811831523664296),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.7004816329413024, 3.4302073318614217, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.5800678730010986, -6.853010177612305, 1.151099443435669),
            rot=(0.7071069478988647, -2.9103830456733704e-11, -2.610711646866548e-11, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.4087997353842634, 3.4302073318614217, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.3393833339214325, -4.095061302185059, 1.151099443435669),
            rot=(1.9470462575554848e-07, 0.0, -3.268496584496461e-13, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.122331226129442, 3.146742786073207, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorOhagsq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorOhagsq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.20077946782112122, -1.0982146263122559, 0.9860119819641113),
            rot=(0.002840709872543812, 0.0, 0.0, 0.9999960660934448),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(2.1852634904016743, 2.2661766388515563, 2.8287788690487865),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    clothesDryerZlmnfg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/clothesDryerZlmnfg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.1633474826812744, -0.6143415570259094, 1.4169716835021973),
            rot=(0.7062118053436279, 0.0, 1.5127170627238229e-09, 0.7080007791519165),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/clothes_dryer/zlmnfg/usd/zlmnfg.usd"),
            visual_material_path="materials",
            scale=(1.133858560212026, 1.5872356366138043, 0.9225526620981678),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.518074899170821, -5.612853060059875, 1.200281898479443),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(1.0000102542942477, 1.0001117672368374, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6601462162426812, 0.8260636442441732, 1.200281898479443),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(0.4737581388454376, 2.111039242754765, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6601442631176813, -1.096467300575827, 1.200281898479443),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(0.4737581388454376, 2.111039242754765, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.8065091032758207, -1.1231299274934312, 1.2002819005619152),
            rot=(0.9999999999998535, -5.413860715801801e-07, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(1.0000102542942477, 1.0001117672368374, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.1491412923884197, -4.042857088410544, 1.200281898479443),
            rot=(0.9999999999999887, 0.0, 0.0, 1.5049435106459336e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(1.0000102542942477, 1.0001117672368374, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.5198685062826813, -5.828757095500827, 1.200281898479443),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(0.4737581388454376, 2.111039242754765, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.6401456058876813, -7.272885513470827, 1.200281898479443),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(0.4737581388454376, 2.111039242754765, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchWseglt7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.5036294658250426, -1.0428552572942034, 1.200281898479443),
            rot=(0.9999999999999887, 0.0, 0.0, -1.5049435106459336e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(1.0000102542942477, 1.0001117672368374, 0.9999999550488176),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorPevdqu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorPevdqu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.5390010375950463, -4.63786645508, 1.299999768361972),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(0.13960105247550086, 28.57776094927954, 1.0363400931148212),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorPevdqu1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorPevdqu1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.674768920894991, 0.3499997463246079, 1.5499997135779582),
            rot=(0.7071069003958291, 0.0, 0.0, 0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(1.1864340073795074, 3.0791628402428755, 1.5545101396722316),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureEtixod0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureEtixod0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.645210240629119, -0.014452511640767877, 1.6498507745232303),
            rot=(0.003977125347584504, 0.0, 0.0, 0.9999920912057103),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/etixod/usd/etixod.usd"),
            visual_material_path="materials",
            scale=(0.8308582844665133, 1.22816416846137, 1.704167846940927),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureFanvpf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureFanvpf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6727165143374663, -3.3700001581185406, 1.700245235190389),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/fanvpf/usd/fanvpf.usd"),
            visual_material_path="materials",
            scale=(0.8729990433662717, 1.1028412941285772, 1.2949702259323224),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureQjkajj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureQjkajj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.671170026115802, -2.7500221868240917, 1.6502857352616866),
            rot=(0.7084564300259695, 0.0, 0.0, -0.7057545513525638),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/qjkajj/usd/qjkajj.usd"),
            visual_material_path="materials",
            scale=(0.7567838708987723, 1.1028412941285772, 1.510782534901735),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureWfdvzv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureWfdvzv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.6849990963185968, -4.162715759775895, 1.6751591863091966),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/wfdvzv/usd/wfdvzv.usd"),
            visual_material_path="materials",
            scale=(0.8002369717711872, 1.1028412941285772, 0.8427804404862955),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfOwvfik1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfOwvfik1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.1796306868558688, -4.8250678745505065, 1.6697713263263025),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(2.3921567884028714, 1.5752197276147508, 0.7921328661840842),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    showerStallInvgma0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/showerStallInvgma0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.2080822293337405, 1.4754074884658561, 1.008180877197743),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shower_stall/invgma/usd/invgma.usd"),
            visual_material_path="materials",
            scale=(1.1556898716892263, 1.0233079467623507, 0.9711121737320462),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkKsecxq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkKsecxq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.2426856756210327, -3.6399941444396973, 0.3922041654586792),
            rot=(0.7071069478988647, -9.89530235528946e-10, 8.294591680169106e-10, 0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/ksecxq/usd/ksecxq.usd"),
            visual_material_path="materials",
            scale=(5.37242822081821, 4.167581969802202, 3.8096994585988377),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkKsecxq1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkKsecxq1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.242686152458191, -2.3099942207336426, 0.3922041654586792),
            rot=(0.7071069478988647, -9.89530235528946e-10, 8.294591680169106e-10, 0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/ksecxq/usd/ksecxq.usd"),
            visual_material_path="materials",
            scale=(5.37242822081821, 4.167581969802202, 3.8096994585988377),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkKsecxq2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkKsecxq2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.3194077014923096, 0.3510149121284485, 0.46142032742500305),
            rot=(0.7099296450614929, 3.914465196430683e-09, 2.852175384759903e-09, 0.7042726278305054),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/ksecxq/usd/ksecxq.usd"),
            visual_material_path="materials",
            scale=(5.246284938493234, 5.025023222691578, 4.481572962832644),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    toiletChuack0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/toiletChuack0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.1859664916992188, 1.5150456428527832, 0.29816675186157227),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/chuack/usd/chuack.usd"),
            visual_material_path="materials",
            scale=(1.1317607708999489, 1.1669033086027447, 1.1733394696608253),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    toiletKfmkbm0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/toiletKfmkbm0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.9446253776550293, -3.7407288551330566, 0.30865713953971863),
            rot=(-0.0030673258006572723, 0.0, 1.5064870240166783e-08, 0.9999953508377075),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/kfmkbm/usd/kfmkbm.usd"),
            visual_material_path="materials",
            scale=(1.367174188457722, 1.183942162223935, 1.1551359314283232),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    towelRackKqrmrh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/towelRackKqrmrh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.30204302420361895, -2.2700008233508773, 1.3200418655299722),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/towel_rack/kqrmrh/usd/kqrmrh.usd"),
            visual_material_path="materials",
            scale=(1.369921556724476, 1.0325864343157334, 0.6218834932011146),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    towelRackKqrmrh1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/towelRackKqrmrh1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6857606457247967, 1.49999939957665, 1.2200418655299723),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/towel_rack/kqrmrh/usd/kqrmrh.usd"),
            visual_material_path="materials",
            scale=(0.967785335083193, 0.8243337080671821, 0.6218834932011146),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvYlvjhb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvYlvjhb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.2641735076904297, -4.5385847091674805, 1.868840217590332),
            rot=(0.9297184944152832, 0.0, 0.0, 0.3682708740234375),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/ylvjhb/usd/ylvjhb.usd"),
            visual_material_path="materials",
            scale=(0.9980540411916419, 0.23377172706115332, 0.6133326996703866),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    washerOmeuop0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/washerOmeuop0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.228666305541992, -0.6169205904006958, 0.5152084827423096),
            rot=(0.7062118053436279, 2.7939677238464355e-09, -6.28642737865448e-09, 0.708000659942627),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/washer/omeuop/usd/omeuop.usd"),
            visual_material_path="materials",
            scale=(1.127293708196312, 1.8210489618452588, 1.1712596528119064),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowIthrgo0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowIthrgo0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.06743767857551575, 1.8612778186798096, 1.4431250095367432),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ithrgo/usd/ithrgo.usd"),
            visual_material_path="materials",
            scale=(1.1587269971407763, 1.1945234173723298, 1.5013621965241501),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowIthrgo1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowIthrgo1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.3524238169193268, -8.450340270996094, 1.3187965154647827),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ithrgo/usd/ithrgo.usd"),
            visual_material_path="materials",
            scale=(1.1521653175601614, 1.5526300183875148, 1.5569807389712804),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.229844331741333, 1.8527380228042603, 1.4058278799057007),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.6984042619354955, 1.199273216095818, 0.4316762811527911),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
