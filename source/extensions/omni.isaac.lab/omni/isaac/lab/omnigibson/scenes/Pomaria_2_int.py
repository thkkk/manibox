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
class pomaria2IntquickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Pomaria_2_int/usd/Pomaria_2_int_quick.usd"),
        )
    )
@configclass
class pomaria2IntfullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Pomaria_2_int/usd/Pomaria_2_int_quick.usd"),
        )
    )
    armchairBslhmj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairBslhmj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.477130889892578, -2.2828595638275146, 0.3809846043586731),
            rot=(0.40203583240509033, -3.259629011154175e-09, -1.6530975699424744e-08, 0.9156239628791809),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/bslhmj/usd/bslhmj.usd"),
            visual_material_path="materials",
            scale=(1.0721674584059175, 1.2088652723221833, 1.2144517750219241),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairVzhxuf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairVzhxuf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.0165998935699463, 0.11365219950675964, 0.49512729048728943),
            rot=(0.8697778582572937, -0.0005243416526354849, -0.002855387283489108, 0.49343517422676086),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/vzhxuf/usd/vzhxuf.usd"),
            visual_material_path="materials",
            scale=(1.1189918266441832, 1.259006989170611, 1.0631359756704073),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableSkczfi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableSkczfi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.4453216791152954, 3.7547974586486816, 0.5178985595703125),
            rot=(0.7071066498756409, -8.330680429935455e-07, 2.491684881533729e-06, 0.7071070671081543),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(0.9609675028114812, 0.7416321070288617, 1.3312232736259184),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableSkczfi1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableSkczfi1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.4997974634170532, 1.809024453163147, 0.7170968651771545),
            rot=(-1.4901161193847656e-07, -1.4156103134155273e-06, -1.930078724399209e-06, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(0.7520542399094734, 1.0823928610039013, 1.8432482228005804),
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
            pos=(0.8000023365020752, 1.0346444845199585, 0.9471278190612793),
            rot=(1.0000001192092896, 0.00010711588402045891, -0.00015107309445738792, 1.0064205525850412e-05),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/vdxlda/usd/vdxlda.usd"),
            visual_material_path="materials",
            scale=(1.136974688413501, 1.174635729751024, 1.581745208650694),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantUdqjui0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantUdqjui0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.992274761199951, 1.3299531936645508, 0.591950535774231),
            rot=(-1.6540288925170898e-06, -0.00040666479617357254, -0.00028466677758842707, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/udqjui/usd/udqjui.usd"),
            visual_material_path="materials",
            scale=(1.8110235642496986, 1.7096045445964816, 1.9168469115558702),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantUdqjui1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantUdqjui1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.8583303689956665, 0.35626959800720215, 0.5919930934906006),
            rot=(0.7130739688873291, 5.1966169849038124e-05, 0.0003354032523930073, -0.7010888457298279),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/udqjui/usd/udqjui.usd"),
            visual_material_path="materials",
            scale=(1.220472401994362, 1.1805671944476064, 1.9168469115558702),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    potPlantUdqjui2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/potPlantUdqjui2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.8583303093910217, -0.09373024106025696, 0.5919934511184692),
            rot=(0.7130743265151978, 5.2024610340595245e-05, 0.0003355736844241619, -0.7010884881019592),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/udqjui/usd/udqjui.usd"),
            visual_material_path="materials",
            scale=(1.220472401994362, 1.1805671944476064, 1.9168469115558702),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    standingTvUdotid0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/standingTvUdotid0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.09147365391254425, 1.0605757236480713, 0.7218504548072815),
            rot=(1.0, 3.026798367500305e-09, 1.0231815394945443e-12, -2.7284841053187847e-12),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/standing_tv/udotid/usd/udotid.usd"),
            visual_material_path="materials",
            scale=(1.0442065276036754, 0.865490970189339, 1.1756532378786644),
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
            pos=(-0.6792545914649963, 5.039178848266602, 0.18866190314292908),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bathtub/fdjykf/usd/fdjykf.usd"),
            visual_material_path="materials",
            scale=(1.5505752900909169, 1.752300329459897, 1.11383127029956),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bedMpgavt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bedMpgavt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.3370097958766263, -1.901262463807973, 0.2588943656683102),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/mpgavt/usd/mpgavt.usd"),
            visual_material_path="materials",
            scale=(1.2176508797746974, 1.1887343292989279, 1.1166271543355137),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetRntwkg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetRntwkg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.5150831937789917, -2.809943914413452, 0.2537539005279541),
            rot=(1.9470718370939721e-07, 0.0, 0.0, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/rntwkg/usd/rntwkg.usd"),
            visual_material_path="materials",
            scale=(0.9470688838373641, 0.9423592733676317, 0.8647638505152566),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopQohxjq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopQohxjq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.21566349267959595, 1.762801170349121, 0.4752134680747986),
            rot=(-1.210719347000122e-08, 2.3283064365386963e-10, -4.4929038267582655e-10, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/qohxjq/usd/qohxjq.usd"),
            visual_material_path="materials",
            scale=(1.3070601297938071, 1.1879182474882555, 1.44663790212104),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopQohxjq1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopQohxjq1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.820816695690155, 3.1304538249969482, 0.4752134680747986),
            rot=(0.7074940800666809, 2.066371962428093e-09, 8.149072527885437e-10, -0.7067192792892456),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/qohxjq/usd/qohxjq.usd"),
            visual_material_path="materials",
            scale=(1.2814157863521138, 1.2755606084347035, 1.44663790212104),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    carpetCtclvd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/carpetCtclvd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.049375039097914, -0.1464666544175538, 0.0023726689250000003),
            rot=(0.708442746952273, 0.0, 0.0, 0.7057682865436202),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(2.008499334098612, 1.9004599670763798, 0.24480330607770978),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    carpetCtclvd1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/carpetCtclvd1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.5297988815350001, 3.29843664551, 0.0023726689250000007),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.1073521974901508, 2.4600176518289154, 0.24480330607770978),
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
            pos=(-4.154844760894775, 1.5741705894470215, 1.2662100791931152),
            rot=(0.7068235278129578, -2.9103830456733704e-11, -3.327116360196669e-12, 0.7073898911476135),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.175460897815606, 2.5740871380162087, 4.9799425513765065),
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
            pos=(-2.359714984893799, 2.6756227016448975, 1.2662101984024048),
            rot=(-0.7053542733192444, 0.0, 5.128342195348523e-12, 0.7088549137115479),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.6468206645382772, 4.0028629799184205, 4.9799425513765065),
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
            pos=(-3.2948460578918457, 2.559352159500122, 1.2662100791931152),
            rot=(0.7071069478988647, 0.0, 1.0947687201223744e-11, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(2.9598540096361803, 2.5740871380162087, 4.9799425513765065),
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
            pos=(-4.175301551818848, 0.024087434634566307, 1.0846130847930908),
            rot=(0.7071224451065063, 0.0, 0.0, 0.7070910930633545),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(2.294252974810241, 2.551611100996981, 3.111699687792625),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorOhagsq1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorOhagsq1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.175301551818848, -2.0459444522857666, 1.0846130847930908),
            rot=(0.7071248888969421, 0.0, 0.0, 0.7070886492729187),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(2.391321734361621, 2.551611100996981, 3.111699687792625),
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
            pos=(-3.4086713334965806, 2.2469388100294547, 1.200281898479443),
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

    electricSwitchWseglt1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.297866158940821, -1.0433331625998743, 1.200281898479443),
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

    electricSwitchWseglt2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.272540475345821, 0.9766630401940852, 1.2002819007529786),
            rot=(0.9999999999998268, -5.885487096944644e-07, 0.0, 0.0),
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

    electricSwitchWseglt3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.0183715288065995, 1.0869410072944545, 1.200281898479443),
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

    electricSwitchWseglt4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.7381946501508208, 3.1466651284151257, 1.200281898479443),
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

    electricSwitchWseglt5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.50735126513658, 2.2469388100294547, 1.200281898479443),
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

    electricSwitchWseglt6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.296229927246599, 1.0869413744539422, 1.2002818981281367),
            rot=(0.9999999999999878, 4.201701223427063e-08, 6.34439248214613e-15, 1.505306521099886e-07),
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
            pos=(0.05520385822353218, 1.5650275878138535, 1.5999997503510544),
            rot=(-1.192488079931532e-08, 0.0, 0.0, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(3.367394309650271, 3.0791628402428755, 2.0728551254756105),
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
            pos=(1.0462387391141776, 2.872333707250855, 1.5999997503510541),
            rot=(0.7082225626776829, 0.0, 0.0, -0.7059892362594883),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(4.510093651467279, 1.6983723289232004, 2.0728551254756105),
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
            pos=(-0.1497179260300776, 1.037150756966845, 0.291037266464479),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(2.728872780656359, 2.528850501619026, 1.3578765880841432),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfVgzdul0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfVgzdul0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.5691850256239785, -2.8917451085526973, 0.2569883288748836),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/vgzdul/usd/vgzdul.usd"),
            visual_material_path="materials",
            scale=(2.591561625973994, 2.520559112851507, 0.854680912407126),
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
            pos=(-3.891071122168567, 3.563866445801663, 1.2098174125871808),
            rot=(0.7112725147881342, 0.0, 0.0, 0.7029163603921619),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shower_stall/invgma/usd/invgma.usd"),
            visual_material_path="materials",
            scale=(1.432673394656066, 1.0862974836554489, 1.1653542935171972),
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
            pos=(0.7115182280540466, 2.4847898483276367, 0.41527754068374634),
            rot=(0.7071069478988647, 2.6193447411060333e-10, -3.6816345527768135e-09, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/ksecxq/usd/ksecxq.usd"),
            visual_material_path="materials",
            scale=(5.585029258444575, 4.728772452732608, 4.033506276597152),
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
            pos=(0.7115182876586914, 3.784789562225342, 0.41527754068374634),
            rot=(0.7071069478988647, 2.6193447411060333e-10, -3.6816345527768135e-09, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/ksecxq/usd/ksecxq.usd"),
            visual_material_path="materials",
            scale=(5.585029258444575, 4.728772452732608, 4.033506276597152),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    toiletWusctd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/toiletWusctd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.074436664581299, 3.6832973957061768, 0.36534881591796875),
            rot=(-0.7058520913124084, -1.4435499906539917e-08, 1.3562384992837906e-08, 0.7083593606948853),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/wusctd/usd/wusctd.usd"),
            visual_material_path="materials",
            scale=(1.269311611391002, 1.173959803536773, 1.3080027152501013),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetDmwxyl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetDmwxyl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.8562045097351074, 3.7161026000976562, 1.7012170553207397),
            rot=(0.7076455354690552, 2.3283064365386963e-10, 2.632987161632627e-10, -0.7065677642822266),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/dmwxyl/usd/dmwxyl.usd"),
            visual_material_path="materials",
            scale=(1.8506526312757252, 0.9932531775298874, 2.2160692313136283),
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
            pos=(-1.5077557563781738, -3.104421854019165, 1.3728241920471191),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ithrgo/usd/ithrgo.usd"),
            visual_material_path="materials",
            scale=(3.345209866993256, 1.6715815117317196, 1.8905791771379403),
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
            pos=(1.1437302827835083, -1.7860321998596191, 1.3728241920471191),
            rot=(0.7073166370391846, 0.0, 6.475602276623249e-10, -0.706896960735321),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ithrgo/usd/ithrgo.usd"),
            visual_material_path="materials",
            scale=(1.6136482424648038, 1.4324264040607395, 1.8905791771379403),
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
            pos=(-2.755429744720459, 4.232533931732178, 1.3262299299240112),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.3616870123037417, 1.199273216095818, 1.942816132621917),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
