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
class ihlen0IntquickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Ihlen_0_int/usd/Ihlen_0_int_quick.usd"),
        )
    )
@configclass
class ihlen0IntfullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Ihlen_0_int/usd/Ihlen_0_int_quick.usd"),
        )
    )
    armchairTcxiue0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairTcxiue0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.6990994811058044, 2.292635917663574, 0.5224980115890503),
            rot=(-0.12993253767490387, -5.9754551330115646e-05, 0.0004114324110560119, 0.9915228486061096),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/tcxiue/usd/tcxiue.usd"),
            visual_material_path="materials",
            scale=(1.036235349193221, 1.0321686402151011, 1.0646395568791862),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairTcxiue1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairTcxiue1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.07866370677948, -0.9610810279846191, 0.4571686387062073),
            rot=(0.43935152888298035, 0.00018265939434058964, 0.00038841250352561474, 0.8983151912689209),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/tcxiue/usd/tcxiue.usd"),
            visual_material_path="materials",
            scale=(0.8915955322444017, 0.8727413183984374, 0.9315259637371488),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairTcxiue2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairTcxiue2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.7583606839179993, 2.369588613510132, 0.522497832775116),
            rot=(0.20855626463890076, 8.784559031482786e-05, 0.0004292521334718913, 0.9780102968215942),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/tcxiue/usd/tcxiue.usd"),
            visual_material_path="materials",
            scale=(1.0976613331605964, 0.9837462260550836, 1.0646395568791862),
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
            pos=(3.574908494949341, 5.03801155090332, 0.4074893891811371),
            rot=(0.9999958276748657, -0.0029167088214308023, -5.811409209854901e-06, 7.11152097210288e-05),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jrhgeu/usd/jrhgeu.usd"),
            visual_material_path="materials",
            scale=(1.1515681830145372, 1.4381301502438182, 1.1562446128650505),
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
            pos=(-3.180426836013794, 10.445656776428223, 0.876495897769928),
            rot=(1.0000001192092896, 1.0535281944612507e-06, 5.734194928663783e-06, 2.3286338546313345e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(2.573804697645186, 1.3831468951907206, 2.252951370596715),
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
            pos=(-3.912633180618286, 2.704249620437622, 0.7701728343963623),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/uhrsex/usd/uhrsex.usd"),
            visual_material_path="materials",
            scale=(0.7200531235698615, 1.3893448421315835, 2.2625264086374237),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coffeeTableFqluyq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coffeeTableFqluyq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.06337933987379074, 3.4699435234069824, 0.2632834315299988),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/fqluyq/usd/fqluyq.usd"),
            visual_material_path="materials",
            scale=(1.2186630721857974, 1.1463526594864584, 1.088391201022594),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coffeeTableQlmqyy0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coffeeTableQlmqyy0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.2653281688690186, 0.06213945150375366, 0.2736167907714844),
            rot=(0.7066556215286255, 6.734579801559448e-05, -3.198679769411683e-05, 0.7075578570365906),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/qlmqyy/usd/qlmqyy.usd"),
            visual_material_path="materials",
            scale=(0.8967385364254062, 0.8830708379591464, 1.0021386405861088),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pillowPjqqmb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pillowPjqqmb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.821636974811554, 0.013674125075340271, 0.12876960635185242),
            rot=(0.7123490571975708, 0.030060533434152603, -0.09255385398864746, -0.6950462460517883),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pillow/pjqqmb/usd/pjqqmb.usd"),
            visual_material_path="materials",
            scale=(2.841659412562218, 2.477967346539179, 3.2879640097901803),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pillowPjqqmb1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pillowPjqqmb1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.1935424655675888, -1.0622270107269287, 0.12861496210098267),
            rot=(0.003801874816417694, 0.04345347732305527, 0.08707276731729507, 0.9952465891838074),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pillow/pjqqmb/usd/pjqqmb.usd"),
            visual_material_path="materials",
            scale=(2.841659412562218, 2.477967346539179, 3.2879640097901803),
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
            pos=(-4.735952377319336, 4.503200531005859, 0.8197152614593506),
            rot=(1.0000001192092896, -0.0001705549657344818, 0.0002488374011591077, 7.82779352448415e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/udqjui/usd/udqjui.usd"),
            visual_material_path="materials",
            scale=(2.1255904833443746, 1.9134874003077023, 2.6542103100794603),
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
            pos=(-1.9937397241592407, 0.6705079078674316, 0.546448290348053),
            rot=(0.9999998211860657, -0.00030303094536066055, 0.00044681131839752197, 1.4976549209677614e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/udqjui/usd/udqjui.usd"),
            visual_material_path="materials",
            scale=(1.6929133317986311, 1.5468238214737509, 1.7695231941538843),
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
            pos=(1.0104584693908691, -1.1909540891647339, 0.84256911277771),
            rot=(-0.3395848274230957, 1.714378595352173e-05, 3.5668858799908776e-06, 0.9405754208564758),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/njwsoa/usd/njwsoa.usd"),
            visual_material_path="materials",
            scale=(0.9655353452096535, 1.9065367100882276, 1.4861429864459788),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfNjwsoa1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfNjwsoa1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.413883209228516, 5.116753578186035, 1.0906336307525635),
            rot=(0.9999985694885254, -0.0017292082775384188, -1.3846574802300893e-05, -5.840198355144821e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/njwsoa/usd/njwsoa.usd"),
            visual_material_path="materials",
            scale=(1.572155581794444, 1.3916395311991867, 1.9232438648124432),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairEospnr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairEospnr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.8957133293151855, 3.4641239643096924, 0.44819819927215576),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/eospnr/usd/eospnr.usd"),
            visual_material_path="materials",
            scale=(1.2614426883105294, 1.265638536151492, 1.1136693110003975),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairEospnr1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairEospnr1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.874709367752075, 2.155236005783081, 0.44819819927215576),
            rot=(-0.004166301339864731, 1.862645149230957e-09, 5.820766091346741e-10, 0.9999913573265076),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/eospnr/usd/eospnr.usd"),
            visual_material_path="materials",
            scale=(1.2614426883105294, 1.265638536151492, 1.1136693110003975),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairEospnr2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairEospnr2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.36099910736084, 2.6587629318237305, 0.44819819927215576),
            rot=(-0.6993380188941956, -7.450580596923828e-09, -5.587935447692871e-09, 0.7147911787033081),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/eospnr/usd/eospnr.usd"),
            visual_material_path="materials",
            scale=(1.2614426883105294, 1.265638536151492, 1.1136693110003975),
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
            pos=(-3.7743837374908598, 2.659701418034755, 0.002372790995),
            rot=(0.6970802624305937, 0.0, 0.0, 0.7169931015914273),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(2.0356015036206707, 1.909094321032718, 0.24480330607770978),
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
            pos=(0.09455795287999998, 3.57379296875, 0.002372790995),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.4900478924281402, 1.601608223423425, 0.24480330607770978),
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
            pos=(-2.9777491285868463, 5.8593864745285265, 1.4354732055650001),
            rot=(-0.7054021247222071, 0.0, 0.0, 0.7088073380245127),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.2490742479372177, 0.34195585770365305, 0.8787402325402669),
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
            pos=(-3.745433517780871, 5.084943359236579, 1.6957887573250001),
            rot=(-0.0015012775631431125, 0.0, 0.0, 0.9999988730822044),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.7081156421356354, 0.445350384757356, 1.467716660802023),
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
            pos=(-2.9777491285868463, 5.8593864745285265, 1.185473205565),
            rot=(-0.7054021247222071, 0.0, 0.0, 0.7088073380245127),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.2490742479372177, 0.34195585770365305, 0.8787402325402669),
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
            pos=(-3.765433517780871, 5.09494311509658, 1.185473205565),
            rot=(-0.0015012775631431125, 0.0, 0.0, 0.9999988730822044),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.7081156421356354, 0.445350384757356, 0.8787402325402669),
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
            pos=(-3.7752474365199045, 5.081265625005143, 1.4354732055650001),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.6498666275167275, 0.45845420502631495, 0.8787402325402669),
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
            pos=(-3.745008707046509, 7.372186183929443, 1.1368626356124878),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ktydvs/usd/ktydvs.usd"),
            visual_material_path="materials",
            scale=(4.730635400308252, 5.102361824187858, 5.30375420379901),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorKtydvs1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorKtydvs1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.1799698770046234, 7.372186183929443, 1.1368626356124878),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ktydvs/usd/ktydvs.usd"),
            visual_material_path="materials",
            scale=(5.160525194529728, 5.102361824187858, 5.30375420379901),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorKtydvs2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorKtydvs2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.3221707344055176, 9.770039558410645, 1.1368626356124878),
            rot=(0.7071070075035095, 0.0, -3.115019353572279e-11, 0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ktydvs/usd/ktydvs.usd"),
            visual_material_path="materials",
            scale=(3.9934175153754334, 5.345740474612082, 5.30375420379901),
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
            pos=(2.588897228240967, 10.904772758483887, 1.1510995626449585),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.43951536609584, 4.861846452003919, 4.527199682615753),
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
            pos=(-1.6047176122665405, 4.849591255187988, 1.1510995626449585),
            rot=(-0.0016322885639965534, 0.0, 5.826450433232822e-13, 0.9999987483024597),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.809829177748401, 4.575518627975419, 4.527199682615753),
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
            pos=(2.2952828407287598, 5.299590110778809, 1.1510995626449585),
            rot=(-0.0006303350673988461, 0.0, 1.8474111129762605e-13, 0.9999998807907104),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.809829177748401, 4.575518627975419, 4.527199682615753),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    clothesDryerXsuyua0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/clothesDryerXsuyua0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.332241535186768, 6.480781078338623, 0.6555021405220032),
            rot=(-0.6941614747047424, 4.656612873077393e-10, 2.3283064365386963e-10, 0.7198193073272705),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/clothes_dryer/xsuyua/usd/xsuyua.usd"),
            visual_material_path="materials",
            scale=(1.3315805904326055, 1.329285165424854, 1.3902927379135446),
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
            pos=(2.8795085969191794, 5.216546842285126, 1.200281898479443),
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
            pos=(3.4012611410635083, 10.167582572507227, 1.200281898479443),
            rot=(0.7071066023725878, 0.0, 0.0, 0.7071069600004621),
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
            pos=(-1.0164204802308208, 4.7665487954101255, 1.200281898479443),
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

    electricSwitchWseglt3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.237772408940821, 7.296543908041545, 1.2002818992731696),
            rot=(0.9999999999999796, -2.0212918469683032e-07, 0.0, 0.0),
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
            pos=(1.7182788788350605, 5.382810579598753, 1.200281898479443),
            rot=(4.371138834797026e-08, 0.0, 0.0, 0.9999999999999992),
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
            pos=(-0.7273058755022477, 7.128473685135206, 1.200281898479443),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
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
            pos=(-1.0323588164799393, 4.9328086264737525, 1.200281898479443),
            rot=(4.371138834797026e-08, 0.0, 0.0, 0.9999999999999992),
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
            pos=(-0.744198661613412, 7.482810579526111, 1.200281898479443),
            rot=(-3.1391647342098555e-07, 0.0, 0.0, 0.9999999999999507),
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

    electricSwitchWseglt8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.267627494157254, 7.482811556115325, 1.200281898479443),
            rot=(-1.9470718387020827e-07, 0.0, 0.0, 0.9999999999999812),
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
            pos=(-1.6853055947422722, 0.4628108084303247, 1.200281898479443),
            rot=(-1.9470718387020827e-07, 0.0, 0.0, 0.9999999999999812),
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
            pos=(4.7636701660149985, 10.484679199220258, 1.7999997725299985),
            rot=(0.7077984227227647, 0.0, 0.0, -0.7064144624731054),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(0.7851247161780048, 2.2000595480360157, 1.381845103901751),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureGwricv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureGwricv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.2804382583197491, 4.766339182735716, 1.7002449756797382),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/gwricv/usd/gwricv.usd"),
            visual_material_path="materials",
            scale=(0.6692944060549836, 1.1028412941285772, 1.2949876923622254),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureSzpupz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureSzpupz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.640438001760378, 4.757974386097227, 1.4753061949458115),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/szpupz/usd/szpupz.usd"),
            visual_material_path="materials",
            scale=(1.3967693062310866, 1.1028412941285772, 1.9209059892023126),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureWeqggl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureWeqggl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.5895619315000586, 4.7579743826047665, 1.7002451161415393),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/weqggl/usd/weqggl.usd"),
            visual_material_path="materials",
            scale=(0.6692944060549836, 1.1028412941285772, 1.5365877174049691),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureYrgaal0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureYrgaal0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.2544296155542511, 1.114690011549991, 1.5253880119725278),
            rot=(-0.7045588471372879, 0.0, 0.0, 0.7096455671111993),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/yrgaal/usd/yrgaal.usd"),
            visual_material_path="materials",
            scale=(1.3821877287571218, 1.1028412941285772, 2.050020438714008),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfNjwsoa2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfNjwsoa2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.2226252310016608, 5.4628050131024946, 1.0941616311616544),
            rot=(0.0005316296791709085, 0.0, 0.0, 0.9999998586849321),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/njwsoa/usd/njwsoa.usd"),
            visual_material_path="materials",
            scale=(1.7158111302590089, 1.1809568323143134, 1.9232438648124432),
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
            pos=(4.539538582833122, 9.002054115567379, 0.8003519067170641),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(0.8150763502519839, 3.399574974169893, 3.7342751866363955),
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
            pos=(-4.857394093488331, 6.1160266993319805, 1.1307498840959507),
            rot=(0.7071069003958291, 0.0, 0.0, 0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/vgzdul/usd/vgzdul.usd"),
            visual_material_path="materials",
            scale=(3.748932650902055, 3.1998517598797402, 3.7607350436132996),
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
            pos=(3.8462307230012556, 8.876372578479678, 1.2098174125871808),
            rot=(0.0007866183206478038, 0.0, 0.0, 0.999999690615761),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shower_stall/invgma/usd/invgma.usd"),
            visual_material_path="materials",
            scale=(1.0558258865427361, 1.063084448946284, 1.1653542935171972),
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
            pos=(4.366479396820068, 8.049981117248535, 0.4614205062389374),
            rot=(0.70710688829422, 2.3283064365386963e-10, 0.0, -0.70710688829422),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/ksecxq/usd/ksecxq.usd"),
            visual_material_path="materials",
            scale=(4.383124725730198, 4.648487691226112, 4.481572962832644),
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
            pos=(4.497707366943359, 10.484673500061035, 0.5075593590736389),
            rot=(0.7071069478988647, 1.1641532182693481e-10, -1.2369127944111824e-10, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/ksecxq/usd/ksecxq.usd"),
            visual_material_path="materials",
            scale=(4.453991738272319, 3.6866762483782916, 4.930092699306999),
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
            pos=(4.500056743621826, 9.920042037963867, 0.411013662815094),
            rot=(0.7092856168746948, 2.0954757928848267e-08, -1.0884832590818405e-08, -0.7049210667610168),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/wusctd/usd/wusctd.usd"),
            visual_material_path="materials",
            scale=(1.2862772377406255, 1.137300451806333, 1.471647983411061),
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
            pos=(4.4000043869018555, 7.293974876403809, 0.6182512044906616),
            rot=(-0.7050836086273193, 0.0, 8.731149137020111e-10, 0.7091243863105774),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/washer/omeuop/usd/omeuop.usd"),
            visual_material_path="materials",
            scale=(1.156821191821943, 1.3289228286271426, 1.4055827341074745),
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
            pos=(-3.9169633388519287, 0.322035551071167, 1.9572854042053223),
            rot=(0.0053756749257445335, -1.862645149230957e-09, 3.3855940273497254e-10, 0.9999856948852539),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.8592095335430964, 3.116898974762161, 0.5396226381844246),
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
            pos=(4.966531276702881, 3.224445343017578, 1.9572854042053223),
            rot=(0.7075382471084595, 0.0, 6.221796411409741e-10, -0.7066752314567566),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.255354818334181, 4.025439289986266, 0.5396226381844246),
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
            pos=(-3.2185940742492676, 10.909473419189453, 1.9572854042053223),
            rot=(0.9999997019767761, 7.457856554538012e-11, 5.354934273782419e-10, -0.0009605885134078562),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.2846942894737663, 2.0387644673628906, 0.5396226381844246),
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
            pos=(-5.1131463050842285, 1.6292380094528198, 1.9572854042053223),
            rot=(0.7108978629112244, 0.0, -1.3028511602897197e-10, 0.7032954692840576),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.8740665423329289, 2.2434888850600556, 0.5396226381844246),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
