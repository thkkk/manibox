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
class benevolence1IntquickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Benevolence_1_int/usd/Benevolence_1_int_quick.usd"),
        )
    )
@configclass
class benevolence1IntfullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Benevolence_1_int/usd/Benevolence_1_int_quick.usd"),
        )
    )
    breakfastTableIdnnmz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableIdnnmz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.10955172777175903, -2.3461039066314697, 0.6336469650268555),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/idnnmz/usd/idnnmz.usd"),
            visual_material_path="materials",
            scale=(0.952339569339586, 1.4398865214392913, 1.7705571268545186),
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
            pos=(0.21455062925815582, -8.13781452178955, 0.1305130273103714),
            rot=(-2.3562461137771606e-07, 7.748091593384743e-05, 0.0005923991557210684, 0.9999998807907104),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/cedar_chest/fwstpx/usd/fwstpx.usd"),
            visual_material_path="materials",
            scale=(1.7703798316449972, 1.078037967041972, 1.9177151611151297),
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
            pos=(-1.8229347467422485, -6.235112190246582, 0.13051196932792664),
            rot=(-0.7009848356246948, -0.00046410830691456795, 0.00048494580551050603, 0.7131759524345398),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/cedar_chest/fwstpx/usd/fwstpx.usd"),
            visual_material_path="materials",
            scale=(1.4126007678443548, 1.1457444688101348, 1.9177151611151297),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    consoleTableEmeeke0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/consoleTableEmeeke0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.2946650981903076, -6.980343341827393, 0.5571462512016296),
            rot=(-0.0033783414401113987, -7.450580596923828e-09, 1.6007106751203537e-10, 0.9999943375587463),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/console_table/emeeke/usd/emeeke.usd"),
            visual_material_path="materials",
            scale=(0.6153207773759206, 1.043307073719974, 1.314191632863149),
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
            pos=(-2.33414626121521, -4.384880065917969, 0.8454899787902832),
            rot=(1.000000238418579, -6.209691491676494e-05, 0.00012342074478510767, -7.339068588407827e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/vdxlda/usd/vdxlda.usd"),
            visual_material_path="materials",
            scale=(1.098936057151758, 1.2503327861695646, 1.413621096855878),
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
            pos=(-2.3638179302215576, -1.990864634513855, 0.7226079702377319),
            rot=(0.7051396369934082, 8.781673386693e-06, -9.265937478630804e-06, 0.7090686559677124),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/njwsoa/usd/njwsoa.usd"),
            visual_material_path="materials",
            scale=(1.1031493051873908, 1.4974532633745494, 1.276316850508764),
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
            pos=(1.2000621557235718, -4.404999256134033, 0.3862664997577667),
            rot=(-0.7030781507492065, -1.695682294666767e-05, -2.3168169605014555e-07, 0.7111126780509949),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(1.8680016354642592, 1.4406532182205258, 1.8104257378421895),
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
            pos=(-2.267498731613159, -3.3832406997680664, 0.2213885635137558),
            rot=(0.7070704102516174, 0.0005208334769122303, 0.0005203019245527685, 0.7071428894996643),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(2.009823500414463, 1.5643877485303859, 1.0409776138485085),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaUixwiv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaUixwiv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.9681351780891418, -5.706408977508545, 0.28768810629844666),
            rot=(0.7136958241462708, 9.313225746154785e-10, 1.6298145055770874e-09, 0.7004558444023132),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/uixwiv/usd/uixwiv.usd"),
            visual_material_path="materials",
            scale=(1.5896067891598837, 1.9419156789613954, 1.7292698489687444),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ottomanMiftfy0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ottomanMiftfy0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.0665936470031738, -8.029690742492676, 0.289838582277298),
            rot=(1.9371509552001953e-07, -1.1641532182693481e-10, -6.039044819772243e-10, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/ottoman/miftfy/usd/miftfy.usd"),
            visual_material_path="materials",
            scale=(1.6116481322136664, 1.4707185217109262, 1.540882061952177),
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
            pos=(-2.326219081878662, -2.515000104904175, 0.5867644548416138),
            rot=(0.709313154220581, -1.3969838619232178e-09, 3.725290298461914e-09, 0.7048936486244202),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/eospnr/usd/eospnr.usd"),
            visual_material_path="materials",
            scale=(1.1213451573203768, 1.0641222056531443, 1.5186516240486598),
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
            pos=(0.6474090814590454, -2.3627960681915283, 0.40646979212760925),
            rot=(-0.6981040239334106, -0.000711055938154459, 0.0014809672720730305, 0.7159945368766785),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/pmpwwi/usd/pmpwwi.usd"),
            visual_material_path="materials",
            scale=(0.982071283403241, 0.8765444194167914, 1.0144430303577696),
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
            pos=(-0.4782020151615143, -2.3481907844543457, 0.4064759314060211),
            rot=(0.7044537663459778, 0.0014634942635893822, 0.0007348275976255536, 0.7097480893135071),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/pmpwwi/usd/pmpwwi.usd"),
            visual_material_path="materials",
            scale=(0.982071283403241, 0.8765444194167914, 1.0144430303577696),
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
            pos=(0.10203824192285538, -2.9328699111938477, 0.4064757227897644),
            rot=(0.008299807086586952, 0.0005338005721569061, 0.0015483546303585172, 0.9999643564224243),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/pmpwwi/usd/pmpwwi.usd"),
            visual_material_path="materials",
            scale=(0.982071283403241, 0.8765444194167914, 1.0144430303577696),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopQudfwe0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopQudfwe0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.4690432846546173, -0.6071784496307373, 0.43988099694252014),
            rot=(-0.005235247313976288, 0.0, -2.5208635179296834e-10, 0.9999862909317017),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/qudfwe/usd/qudfwe.usd"),
            visual_material_path="materials",
            scale=(1.347167811116611, 1.2548712836737408, 1.4413543934632258),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopSpojpj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopSpojpj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.4188784062862396, 1.5547670125961304, 0.4633547365665436),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/spojpj/usd/spojpj.usd"),
            visual_material_path="materials",
            scale=(1.1308769356865367, 1.298078463917706, 1.4681359525762268),
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
            pos=(0.5952725410461426, -0.6053071618080139, 0.4786028265953064),
            rot=(-0.00549428490921855, 3.979039320256561e-12, -2.927347531045399e-10, 0.9999849200248718),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/ufhpbn/usd/ufhpbn.usd"),
            visual_material_path="materials",
            scale=(1.035042163449069, 0.9359014425612057, 0.9513342274725531),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopUfhpbn1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopUfhpbn1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.8854832053184509, 1.540571689605713, 0.47860288619995117),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/ufhpbn/usd/ufhpbn.usd"),
            visual_material_path="materials",
            scale=(0.8470241762854773, 1.034400045632589, 0.9513342274725531),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopVzzafs0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopVzzafs0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.2131124585866928, -0.6134189963340759, 0.40490996837615967),
            rot=(-0.003562876721844077, 0.0, -7.450580596923828e-09, 0.9999936819076538),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/vzzafs/usd/vzzafs.usd"),
            visual_material_path="materials",
            scale=(0.880840290562024, 0.882603203042801, 1.0016042753519663),
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
            pos=(-0.11921576786034803, -6.465051788048851, 0.002257983865),
            rot=(0.7083774812905553, 0.0, 0.0, 0.7058337934673069),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.9836828897169676, 2.2182557410514496, 0.24480330607770978),
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
            pos=(0.20955224609500012, -1.0905308837899998, 1.0514628295900001),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(2.2644671548738757, 0.8194375277780452, 2.935433321604046),
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
            pos=(0.6945550927577002, 1.519298889639466, 0.8902008019563301),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.278639294012697, 1.1044904947247125, 0.5858268216935112),
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
            pos=(0.20455229970466282, -0.5556479370210349, 0.8902008019217902),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(2.23519580130908, 1.0154563186506904, 0.5858268216935112),
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
            pos=(1.0645572285361002, 0.8792563188804492, 0.8902008021147135),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.5563515127382402, 1.1757537364613793, 0.5858268216935112),
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
            pos=(-0.8854419250500001, 1.51428814697, 0.890200805665),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.26354007958672226, 1.1222614290620676, 0.5858268216935112),
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
            pos=(1.105373501777649, 0.8790869116783142, 0.4499336779117584),
            rot=(0.7092726826667786, 9.313225746154785e-10, -4.5838532969355583e-10, -0.704934298992157),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/dishwasher/dngvvi/usd/dngvvi.usd"),
            visual_material_path="materials",
            scale=(1.086021750648125, 0.9137292136773469, 1.2170729923012398),
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
            pos=(-3.2450900077819824, 0.3506544530391693, 1.1367478370666504),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ktydvs/usd/ktydvs.usd"),
            visual_material_path="materials",
            scale=(3.870855811865299, 7.089476922945642, 5.30375420379901),
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
            pos=(-2.065521240234375, -0.12051581591367722, 1.150984764099121),
            rot=(0.704558789730072, -1.4551915228366852e-11, -7.631228982063476e-12, 0.7096457481384277),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.1633406521941874, 4.289190803946919, 4.527199682615753),
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
            pos=(-1.7159794569015503, -7.821760177612305, 0.9858973622322083),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(1.7358035072659002, 5.38577348775408, 2.8287788690487865),
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
            pos=(1.4264258705880035, -3.522183157143153, 1.200281898479443),
            rot=(-0.7071067215818997, 0.0, 0.0, 0.7071068407911903),
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
            pos=(-2.2030439966787676, -0.4969103523820322, 1.200281898479443),
            rot=(1.6292068456008897e-07, 0.0, 0.0, 0.9999999999999869),
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
            pos=(-3.6272988794937726, 0.5030896323579677, 1.200281898479443),
            rot=(1.6292068456008897e-07, 0.0, 0.0, 0.9999999999999869),
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
            pos=(-1.987308194893624, -0.48788390360671596, 1.200281898479443),
            rot=(0.7071065427679242, 0.0, 0.0, 0.7071070196050905),
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
            pos=(-0.8693596094737821, -7.7669106117820315, 1.200281898479443),
            rot=(1.6292068456008897e-07, 0.0, 0.0, 0.9999999999999869),
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

    fridgeXyejdx0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/fridgeXyejdx0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.5006803274154663, 1.4377108812332153, 0.8513244390487671),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/fridge/xyejdx/usd/xyejdx.usd"),
            visual_material_path="materials",
            scale=(1.4434995087249642, 1.2179946765465108, 1.0371630015426667),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    microwaveBfbeeb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/microwaveBfbeeb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.350424587726593, 1.633657455444336, 1.5652587413787842),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/microwave/bfbeeb/usd/bfbeeb.usd"),
            visual_material_path="materials",
            scale=(1.5034127769117709, 1.3356521028214596, 1.2264218334423032),
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
            pos=(-0.34276917576789856, 1.5018638372421265, 0.5036253333091736),
            rot=(0.9999997019767761, 1.4551915228366852e-10, 1.1350493878126144e-09, -0.0007081028306856751),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/oven/wuinhm/usd/wuinhm.usd"),
            visual_material_path="materials",
            scale=(1.7700578755752088, 1.6780595608788464, 1.3710236426379534),
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
            pos=(-3.300441000710101, -7.211322357662647, 1.6497361504982304),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/etixod/usd/etixod.usd"),
            visual_material_path="materials",
            scale=(0.8452940461657386, 1.22816416846137, 1.704167846940927),
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
            pos=(-2.4700097835064185, -3.6705407500619067, 1.4299914277491117),
            rot=(0.7071069003958291, 0.0, 0.0, 0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/hhxttu/usd/hhxttu.usd"),
            visual_material_path="materials",
            scale=(0.37678796192725006, 1.1028412941285772, 0.5612415003028587),
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
            pos=(-2.467011009485953, -4.385018996718589, 1.8000487695365484),
            rot=(0.7026173831272423, 0.0, 0.0, 0.711567855462447),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/jpfyrq/usd/jpfyrq.usd"),
            visual_material_path="materials",
            scale=(0.39282769714861127, 1.1028412941285772, 0.7817686271525172),
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
            pos=(-2.46769990328706, -3.1150414347086026, 1.7300241129124583),
            rot=(0.7071069003958291, 0.0, 0.0, 0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/lucjyq/usd/lucjyq.usd"),
            visual_material_path="materials",
            scale=(0.5091886853908503, 1.1028412941285772, 0.48976118627549564),
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
            pos=(1.4172787959814392, 0.14495576292448495, 2.1399669831884562),
            rot=(0.7077160653264127, 0.0, 0.0, -0.7064969715992424),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/qavxsz/usd/qavxsz.usd"),
            visual_material_path="materials",
            scale=(0.960196876660581, 1.1028412941285772, 0.4606447770868122),
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
            pos=(1.416835422894227, -1.1800414026853379, 1.7200649882206347),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/rciuob/usd/rciuob.usd"),
            visual_material_path="materials",
            scale=(0.40740927462257603, 1.1028412941285772, 0.8450667773884475),
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
            pos=(1.4156854840097677, -4.4150303942159415, 1.5002939149315953),
            rot=(-0.7048220620503869, 0.0, 0.0, 0.709384141947817),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/tlwjpv/usd/tlwjpv.usd"),
            visual_material_path="materials",
            scale=(0.9756533487829837, 1.1028412941285772, 2.3046870748291743),
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
            pos=(-2.8548301848733835, -0.14005931745509456, 1.6200649556389866),
            rot=(0.7108154992272012, 0.0, 0.0, -0.7033785083853392),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/zsirgc/usd/zsirgc.usd"),
            visual_material_path="materials",
            scale=(0.4644232425457784, 1.1028412941285772, 1.014154116542171),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfOwvfik2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfOwvfik2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.288794531970608, -3.10509758021492, 1.0245070012970139),
            rot=(0.7101742976139364, 0.0, 0.0, 0.7040258993876235),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(1.0227504203292532, 1.4873140511993284, 0.8148176083744876),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfOwvfik3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfOwvfik3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.2782631586594437, -3.6949340799035326, 1.824507092847014),
            rot=(0.7043607288239969, 0.0, 0.0, 0.7098422104175884),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(0.9526382342775255, 1.5731366547139114, 0.8148176083744876),
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
            pos=(-3.6661666357667233, -6.303861942023314, 1.611066907208857),
            rot=(0.7038852954150981, 0.0, 0.0, 0.7103136567027274),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/vgzdul/usd/vgzdul.usd"),
            visual_material_path="materials",
            scale=(0.6993336659819912, 1.0076338107148182, 1.367524217106888),
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
            pos=(1.0693252086639404, 0.15510408580303192, 0.3989581763744354),
            rot=(0.7071069478988647, 9.313225746154785e-09, -1.280568540096283e-08, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/czyfhq/usd/czyfhq.usd"),
            visual_material_path="materials",
            scale=(5.389658115238928, 4.166992697611228, 4.034865427313741),
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
            pos=(-0.8907564878463745, 1.6714835166931152, 1.7355198860168457),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/dmwxyl/usd/dmwxyl.usd"),
            visual_material_path="materials",
            scale=(0.5405722172625514, 1.5415289315263854, 1.1554645861896293),
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
            pos=(0.4087097942829132, 1.6714835166931152, 1.7355198860168457),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/dmwxyl/usd/dmwxyl.usd"),
            visual_material_path="materials",
            scale=(1.4556911962353407, 1.5415289315263854, 1.1554645861896293),
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
            pos=(1.3422905206680298, 0.9657226204872131, 1.7355198860168457),
            rot=(0.7071069478988647, -1.862645149230957e-09, 3.2741809263825417e-10, -0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/dmwxyl/usd/dmwxyl.usd"),
            visual_material_path="materials",
            scale=(1.3100804140131739, 1.1451105522277902, 1.1554645861896293),
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
            pos=(0.9250950217247009, 1.6554834842681885, 1.7363892793655396),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/eobsmt/usd/eobsmt.usd"),
            visual_material_path="materials",
            scale=(1.3398123437847886, 1.1427166330412744, 1.1564262598856923),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetEobsmt1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetEobsmt1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.3280916213989258, 1.3923029899597168, 1.7363892793655396),
            rot=(-0.7060503959655762, 1.7462298274040222e-10, -9.458744898438454e-11, 0.7081615924835205),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/eobsmt/usd/eobsmt.usd"),
            visual_material_path="materials",
            scale=(0.6181380707033526, 0.8671260583198646, 1.1564262598856923),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetEobsmt2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetEobsmt2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.3189095258712769, -0.5356234312057495, 1.7363892793655396),
            rot=(-0.7054978013038635, 0.0, -3.41970007866621e-10, 0.7087122201919556),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/eobsmt/usd/eobsmt.usd"),
            visual_material_path="materials",
            scale=(1.344815952078153, 0.9416011302981503, 1.1564262598856923),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetLsyzkh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetLsyzkh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.4915837049484253, 1.5524613857269287, 1.9497758150100708),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/lsyzkh/usd/lsyzkh.usd"),
            visual_material_path="materials",
            scale=(1.6241526948828424, 2.8121707529448927, 1.4684960844863375),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetLsyzkh1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetLsyzkh1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.35140979290008545, 1.6616045236587524, 1.9197540283203125),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/lsyzkh/usd/lsyzkh.usd"),
            visual_material_path="materials",
            scale=(1.376964404791184, 1.5139458998062847, 1.7622943901882262),
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
            pos=(1.3423676490783691, -6.290794849395752, 1.6916725635528564),
            rot=(0.7094442248344421, 0.0, 0.0, -0.7047616839408875),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/ylvjhb/usd/ylvjhb.usd"),
            visual_material_path="materials",
            scale=(1.2939459292702298, 0.4809018385258011, 0.8178324883920075),
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
            pos=(1.5609053373336792, -2.193742036819458, 1.2717430591583252),
            rot=(0.708434522151947, 1.862645149230957e-09, 7.262315193656832e-10, -0.7057765126228333),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(2.3073309197050222, 2.9969716531525794, 1.6189770615270167),
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
            pos=(1.5610584020614624, -7.768055438995361, 1.2717430591583252),
            rot=(0.7088972330093384, -1.862645149230957e-09, 2.894466888392344e-10, -0.7053119540214539),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.1829425065854167, 2.9969716531525794, 1.6189770615270167),
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
            pos=(0.43189874291419983, -8.523725509643555, 1.2717430591583252),
            rot=(0.003184627741575241, 3.725290298461914e-09, 4.320099833421409e-11, 0.9999949932098389),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(2.0577581417985056, 3.4766809395909064, 1.6189770615270167),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
