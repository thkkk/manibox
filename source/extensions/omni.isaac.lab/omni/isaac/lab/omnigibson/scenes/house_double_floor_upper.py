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
class houseDoubleFloorUpperquickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/house_double_floor_upper/usd/house_double_floor_upper_quick.usd"),
        )
    )
@configclass
class houseDoubleFloorUpperfullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/house_double_floor_upper/usd/house_double_floor_upper_quick.usd"),
        )
    )
    bidetLcyvov0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bidetLcyvov0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.08038553160196016, 3.8684791262016422, 0.34934098064922886),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bidet/lcyvov/usd/lcyvov.usd"),
            visual_material_path="materials",
            scale=(1.0000360294540607, 1.0000269649055216, 1.0000060665452475),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchStrbnw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchStrbnw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.30884674191474915, 1.3502700328826904, 1.2362016439437866),
            rot=(-0.7071066498756409, -4.656612873077393e-10, -2.0404513634275645e-09, 0.7071070671081543),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/strbnw/usd/strbnw.usd"),
            visual_material_path="materials",
            scale=(1.0013957018592636, 1.0000000223517422, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    electricSwitchStrbnw1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/electricSwitchStrbnw1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.6387317180633545, 1.298702359199524, 1.2362016439437866),
            rot=(1.0000001192092896, 5.129550117999315e-10, 3.1104718800634146e-10, -1.5051045920699835e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/electric_switch/strbnw/usd/strbnw.usd"),
            visual_material_path="materials",
            scale=(1.0013957018592636, 1.0000000223517422, 1.0000000223517422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hookAkwlam0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hookAkwlam0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.39085096280356185, 4.081344521205848, 1.0294354154334258),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hook/akwlam/usd/akwlam.usd"),
            visual_material_path="materials",
            scale=(0.9996859003305063, 0.9994481709832832, 0.9989967511602638),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    stairsTikozn0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/stairsTikozn0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.10299262841682155, -2.4948272285415207, -1.479396849809227),
            rot=(7.54979013252756e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/stairs/tikozn/usd/tikozn.usd"),
            visual_material_path="materials",
            scale=(0.999996447385544, 1.000011004713109, 0.9999957382606783),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowLhzwtz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowLhzwtz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.591843828450902, -1.350947805163359, 1.192079935905505),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/lhzwtz/usd/lhzwtz.usd"),
            visual_material_path="materials",
            scale=(0.9999639513116041, 1.0003947409155876, 0.9999814355365522),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowLhzwtz1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowLhzwtz1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.401225088807614, 0.7454794199153574, 1.192076029655505),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/lhzwtz/usd/lhzwtz.usd"),
            visual_material_path="materials",
            scale=(0.9999639513116041, 1.0003947409155876, 0.9999814355365522),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowLhzwtz2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowLhzwtz2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.401225088807615, -1.3970010488346425, 1.1920760296555049),
            rot=(0.7071069003958291, 0.0, 0.0, -0.7071066619772458),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/lhzwtz/usd/lhzwtz.usd"),
            visual_material_path="materials",
            scale=(0.9999639513116041, 1.0003947409155876, 0.9999814355365522),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowLhzwtz3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowLhzwtz3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.591843828450902, 0.5852671606566413, 1.192079935905505),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/lhzwtz/usd/lhzwtz.usd"),
            visual_material_path="materials",
            scale=(0.9999639513116041, 1.0003947409155876, 0.9999814355365522),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetNcgmqr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetNcgmqr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.850066900253296, -4.409877777099609, 0.40412816405296326),
            rot=(0.6962979435920715, -0.0007187383016571403, 0.7177522778511047, -0.000694590387865901),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/ncgmqr/usd/ncgmqr.usd"),
            visual_material_path="materials",
            scale=(1.000069083755312, 0.9999368938928446, 0.999994864325056),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    servingCartVvtcby0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/servingCartVvtcby0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.055343508720398, 1.6547287702560425, 0.3539902865886688),
            rot=(1.0000001192092896, 0.0003048484504688531, 8.531670573574957e-06, 9.199229680234566e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/serving_cart/vvtcby/usd/vvtcby.usd"),
            visual_material_path="materials",
            scale=(1.000130908934833, 0.9999820109003491, 1.0000242138861881),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfBsvnni0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfBsvnni0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.327206611633301, -3.8684401512145996, 0.3626537024974823),
            rot=(-0.5016422867774963, 0.4983437657356262, 0.5016624927520752, -0.49834057688713074),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/bsvnni/usd/bsvnni.usd"),
            visual_material_path="materials",
            scale=(1.0000188581443292, 1.0000659072179454, 0.999895902674935),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorDlncrt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorDlncrt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.1362345218658447, 2.8556714057922363, 1.0276659727096558),
            rot=(-0.7071067690849304, -1.9049912225455046e-06, 9.530822353553958e-07, 0.70710688829422),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/dlncrt/usd/dlncrt.usd"),
            visual_material_path="materials",
            scale=(1.0003868178775288, 0.9999827634965138, 0.9999901726467587),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorPevmgl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorPevmgl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.3618625402450562, 3.7988786697387695, 0.8276862502098083),
            rot=(-0.7071067690849304, -1.9017606973648071e-06, 9.554642019793391e-07, 0.7071068286895752),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/pevmgl/usd/pevmgl.usd"),
            visual_material_path="materials",
            scale=(0.9999867127669987, 0.9997028376630565, 1.0000007027078848),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfEckdny0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfEckdny0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.6011537280769037, -3.688903175480692, 1.516076585892645),
            rot=(0.7071063043492178, 0.7071072580235509, 5.7367473579563867e-08, 5.736739887730709e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/eckdny/usd/eckdny.usd"),
            visual_material_path="materials",
            scale=(0.9998284889443365, 1.000009651822534, 0.9999726700718992),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairAxcwcm0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairAxcwcm0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.8405380249023438, -2.9386708736419678, 0.4607158601284027),
            rot=(-0.7071064710617065, 2.3954547941684723e-05, -7.268437184393406e-05, 0.7071071863174438),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/axcwcm/usd/axcwcm.usd"),
            visual_material_path="materials",
            scale=(0.9999965805762687, 0.9999985532777947, 0.9999690360546069),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bedKlcjcy0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bedKlcjcy0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.158380031585693, 3.2053945064544678, 0.28779760003089905),
            rot=(0.7071083784103394, 0.707105278968811, -0.00017264019697904587, -0.00017292212578468025),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/klcjcy/usd/klcjcy.usd"),
            visual_material_path="materials",
            scale=(1.0000181692100205, 1.000015677996259, 1.0000228165013025),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bedSiuxgz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bedSiuxgz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.444109916687012, 3.039479970932007, 0.22737279534339905),
            rot=(-0.5001658797264099, -0.49997544288635254, 0.5000233054161072, 0.4998356103897095),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/siuxgz/usd/siuxgz.usd"),
            visual_material_path="materials",
            scale=(0.999981087481783, 0.9999628036387286, 0.9999961347646038),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bedTjfzsb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bedTjfzsb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.067856311798096, -1.424709677696228, 0.26378899812698364),
            rot=(0.5000914931297302, 0.49990859627723694, -0.5002939701080322, -0.49970611929893494),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bed/tjfzsb/usd/tjfzsb.usd"),
            visual_material_path="materials",
            scale=(1.0000120872924623, 0.999949400636937, 1.0000029589547506),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetAkdubn0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetAkdubn0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.02313494682312, 2.024624824523926, 0.486118882894516),
            rot=(0.7071071863174438, -5.093170329928398e-11, 2.8801044882342808e-11, -0.7071064710617065),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/akdubn/usd/akdubn.usd"),
            visual_material_path="materials",
            scale=(1.0000000444509234, 0.9999908200663318, 1.0000065984520974),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bottomCabinetQwskbo0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bottomCabinetQwskbo0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.529965400695801, -4.505964279174805, 0.3621748387813568),
            rot=(0.7071065902709961, -0.7071066498756409, 0.0005350566934794188, -0.0005355000030249357),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bottom_cabinet/qwskbo/usd/qwskbo.usd"),
            visual_material_path="materials",
            scale=(0.9999940358651054, 1.0000624015944528, 0.9999344080454694),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coffeeTableOsroux0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coffeeTableOsroux0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.076787948608398, -2.7326455116271973, 0.3334447741508484),
            rot=(-0.4999988377094269, -0.5000011324882507, 0.4999989867210388, 0.5000011920928955),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/osroux/usd/osroux.usd"),
            visual_material_path="materials",
            scale=(0.9999997615814777, 1.0000087033590224, 1.0000071869235048),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskAduafr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskAduafr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.140471935272217, -0.0028147906996309757, 0.4222690165042877),
            rot=(-0.2141880989074707, -0.22046062350273132, 0.6718595623970032, 0.6738883852958679),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/aduafr/usd/aduafr.usd"),
            visual_material_path="materials",
            scale=(0.9999877903494708, 0.9999872630407661, 1.0000212059615183),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskIotfzl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskIotfzl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.3021730184555054, -2.949985980987549, 0.6280746459960938),
            rot=(0.707074761390686, -7.712733349762857e-06, -0.7071388363838196, 7.5107673183083534e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/iotfzl/usd/iotfzl.usd"),
            visual_material_path="materials",
            scale=(1.0000572212306753, 1.0000188836129633, 1.000085082015752),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    deskUqcmzf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/deskUqcmzf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.9025728702545166, -3.9041545391082764, 0.5970970392227173),
            rot=(-0.7072010040283203, -0.00749841146171093, 0.008205728605389595, 0.7069252729415894),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/desk/uqcmzf/usd/uqcmzf.usd"),
            visual_material_path="materials",
            scale=(0.9999882878244784, 0.9999412645737312, 0.9999312532233969),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    floorLampDrpann0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/floorLampDrpann0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.1697611808776855, -2.952709197998047, 0.9896970391273499),
            rot=(1.0000001192092896, 2.5807501515373588e-05, 1.9115395843982697e-06, 2.5722083591972478e-05),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/drpann/usd/drpann.usd"),
            visual_material_path="materials",
            scale=(0.9999608077140459, 0.9999681222010178, 0.9999668463785943),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    floorLampMqfdjk0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/floorLampMqfdjk0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.8312346935272217, 1.8540140390396118, 0.45173612236976624),
            rot=(-0.0018119961023330688, 0.999998152256012, -0.0007377099245786667, 9.299046359956264e-05),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/mqfdjk/usd/mqfdjk.usd"),
            visual_material_path="materials",
            scale=(1.0000792446525344, 1.000029024016156, 1.000067312810348),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    floorLampOgolip0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/floorLampOgolip0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.653611183166504, 1.379639744758606, 1.0129410028457642),
            rot=(0.9926284551620483, 0.0007969639264047146, -0.00010987532732542604, -0.12119459360837936),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/floor_lamp/ogolip/usd/ogolip.usd"),
            visual_material_path="materials",
            scale=(0.9999704760726608, 0.9998933310755388, 1.0000156099269881),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    nightstandAykehx0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/nightstandAykehx0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.925800323486328, 2.111380100250244, 0.21042633056640625),
            rot=(0.9999990463256836, 0.0006742107798345387, -0.0012811613269150257, -8.528187026968226e-05),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/nightstand/aykehx/usd/aykehx.usd"),
            visual_material_path="materials",
            scale=(0.9999997615814777, 0.9999998478019995, 0.9999997714334805),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    nightstandRoxnbe0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/nightstandRoxnbe0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.924409866333008, 3.7766873836517334, 0.41135385632514954),
            rot=(0.7071070671081543, -3.895576810464263e-05, 2.509264595573768e-05, -0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/nightstand/roxnbe/usd/roxnbe.usd"),
            visual_material_path="materials",
            scale=(0.9999983245561287, 0.9999708477198774, 0.9999985694905716),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    nightstandRoxnbe1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/nightstandRoxnbe1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.9673967361450195, 3.776684045791626, 0.4113522469997406),
            rot=(0.7071070671081543, -3.558053867891431e-05, 2.7893262085854076e-05, -0.7071066498756409),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/nightstand/roxnbe/usd/roxnbe.usd"),
            visual_material_path="materials",
            scale=(0.9999983245561287, 0.9999708477198774, 0.9999985694905716),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    nightstandUzxrlg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/nightstandUzxrlg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.7879605293273926, -0.851341962814331, 0.16684168577194214),
            rot=(0.7071694731712341, 0.7070440649986267, -0.00015519712178502232, 0.00012577914458233863),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/nightstand/uzxrlg/usd/uzxrlg.usd"),
            visual_material_path="materials",
            scale=(0.999999723126888, 0.9999999917549771, 1.0000000039986343),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ottomanHlnste0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ottomanHlnste0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.6055846214294434, 3.5302703380584717, 0.2484850287437439),
            rot=(0.9247379302978516, 0.0013660835102200508, 2.7192756533622742e-05, -0.38060227036476135),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/ottoman/hlnste/usd/hlnste.usd"),
            visual_material_path="materials",
            scale=(0.9999613780976201, 0.9999497347058997, 0.9999669604100281),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ottomanQsnawv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ottomanQsnawv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.585765838623047, 1.4363558292388916, 0.24635687470436096),
            rot=(0.7345550656318665, -0.027117442339658737, -0.019306611269712448, -0.6777321696281433),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/ottoman/qsnawv/usd/qsnawv.usd"),
            visual_material_path="materials",
            scale=(1.000073196066596, 1.0000185985740015, 1.000011499348454),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ottomanYpwkkn0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ottomanYpwkkn0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.7473227977752686, 2.675696611404419, 0.22659768164157867),
            rot=(-0.6564698219299316, 0.0068879942409694195, 0.0032433990854769945, 0.7543139457702637),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/ottoman/ypwkkn/usd/ypwkkn.usd"),
            visual_material_path="materials",
            scale=(1.0000118236238136, 1.0000543191430467, 0.9999963155014605),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfKdnyfh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfKdnyfh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.844667434692383, 3.342198371887207, 0.3236910402774811),
            rot=(1.0000001192092896, -1.5643759070371743e-06, 8.127317414619029e-07, 1.0008079698309302e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/kdnyfh/usd/kdnyfh.usd"),
            visual_material_path="materials",
            scale=(1.0000849040904676, 1.000024046366481, 0.9999461023800241),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfKmuacd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfKmuacd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.2467780113220215, -0.13761994242668152, 0.6230291128158569),
            rot=(0.00012282084207981825, 3.8743019104003906e-07, -0.0013665994629263878, 0.9999991059303284),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/kmuacd/usd/kmuacd.usd"),
            visual_material_path="materials",
            scale=(0.9999724807361839, 1.0000849040904676, 0.9999675332918491),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfOpryhp0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfOpryhp0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.305893421173096, -4.56041955947876, 0.361173152923584),
            rot=(0.7075334787368774, -0.7066798210144043, 0.0004138017538934946, -0.00041394055006094277),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/opryhp/usd/opryhp.usd"),
            visual_material_path="materials",
            scale=(1.0000382775296943, 1.0000654064130847, 0.9998958274702006),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfOpryhp1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfOpryhp1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.0781354904174805, -4.564090728759766, 0.36229029297828674),
            rot=(0.7107097506523132, -0.7034854292869568, 0.00023317220620810986, -0.00023499579401686788),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/opryhp/usd/opryhp.usd"),
            visual_material_path="materials",
            scale=(1.0000382775296943, 1.0000654064130847, 0.9998958274702006),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfOtwukr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfOtwukr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.575839519500732, -0.6310573220252991, 0.5226165056228638),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/otwukr/usd/otwukr.usd"),
            visual_material_path="materials",
            scale=(1.0000000125483464, 0.9999999602635717, 1.0000000454130649),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfOtwukr1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfOtwukr1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.0533223152160645, -0.6310573220252991, 0.5226165056228638),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/otwukr/usd/otwukr.usd"),
            visual_material_path="materials",
            scale=(1.0000000125483464, 0.9999999602635717, 1.0000000454130649),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfOtwukr2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfOtwukr2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.291658401489258, -0.6310573220252991, 0.5226165056228638),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/otwukr/usd/otwukr.usd"),
            visual_material_path="materials",
            scale=(1.0000000125483464, 0.9999999602635717, 1.0000000454130649),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfOtwukr3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfOtwukr3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.814175605773926, -0.6310573220252991, 0.5226165056228638),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/otwukr/usd/otwukr.usd"),
            visual_material_path="materials",
            scale=(1.0000000125483464, 0.9999999602635717, 1.0000000454130649),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaUkfaaz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaUkfaaz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.008310317993164, -3.7901737689971924, 0.2669062614440918),
            rot=(0.9999951720237732, 0.0025986304972320795, 0.00015266379341483116, 0.0017339653568342328),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/ukfaaz/usd/ukfaaz.usd"),
            visual_material_path="materials",
            scale=(0.999988507203482, 1.0000010549369815, 0.9999796822133421),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    taboretCgwxtq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/taboretCgwxtq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.227475643157959, 0.3015724718570709, 0.33433154225349426),
            rot=(-8.046627044677734e-07, 5.552079528570175e-06, -1.4258548617362976e-06, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/taboret/cgwxtq/usd/cgwxtq.usd"),
            visual_material_path="materials",
            scale=(0.999899535847252, 0.999934954863748, 1.0000373367135407),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    swivelChairIiihwn0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/swivelChairIiihwn0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.506620168685913, -3.5552985668182373, 0.47643208503723145),
            rot=(0.8433913588523865, -2.2748252376914024e-05, -0.00010396307334303856, -0.5372998714447021),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/swivel_chair/iiihwn/usd/iiihwn.usd"),
            visual_material_path="materials",
            scale=(1.0000235671646207, 0.999993046635411, 0.9999864363268728),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampErfbgw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampErfbgw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.8057637214660645, 3.791724681854248, 1.0135643482208252),
            rot=(0.7067894339561462, 0.7074235081672668, 0.0005605884362012148, -0.0005691059050150216),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/erfbgw/usd/erfbgw.usd"),
            visual_material_path="materials",
            scale=(0.9999628618247469, 1.000101955680945, 0.9999637883738782),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampHtmtsr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampHtmtsr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.73391056060791, -0.0018362952396273613, 1.1706981658935547),
            rot=(-0.21835896372795105, -0.21241526305675507, 0.6769976019859314, 0.6699801683425903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/htmtsr/usd/htmtsr.usd"),
            visual_material_path="materials",
            scale=(1.0000460974106125, 0.9999646697045756, 1.0001732898846192),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampLshxmu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampLshxmu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.2298682928085327, -2.567225694656372, 1.0066254138946533),
            rot=(-0.7071098685264587, -0.00044318288564682007, -0.0013347857166081667, 0.7071024775505066),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/lshxmu/usd/lshxmu.usd"),
            visual_material_path="materials",
            scale=(1.0000919055395232, 0.9996259589487904, 1.00005878734355),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampVbjpad0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampVbjpad0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.925945281982422, 2.006399154663086, 0.6277440786361694),
            rot=(0.4999997615814209, 0.4999999701976776, 0.5000002980232239, 0.5000000596046448),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/vbjpad/usd/vbjpad.usd"),
            visual_material_path="materials",
            scale=(0.9999633250990979, 1.0001018922183138, 0.9999628618247469),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    tableLampWbcgev0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/tableLampWbcgev0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.664452314376831, -0.9059333205223083, 0.6534416079521179),
            rot=(0.9999999403953552, 0.0004675091477110982, -0.00031845836201682687, -5.4065167205408216e-06),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/table_lamp/wbcgev/usd/wbcgev.usd"),
            visual_material_path="materials",
            scale=(0.9998542081709924, 0.9999492896400076, 1.0000843935066144),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    bathtubRufepf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/bathtubRufepf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.2975157588140522, 3.488691945508239, 0.29530364876784954),
            rot=(0.9999999999928024, 3.788088279862108e-06, 2.1339850329527557e-07, -8.083764349775049e-13),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bathtub/rufepf/usd/rufepf.usd"),
            visual_material_path="materials",
            scale=(1.0000211726376194, 0.9999748356990201, 0.9999594486438418),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    chandelierFveyao0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/chandelierFveyao0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.412639328977594, 1.6917735788182704, 2.0091629627583276),
            rot=(0.9999999992183348, 3.9533772304859275e-05, 6.397595808601739e-07, 4.368609484875987e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/chandelier/fveyao/usd/fveyao.usd"),
            visual_material_path="materials",
            scale=(0.9999768268221825, 0.9999265392490627, 1.0000466921086388),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    curtainDidlbp0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/curtainDidlbp0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.415046920652207, 0.5435205559109483, 1.291085021425676),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/curtain/didlbp/usd/didlbp.usd"),
            visual_material_path="materials",
            scale=(0.999778854083245, 0.9999882137818166, 0.9999897814802154),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    curtainZmodhv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/curtainZmodhv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.415188724592329, -1.2499953148961067, 1.2926491434526337),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/curtain/zmodhv/usd/zmodhv.usd"),
            visual_material_path="materials",
            scale=(0.9998509163499802, 1.0000345162572282, 1.0000121661402281),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    folderalYdrlth0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/folderalYdrlth0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.33100303085386, -0.28473714897386143, 1.1173892605655633),
            rot=(4.853386684268557e-07, -3.7856759796057755e-07, 0.7071074964418015, 0.7071060659303022),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/folderal/ydrlth/usd/ydrlth.usd"),
            visual_material_path="materials",
            scale=(1.0001829290481263, 0.9998600042789197, 1.0007089315139595),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorPxhbim0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorPxhbim0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.20764629542827606, 1.2350890636444092, 1.1892262697219849),
            rot=(7.589551387354732e-07, 0.0, 2.6147972675971687e-12, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/pxhbim/usd/pxhbim.usd"),
            visual_material_path="materials",
            scale=(1.000030611247557, 0.9997081869042377, 0.9999773953994178),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorPxhbim1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorPxhbim1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.3248894214630127, -2.386824607849121, 1.18923020362854),
            rot=(0.7071071863174438, -2.3283064365386963e-10, -3.6266101233195513e-11, 0.7071064710617065),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/pxhbim/usd/pxhbim.usd"),
            visual_material_path="materials",
            scale=(1.000030611247557, 0.9997081869042377, 0.9999773953994178),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorPxhbim2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorPxhbim2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.5292656421661377, 0.6931416988372803, 1.1892262697219849),
            rot=(-0.7071067690849304, -2.3283064365386963e-10, 1.5705836631241255e-10, 0.70710688829422),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/pxhbim/usd/pxhbim.usd"),
            visual_material_path="materials",
            scale=(1.000030611247557, 0.9997081869042377, 0.9999773953994178),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    doorPxhbim3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorPxhbim3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.315657138824463, 0.6993938088417053, 1.1892262697219849),
            rot=(0.7071071863174438, -2.3283064365386963e-10, -3.6266101233195513e-11, 0.7071064710617065),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/pxhbim/usd/pxhbim.usd"),
            visual_material_path="materials",
            scale=(1.000030611247557, 0.9997081869042377, 0.9999773953994178),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightOxglnt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightOxglnt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.869467016921837, -2.4360839186526104, 2.4455537409354124),
            rot=(0.7071067811865477, 0.0, 0.0, 0.7071067811865474),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/oxglnt/usd/oxglnt.usd"),
            visual_material_path="materials",
            scale=(0.99997183825497, 0.999880368708384, 0.9995734723515174),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightOxglnt1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightOxglnt1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.351259985671837, -2.436083918652611, 2.4455537409354124),
            rot=(0.7071067811865477, 0.0, 0.0, 0.7071067811865474),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/oxglnt/usd/oxglnt.usd"),
            visual_material_path="materials",
            scale=(0.99997183825497, 0.999880368708384, 0.9995734723515174),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightOxglnt2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightOxglnt2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.09024697233316296, -2.436083918652611, 2.4455537409354124),
            rot=(0.7071067811865477, 0.0, 0.0, 0.7071067811865474),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/oxglnt/usd/oxglnt.usd"),
            visual_material_path="materials",
            scale=(0.99997183825497, 0.999880368708384, 0.9995734723515174),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightOxglnt3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightOxglnt3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.09024697233316296, -0.5440939589326107, 2.4455537409354124),
            rot=(0.7071067811865477, 0.0, 0.0, 0.7071067811865474),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/oxglnt/usd/oxglnt.usd"),
            visual_material_path="materials",
            scale=(0.99997183825497, 0.999880368708384, 0.9995734723515174),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightVlplia0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightVlplia0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.7261422468685979, 1.7027362428587063, 2.2036402055337714),
            rot=(0.9914118306157947, 0.008096682560266105, 0.0010659474279587386, 0.13052160588438158),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/vlplia/usd/vlplia.usd"),
            visual_material_path="materials",
            scale=(1.0002220624358542, 1.0000911262435974, 1.0001221647077525),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightVlplia1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightVlplia1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.1158922468698487, 1.7027342897340398, 2.2036362992838505),
            rot=(0.9914118306157947, 0.008096682560266105, 0.0010659474279587386, 0.13052160588438158),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/vlplia/usd/vlplia.usd"),
            visual_material_path="materials",
            scale=(1.0002220624358542, 1.0000911262435974, 1.0001221647077525),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightVlplia2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightVlplia2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.5056441963361038, 1.7027343010179445, 2.2036362993483483),
            rot=(0.9914118306157947, 0.008096682560266105, 0.0010659474279587386, 0.13052160588438158),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/vlplia/usd/vlplia.usd"),
            visual_material_path="materials",
            scale=(1.0002220624358542, 1.0000911262435974, 1.0001221647077525),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightVlplia3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightVlplia3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.10460287948007052, 1.7027323423324463, 2.203636299283793),
            rot=(0.9914118306157947, 0.008096682560266105, 0.0010659474279587386, 0.13052160588438158),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/vlplia/usd/vlplia.usd"),
            visual_material_path="materials",
            scale=(1.0002220624358542, 1.0000911262435974, 1.0001221647077525),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightVlplia4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightVlplia4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.9353470109414022, 1.702736242858707, 2.2036362992837715),
            rot=(0.9914118306157947, 0.008096682560266105, 0.0010659474279587386, 0.13052160588438158),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/vlplia/usd/vlplia.usd"),
            visual_material_path="materials",
            scale=(1.0002220624358542, 1.0000911262435974, 1.0001221647077525),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightVlplia5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightVlplia5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.3251028703154866, 1.7027303834852898, 2.2036402055338504),
            rot=(0.9914118306157947, 0.008096682560266105, 0.0010659474279587386, 0.13052160588438158),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/vlplia/usd/vlplia.usd"),
            visual_material_path="materials",
            scale=(1.0002220624358542, 1.0000911262435974, 1.0001221647077525),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    downlightVlplia6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/downlightVlplia6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.7148567786108471, 1.7027323442386937, 2.2036402055337714),
            rot=(0.9914118306157947, 0.008096682560266105, 0.0010659474279587386, 0.13052160588438158),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/downlight/vlplia/usd/vlplia.usd"),
            visual_material_path="materials",
            scale=(1.0002220624358542, 1.0000911262435974, 1.0001221647077525),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    mirrorOvdinr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/mirrorOvdinr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.3946311943808825, 2.223405481983632, 1.4635722670545),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/mirror/ovdinr/usd/ovdinr.usd"),
            visual_material_path="materials",
            scale=(1.0000140051796582, 0.9987480676065599, 1.0000138548417017),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    paintingEexydp0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/paintingEexydp0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.06760861577881, -0.4927383439264607, 1.6653991041445906),
            rot=(0.9990800316524364, 0.04288461674501297, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/painting/eexydp/usd/eexydp.usd"),
            visual_material_path="materials",
            scale=(1.0000278482153273, 1.0001733768174885, 0.9999808284607189),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    paintingJfkvxh0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/paintingJfkvxh0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.206398281088225, -0.49505812245251, 1.5869211413423059),
            rot=(0.9947919965064037, 0.10192587349050912, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/painting/jfkvxh/usd/jfkvxh.usd"),
            visual_material_path="materials",
            scale=(1.0000509186639341, 0.9999696920346808, 1.0000356633935774),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    paintingLjabhq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/paintingLjabhq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.210649987581763, -0.28816022028048277, 1.6509161679357176),
            rot=(8.748346274679049e-07, 7.65381526566016e-08, 0.08715578464015523, 0.9961946944262391),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/painting/ljabhq/usd/ljabhq.usd"),
            visual_material_path="materials",
            scale=(1.0000307112073894, 0.9998818548176587, 0.9999197920294192),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureAbtgvz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureAbtgvz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.1127578125, -0.28365899658000004, 1.20252441406),
            rot=(4.853386684268557e-07, -3.7856759796057745e-07, 0.7071074964418014, 0.7071060659303023),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/abtgvz/usd/abtgvz.usd"),
            visual_material_path="materials",
            scale=(1.0001844586290876, 1.000455403969754, 1.0),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureAicjaq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureAicjaq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.7778368171095242, 1.135720365766082, 1.4332450999141195),
            rot=(0.7074147807000508, 0.7067986474570331, -6.179029851996728e-08, -6.1844157727904e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/aicjaq/usd/aicjaq.usd"),
            visual_material_path="materials",
            scale=(1.0000498835068492, 0.9999761386945459, 1.0017814379467018),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureAqahkx0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureAqahkx0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.463949496789548, 2.981229213743897, 1.1987812146306631),
            rot=(0.7071067215754291, 2.573001937288052e-06, 3.417499842113675e-06, 0.7071068407847211),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/aqahkx/usd/aqahkx.usd"),
            visual_material_path="materials",
            scale=(0.999947778208581, 0.9999927580881055, 1.0000432683283098),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureBzmdxc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureBzmdxc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.122527352396595, -0.2847371317550173, 1.1182666320774957),
            rot=(4.853386684268557e-07, -3.785675979605773e-07, 0.7071074964418014, 0.7071060659303023),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/bzmdxc/usd/bzmdxc.usd"),
            visual_material_path="materials",
            scale=(0.9997720244819923, 0.9997694386609427, 1.0),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureFdtxut0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureFdtxut0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.354017578125001, -0.28473712158000003, 1.18989160156),
            rot=(4.853386684268557e-07, -3.785675979605774e-07, 0.7071074964418014, 0.7071060659303023),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/fdtxut/usd/fdtxut.usd"),
            visual_material_path="materials",
            scale=(0.9997667359301079, 0.9999116695673325, 1.0),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureHsbtqi0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureHsbtqi0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.196123035391208, -0.28473711649835504, 1.1182665710380983),
            rot=(4.853386113613922e-07, -3.785675696204661e-07, 0.7071074964418014, 0.7071060659303023),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/hsbtqi/usd/hsbtqi.usd"),
            visual_material_path="materials",
            scale=(0.9998931818525443, 0.9997694386609427, 1.0),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureHyjqxp0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureHyjqxp0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.4661482201985265, 2.234197244254003, 1.704531009024547),
            rot=(0.7071067215754292, 2.5730019372880496e-06, 3.4174998421136764e-06, 0.707106840784721),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/hyjqxp/usd/hyjqxp.usd"),
            visual_material_path="materials",
            scale=(1.0001199706835706, 0.9999922924337795, 0.9998787950771428),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureJovfqj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureJovfqj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.4015707471900387, -0.1708081847804868, 1.5163605553061517),
            rot=(0.5002177926199941, 0.4997821124714054, 0.4997821124714055, 0.5002177926199941),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/jovfqj/usd/jovfqj.usd"),
            visual_material_path="materials",
            scale=(1.0000487035956838, 0.9999559354489547, 1.0017635478326785),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureNxjgqw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureNxjgqw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.1869429600348276, 1.1357177213362544, 1.4332471670783813),
            rot=(0.7074147211213802, 0.7067987070876349, -6.179030565407825e-08, -6.184416480921135e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/nxjgqw/usd/nxjgqw.usd"),
            visual_material_path="materials",
            scale=(1.0000500044944658, 0.9999761386945459, 1.0017814379467018),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureNxqoed0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureNxqoed0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.220983318341858, -1.2066001679970515, 1.532578998271179),
            rot=(-0.5002176213215641, -0.4997822093873337, 0.49978229879430164, 0.5002176809262098),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/nxqoed/usd/nxqoed.usd"),
            visual_material_path="materials",
            scale=(1.0000493390629366, 0.9999761386945459, 1.001775043056829),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureNzctlq0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureNzctlq0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.466136344713994, 3.029840636615662, 1.652089611783528),
            rot=(0.7071067215754291, 2.5730019372880504e-06, 3.417499842113674e-06, 0.7071068407847211),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/nzctlq/usd/nzctlq.usd"),
            visual_material_path="materials",
            scale=(0.9999559905592375, 0.9999855870595711, 0.9998576711581312),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureRypaxo0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureRypaxo0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.4661913420842385, 1.8792226978871425, 1.6780148017378789),
            rot=(0.7071067215754294, 2.5730019372880483e-06, 3.417499842113676e-06, 0.7071068407847207),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/rypaxo/usd/rypaxo.usd"),
            visual_material_path="materials",
            scale=(1.0001704557659155, 0.9999843763765897, 1.0001413757107203),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureSvpzro0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureSvpzro0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.126955085781034, -0.2847351684550107, 1.027887710569991),
            rot=(4.853386684268557e-07, -3.7856759796057745e-07, 0.7071074964418014, 0.7071060659303023),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/svpzro/usd/svpzro.usd"),
            visual_material_path="materials",
            scale=(1.0002256790966153, 0.9995407820714132, 1.0),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureTrqgni0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureTrqgni0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.220983318341858, -0.5377368182422851, 1.532578997499926),
            rot=(-0.5002176213215641, -0.4997822093873337, 0.49978229879430164, 0.5002176809262098),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/trqgni/usd/trqgni.usd"),
            visual_material_path="materials",
            scale=(1.0000494600504215, 0.9999761386945459, 1.001775043056829),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureTtwhjj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureTtwhjj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.464763388616674, 2.597031095542132, 1.1559843478626788),
            rot=(0.7071067215754288, 2.5730019372880525e-06, 3.4174998421136756e-06, 0.7071068407847214),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/ttwhjj/usd/ttwhjj.usd"),
            visual_material_path="materials",
            scale=(0.9998861159884277, 1.0023551551548662, 1.000029149089483),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureVchhhl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureVchhhl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.1910644531250005, -0.28473712158333336, 1.2494736328100002),
            rot=(4.853386684268557e-07, -3.785675979605774e-07, 0.7071074964418014, 0.7071060659303023),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/vchhhl/usd/vchhhl.usd"),
            visual_material_path="materials",
            scale=(0.9996225973241264, 0.9997766780352748, 1.0),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureVezfau0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureVezfau0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.4647710393163544, 2.1820565992751746, 1.2114173261240542),
            rot=(0.7071067215754291, 2.573001937288052e-06, 3.417499842113674e-06, 0.7071068407847211),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/vezfau/usd/vezfau.usd"),
            visual_material_path="materials",
            scale=(1.0000632518754209, 1.0023575961553117, 0.9998894064424307),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureXnuynn0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureXnuynn0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.226186504995274, 2.0101629654113453, 1.4701206949097347),
            rot=(-0.5002176213215641, -0.49978220938733364, 0.4997822987943017, 0.5002176809262098),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/xnuynn/usd/xnuynn.usd"),
            visual_material_path="materials",
            scale=(1.0000490970880547, 1.0000397000011343, 0.9984018917721906),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    pictureYrkfct0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/pictureYrkfct0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.466164964261096, 2.664035534628298, 1.7251828128657056),
            rot=(0.7071067215754292, 2.5730019372880496e-06, 3.4174998421136735e-06, 0.707106840784721),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/picture/yrkfct/usd/yrkfct.usd"),
            visual_material_path="materials",
            scale=(0.9999928396154946, 0.9999852145414184, 0.999977675393437),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railingPqzbbb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railingPqzbbb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.666592350900178, -1.3434766776587437, 0.39411897203451224),
            rot=(0.9999999999999887, 0.0, 0.0, -1.5049435106459336e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/railing/pqzbbb/usd/pqzbbb.usd"),
            visual_material_path="materials",
            scale=(0.9999908928314019, 1.0000152940392906, 0.9999874574776103),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railingPqzbbb1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railingPqzbbb1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.475971257150184, -1.3965610160268571, 0.39411897203451224),
            rot=(7.54979013252756e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/railing/pqzbbb/usd/pqzbbb.usd"),
            visual_material_path="materials",
            scale=(0.9999908928314019, 1.0000152940392906, 0.9999874574776103),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railingPqzbbb2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railingPqzbbb2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.666592350900168, 0.5851558907012564, 0.39411897203451224),
            rot=(0.9999999999999887, 0.0, 0.0, -1.5049435106459336e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/railing/pqzbbb/usd/pqzbbb.usd"),
            visual_material_path="materials",
            scale=(0.9999908928314019, 1.0000152940392906, 0.9999874574776103),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railingPqzbbb3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railingPqzbbb3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.475971257150188, 0.73800731932552, 0.3941150657845122),
            rot=(7.54979013252756e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/railing/pqzbbb/usd/pqzbbb.usd"),
            visual_material_path="materials",
            scale=(0.9999908928314019, 1.0000152940392906, 0.9999874574776103),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    railingPqzbbb4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/railingPqzbbb4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.475971257150185, -1.4044731253968574, 0.3941150657845123),
            rot=(7.54979013252756e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/railing/pqzbbb/usd/pqzbbb.usd"),
            visual_material_path="materials",
            scale=(0.9999908928314019, 1.0000152940392906, 0.9999874574776103),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomDividerBydmct0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomDividerBydmct0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.458021007009561, -3.8973334807629487, 0.8730443878367123),
            rot=(-0.7071066023725877, 0.0, 0.0, 0.7071069600004622),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_divider/bydmct/usd/bydmct.usd"),
            visual_material_path="materials",
            scale=(1.0000001341104687, 1.0003511244178473, 1.000074989141063),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfSapyzl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfSapyzl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.5354965923029398, 2.453587837435626, 1.4687581154536289),
            rot=(0.7071067215754292, 2.57300193728805e-06, 3.4174998421136735e-06, 0.707106840784721),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/sapyzl/usd/sapyzl.usd"),
            visual_material_path="materials",
            scale=(0.9999921930921963, 1.000213906607349, 1.0006416183103666),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    shelfSapyzl1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/shelfSapyzl1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.534408701682495, 2.453587837435556, 0.9452612673145202),
            rot=(0.7071067215754292, 2.573001482528597e-06, 3.417499160004735e-06, 0.707106840784721),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shelf/sapyzl/usd/sapyzl.usd"),
            visual_material_path="materials",
            scale=(0.9999921930921963, 1.000213906607349, 1.0006416183103666),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    showerGiialz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/showerGiialz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.7971031239963797, 3.4692895248654567, 0.03084747329210656),
            rot=(-0.707106721580295, -1.9049188366815391e-06, 9.530667901996477e-07, 0.7071068407895869),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/shower/giialz/usd/giialz.usd"),
            visual_material_path="materials",
            scale=(1.0000322153182288, 0.9999756078413394, 1.000690107440948),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    showerheadAfoeoa0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/showerheadAfoeoa0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.201630967779453, 3.4443432764882256, 0.8904176443327287),
            rot=(-0.7071067215768098, -2.8294924079612806e-06, 2.5277002328115105e-06, 0.7071068407861014),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/showerhead/afoeoa/usd/afoeoa.usd"),
            visual_material_path="materials",
            scale=(1.0001590207423419, 0.9995368122813805, 0.9999916162628374),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    showerheadSvuhzb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/showerheadSvuhzb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.12328495507893, 3.2550842655422616, 1.3249112986166742),
            rot=(-0.7071067215768094, -2.8294924079612814e-06, 2.52770023281151e-06, 0.7071068407861016),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/showerhead/svuhzb/usd/svuhzb.usd"),
            visual_material_path="materials",
            scale=(1.0001643644997291, 0.9999036063889518, 1.0000363863994),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sinkOjjqku0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sinkOjjqku0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.1639554540788435, 2.223419370800977, 0.6277831198579753),
            rot=(0.7071067215818995, 0.0, 0.0, 0.7071068407911907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sink/ojjqku/usd/ojjqku.usd"),
            visual_material_path="materials",
            scale=(1.0000002582868608, 0.9999998914133322, 0.9999822562657863),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    spotlightJxermw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/spotlightJxermw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.08866348556365808, 2.4863905300509104, 2.2509022300554586),
            rot=(-0.13052600623861502, -2.363789804347731e-07, -3.1119835603308554e-08, 0.9914448858586846),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/spotlight/jxermw/usd/jxermw.usd"),
            visual_material_path="materials",
            scale=(0.9996739106353868, 1.0002568640321357, 1.0001883198507033),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    spotlightJxermw1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/spotlightJxermw1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.923718133643362, 2.4859413147092986, 2.250906014235477),
            rot=(-0.13052600623861502, -2.3637900882572893e-07, -3.111982494111872e-08, 0.9914448858586846),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/spotlight/jxermw/usd/jxermw.usd"),
            visual_material_path="materials",
            scale=(0.9996739106353868, 1.0002568640321357, 1.0001883198507033),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    spotlightJxermw2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/spotlightJxermw2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.3127786805146118, 2.486388580333964, 2.2509060142354773),
            rot=(-0.13052600623861502, -2.3637900882572893e-07, -3.111982494111872e-08, 0.9914448858586846),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/spotlight/jxermw/usd/jxermw.usd"),
            visual_material_path="materials",
            scale=(0.9996739106353868, 1.0002568640321357, 1.0001883198507033),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    spotlightJxermw3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/spotlightJxermw3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.6981575888090585, 2.491251869213954, 2.250906014235477),
            rot=(-0.13052600623861502, -2.3637900882572893e-07, -3.111982494111872e-08, 0.9914448858586846),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/spotlight/jxermw/usd/jxermw.usd"),
            visual_material_path="materials",
            scale=(0.9996739106353868, 1.0002568640321357, 1.0001883198507033),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    spotlightJxermw4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/spotlightJxermw4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.5126393284249154, 2.4954556515197974, 2.2509060049629355),
            rot=(0.9914448858587109, 4.9042906621824384e-08, -3.7631959705790236e-08, 0.13052600623861832),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/spotlight/jxermw/usd/jxermw.usd"),
            visual_material_path="materials",
            scale=(0.9996739106353868, 1.0002568640321357, 1.0001883198507033),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    spotlightJxermw5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/spotlightJxermw5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.122682314376383, 2.4954595664678085, 2.250906004962939),
            rot=(0.9914448858587109, 4.9042906621824384e-08, -3.7631959705790236e-08, 0.13052600623861832),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/spotlight/jxermw/usd/jxermw.usd"),
            visual_material_path="materials",
            scale=(0.9996739106353868, 1.0002568640321357, 1.0001883198507033),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    spotlightJxermw6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/spotlightJxermw6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.7330553612513828, 2.4954556602178086, 2.250906004962939),
            rot=(0.9914448858587109, 4.9042906621824384e-08, -3.7631959705790236e-08, 0.13052600623861832),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/spotlight/jxermw/usd/jxermw.usd"),
            visual_material_path="materials",
            scale=(0.9996739106353868, 1.0002568640321357, 1.0001883198507033),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    toiletUdiezm0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/toiletUdiezm0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.8019963502883911, 3.8419888019561768, 0.33442676067352295),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/toilet/udiezm/usd/udiezm.usd"),
            visual_material_path="materials",
            scale=(1.000035867868454, 1.0000370489706725, 1.0001188158551786),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    towelRackQedffr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/towelRackQedffr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.7141887314420253, 1.4411866834981346, 1.313070210029628),
            rot=(-0.4999999403953534, -0.4999999999999983, 0.500000059604643, 0.4999999999999983),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/towel_rack/qedffr/usd/qedffr.usd"),
            visual_material_path="materials",
            scale=(1.0001535012618432, 1.0000251590723575, 1.0000013113039046),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedLightEtqbld0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedLightEtqbld0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.327539539692286, 2.9187644652005496, 1.5099123139132498),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_light/etqbld/usd/etqbld.usd"),
            visual_material_path="materials",
            scale=(0.9998317344017316, 1.0001854984051857, 1.0000163642708102),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedLightEtqbld1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedLightEtqbld1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.327539539692286, 1.5165278929355495, 1.5099123139132495),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_light/etqbld/usd/etqbld.usd"),
            visual_material_path="materials",
            scale=(0.9998317344017316, 1.0001854984051857, 1.0000163642708102),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedTvSodbbr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedTvSodbbr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.672131105353413, 2.7361305632111033, 1.3592270562656585),
            rot=(-0.7071067215818997, 0.0, 0.0, 0.7071068407911903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_tv/sodbbr/usd/sodbbr.usd"),
            visual_material_path="materials",
            scale=(1.0000014195547584, 1.0008065659114556, 0.9999944860890104),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallSocketPlssag0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallSocketPlssag0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.6365433027850385, 1.343352637921352, 0.16072996671171488),
            rot=(0.9999999999999887, 0.0, 0.0, -1.5049435106459336e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_socket/plssag/usd/plssag.usd"),
            visual_material_path="materials",
            scale=(0.996921970774958, 1.0000925922874855, 1.0000929380862313),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallSocketZyzufw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallSocketZyzufw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(6.4687441117870685, -2.451951912140004, 0.18528945259871027),
            rot=(0.9999999999999887, 0.0, 0.0, -1.5049435106459336e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_socket/zyzufw/usd/zyzufw.usd"),
            visual_material_path="materials",
            scale=(1.0025856008366225, 1.0000940619338063, 1.0000929380862313),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowEtjpqr0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowEtjpqr0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.425383987044591, 3.3834941269358327, 2.096337977293591),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/etjpqr/usd/etjpqr.usd"),
            visual_material_path="materials",
            scale=(1.000023436627975, 1.0000270486118108, 1.0000121304080707),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowEtjpqr1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowEtjpqr1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.757961258094551, -4.074851606823772, 2.096339930413591),
            rot=(7.54979013252756e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/etjpqr/usd/etjpqr.usd"),
            visual_material_path="materials",
            scale=(1.000023436627975, 1.0000270486118108, 1.0000121304080707),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowEtjpqr2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowEtjpqr2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.5010322111454495, -4.074851606823781, 2.096339930413591),
            rot=(7.54979013252756e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/etjpqr/usd/etjpqr.usd"),
            visual_material_path="materials",
            scale=(1.000023436627975, 1.0000270486118108, 1.0000121304080707),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowEtjpqr3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowEtjpqr3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.422145126394852, -4.074851606823744, 2.096339930413591),
            rot=(7.54979013252756e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/etjpqr/usd/etjpqr.usd"),
            visual_material_path="materials",
            scale=(1.000023436627975, 1.0000270486118108, 1.0000121304080707),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowEtjpqr4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowEtjpqr4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.7266792758904094, 3.383314439435833, 2.096484461663591),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/etjpqr/usd/etjpqr.usd"),
            visual_material_path="materials",
            scale=(1.000023436627975, 1.0000270486118108, 1.0000121304080707),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowEtjpqr5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowEtjpqr5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.9782085422504092, 3.3833144394358325, 2.096484461663591),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/etjpqr/usd/etjpqr.usd"),
            visual_material_path="materials",
            scale=(1.000023436627975, 1.0000270486118108, 1.0000121304080707),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
