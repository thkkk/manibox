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
class merom0IntquickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Merom_0_int/usd/Merom_0_int_quick.usd"),
        )
    )
@configclass
class merom0IntfullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/Merom_0_int/usd/Merom_0_int_quick.usd"),
        )
    )
    armchairBslhmj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairBslhmj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.8012287616729736, -1.1783872842788696, 0.2662072479724884),
            rot=(0.26669347286224365, -0.0008669719099998474, 0.00232614204287529, 0.9637783169746399),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/bslhmj/usd/bslhmj.usd"),
            visual_material_path="materials",
            scale=(0.8678335290908785, 0.8749412372075808, 0.8501039293066374),
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
            pos=(1.5951576232910156, -0.13014176487922668, 0.2742346227169037),
            rot=(0.710818886756897, -0.00013300019782036543, -0.00016278785187751055, 0.7033752799034119),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/vzhxuf/usd/vzhxuf.usd"),
            visual_material_path="materials",
            scale=(1.4674215227061214, 0.8828162264878476, 0.5912704817327975),
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
            pos=(4.541855335235596, 1.2253882884979248, 0.17046426236629486),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/zrumze/usd/zrumze.usd"),
            visual_material_path="materials",
            scale=(0.5145928506245492, 0.7545275349749014, 0.5875182607703494),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetImmwzb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetImmwzb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.4930751323699951, 0.7802926898002625, 0.3379143178462982),
            rot=(0.707120954990387, -0.003082753624767065, -0.0030808355659246445, 0.707079291343689),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/immwzb/usd/immwzb.usd"),
            visual_material_path="materials",
            scale=(2.0852266311675987, 1.0576690341207025, 1.2737255122042237),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNyfebf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNyfebf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.4858665466308594, 2.154510498046875, 0.5596002340316772),
            rot=(0.7071069478988647, 1.6298145055770874e-08, 6.344816938508302e-08, 0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/nyfebf/usd/nyfebf.usd"),
            visual_material_path="materials",
            scale=(1.3436973987136538, 1.5545942578607768, 1.188210795232437),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableDnsjnv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableDnsjnv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.039973258972168, 7.429669380187988, 0.37357297539711),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/dnsjnv/usd/dnsjnv.usd"),
            visual_material_path="materials",
            scale=(1.1972557148943659, 1.143867514119013, 1.3975343090515038),
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
            pos=(4.518186569213867, 2.308764696121216, 0.07849932461977005),
            rot=(1.9476283341646194e-07, 0.0, -2.2509993868879974e-11, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/cedar_chest/fwstpx/usd/fwstpx.usd"),
            visual_material_path="materials",
            scale=(1.416341270340964, 0.702141499817986, 1.1507841888778216),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pianoBnxcvw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pianoBnxcvw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.3946385383605957, 5.958283424377441, 0.4047319293022156),
            rot=(0.70710688829422, -5.587935447692871e-08, -7.410744728986174e-08, 0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/piano/bnxcvw/usd/bnxcvw.usd"),
            visual_material_path="materials",
            scale=(0.6062771378318927, 0.5633070950741971, 0.7223296080688868),
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
            pos=(4.763285160064697, 6.547177791595459, 0.546491265296936),
            rot=(-0.7002769708633423, -5.8501726016402245e-05, -0.0003647387493401766, 0.7138712406158447),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/pot_plant/udqjui/usd/udqjui.usd"),
            visual_material_path="materials",
            scale=(1.1023621695432948, 1.0991768328862408, 1.7695231941538843),
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
            pos=(-0.040457021445035934, 5.569638252258301, 0.3872830271720886),
            rot=(0.7070593237876892, 6.691738963127136e-05, -4.8743935622042045e-05, -0.707154393196106),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(1.4175086526812593, 1.1606882203477111, 1.8104257378421895),
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
            pos=(4.619558334350586, 9.237770080566406, 0.2178695648908615),
            rot=(-0.7057101726531982, -6.219022907316685e-06, -1.0788535291794688e-06, 0.7085007429122925),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(2.0032560298222757, 2.405532585889334, 1.0185220104681094),
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
            pos=(3.0299110412597656, -1.509596347808838, 0.19365626573562622),
            rot=(3.117311280220747e-07, -7.22415279597044e-06, 8.37311745272018e-06, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(1.27586428693625, 0.8707244725508673, 0.9053274383260967),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    loudspeakerSnbvop0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/loudspeakerSnbvop0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.475841999053955, 8.511186599731445, 0.5009580254554749),
            rot=(-0.39687690138816833, 0.0, -1.3869794202037156e-11, 0.91787189245224),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/loudspeaker/snbvop/usd/snbvop.usd"),
            visual_material_path="materials",
            scale=(0.9353875222402975, 1.4426942443780562, 2.249783883658761),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    loudspeakerSnbvop1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/loudspeakerSnbvop1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.4840240478515625, 9.981164932250977, 0.5009580254554749),
            rot=(0.8137334585189819, 0.0, 2.8194335754960775e-11, -0.5812382698059082),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/loudspeaker/snbvop/usd/snbvop.usd"),
            visual_material_path="materials",
            scale=(0.9353875222402975, 1.4426942443780562, 2.249783883658761),
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
            pos=(4.582403182983398, 9.231735229492188, 0.5768308043479919),
            rot=(-0.7047299146652222, 2.3283064365386963e-10, 1.651869752095081e-10, 0.7094758152961731),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/standing_tv/udotid/usd/udotid.usd"),
            visual_material_path="materials",
            scale=(1.1737882634635652, 1.2546365342293575, 1.1844323216699364),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairAmgwaw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairAmgwaw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.8913025856018066, 5.908707141876221, 0.21196572482585907),
            rot=(-0.6989345550537109, -6.751902401447296e-05, 2.7546542696654797e-05, 0.7151856422424316),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/amgwaw/usd/amgwaw.usd"),
            visual_material_path="materials",
            scale=(0.9302546311907809, 0.5477785810123099, 0.5066445784947106),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairAmgwaw1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairAmgwaw1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.045694828033447, 7.914733409881592, 0.2767890989780426),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/amgwaw/usd/amgwaw.usd"),
            visual_material_path="materials",
            scale=(0.8005827735096417, 0.7302952021596266, 0.6333057231183882),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    straightChairAmgwaw2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/straightChairAmgwaw2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.205724716186523, 6.904610633850098, 0.2767890989780426),
            rot=(-0.14839129149913788, 0.0, 2.1012965589761734e-08, 0.9889287352561951),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/straight_chair/amgwaw/usd/amgwaw.usd"),
            visual_material_path="materials",
            scale=(0.8005827735096417, 0.7302952021596266, 0.6333057231183882),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    trashCanWklill0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/trashCanWklill0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.994970977306366, -0.8599866032600403, 0.1811416745185852),
            rot=(0.9999992847442627, -0.0012630181154236197, 0.0001858830073615536, 0.0002842117100954056),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/trash_can/wklill/usd/wklill.usd"),
            visual_material_path="materials",
            scale=(0.8603077690746672, 0.8286544697757334, 1.0266424372090468),
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
            pos=(3.054969072341919, 4.290130138397217, 0.17370612919330597),
            rot=(0.999997079372406, -0.0023725403007119894, 0.0006690663285553455, 2.2038480892661028e-05),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/trash_can/zotrbg/usd/zotrbg.usd"),
            visual_material_path="materials",
            scale=(0.5899991362202983, 0.6740719920857905, 0.7855449201192258),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetDajebq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetDajebq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.44283390045166, 4.753091335296631, 0.883004367351532),
            rot=(0.7075175642967224, -5.4569682106375694e-12, -3.092281986027956e-11, 0.7066957354545593),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/dajebq/usd/dajebq.usd"),
            visual_material_path="materials",
            scale=(1.4056800706956214, 1.2114874582185504, 1.9446632064509644),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNoTopVdedzt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNoTopVdedzt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.170546755194664, 8.399528503417969, 0.421340674161911),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet_no_top/vdedzt/usd/vdedzt.usd"),
            visual_material_path="materials",
            scale=(1.0477088997515607, 1.144207598381883, 1.3109182778400208),
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
            pos=(-2.2106740041259063, -0.7322117746917175, 0.7892540869679651),
            rot=(0.7085662413473311, 0.0, 0.0, 0.7056443024803047),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/skczfi/usd/skczfi.usd"),
            visual_material_path="materials",
            scale=(1.6935041844787062, 1.3449495245386516, 2.048099796698648),
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
            pos=(3.884581543017661, 5.504668457037483, 0.002371712260245719),
            rot=(-0.7049606277910362, -7.153321624783706e-15, -4.760267781590695e-17, 0.709246440431299),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(0.5455536111925307, 0.6790210596409741, 0.24480330607770978),
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
            pos=(3.9596810259139064, 4.569670410155039, 0.0023726689250000003),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(0.5699618903705296, 0.48687446637380916, 0.24480330607770978),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    carpetCtclvd10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/carpetCtclvd10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.0499487304699997, -0.6310666961649999, 0.0023726689250000003),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(0.55371691526544, 1.3325256702766508, 0.24480330607770978),
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
            pos=(3.969727852899479, 7.390934083220235, 0.0023726689250000003),
            rot=(-0.6990274198990035, 0.0, 0.0, 0.71509486519576),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.4213945051749728, 1.562302582278901, 0.24480330607770978),
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
            pos=(-1.312858917235, -1.22567739868, 0.002372668925),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(0.8142079482319767, 0.6278592906758068, 0.24480330607770978),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    carpetCtclvd4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/carpetCtclvd4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.1350536193850001, 0.058805938725000055, 0.0023726689250000003),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.3597615594245074, 1.5632046789609066, 0.24480330607770978),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    carpetCtclvd5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/carpetCtclvd5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7249483642550001, 6.814322753904998, 0.002372668925),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(0.6269417527994366, 0.6278592906758068, 0.24480330607770978),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    carpetCtclvd6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/carpetCtclvd6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6804683269773486, 7.089954510265187, 0.0023726689250000003),
            rot=(-0.4692384426784355, 0.0, 0.0, 0.8830715055490789),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(0.8049834146295892, 0.9173034546449903, 0.24480330607770978),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    carpetCtclvd7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/carpetCtclvd7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.5836083374000003, 7.658771972654999, 0.0023726689250000007),
            rot=(0.7099296325495431, 0.0, 0.0, 0.704272615418256),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(0.6332274969355768, 0.6571129973636984, 0.24480330607770978),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    carpetCtclvd8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/carpetCtclvd8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.0299484863250004, 9.81432373047, 0.0023726689250000003),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(0.6514316650181647, 0.6278592906758068, 0.24480330607770978),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    carpetCtclvd9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/carpetCtclvd9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.079946777345001, 1.203374145505, 0.0023726689250000007),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/carpet/ctclvd/usd/ctclvd.usd"),
            visual_material_path="materials",
            scale=(1.2865367218905108, 2.34480701844136, 0.24480330607770978),
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
            pos=(-1.19505755615, 8.36907348633, 0.81031542969),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(2.645092648719781, 0.9975058799260892, 0.5858268216935112),
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
            pos=(-1.1950575561499999, 8.494297851565, 1.3103154907249999),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(2.645092648719781, 0.6234187369054001, 0.5858268216935112),
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
            pos=(-1.1950575561499999, 8.494297851565001, 1.710315490725),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/countertop/tpuwys/usd/tpuwys.usd"),
            visual_material_path="materials",
            scale=(2.645092648719781, 0.6234187369054001, 0.5858268216935112),
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
            pos=(1.2300137281417847, 7.725309371948242, 1.1510981321334839),
            rot=(0.708690345287323, 0.0, -3.33244543071487e-12, -0.7055197954177856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.281188944471071, 3.4302073318614217, 4.527199682615753),
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
            pos=(2.195591688156128, 4.064608573913574, 1.1510995626449585),
            rot=(1.9470462575554848e-07, 0.0, 6.536993168992922e-13, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.281188944471071, 3.146742786073207, 4.527199682615753),
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
            pos=(2.8598825931549072, 5.674027919769287, 1.1510995626449585),
            rot=(0.7076565027236938, 0.0, 1.3208989457780262e-11, 0.7065567970275879),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.281188944471071, 3.4302073318614217, 4.527199682615753),
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
            pos=(0.7042771577835083, 8.714754104614258, 1.1510995626449585),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.492645037782004, 4.289190803946919, 4.527199682615753),
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
            pos=(4.124341011047363, 3.084719657897949, 1.1510995626449585),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/lvgliq/usd/lvgliq.usd"),
            visual_material_path="materials",
            scale=(4.06973285116014, 2.5740871380162087, 4.527199682615753),
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
            pos=(3.3692948818206787, 10.187009811401367, 1.0846130847930908),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ohagsq/usd/ohagsq.usd"),
            visual_material_path="materials",
            scale=(2.112157820614232, 3.4021481346626414, 3.111699687792625),
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
            pos=(0.4380280673503876, -1.182214617729187, 0.5285660624504089),
            rot=(1.9470462575554848e-07, 0.0, -2.892193151637912e-10, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/clothes_dryer/zlmnfg/usd/zlmnfg.usd"),
            visual_material_path="materials",
            scale=(1.1831351174819953, 1.3613291804096932, 1.1835704280242865),
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
            pos=(-2.569917090262681, 4.020249984574173, 1.019928138714443),
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
            pos=(3.320086815987319, 3.2040290373141733, 1.000281898479443),
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
            pos=(2.6818545441891795, 4.006536710450126, 1.200281898479443),
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
            pos=(2.920084618722319, 5.172113021684173, 1.200281898479443),
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
            pos=(1.290084374577319, 8.214041488484174, 1.200281898479443),
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

    electricSwitchWseglt5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchWseglt5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.1814132600091794, 8.786814664550125, 1.200281898479443),
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
            pos=(1.1698064204773189, 8.208566879109174, 1.200281898479443),
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

    mirrorPevdqu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorPevdqu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.60060864257938, 4.539669433590224, 1.4499998314820404),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/pevdqu/usd/pevdqu.usd"),
            visual_material_path="materials",
            scale=(1.3783417198677588, 2.637309876620579, 1.20918006813127),
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
            pos=(4.967252538585605, 7.369674980934204, 1.4502861891022354),
            rot=(-0.7057935764754325, 0.0, 0.0, 0.7084175515937038),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/fanvpf/usd/fanvpf.usd"),
            visual_material_path="materials",
            scale=(0.7710738168232578, 1.1028412941285772, 1.5107621578916675),
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
            pos=(1.3028673078059947, 1.6746764998087522, 1.6251020553558753),
            rot=(0.7056443622078424, 0.0, 0.0, 0.7085661818660889),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/fhkzlm/usd/fhkzlm.usd"),
            visual_material_path="materials",
            scale=(0.8148185492451521, 1.1028412941285772, 0.24011337860864473),
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
            pos=(1.2944453282412423, 0.6646415101280142, 1.6251020681167254),
            rot=(0.7056443622078424, 0.0, 0.0, 0.7085661818660889),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/gwricv/usd/gwricv.usd"),
            visual_material_path="materials",
            scale=(0.8148185492451521, 1.1028412941285772, 0.5395964249113577),
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
            pos=(4.9695981595129775, 8.127220729206172, 1.4502858573316866),
            rot=(-0.7057935764754325, 0.0, 0.0, 0.7084175515937038),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/qjkajj/usd/qjkajj.usd"),
            visual_material_path="materials",
            scale=(0.923742932975669, 1.1028412941285772, 1.510782534901735),
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
            pos=(3.994950943702164, 6.3913715611628215, 1.6501225878437664),
            rot=(1.9470718377062835e-07, 0.0, 0.0, 0.9999999999999812),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/szpupz/usd/szpupz.usd"),
            visual_material_path="materials",
            scale=(1.4113508837050515, 1.1028412941285772, 0.7682067306899037),
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
            pos=(1.3039595319827701, 6.6072842572309884, 1.5003266587621114),
            rot=(0.7091052049834872, 0.0, 0.0, 0.705102693418006),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/weqggl/usd/weqggl.usd"),
            visual_material_path="materials",
            scale=(1.1856280644080766, 1.1028412941285772, 2.0486971474501163),
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
            pos=(1.3028228019045356, 2.7946762323130874, 1.6251020377443195),
            rot=(0.7056443622078424, 0.0, 0.0, 0.7085661818660889),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/yrgaal/usd/yrgaal.usd"),
            visual_material_path="materials",
            scale=(0.8148185492451521, 1.1028412941285772, 0.5395020732294916),
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
            pos=(-2.044998779300051, 8.335479744265493, 0.3880501775135924),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(1.789724485973596, 2.155980452368774, 1.8104257378421895),
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
            pos=(-1.0249987793000508, 8.335479744265493, 0.38805017751359244),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/owvfik/usd/owvfik.usd"),
            visual_material_path="materials",
            scale=(1.789724485973596, 2.155980452368774, 1.8104257378421895),
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
            pos=(4.674096138892654, 5.6706965601723285, 1.2098174125871806),
            rot=(-0.7065042793935277, 0.0, 0.0, 0.7077087700450182),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shower_stall/invgma/usd/invgma.usd"),
            visual_material_path="materials",
            scale=(1.400030203385421, 0.9719249272238346, 1.1653542935171972),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkXiybkb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkXiybkb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.357407569885254, 4.707003116607666, 0.4309220016002655),
            rot=(0.7071070075035095, -1.4901161193847656e-08, -9.313225746154785e-10, -0.7071067094802856),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/xiybkb/usd/xiybkb.usd"),
            visual_material_path="materials",
            scale=(3.69835406069099, 5.1545155888418375, 4.348833940264611),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaMnfbbh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaMnfbbh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.753133832329457, 9.07213943776784, 0.379156404672343),
            rot=(0.7071069003958291, 0.0, 0.0, 0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/mnfbbh/usd/mnfbbh.usd"),
            visual_material_path="materials",
            scale=(1.220086186091382, 1.2532786941711263, 1.188806913396657),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaMnfbbh1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaMnfbbh1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.499468743048816, -0.7753057027830802, 0.37650766898562876),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/mnfbbh/usd/mnfbbh.usd"),
            visual_material_path="materials",
            scale=(0.9796325492408042, 1.3296856194704296, 1.1963837579689747),
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
            pos=(3.429351806640625, 4.42055606842041, 0.3307015597820282),
            rot=(1.9511207938194275e-07, 0.0, 3.0740920919924974e-10, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/kfmkbm/usd/kfmkbm.usd"),
            visual_material_path="materials",
            scale=(1.1433822779154263, 1.1496923453490169, 1.2377172845579312),
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
            pos=(3.6149510115867707, 6.227627283817501, 1.4100209937966528),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/towel_rack/kqrmrh/usd/kqrmrh.usd"),
            visual_material_path="materials",
            scale=(1.7070745903985425, 1.0325864343157334, 0.31173294697358667),
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
            pos=(-0.3960520029067993, -1.228691577911377, 0.5788235664367676),
            rot=(1.9371509552001953e-07, 0.0, -4.656612873077393e-10, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/washer/omeuop/usd/omeuop.usd"),
            visual_material_path="materials",
            scale=(1.208986412893891, 1.52559101297616, 1.2884211934596905),
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
            pos=(2.803048849105835, -1.8359496593475342, 1.757285237312317),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.0850610369112248, 1.9188371457533089, 0.5396226381844246),
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
            pos=(-0.01695145294070244, -1.8359497785568237, 1.757285237312317),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.0850610369112248, 1.9188371457533089, 0.5396226381844246),
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
            pos=(-2.628061532974243, 5.917767524719238, 1.757285237312317),
            rot=(0.7071070075035095, -4.656612873077393e-10, -5.991296347929165e-11, 0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.0850610369112248, 1.3192005377053997, 0.5396226381844246),
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
            pos=(-2.628061294555664, 1.6477677822113037, 1.757285237312317),
            rot=(0.7071070075035095, -4.656612873077393e-10, -5.991296347929165e-11, 0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.0850610369112248, 1.3192005377053997, 0.5396226381844246),
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
            pos=(5.053782939910889, 6.708799839019775, 1.6058279275894165),
            rot=(0.7071069478988647, 9.313225746154785e-10, 3.2036950869951397e-10, -0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(0.6859193805995017, 1.6789825025341452, 0.4316762811527911),
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
            pos=(5.053782939910889, 1.3215707540512085, 1.757285237312317),
            rot=(0.7071070075035095, 4.656612873077393e-10, -4.745857040688861e-10, -0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ulnafj/usd/ulnafj.usd"),
            visual_material_path="materials",
            scale=(1.0850610369112248, 1.6789825025341452, 0.5396226381844246),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
