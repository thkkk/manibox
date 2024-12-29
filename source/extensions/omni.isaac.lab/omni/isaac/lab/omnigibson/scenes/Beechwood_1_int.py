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
class beechwood1IntquickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Beechwood_1_int/usd/Beechwood_1_int_quick.usd"),
        )
    )
@configclass
class beechwood1IntfullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Beechwood_1_int/usd/Beechwood_1_int_quick.usd"),
        )
    )
    armchairVzhxuf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairVzhxuf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.3256375789642334, 8.872365951538086, 0.22264212369918823),
            rot=(0.9703390002250671, 2.6193447411060333e-09, 1.6880221664905548e-09, 0.24174809455871582),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/vzhxuf/usd/vzhxuf.usd"),
            visual_material_path="materials",
            scale=(0.7703778737360991, 0.4905264704675684, 0.4494470875945373),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairVzhxuf1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairVzhxuf1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.14003099501132965, 9.028178215026855, 0.2214096337556839),
            rot=(6.239861249923706e-08, 3.7030549719929695e-05, -0.0002952616778202355, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/vzhxuf/usd/vzhxuf.usd"),
            visual_material_path="materials",
            scale=(0.7703778737360991, 0.4905264704675684, 0.4730643391965975),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairVzhxuf2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairVzhxuf2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.0143375396728516, 8.106998443603516, 0.22264212369918823),
            rot=(-0.26693370938301086, 6.170012056827545e-09, -1.8917489796876907e-08, 0.9637148380279541),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/vzhxuf/usd/vzhxuf.usd"),
            visual_material_path="materials",
            scale=(0.7703778737360991, 0.4905264704675684, 0.4494470875945373),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairVzhxuf3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairVzhxuf3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.45996901392936707, 9.01817798614502, 0.2214096188545227),
            rot=(8.381903171539307e-08, 3.700796514749527e-05, -0.00029526176513172686, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/vzhxuf/usd/vzhxuf.usd"),
            visual_material_path="materials",
            scale=(0.7703778737360991, 0.4905264704675684, 0.4730643391965975),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetJhymlr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetJhymlr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.5834808349609375, -4.715108394622803, 0.3951106071472168),
            rot=(0.7071068286895752, -1.862645149230957e-09, -1.178705133497715e-09, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jhymlr/usd/jhymlr.usd"),
            visual_material_path="materials",
            scale=(1.793763610542629, 1.9888139310911077, 2.10561188106883),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetJhymlr1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetJhymlr1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.3663742542266846, 3.682480573654175, 0.3459720313549042),
            rot=(0.707682192325592, 7.450580596923828e-09, 2.713932190090418e-09, 0.7065310478210449),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jhymlr/usd/jhymlr.usd"),
            visual_material_path="materials",
            scale=(1.480629412319034, 1.5588881355471549, 1.8424103959352263),
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
            pos=(-0.7951755523681641, 6.322873592376709, 0.4343213438987732),
            rot=(-2.1573156118392944e-05, 5.6549906730651855e-06, -0.005138571839779615, 0.9999868273735046),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jrhgeu/usd/jrhgeu.usd"),
            visual_material_path="materials",
            scale=(1.2100160034949095, 1.2505751839916852, 1.2284277088786149),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNddvba0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNddvba0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.177555561065674, -3.4974937438964844, 0.3029528558254242),
            rot=(0.707107663154602, -1.615099608898163e-05, 0.00016877532470971346, 0.7071059942245483),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/nddvba/usd/nddvba.usd"),
            visual_material_path="materials",
            scale=(1.4479128208589158, 1.0247754143914667, 1.4537082124760177),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNddvba1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNddvba1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.167555332183838, -6.077494144439697, 0.30295297503471375),
            rot=(0.7071084976196289, -1.5768222510814667e-05, 0.0001699738932074979, 0.7071052193641663),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/nddvba/usd/nddvba.usd"),
            visual_material_path="materials",
            scale=(1.4479128208589158, 1.0247754143914667, 1.4537082124760177),
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
            pos=(-2.6453733444213867, -3.871006727218628, 0.30135729908943176),
            rot=(0.7071068286895752, 3.8533471524715424e-08, 5.1659299060702324e-08, -0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/slgzfc/usd/slgzfc.usd"),
            visual_material_path="materials",
            scale=(0.9267115447630785, 1.3439968857705775, 1.0917638849626186),
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
            pos=(-2.1421122550964355, 8.470818519592285, 0.3926663398742676),
            rot=(0.9683459997177124, -4.656612873077393e-10, -1.1841621017083526e-09, 0.2496124804019928),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(0.5130688593724131, 0.7737983138937623, 0.9830795835697105),
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
            pos=(1.485207438468933, -0.009605474770069122, 0.4003962576389313),
            rot=(1.0, 7.271592039614916e-07, 4.367626388557255e-06, 6.596310413442552e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(0.35935761742165745, 0.8419504646887701, 1.024049898349324),
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
            pos=(-0.22859472036361694, 9.484464645385742, 0.3939599096775055),
            rot=(1.0000001192092896, -4.9219102947972715e-05, 6.147867679828778e-06, -2.6746420189738274e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/uhrsex/usd/uhrsex.usd"),
            visual_material_path="materials",
            scale=(1.247611822062531, 1.1884736898687391, 1.1543835712112702),
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
            pos=(-7.119861602783203, -2.980384588241577, 0.8307554125785828),
            rot=(1.0000001192092896, 0.0001436863385606557, -0.000105897372122854, 3.3268172501266235e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/vdxlda/usd/vdxlda.usd"),
            visual_material_path="materials",
            scale=(1.4401425795695932, 1.2883715079879268, 1.384052031442173),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    floorLampVdxlda1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/floorLampVdxlda1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.179919719696045, -6.5503668785095215, 0.8011457324028015),
            rot=(1.0000001192092896, 0.00013173972547519952, -0.0001325194607488811, 8.401586342188239e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/vdxlda/usd/vdxlda.usd"),
            visual_material_path="materials",
            scale=(1.136974688413501, 1.0608999515141209, 1.3346037632672272),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    floorLampVdxlda2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/floorLampVdxlda2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.599924325942993, -5.75005578994751, 1.0438213348388672),
            rot=(-0.6966354250907898, 1.7368278349749744e-05, 0.0001353084808215499, 0.7174254059791565),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/vdxlda/usd/vdxlda.usd"),
            visual_material_path="materials",
            scale=(0.985200549679146, 0.9852028950955802, 1.7398797713192584),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    floorLampVdxlda3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/floorLampVdxlda3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.6499252319335938, -3.5300562381744385, 1.0438212156295776),
            rot=(-0.7006306648254395, 1.6586753190495074e-05, 0.00013533873425330967, 0.7135241031646729),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/vdxlda/usd/vdxlda.usd"),
            visual_material_path="materials",
            scale=(0.985200549679146, 0.9852028950955802, 1.7398797713192584),
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
            pos=(-2.3423149585723877, 9.67229175567627, 0.29254186153411865),
            rot=(1.0, -0.00023517990484833717, -5.882145615032641e-08, -0.00016340047295670956),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(1.3259190628010278, 1.3702453541721544, 1.3578765880841432),
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
            pos=(-1.5755542516708374, 9.668994903564453, 0.29246023297309875),
            rot=(0.9999890923500061, 8.29999589768704e-06, 1.0360322448832449e-05, -0.004673261195421219),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(1.3259190628010278, 1.3702453541721544, 1.3578765880841432),
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
            pos=(1.4044324159622192, 9.659174919128418, 0.292460173368454),
            rot=(0.9999881982803345, 8.324359441758133e-06, 1.0345785995014012e-05, -0.0048540011048316956),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(1.3259190628010278, 1.3702453541721544, 1.3578765880841432),
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
            pos=(2.3354523181915283, 8.928133010864258, 0.2924601435661316),
            rot=(0.7080664038658142, 1.3299752026796341e-05, 1.462587420064665e-06, -0.7061458826065063),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(1.3259190628010278, 1.3702453541721544, 1.3578765880841432),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfOwvfik4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfOwvfik4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.030263938009738922, 5.850417137145996, 0.14722807705402374),
            rot=(1.0, -5.915790552535327e-06, 1.90846185432747e-06, -1.7077254597097635e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(2.126262979021889, 1.6168811856315388, 0.6789382940420716),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfOwvfik5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfOwvfik5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.08979915827512741, 2.006108045578003, 0.24403433501720428),
            rot=(2.5931280106306076e-05, -1.4774501323699951e-05, 5.3545682021649554e-06, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(0.7795765092131344, 1.8243552465551425, 1.131487443800118),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfOwvfik6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfOwvfik6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.259838730096817, -1.1734668016433716, 0.2924603223800659),
            rot=(2.1385494619607925e-07, -1.0870862752199173e-05, 6.612384822801687e-06, 1.000000238418579),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(1.27586428693625, 1.7826937885383547, 1.3578765880841432),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfOwvfik7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfOwvfik7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.49016129970550537, -1.173466682434082, 0.2924603223800659),
            rot=(2.0256265997886658e-07, -1.0874588042497635e-05, 6.6100592448492534e-06, 1.000000238418579),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(1.27586428693625, 1.7826937885383547, 1.3578765880841432),
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
            pos=(-2.5445051193237305, 9.704917907714844, 0.7778534293174744),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/xbfgjc/usd/xbfgjc.usd"),
            visual_material_path="materials",
            scale=(1.698620220313959, 1.6986008894152753, 1.644819105388792),
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
            pos=(-6.375986585668863, -4.792289540586021, 0.4038584371804823),
            rot=(0.7060505143951661, 0.0, 0.0, 0.7081614724922003),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/zrumze/usd/zrumze.usd"),
            visual_material_path="materials",
            scale=(1.2687257252408617, 1.071555083912308, 1.4099234327626151),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bedZrumze1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bedZrumze1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.9665932257733246, 2.6979974893358416, 0.336884849428126),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/zrumze/usd/zrumze.usd"),
            visual_material_path="materials",
            scale=(0.9750938068788919, 0.9995078421171569, 1.1749161284544754),
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
            pos=(0.7258026045348307, 1.0173311786312174, 0.23640774691342564),
            rot=(-0.7056912171016345, 0.0, 0.0, 0.7085195170957634),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/zrumze/usd/zrumze.usd"),
            visual_material_path="materials",
            scale=(0.7519390335265195, 1.0892224061831133, 0.8225255650784892),
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
            pos=(-8.485218048095703, -3.1825220584869385, 0.5077195167541504),
            rot=(1.9371509552001953e-07, 0.0, -8.731149137020111e-11, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/bamfsz/usd/bamfsz.usd"),
            visual_material_path="materials",
            scale=(1.459753162331445, 1.1678290942388887, 1.819792631949551),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetJhymlr2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetJhymlr2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.003229022026062, -3.8100745677948, 0.3498724400997162),
            rot=(0.7071070075035095, 0.0, 4.0745362639427185e-10, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/jhymlr/usd/jhymlr.usd"),
            visual_material_path="materials",
            scale=(2.450132634537211, 1.7860648343289025, 1.8424103959352263),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetKubcdk0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetKubcdk0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.124483108520508, 0.08751066029071808, 1.223276972770691),
            rot=(0.7075420618057251, -1.1641532182693481e-10, -1.4165379980113357e-10, 0.7066713571548462),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/kubcdk/usd/kubcdk.usd"),
            visual_material_path="materials",
            scale=(2.7391813391185416, 1.430054104736029, 2.5955816856002447),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetKubcdk1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetKubcdk1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.6309096813201904, -6.342732906341553, 1.223276972770691),
            rot=(0.7071069478988647, -5.820766091346741e-11, -3.064997144974768e-10, -0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/kubcdk/usd/kubcdk.usd"),
            visual_material_path="materials",
            scale=(3.06778389903996, 2.31283750400577, 2.5955816856002447),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetKubcdk2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetKubcdk2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.6309096813201904, -2.972733736038208, 1.223276972770691),
            rot=(0.7071069478988647, -5.820766091346741e-11, -3.064997144974768e-10, -0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/kubcdk/usd/kubcdk.usd"),
            visual_material_path="materials",
            scale=(3.06778389903996, 2.31283750400577, 2.5955816856002447),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetRvpunw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetRvpunw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.4479175806045532, -5.100203990936279, 0.3252153992652893),
            rot=(0.70710688829422, 0.0, 8.032657206058502e-09, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/rvpunw/usd/rvpunw.usd"),
            visual_material_path="materials",
            scale=(1.1930593815121477, 1.447841808242337, 1.6875957105161172),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetRvpunw1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetRvpunw1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.4479174613952637, -2.5202038288116455, 0.3252153992652893),
            rot=(0.70710688829422, 0.0, 8.032657206058502e-09, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/rvpunw/usd/rvpunw.usd"),
            visual_material_path="materials",
            scale=(1.1930593815121477, 1.447841808242337, 1.6875957105161172),
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
            pos=(-9.894464355470031, -1.1452032470700002, 0.004372974155),
            rot=(0.7071069003958291, 0.0, 0.0, 0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(0.9038410269525212, 0.6022139707159371, 0.24480330607770978),
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
            pos=(-2.853516479566223, 3.6484763104330833, 0.004372974155),
            rot=(0.7104981600871123, 0.0, 0.0, 0.7036990582008962),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(0.6244111285368348, 0.564712522935424, 0.24480330607770978),
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
            pos=(-2.556207195434693, 5.074074707423591, 0.004372974155),
            rot=(0.7104031557619888, 0.0, 0.0, 0.70379496750361),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(0.6580439413172212, 0.4538835020033234, 0.24480330607770978),
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
            pos=(-2.2244185457201184, 8.469443441162312, 0.004372974155),
            rot=(0.9159531785645701, 0.0, 0.0, 0.401285153821395),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.1131481433819164, 0.9356031301942441, 0.24480330607770978),
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
            pos=(-10.804796875000001, -2.611842834475, 0.56236419678),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(0.5368699095295635, 2.743365550280803, 0.5826772151252665),
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
            pos=(-10.01479882813, -3.11576818848, 0.56236419678),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(1.0053094640698554, 0.9441930769140238, 0.5826772151252665),
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
            pos=(0.61519773865, 1.41444482422, 2.11747351074),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(2.1765551966759276, 0.5878768682306896, 0.8787402325402669),
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
            pos=(1.7952651977539062, 7.2007927894592285, 1.2682102918624878),
            rot=(0.7071069478988647, 0.0, 7.276312885551306e-11, -0.7071065902709961),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(6.659804345860621, 3.146742786073207, 4.9799425513765065),
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
            pos=(1.7952650785446167, 5.0807929039001465, 1.2682102918624878),
            rot=(0.7071069478988647, 5.820766091346741e-11, 7.183942329902493e-11, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(6.659804345860621, 3.146742786073207, 4.9799425513765065),
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
            pos=(-8.57956600189209, -1.065264344215393, 1.2682104110717773),
            rot=(0.39398807287216187, 2.9103830456733704e-11, -4.972022793481301e-12, 0.9191155433654785),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.5628757832741385, 2.554044190334214, 4.9799425513765065),
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
            pos=(-2.0147571563720703, 3.230175733566284, 1.2682102918624878),
            rot=(0.7071069478988647, 1.4551915228366852e-11, -1.0130563055099628e-11, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(2.5369418230143173, 2.0014314899592103, 4.9799425513765065),
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
            pos=(-1.5648542642593384, 2.249225378036499, 1.2682102918624878),
            rot=(0.705384373664856, -2.9103830456733704e-11, -1.7895018800118123e-11, 0.7088251113891602),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.805678382879907, 3.146742786073207, 4.9799425513765065),
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
            pos=(-1.5648542642593384, 1.1392254829406738, 1.2682102918624878),
            rot=(0.705384373664856, -2.9103830456733704e-11, -1.7895018800118123e-11, 0.7088251113891602),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.805678382879907, 3.146742786073207, 4.9799425513765065),
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
            pos=(-7.409740924835205, -1.9496654272079468, 1.2682102918624878),
            rot=(0.70710688829422, 1.4551915228366852e-11, 1.6852297335390176e-11, -0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.594222289568975, 2.860414962044708, 4.9799425513765065),
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
            pos=(-2.3548507690429688, -2.0003063678741455, 1.2682104110717773),
            rot=(0.7099986672401428, 0.0, -7.364775456153438e-12, 0.7042030096054077),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.910343836101649, 2.5740871380162087, 4.9799425513765065),
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
            pos=(-2.189241647720337, 6.119740962982178, 1.2682104110717773),
            rot=(1.9470462575554848e-07, 0.0, -1.4210854715202004e-14, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.699950336224441, 2.860414962044708, 4.9799425513765065),
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
            pos=(1.0107582807540894, 6.119740962982178, 1.2682104110717773),
            rot=(1.9470462575554848e-07, 0.0, -1.4210854715202004e-14, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.699950336224441, 2.860414962044708, 4.9799425513765065),
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
            pos=(-2.4842498302459717, 2.7897403240203857, 1.2682104110717773),
            rot=(1.9470462575554848e-07, 0.0, -8.171241461241152e-14, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.6468206645382772, 2.860414962044708, 4.9799425513765065),
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
            pos=(-5.724745750427246, -1.929665446281433, 1.2682102918624878),
            rot=(0.70710688829422, 1.4551915228366852e-11, 1.4031442674422578e-11, -0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(3.594222289568975, 2.5740871380162087, 4.9799425513765065),
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
            pos=(-1.5898419618606567, -0.3482707440853119, 1.0866132974624634),
            rot=(0.70710688829422, 0.0, 0.0, 0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(1.8269119043886863, 3.1167136725172164, 3.111699687792625),
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
            pos=(-3.9453041553497314, -2.5074284076690674, 1.0866132974624634),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(1.6387347477145204, 2.834162386757099, 3.111699687792625),
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
            pos=(-4.799665259212681, -1.6081906892508269, 1.200281898479443),
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

    electricSwitchWseglt1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.850338891182319, 7.929400131064173, 1.200281898479443),
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
            pos=(-5.592983834720821, -1.5133370688498742, 1.200281898479443),
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

    electricSwitchWseglt11 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt11",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.539106393315821, -1.5133370688498742, 1.200281898479443),
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

    electricSwitchWseglt12 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt12",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.262740973180334, -1.3431316290992759, 1.200281898479443),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/wseglt/usd/wseglt.usd"),
            visual_material_path="materials",
            scale=(0.7152304312209515, 1.5735830575914782, 0.9999999550488176),
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
            pos=(-2.900936958496578, 2.8369366048123057, 1.2002819014327062),
            rot=(0.9999999999999226, -3.632784865903148e-07, -5.4853526623893376e-14, 1.5097625910515964e-07),
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

    electricSwitchWseglt14 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt14",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.979661108817681, 3.507519759969173, 1.200281898479443),
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

    electricSwitchWseglt15 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt15",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6199354008126812, 1.6921830900441732, 1.200281898479443),
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
            pos=(1.8503388911823189, 5.799442123249173, 1.200281898479443),
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
            pos=(-1.741916572756578, 6.1669411214123055, 1.2002819014327064),
            rot=(0.9999999999999226, -3.632784865903148e-07, -5.4853526623893376e-14, 1.5097625910515964e-07),
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
            pos=(1.4374208283691794, 6.166935514160126, 1.200281898479443),
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
            pos=(-1.4166430131865964, 1.7569409993423055, 1.200281901432662),
            rot=(0.9999999999999226, -3.632784865903148e-07, -5.4853526623893376e-14, 1.5097625910515964e-07),
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
            pos=(-1.5096592777626812, 0.7017531584041732, 1.200281898479443),
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
            pos=(-1.7130916228108206, 0.5666648842751256, 1.200281898479443),
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

    electricSwitchWseglt8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.3096614750326814, -2.458424820110827, 1.200281898479443),
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

    electricSwitchWseglt9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.705129830815821, -2.583340773923925, 1.2002819060545995),
            rot=(0.9999999999980815, -1.958808508532894e-06, 0.0, 0.0),
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
            pos=(-8.489796874998893, -3.359641601565, 1.7270000260464788),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(3.349900443425271, 1.7582065844137194, 2.159100173737867),
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
            pos=(-6.339796142580403, -1.52976513672, 1.3520000492679582),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(1.2212468011672577, 1.7582065844137194, 1.5545101396722316),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorPevdqu2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorPevdqu2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.4366717530748314, -4.730241333988064, 1.3025000818519232),
            rot=(0.707529519918363, 0.0, 0.0, -0.7066837895721756),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(1.1864340073795074, 3.2770761468653617, 1.725600722229),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorPevdqu3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorPevdqu3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.6211704561271256, 3.654800049056733, 1.6020000818730264),
            rot=(0.7088547864096404, 0.0, 0.0, 0.7053544440805226),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(2.547281861022266, 3.958266132449735, 1.7273501146886807),
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
            pos=(0.1402041930989645, -1.4084885484717486, 1.6021636961633297),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/cltbty/usd/cltbty.usd"),
            visual_material_path="materials",
            scale=(1.367606151283157, 1.1028412941285772, 0.8633032227918153),
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
            pos=(-2.717555013908179, 7.064793548059169, 1.5022861456127106),
            rot=(0.7074766504495724, 0.0, 0.0, 0.7067367183532023),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/fhkzlm/usd/fhkzlm.usd"),
            visual_material_path="materials",
            scale=(1.3385888121099672, 1.1028412941285772, 0.672278543835387),
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
            pos=(-2.3064578350857152, -3.8577043574337697, 1.5022859982360224),
            rot=(0.7071069003958291, 0.0, 0.0, 0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/gwricv/usd/gwricv.usd"),
            visual_material_path="materials",
            scale=(0.909307171276444, 1.1028412941285772, 1.510782534901735),
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
            pos=(-2.295990893805024, -5.375213469332692, 1.6271840343527813),
            rot=(0.7091125749435224, 0.0, 0.0, 0.7050952815449606),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/szpupz/usd/szpupz.usd"),
            visual_material_path="materials",
            scale=(1.0767036806775596, 1.1028412941285772, 1.1524398168607066),
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
            pos=(-7.348093279094767, -5.19770394660728, 1.5772248525539847),
            rot=(0.7071069003958291, 0.0, 0.0, 0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/weqggl/usd/weqggl.usd"),
            visual_material_path="materials",
            scale=(0.909307171276444, 1.1028412941285772, 1.4084306462589191),
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
            pos=(-7.348080288502694, -4.5077044372212125, 1.577224824828672),
            rot=(0.7071069003958291, 0.0, 0.0, 0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/yrgaal/usd/yrgaal.usd"),
            visual_material_path="materials",
            scale=(0.909307171276444, 1.1028412941285772, 1.1867734017677918),
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
            pos=(-1.142286438213204, -1.5236531025916227, 1.5022861456127106),
            rot=(0.9999963482487709, 0.0, 0.0, 0.002702496831239154),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/ytxhyl/usd/ytxhyl.usd"),
            visual_material_path="materials",
            scale=(0.909307171276444, 1.1028412941285772, 0.672278543835387),
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
            pos=(1.5471298190954472, -5.079459871179058, 1.5479915973223686),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/njwsoa/usd/njwsoa.usd"),
            visual_material_path="materials",
            scale=(1.815609221559937, 2.6443985389182103, 1.4852572703803932),
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
            pos=(1.547129330815458, -2.5394597805661028, 1.5479915973223686),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/njwsoa/usd/njwsoa.usd"),
            visual_material_path="materials",
            scale=(1.815609221559937, 2.6443985389182103, 1.4852572703803932),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfOwvfik8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfOwvfik8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.7054376002013845, -0.4952975770879741, 1.9900505499235925),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(3.27805532152736, 1.6168811856315388, 1.8104257378421895),
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
            pos=(-8.374937253760812, 0.6824039999860153, 1.2355468728870773),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/vgzdul/usd/vgzdul.usd"),
            visual_material_path="materials",
            scale=(2.8687086054935422, 4.266469013172987, 4.102746437598094),
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
            pos=(-10.730951207231982, -0.8317039946463096, 1.211817656727181),
            rot=(0.7071069003958291, 0.0, 0.0, 0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shower_stall/invgma/usd/invgma.usd"),
            visual_material_path="materials",
            scale=(2.1068157447490803, 1.0534123511507987, 1.1653542935171972),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    showerStallInvgma1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/showerStallInvgma1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.354000839701719, 5.3532881952524525, 1.2118176567271808),
            rot=(0.7075836660429415, 0.0, 0.0, 0.7066295744937591),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shower_stall/invgma/usd/invgma.usd"),
            visual_material_path="materials",
            scale=(1.6853558752325364, 0.9618901257610186, 1.1653542935171972),
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
            pos=(-9.149801254272461, -3.0569772720336914, 0.46342068910598755),
            rot=(1.94646418094635e-07, 1.4551915228366852e-11, -1.8203536455985159e-09, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/ksecxq/usd/ksecxq.usd"),
            visual_material_path="materials",
            scale=(4.665884105773261, 4.247866731308698, 4.481572962832644),
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
            pos=(-7.81980037689209, -3.0569779872894287, 0.46342068910598755),
            rot=(1.94646418094635e-07, 1.4551915228366852e-11, -1.8203536455985159e-09, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/ksecxq/usd/ksecxq.usd"),
            visual_material_path="materials",
            scale=(4.665884105773261, 4.247866731308698, 4.481572962832644),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkZexzrc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkZexzrc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.3790650367736816, 3.6379318237304688, 0.4518513083457947),
            rot=(0.705139696598053, 4.656612873077393e-10, 1.2397549653542228e-09, 0.7090684175491333),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/zexzrc/usd/zexzrc.usd"),
            visual_material_path="materials",
            scale=(5.4676421703345595, 3.858584913549418, 4.472965008294247),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaQnnwfx0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaQnnwfx0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.8318585204554998, -3.8355503037968686, 0.420889709652545),
            rot=(0.7065748482298733, 0.0, 0.0, 0.7076383142884024),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/qnnwfx/usd/qnnwfx.usd"),
            visual_material_path="materials",
            scale=(1.0820632334623141, 1.2211066309359058, 1.2072795829177738),
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
            pos=(-10.808442115783691, 0.6319103837013245, 0.28861311078071594),
            rot=(0.7054212093353271, -1.1990778148174286e-08, 1.3504177331924438e-08, 0.7087884545326233),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/kfmkbm/usd/kfmkbm.usd"),
            visual_material_path="materials",
            scale=(1.1585841782974753, 0.9677724637571141, 1.0725545782987151),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    toiletKfmkbm1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/toiletKfmkbm1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.9640876054763794, 5.57883882522583, 0.28861314058303833),
            rot=(-0.706541121006012, -3.91155481338501e-08, 5.005858838558197e-09, 0.707672119140625),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/kfmkbm/usd/kfmkbm.usd"),
            visual_material_path="materials",
            scale=(1.1917293053599758, 1.081709040496792, 1.0725545782987151),
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
            pos=(-10.981155395507812, 0.5449404120445251, 1.8026957511901855),
            rot=(0.7066763043403625, -9.313225746154785e-10, -1.901980795082636e-09, 0.7075371146202087),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/dmwxyl/usd/dmwxyl.usd"),
            visual_material_path="materials",
            scale=(1.439859408754819, 1.2753370799483754, 1.2663481659487783),
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
            pos=(-0.7723817825317383, 5.576444149017334, 1.8026957511901855),
            rot=(-0.7043524384498596, 0.0, 1.8178525351686403e-10, 0.709850549697876),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/dmwxyl/usd/dmwxyl.usd"),
            visual_material_path="materials",
            scale=(1.7258731483700342, 1.041370775908002, 1.2663481659487783),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    topCabinetFqhdne0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/topCabinetFqhdne0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.00483905291184783, 5.996791839599609, 2.001493453979492),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/top_cabinet/fqhdne/usd/fqhdne.usd"),
            visual_material_path="materials",
            scale=(1.3262186319739333, 0.8721194246066409, 0.9814756760807563),
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
            pos=(-9.109798482060775, -0.610674708408806, 0.9670316738083125),
            rot=(0.9165372415276547, 0.0, 0.0, -0.39994935290968725),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/towel_rack/kqrmrh/usd/kqrmrh.usd"),
            visual_material_path="materials",
            scale=(1.2222324931626198, 0.6889694360056238, 0.4668082200873506),
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
            pos=(-1.6582854898986086, 4.574799202425936, 0.9670316738083125),
            rot=(-0.7058184174947736, 0.0, 0.0, 0.708392801717503),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/towel_rack/kqrmrh/usd/kqrmrh.usd"),
            visual_material_path="materials",
            scale=(1.475202760606428, 1.2043949334707882, 0.4668082200873506),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    towelRackKqrmrh2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/towelRackKqrmrh2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.3097952034106861, 6.028407047324508, 0.9670316738083123),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/towel_rack/kqrmrh/usd/kqrmrh.usd"),
            visual_material_path="materials",
            scale=(1.2644293684660073, 1.376203432625843, 0.4668082200873506),
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
            pos=(1.0980095863342285, -3.7481021881103516, 1.2972817420959473),
            rot=(-0.7053802013397217, 0.0, 5.820766091346741e-11, 0.7088292241096497),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/ylvjhb/usd/ylvjhb.usd"),
            visual_material_path="materials",
            scale=(1.261621605362485, 0.22423002391580013, 0.9676656669256155),
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
            pos=(1.807605504989624, 2.8177013397216797, 1.5694540739059448),
            rot=(0.70710688829422, 3.725290298461914e-09, -4.580215318128467e-09, -0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ithrgo/usd/ithrgo.usd"),
            visual_material_path="materials",
            scale=(0.9950787084002418, 1.3134749107165347, 1.4457436540770203),
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
            pos=(1.807611346244812, -0.06741444766521454, 1.5694540739059448),
            rot=(0.7081077098846436, 1.862645149230957e-09, -1.3378667063079774e-09, -0.7061045169830322),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ithrgo/usd/ithrgo.usd"),
            visual_material_path="materials",
            scale=(1.067060333399587, 1.3134749107165347, 1.4457436540770203),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowIthrgo2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowIthrgo2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.3113931715488434, -6.052803039550781, 1.4721397161483765),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ithrgo/usd/ithrgo.usd"),
            visual_material_path="materials",
            scale=(1.6169290822551112, 1.3134749107165347, 1.66821782386554),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowIthrgo3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowIthrgo3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.871668338775635, -6.768926620483398, 1.4261672496795654),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ithrgo/usd/ithrgo.usd"),
            visual_material_path="materials",
            scale=(1.4860235746218449, 1.1945234173723298, 2.0018162620322),
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
            pos=(-10.372308731079102, -3.432192087173462, 1.425315499305725),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.5340173697535633, 1.3192005377053997, 1.7269234185586502),
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
            pos=(-11.136509895324707, -2.5626895427703857, 1.425315499305725),
            rot=(0.70710688829422, -1.862645149230957e-09, 2.5693225325085223e-10, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.5340173697535633, 1.4391278593149817, 1.7269234185586502),
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
            pos=(-0.22940385341644287, 9.928354263305664, 1.2767727375030518),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.746010654838739, 1.5590551809245634, 1.8348697755902836),
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
            pos=(-3.2467334270477295, 8.521687507629395, 1.2767727375030518),
            rot=(0.708284318447113, 9.313225746154785e-10, 7.848370842111763e-10, -0.7059272527694702),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.1723303574498218, 1.4391278593149817, 1.8348697755902836),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
