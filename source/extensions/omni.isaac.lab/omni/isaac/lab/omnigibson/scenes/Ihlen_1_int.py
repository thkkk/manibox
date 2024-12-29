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
class ihlen1IntquickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Ihlen_1_int/usd/Ihlen_1_int_quick.usd"),
        )
    )
@configclass
class ihlen1IntfullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Ihlen_1_int/usd/Ihlen_1_int_quick.usd"),
        )
    )
    armchairBslhmj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairBslhmj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.397499442100525, -1.102559208869934, 0.3112495541572571),
            rot=(0.07111644744873047, -2.3283064365386963e-10, 4.5693013817071915e-09, 0.997468113899231),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/bslhmj/usd/bslhmj.usd"),
            visual_material_path="materials",
            scale=(0.793518450339995, 0.8975406899532368, 0.9108080482446693),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairBslhmj1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairBslhmj1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.999676465988159, -1.0617810487747192, 0.31124958395957947),
            rot=(-0.16004812717437744, 1.3969838619232178e-09, -1.3154931366443634e-08, 0.9871093034744263),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/bslhmj/usd/bslhmj.usd"),
            visual_material_path="materials",
            scale=(0.793518450339995, 0.8975406899532368, 0.9108080482446693),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairTcxiue0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairTcxiue0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7834811210632324, 2.016514301300049, 0.5224981307983398),
            rot=(0.9809646010398865, 0.00042682490311563015, 8.316291496157646e-05, 0.19418683648109436),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/tcxiue/usd/tcxiue.usd"),
            visual_material_path="materials",
            scale=(1.078498526196415, 1.0033427644227146, 1.0646395568791862),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.687422752380371, 8.22443675994873, 0.3532519042491913),
            rot=(-0.7049995064735413, -1.993030309677124e-07, 4.858680767938495e-06, 0.7092079520225525),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.1122924255219238, 0.8592043165931483, 1.2737257921324534),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetBamfsz1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetBamfsz1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.7174296379089355, 10.404434204101562, 0.35325339436531067),
            rot=(-0.7049994468688965, 3.0463561415672302e-06, 8.892093319445848e-07, 0.709208071231842),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.1122924255219238, 0.8592043165931483, 1.2737257921324534),
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
            pos=(2.005131721496582, 2.8619422912597656, 0.30542075634002686),
            rot=(0.0015546288341283798, 3.0882656574249268e-06, -0.003664181334897876, 0.9999921321868896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jrhgeu/usd/jrhgeu.usd"),
            visual_material_path="materials",
            scale=(0.6851545755811654, 1.0003975245001089, 0.8670738699281195),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetJrhgeu1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetJrhgeu1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.405265808105469, 2.854586362838745, 0.30457261204719543),
            rot=(-8.568167686462402e-08, 6.974674761295319e-06, -0.00643389904871583, 0.9999794363975525),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jrhgeu/usd/jrhgeu.usd"),
            visual_material_path="materials",
            scale=(0.6851545755811654, 1.0003975245001089, 0.8670738699281195),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetJrhgeu2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetJrhgeu2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.205198049545288, -1.3884406089782715, 0.4081771671772003),
            rot=(0.0017269393429160118, 3.885477781295776e-06, -0.0014966242015361786, 0.9999974966049194),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jrhgeu/usd/jrhgeu.usd"),
            visual_material_path="materials",
            scale=(1.0944354384949733, 1.2781291690170404, 1.1562446128650505),
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
            pos=(-2.2344086170196533, 10.566604614257812, 0.3983904719352722),
            rot=(1.0, -9.201990906149149e-06, 3.515769640216604e-05, -1.623710704734549e-05),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(0.35935761742165745, 0.7617359863194246, 1.024049898349324),
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
            pos=(-4.454451560974121, 10.610631942749023, 0.39839550852775574),
            rot=(1.0, -1.0003350325860083e-06, 2.854966623999644e-06, -9.675422916188836e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(0.35935761742165745, 0.7617359863194246, 1.024049898349324),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableUhrsex0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableUhrsex0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.9095346927642822, 1.8646214008331299, 0.6176699995994568),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/uhrsex/usd/uhrsex.usd"),
            visual_material_path="materials",
            scale=(1.6662746316951704, 1.5232030995611185, 1.7776993210722614),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    cedarChestFwstpx0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/cedarChestFwstpx0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.5625817775726318, 9.214261054992676, 0.11766231805086136),
            rot=(0.7055678963661194, 5.820766091346741e-11, 7.275957614183426e-12, 0.7086426019668579),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/cedar_chest/fwstpx/usd/fwstpx.usd"),
            visual_material_path="materials",
            scale=(1.4350437828240084, 1.0113345245592633, 1.3423230666762191),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    cedarChestFwstpx1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/cedarChestFwstpx1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.2755026817321777, 5.177698612213135, 0.15618401765823364),
            rot=(0.0020081549882888794, 0.0, 3.115019353572279e-10, 0.9999980926513672),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/cedar_chest/fwstpx/usd/fwstpx.usd"),
            visual_material_path="materials",
            scale=(1.845002856452345, 1.2284968598601118, 1.9177151611151297),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    cedarChestFwstpx2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/cedarChestFwstpx2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.3920897245407104, 9.860076904296875, 0.15618398785591125),
            rot=(0.7071070075035095, 0.0, -7.003109203651547e-11, -0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/cedar_chest/fwstpx/usd/fwstpx.usd"),
            visual_material_path="materials",
            scale=(0.9317591719052796, 1.2410351009282903, 1.9177151611151297),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    cedarChestFwstpx3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/cedarChestFwstpx3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.3671578168869019, 10.557577133178711, 0.11766228079795837),
            rot=(0.70710688829422, 5.820766091346741e-10, -1.8025048120762222e-10, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/cedar_chest/fwstpx/usd/fwstpx.usd"),
            visual_material_path="materials",
            scale=(0.8292694034981954, 1.2159586187919336, 1.3423230666762191),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coffeeTableGcollb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coffeeTableGcollb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.8605399131774902, 0.7549685835838318, 0.3404593765735626),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/gcollb/usd/gcollb.usd"),
            visual_material_path="materials",
            scale=(0.9079331739706812, 1.1087904415223155, 1.0916110634813054),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    floorLampJqsuky0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/floorLampJqsuky0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.476180553436279, 2.1874287128448486, 0.587406575679779),
            rot=(1.000000238418579, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/jqsuky/usd/jqsuky.usd"),
            visual_material_path="materials",
            scale=(2.618198989745777, 2.049139672278632, 2.113602175055458),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaXhxdqf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaXhxdqf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.717698097229004, 2.1367084980010986, 0.33491387963294983),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/xhxdqf/usd/xhxdqf.usd"),
            visual_material_path="materials",
            scale=(1.0542514402187035, 1.0690359263799123, 1.0273866407009256),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairEnuago0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairEnuago0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.6096993684768677, 10.372477531433105, 0.5495724678039551),
            rot=(0.8847296833992004, 0.00041878363117575645, -0.0009285099804401398, 0.4661036431789398),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/enuago/usd/enuago.usd"),
            visual_material_path="materials",
            scale=(1.1259547705200474, 1.1003001009013356, 1.141104097464934),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairEnuago1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairEnuago1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.365039825439453, 7.76556921005249, 0.5580676794052124),
            rot=(0.29874950647354126, 1.3969838619232178e-09, 4.6333298087120056e-08, 0.954331636428833),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/enuago/usd/enuago.usd"),
            visual_material_path="materials",
            scale=(1.1259547705200474, 1.1003001009013356, 1.103028834354375),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairHwpixe0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairHwpixe0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.7042616605758667, 6.0261640548706055, 0.4096618592739105),
            rot=(0.9320442080497742, 8.106893801596016e-06, 1.139793312177062e-06, 0.36234480142593384),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/hwpixe/usd/hwpixe.usd"),
            visual_material_path="materials",
            scale=(1.3173835287947488, 1.1447197671726999, 1.1380272215667697),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairPmpwwi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairPmpwwi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.547504425048828, 2.4311866760253906, 0.5178982615470886),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/pmpwwi/usd/pmpwwi.usd"),
            visual_material_path="materials",
            scale=(1.1728549616151702, 1.089088462775831, 1.2299464720399902),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairPmpwwi1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairPmpwwi1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.2875049114227295, 2.4311861991882324, 0.5178982615470886),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/pmpwwi/usd/pmpwwi.usd"),
            visual_material_path="materials",
            scale=(1.1728549616151702, 1.089088462775831, 1.2299464720399902),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairPmpwwi2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairPmpwwi2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.581279993057251, 1.2390060424804688, 0.5178982615470886),
            rot=(-0.001730278367176652, 0.0, 2.0745574147440493e-09, 0.9999984502792358),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/pmpwwi/usd/pmpwwi.usd"),
            visual_material_path="materials",
            scale=(1.1728549616151702, 1.089088462775831, 1.2299464720399902),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairPmpwwi3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairPmpwwi3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.2812798023223877, 1.259006142616272, 0.5178982615470886),
            rot=(-0.001730278367176652, 0.0, 2.0745574147440493e-09, 0.9999984502792358),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/pmpwwi/usd/pmpwwi.usd"),
            visual_material_path="materials",
            scale=(1.1728549616151702, 1.089088462775831, 1.2299464720399902),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampXbfgjc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampXbfgjc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.675613880157471, 8.254728317260742, 0.9261608123779297),
            rot=(-0.7052009105682373, -0.00020343891810625792, -4.246639582561329e-05, 0.7090075612068176),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(1.698620220313959, 1.8342980299185432, 2.0538011532151943),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampXbfgjc1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampXbfgjc1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.665650844573975, 10.37474536895752, 0.9261684417724609),
            rot=(-0.7052488327026367, -0.0001486387336626649, -7.36593792680651e-05, 0.7089599370956421),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(1.698620220313959, 1.8342980299185432, 2.0538011532151943),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampXbfgjc2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampXbfgjc2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.040173053741455, 2.9273321628570557, 0.7949036955833435),
            rot=(1.94646418094635e-07, 0.0, 8.731149137020111e-11, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(2.1739065685912893, 1.4947142310711696, 1.6420406947377972),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampXbfgjc3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampXbfgjc3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.400173187255859, 2.889984607696533, 0.7765501141548157),
            rot=(1.94646418094635e-07, 0.0, 8.731149137020111e-11, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(2.1739065685912893, 1.4947142310711696, 1.6420406947377972),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampXbfgjc4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampXbfgjc4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.443996429443359, 10.620220184326172, 0.6939685344696045),
            rot=(1.0000001192092896, 7.056249160086736e-05, 0.00012913777027279139, -9.143175702774897e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(2.3777955472640606, 2.1738818287659165, 1.6970532256274902),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampXbfgjc5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampXbfgjc5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.243917465209961, 10.56614875793457, 0.6939576864242554),
            rot=(1.0000001192092896, 0.00016404241614509374, 0.00022023475321475416, 1.3827211660100147e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(2.3777955472640606, 2.1738818287659165, 1.6970532256274902),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampXbfgjc6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampXbfgjc6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.040313720703125, -1.2980647087097168, 1.0164294242858887),
            rot=(-0.006041824817657471, 1.1641532182693481e-10, 2.9103830456733704e-11, 0.9999818205833435),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(1.3590325568389083, 1.4265247132303316, 1.7792941808969296),
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
            pos=(-0.49438273906707764, 10.148993492126465, 0.1320711076259613),
            rot=(0.7043923735618591, 0.0, -1.235548552358523e-09, 0.7098109126091003),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bathtub/fdjykf/usd/fdjykf.usd"),
            visual_material_path="materials",
            scale=(1.2555608260171256, 0.9276648583454491, 0.7795460008887933),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bedSmmmaf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bedSmmmaf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.309880417768537, 9.98345824944973, 0.3527554202089611),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/smmmaf/usd/smmmaf.usd"),
            visual_material_path="materials",
            scale=(0.8320652671436679, 1.410258316481783, 1.4557086149594045),
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
            pos=(3.943977982876311, 9.377531413871225, 0.46883205294667785),
            rot=(0.7077085913834887, 0.0, 0.0, -0.7065044583596045),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/zrumze/usd/zrumze.usd"),
            visual_material_path="materials",
            scale=(0.9763964000259564, 1.0528542971075556, 1.6449307370707549),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bedZrumze2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bedZrumze2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.1815386633052913, 3.680792600133533, 0.4520885908604193),
            rot=(0.0009451666568634094, 0.0, 0.0, 0.9999995533298957),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/zrumze/usd/zrumze.usd"),
            visual_material_path="materials",
            scale=(1.0224670629116075, 1.0436023288988887, 1.5861789109937199),
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
            pos=(-1.9892805814743042, 6.0882463455200195, 0.45000001788139343),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/slgzfc/usd/slgzfc.usd"),
            visual_material_path="materials",
            scale=(0.602478633362262, 1.542240841654608, 1.6378301847362213),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetSlgzfc1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetSlgzfc1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.089280605316162, 6.068246364593506, 0.45000001788139343),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/slgzfc/usd/slgzfc.usd"),
            visual_material_path="materials",
            scale=(0.602478633362262, 1.542240841654608, 1.6378301847362213),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopBmsclc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopBmsclc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.817144870758057, 4.268896579742432, 0.47712916135787964),
            rot=(0.7062403559684753, -3.725290298461914e-09, 2.9103830456733704e-11, 0.7079722285270691),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/bmsclc/usd/bmsclc.usd"),
            visual_material_path="materials",
            scale=(1.1515590723406108, 1.256575192262587, 1.4873191692003036),
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
            pos=(-4.218715667724609, 3.807856559753418, 0.47521382570266724),
            rot=(1.955777406692505e-07, 0.0, 3.4797267289832234e-09, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/qohxjq/usd/qohxjq.usd"),
            visual_material_path="materials",
            scale=(1.332437344657983, 1.2826249800978933, 1.44663790212104),
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
            pos=(-3.7287540435791016, 3.807856321334839, 0.47521382570266724),
            rot=(1.9371509552001953e-07, -4.656612873077393e-10, -2.3137545213103294e-09, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/qohxjq/usd/qohxjq.usd"),
            visual_material_path="materials",
            scale=(1.2255859136509273, 1.2826249800978933, 1.44663790212104),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopUfhpbn0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopUfhpbn0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.830626010894775, 6.000043869018555, 0.4895991384983063),
            rot=(0.70710688829422, -1.5075727333169198e-09, 1.8391510536730493e-10, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/ufhpbn/usd/ufhpbn.usd"),
            visual_material_path="materials",
            scale=(0.9495222763111142, 0.9499020801215193, 0.9729877712177613),
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
            pos=(-3.424461791995, 8.10926904297, 0.0023729740949999995),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(2.0274381995477615, 1.486268719081297, 0.24480330607770978),
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
            pos=(-0.32567156967377037, 5.088245239297604, 0.0023729740949999995),
            rot=(-0.7066687899038125, 0.0, 0.0, 0.7075445013395845),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.934131633994408, 1.017178444438453, 0.24480330607770978),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    carpetCtclvd2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/carpetCtclvd2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.939460998535, 1.8338098144500001, 0.002372974095),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(2.24727597823121, 2.3191616984814902, 0.24480330607770978),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    carpetCtclvd3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/carpetCtclvd3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.660539794924999, 0.5189866790749998, 0.002372974094999999),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.9704583371188547, 1.998788505414976, 0.24480330607770978),
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
            pos=(-3.0094560546849998, 6.139686523435, 2.010315612795),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.42947634812293856, 0.6769110443047116, 0.5858268216935112),
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
            pos=(-3.0094560546849998, 6.139686523435, 1.660315734865),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.42947634812293856, 0.6769110443047116, 0.5858268216935112),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopTpuwys2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopTpuwys2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.77445629883, 4.259856933595, 0.9103157348650001),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.5563515127382402, 0.3918580773580444, 0.5858268216935112),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopTpuwys3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopTpuwys3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.2794591064450005, 3.8544631347650005, 0.9103157348650001),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.522599872887181, 1.0509981873254008, 0.5858268216935112),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopTpuwys4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopTpuwys4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.7744562988300006, 5.689133056639999, 0.9103157348650001),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.5563515127382402, 1.60333318688138, 0.5858268216935112),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopTpuwys5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopTpuwys5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.86945968628, 3.519345947265, 0.88111550903),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.659264787858602, 1.247016978198046, 1.1433071842728204),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    countertopTpuwys6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/countertopTpuwys6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.8744595336899998, 3.44463330078, 0.44356701851),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.649475037502483, 0.7659452203787337, 25.231498218208166),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    dishwasherDngvvi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/dishwasherDngvvi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.799849987030029, 5.534269332885742, 0.4602765440940857),
            rot=(0.7066361308097839, 2.561137080192566e-09, -1.1641532182693481e-10, 0.7075771689414978),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/dishwasher/dngvvi/usd/dngvvi.usd"),
            visual_material_path="materials",
            scale=(1.1508947313284332, 1.0467149228204164, 1.2446790448194136),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorKtydvs0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorKtydvs0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.145988941192627, 6.837808132171631, 1.1368627548217773),
            rot=(0.7086693048477173, 0.0, -1.7143975128419697e-10, 0.7055407762527466),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ktydvs/usd/ktydvs.usd"),
            visual_material_path="materials",
            scale=(4.885839165557266, 5.385826369976072, 5.30375420379901),
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
            pos=(-0.9395303130149841, -0.6107699275016785, 1.2086513042449951),
            rot=(0.7058908343315125, 5.820766091346741e-11, -5.0249582272954285e-11, 0.7083207964897156),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.75776209949596, 4.0028629799184205, 4.753456614500236),
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
            pos=(-0.9393729567527771, 7.865919589996338, 1.1510998010635376),
            rot=(-0.7045915126800537, 0.0, -7.16582349014061e-12, 0.7096131443977356),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.756267788211774, 4.0028629799184205, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.6949434280395508, 7.315030097961426, 1.1510998010635376),
            rot=(1.9470462575554848e-07, 0.0, -3.659295089164516e-13, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.5533124423706286, 3.146742786073207, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.183879375457764, 6.490148544311523, 1.1510998010635376),
            rot=(0.9999979734420776, 5.684341886080802e-14, -6.928291274022058e-12, -0.002012490062043071),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.5533124423706286, 2.860414962044708, 4.527199682615753),
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
            pos=(-3.1943793296813965, 6.905660152435303, 1.1495912075042725),
            rot=(-0.7050483226776123, 2.9103830456733704e-11, 1.5784706874910626e-11, 0.7091593146324158),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.805678382879907, 3.716535155889921, 4.5354438623200455),
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
            pos=(-1.3951725959777832, 7.365021228790283, 1.1510998010635376),
            rot=(-0.0021533512044698, 2.9103830456733704e-11, 5.471179065352771e-13, 0.9999977350234985),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.3381372720416658, 3.716535155889921, 4.527199682615753),
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
            pos=(0.6149435043334961, 8.380012512207031, 1.1510998010635376),
            rot=(1.9470462575554848e-07, 0.0, -4.192202140984591e-13, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.5533124423706286, 4.0028629799184205, 4.527199682615753),
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
            pos=(1.2354848384857178, 7.832520961761475, 1.1510998010635376),
            rot=(0.7065150737762451, 0.0, -2.0452972648854484e-11, 0.7076980471611023),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.6245062024300885, 3.146742786073207, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.21049052476882935, 4.5725202560424805, 1.1510998010635376),
            rot=(0.7065150737762451, 2.9103830456733704e-11, -2.7966962079517543e-11, 0.7076980471611023),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.6245062024300885, 2.860414962044708, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.21060463786125183, 6.833606243133545, 1.1510998010635376),
            rot=(-0.7045915126800537, 2.9103830456733704e-11, 1.2402523452692549e-11, 0.7096131443977356),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.6245062024300885, 2.860414962044708, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.21060319244861603, 3.453606605529785, 1.1510998010635376),
            rot=(-0.7055119872093201, 0.0, 1.468336563448247e-11, 0.708698034286499),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.6245062024300885, 2.860414962044708, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorLvgliq9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorLvgliq9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.054943323135376, 7.315030097961426, 1.1510998010635376),
            rot=(1.9470462575554848e-07, 0.0, -3.659295089164516e-13, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.5533124423706286, 3.146742786073207, 4.527199682615753),
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
            pos=(3.7526248090834198, 6.537236783659455, 1.104785072304443),
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
            pos=(0.26067798725231894, 3.8671525724691733, 1.200281898479443),
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

    electricSwitchWseglt10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.50127446728342, 7.367233853974455, 1.200281898479443),
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

    electricSwitchWseglt11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.009597998467681, 8.320373763874173, 1.200281898479443),
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

    electricSwitchWseglt12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.0554277863691794, 8.447233609865126, 1.200281898479443),
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

    electricSwitchWseglt13 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt13",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.8693174808876811, 4.389734115434173, 1.200281898479443),
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

    electricSwitchWseglt14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.1709814667941794, 8.306960172365127, 1.200281898479443),
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
            pos=(0.4043675153834197, 4.15723385397445, 1.200281898479443),
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

    electricSwitchWseglt3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.180400902897319, 7.172424545124173, 1.200281898479443),
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

    electricSwitchWseglt4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.1389438729541794, 2.5469639565451256, 1.200281898479443),
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
            pos=(-1.0890134978108206, 0.22723594446012563, 1.200281898479443),
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

    electricSwitchWseglt6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.5135558549815804, 3.547235685029455, 1.200281898479443),
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

    electricSwitchWseglt7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.009597510187681, 5.401155990434174, 1.200281898479443),
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

    electricSwitchWseglt8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.0596891569858204, 7.296960904785126, 1.200281898479443),
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

    electricSwitchWseglt9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.009599463312681, 7.203320052934173, 1.200281898479443),
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

    fridgeXyejdx0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/fridgeXyejdx0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.4296627044677734, 5.9822587966918945, 0.7982249855995178),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/fridge/xyejdx/usd/xyejdx.usd"),
            visual_material_path="materials",
            scale=(1.255203227875746, 1.1367859780768024, 0.9723216728098847),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    radiatorWntwxx0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/radiatorWntwxx0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.1150031089782715, 10.760151863098145, 0.2703810930252075),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/radiator/wntwxx/usd/wntwxx.usd"),
            visual_material_path="materials",
            scale=(1.9296878814026943, 3.545689252539957, 2.730407282343422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    radiatorWntwxx1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/radiatorWntwxx1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.979506492614746, 8.253888130187988, 0.2703810930252075),
            rot=(0.7071070075035095, 9.313225746154785e-10, -1.9102230908174533e-10, 0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/radiator/wntwxx/usd/wntwxx.usd"),
            visual_material_path="materials",
            scale=(2.1369423215941525, 3.1016284899215343, 2.730407282343422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    radiatorWntwxx2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/radiatorWntwxx2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.018896974623203278, -1.4473896026611328, 0.2703810930252075),
            rot=(0.00025613713660277426, -2.3283064365386963e-10, -1.7124079931818414e-11, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/radiator/wntwxx/usd/wntwxx.usd"),
            visual_material_path="materials",
            scale=(3.6507152544986563, 4.259358335319565, 2.730407282343422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    radiatorWntwxx3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/radiatorWntwxx3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.001103401184082, -1.4573897123336792, 0.2703810930252075),
            rot=(0.00025613713660277426, -2.3283064365386963e-10, -1.7124079931818414e-11, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/radiator/wntwxx/usd/wntwxx.usd"),
            visual_material_path="materials",
            scale=(3.6507152544986563, 4.259358335319565, 2.730407282343422),
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
            pos=(1.1231526545467376, 9.737618652403418, 1.6500000187529582),
            rot=(-0.7067358834512703, 0.0, 0.0, 0.7074774844773172),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(0.9161537742032558, 5.044488001354546, 1.5545101396722316),
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
            pos=(4.856980224609997, 0.6500349121110031, 1.8050000206290986),
            rot=(0.7080011488138953, 0.0, 0.0, -0.7062112809055123),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(3.0355356673620193, 5.426506709486323, 1.710031129337842),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ovenWuinhm0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ovenWuinhm0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.542356252670288, 5.990156650543213, 0.6869125366210938),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/oven/wuinhm/usd/wuinhm.usd"),
            visual_material_path="materials",
            scale=(1.8155431094329813, 1.9908152355629345, 1.8694488469739425),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureCltbty0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureCltbty0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.880533539964419, 7.385763368627625, 1.60032702612669),
            rot=(-0.0035207953800128196, 0.0, 0.0, 0.9999938019807384),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/cltbty/usd/cltbty.usd"),
            visual_material_path="materials",
            scale=(1.2222278238677282, 1.1028412941285772, 1.7263878324606141),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureFhkzlm0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureFhkzlm0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.7405450478072275, 10.848330765469614, 1.6003271020306902),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/fhkzlm/usd/fhkzlm.usd"),
            visual_material_path="materials",
            scale=(1.2220820080929884, 1.1028412941285772, 0.7683044371444357),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureHhxttu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureHhxttu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.829453089864679, 0.23952168011853425, 1.6004085768689187),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/hhxttu/usd/hhxttu.usd"),
            visual_material_path="materials",
            scale=(1.3094256571620375, 1.1028412941285772, 2.1581670625202642),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureJpfyrq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureJpfyrq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.087732247842464, 9.730091163982081, 1.6003273364374768),
            rot=(0.7071069003958291, 0.0, 0.0, 0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/jpfyrq/usd/jpfyrq.usd"),
            visual_material_path="materials",
            scale=(1.4257866454042765, 1.1028412941285772, 1.5633392880788626),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureLucjyq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureLucjyq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.087713274540576, 2.565098416333754, 1.6004090084259608),
            rot=(0.7054831983277056, 0.0, 0.0, 0.7087266446785468),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/lucjyq/usd/lucjyq.usd"),
            visual_material_path="materials",
            scale=(1.3094256571620375, 1.1028412941285772, 1.44053416857134),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureQavxsz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureQavxsz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.907834433961082, 5.900090902674251, 1.6002044757977656),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/qavxsz/usd/qavxsz.usd"),
            visual_material_path="materials",
            scale=(0.843835888418342, 1.1028412941285772, 1.1518452987337917),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureQtvjzk0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureQtvjzk0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.7755448098836824, 2.538380132783817, 1.375265883448994),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/qtvjzk/usd/qtvjzk.usd"),
            visual_material_path="materials",
            scale=(2.3715477603656328, 1.1028412941285772, 1.498120302174817),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureRciuob0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureRciuob0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.540544911755615, 6.428367344194398, 1.6004089642614754),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/rciuob/usd/rciuob.usd"),
            visual_material_path="materials",
            scale=(1.3094256571620375, 1.1028412941285772, 1.9207124475250665),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureTlwjpv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureTlwjpv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.979445530541566, 7.444302252163327, 1.6003271729618975),
            rot=(0.00297613105096937, 0.0, 0.0, 0.9999955713121771),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/tlwjpv/usd/tlwjpv.usd"),
            visual_material_path="materials",
            scale=(1.2222278238677282, 1.1028412941285772, 1.843796355984803),
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
            pos=(2.2105450010447654, -1.5581938462132112, 1.6504494205245726),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/wfdvzv/usd/wfdvzv.usd"),
            visual_material_path="materials",
            scale=(1.3967693062310866, 1.1028412941285772, 2.3770786501923853),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureYtxhyl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureYtxhyl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.908785111350361, 3.240091267194744, 1.6002045989867504),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/ytxhyl/usd/ytxhyl.usd"),
            visual_material_path="materials",
            scale=(0.843835888418342, 1.1028412941285772, 0.48022675721728947),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureZsirgc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureZsirgc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.167068045428348, 10.515252854810912, 1.700245258672365),
            rot=(-0.7043174963140025, 0.0, 0.0, 0.7098851064686278),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/zsirgc/usd/zsirgc.usd"),
            visual_material_path="materials",
            scale=(0.6539837497073205, 1.1028412941285772, 1.3831072604833707),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfNjwsoa0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfNjwsoa0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.0590448136888977, 4.180490214855631, 0.9946926283552344),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/njwsoa/usd/njwsoa.usd"),
            visual_material_path="materials",
            scale=(0.974262084135071, 0.7421132734263145, 1.7484035134658573),
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
            pos=(-0.5074835456326096, 8.916529641122903, 1.2098176567271808),
            rot=(0.7059975044240558, 0.0, 0.0, 0.7082143204899243),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shower_stall/invgma/usd/invgma.usd"),
            visual_material_path="materials",
            scale=(1.0991083401534425, 1.1402194288652798, 1.1653542935171972),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkCzyfhq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkCzyfhq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.763969898223877, 4.789501667022705, 0.4877566695213318),
            rot=(0.7064481377601624, -7.450580596923828e-09, 3.4924596548080444e-10, 0.7077648639678955),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/czyfhq/usd/czyfhq.usd"),
            visual_material_path="materials",
            scale=(6.0389385665484125, 4.361040305123307, 4.931451850023588),
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
            pos=(0.902244508266449, 9.741680145263672, 0.48449012637138367),
            rot=(0.7102846503257751, -6.111804395914078e-10, 2.1245796233415604e-09, -0.7039147019386292),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/ksecxq/usd/ksecxq.usd"),
            visual_material_path="materials",
            scale=(4.242099370771377, 3.507641230218806, 4.705832831069821),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    toiletSjjweo0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/toiletSjjweo0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.3763653337955475, 10.533782005310059, 0.3698437511920929),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/sjjweo/usd/sjjweo.usd"),
            visual_material_path="materials",
            scale=(1.3385658350851102, 1.2877242706439138, 1.347465746144534),
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
            pos=(-2.460230827331543, 6.199113845825195, 1.9657217264175415),
            rot=(1.0, 5.766196409240365e-10, -1.0186340659856796e-10, -8.686765795573592e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/dmwxyl/usd/dmwxyl.usd"),
            visual_material_path="materials",
            scale=(1.3309117133296497, 1.8496581394889902, 1.3137781364815935),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetDmwxyl1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetDmwxyl1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.117772579193115, 3.6707606315612793, 1.8409391641616821),
            rot=(-0.001540378201752901, 0.0, 2.1589130483334884e-10, 0.9999988079071045),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/dmwxyl/usd/dmwxyl.usd"),
            visual_material_path="materials",
            scale=(2.576206786468583, 1.5583038740802233, 1.7095620122115038),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetDmwxyl2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetDmwxyl2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.964286804199219, 5.688180923461914, 1.840938925743103),
            rot=(0.7047770023345947, 0.0, -6.252776074688882e-10, 0.7094290256500244),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/dmwxyl/usd/dmwxyl.usd"),
            visual_material_path="materials",
            scale=(1.8694008006605536, 1.340671066737008, 1.7095620122115038),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetEobsmt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetEobsmt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.872264862060547, 4.233767509460449, 1.842225432395935),
            rot=(0.7042499780654907, 0.0, -1.509761204943061e-10, 0.7099522352218628),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/eobsmt/usd/eobsmt.usd"),
            visual_material_path="materials",
            scale=(0.7940341468624013, 1.6801182537480237, 1.7108244821051954),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetJvdbxh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetJvdbxh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.5895171165466309, 6.19789981842041, 2.0892653465270996),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/jvdbxh/usd/jvdbxh.usd"),
            visual_material_path="materials",
            scale=(1.9274316707003813, 1.6987378961840551, 1.4232649162957127),
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
            pos=(5.012438774108887, 4.552509307861328, 1.4187968969345093),
            rot=(-0.7055473327636719, -3.725290298461914e-09, 2.078195393551141e-09, 0.7086628079414368),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ithrgo/usd/ithrgo.usd"),
            visual_material_path="materials",
            scale=(1.2506561280651902, 1.790533005075924, 1.5569807389712804),
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
            pos=(-3.8540198802948, 0.11980679631233215, 1.4187970161437988),
            rot=(0.00035365024814382195, -3.725290298461914e-09, -4.092726157978177e-11, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ithrgo/usd/ithrgo.usd"),
            visual_material_path="materials",
            scale=(1.455118063797149, 2.148639606091109, 1.5569807389712804),
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
            pos=(0.24867255985736847, -1.6753820180892944, 1.4204007387161255),
            rot=(1.9470462575554848e-07, 0.0, -6.821210263296962e-12, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.9829737025959022, 2.39733504510467, 1.5110307044953832),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.191556453704834, -1.6753820180892944, 1.4204007387161255),
            rot=(1.946973497979343e-07, 0.0, 3.001332515850663e-11, 0.9999999403953552),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.8582497380493235, 2.39733504510467, 1.5110307044953832),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.999651908874512, 8.14199161529541, 1.4204007387161255),
            rot=(0.7071069478988647, 1.862645149230957e-09, 1.5105570128071122e-09, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.0850610369112248, 1.798909824143727, 1.5110307044953832),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.999651908874512, -0.8323668241500854, 1.4204007387161255),
            rot=(0.7071069478988647, -1.862645149230957e-09, 1.8098944565281272e-10, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.403050964538988, 1.798909824143727, 1.5110307044953832),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.169323921203613, 0.9923223853111267, 1.4204007387161255),
            rot=(0.7060202360153198, 1.862645149230957e-09, -4.979483492206782e-10, 0.7081917524337769),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.897701963071064, 2.278619110582054, 1.5110307044953832),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.1699604988098145, 8.09501838684082, 1.4204007387161255),
            rot=(0.7088415026664734, 1.862645149230957e-09, -3.7567815525108017e-10, 0.7053678631782532),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.0850610369112248, 2.278619110582054, 1.5110307044953832),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.169454574584961, 4.739484786987305, 1.7116578817367554),
            rot=(0.7059080600738525, 0.0, -2.293745637871325e-09, 0.708303689956665),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.0473566952765234, 2.278619110582054, 0.8634617092793251),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.786380648612976, 10.928194999694824, 1.4204007387161255),
            rot=(0.9999932646751404, -2.546585164964199e-11, 7.825029513242043e-10, 0.003676492953673005),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.0850610369112248, 1.5590551809245634, 1.5110307044953832),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.3179171681404114, 10.928648948669434, 1.5903006792068481),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.0101517488952618, 1.5590551809245634, 1.1332730283715373),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowUlnafj9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowUlnafj9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.893619179725647, 10.928194999694824, 1.4204007387161255),
            rot=(0.9999932646751404, -2.546585164964199e-11, 7.825029513242043e-10, 0.003676492953673005),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.0850610369112248, 1.5590551809245634, 1.5110307044953832),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
