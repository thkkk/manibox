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
class restaurantBrunchquickSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/restaurant_brunch/usd/restaurant_brunch_quick.usd"),
        )
    )
@configclass
class restaurantBrunchfullSceneCfg(InteractiveSceneCfg):
    robot: ArticulationCfg = MISSING
    ee_frame: FrameTransformerCfg = MISSING
    object: RigidObjectCfg = MISSING
    
    wall_ceiling_floor = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wall_ceiling_floor",
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_scenes/restaurant_brunch/usd/restaurant_brunch_quick.usd"),
        )
    )
    doorKtydvs0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/doorKtydvs0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.15706168115139008, 8.090047836303711, 1.0986685752868652),
            rot=(-0.49999988079071045, -0.5000001192092896, 0.5000000596046448, 0.5000000596046448),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/door/ktydvs/usd/ktydvs.usd"),
            visual_material_path="materials",
            scale=(0.7981907927092168, 78.1503162903386, 3.650054054147422),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    benchKpeeai0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/benchKpeeai0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.604038373945894, 3.3837999312379567, 0.24092967407843457),
            rot=(0.7071067215818995, 0.7071068407911907, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bench/kpeeai/usd/kpeeai.usd"),
            visual_material_path="materials",
            scale=(0.9999901633148756, 0.9999997615814777, 0.9999949907817287),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    benchYbkjzd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/benchYbkjzd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.155945872785535, -3.11282896287213, 0.4569566798803066),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bench/ybkjzd/usd/ybkjzd.usd"),
            visual_material_path="materials",
            scale=(1.0000066863794, 0.9999997597448643, 1.000000052361959),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantBedomm0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantBedomm0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.4423244883962427, -1.468380631203471, 1.3867863012866337),
            rot=(-0.13052628453710474, 3.763194414914132e-08, 4.904291547350236e-08, 0.9914448492200336),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/bedomm/usd/bedomm.usd"),
            visual_material_path="materials",
            scale=(0.9999471335528047, 1.000013133252095, 1.0000421140752795),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantBedomm1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantBedomm1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.2646894455699695, -2.110394055508496, 2.733017716086629),
            rot=(0.9999999999999971, 4.386783077268544e-08, -4.3867830749295885e-08, 4.3867830772685436e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/bedomm/usd/bedomm.usd"),
            visual_material_path="materials",
            scale=(0.9999471335528047, 1.000013133252095, 1.0000421140752795),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantBedomm2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantBedomm2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.4066141807101582, -1.1741943186632038, 3.142210587176632),
            rot=(0.923879498955896, 5.711167683737469e-08, -2.3656424232182216e-08, 0.38268351337495404),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/bedomm/usd/bedomm.usd"),
            visual_material_path="materials",
            scale=(0.9999471335528047, 1.000013133252095, 1.0000421140752795),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantBftzho0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantBftzho0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.643581641657482, 1.7353949023742823, 3.3670567838726373),
            rot=(0.7660443203778362, 9.705825495186061e-08, -1.1566947954887098e-07, 0.64278775596369),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/bftzho/usd/bftzho.usd"),
            visual_material_path="materials",
            scale=(0.999961615123175, 1.0000171234455824, 1.0000278503325635),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantEvmhsg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantEvmhsg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.6212587698355091, 7.167349394033727, 4.136958133300751),
            rot=(0.7660443203778362, 9.705825495186061e-08, -1.1566947954887098e-07, 0.64278775596369),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/evmhsg/usd/evmhsg.usd"),
            visual_material_path="materials",
            scale=(0.9999612954661625, 1.000016811041665, 1.0000280077653114),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantEvmhsg1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantEvmhsg1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.365886441137102, 1.0949523078423928, 3.689213992675739),
            rot=(0.0871557180943196, 1.5042123516007888e-07, -1.3160140161740026e-08, 0.9961947002486216),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/evmhsg/usd/evmhsg.usd"),
            visual_material_path="materials",
            scale=(0.9999612954661625, 1.000016811041665, 1.0000280077653114),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantFotcaz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantFotcaz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.009427178555092, -4.7192593291392395, 2.789817795940642),
            rot=(0.7660443203778362, 9.705825495186066e-08, -1.1566947954887091e-07, 0.64278775596369),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/fotcaz/usd/fotcaz.usd"),
            visual_material_path="materials",
            scale=(1.0000640562994259, 0.9999773378652537, 1.0000158219121436),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantGccsfy0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantGccsfy0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.105350537236127, 6.0981383116940355, 3.292010825814202),
            rot=(0.7660444529585763, -9.705822780955219e-08, -1.1566948681653819e-07, -0.6427875979601448),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/gccsfy/usd/gccsfy.usd"),
            visual_material_path="materials",
            scale=(0.9999324889750183, 1.000011317693284, 1.000029532633115),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantHchlkz0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantHchlkz0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.3722446207333403, 5.651081407279367, 3.253013803190477),
            rot=(0.7660444529585763, -9.705822780955215e-08, -1.1566948681653818e-07, -0.6427875979601448),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/hchlkz/usd/hchlkz.usd"),
            visual_material_path="materials",
            scale=(1.0000107906412194, 0.9999377065282393, 1.0000195410708876),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantHdbgla0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantHdbgla0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.135792859266473, 6.651457163626565, 3.2546908089737854),
            rot=(0.7660444529585763, -9.705822780955208e-08, -1.1566948681653812e-07, -0.6427875979601448),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/hdbgla/usd/hdbgla.usd"),
            visual_material_path="materials",
            scale=(0.9999742013103973, 0.9999729409657577, 1.0000304508894424),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantIpimgx0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantIpimgx0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.581062096610653, -4.737861585897123, 3.5820639437477686),
            rot=(0.08715579942815879, 0.0, 0.0, 0.9961946931328427),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/ipimgx/usd/ipimgx.usd"),
            visual_material_path="materials",
            scale=(0.9999380407458888, 0.9999558156988065, 0.9999635278324808),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantIpimgx1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantIpimgx1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.504497954168764, -5.565724716156594, 3.431038431047768),
            rot=(0.887010822036624, 0.0, 0.0, 0.46174863463784344),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/ipimgx/usd/ipimgx.usd"),
            visual_material_path="materials",
            scale=(0.9999380407458888, 0.9999558156988065, 0.9999635278324808),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantKcajqg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantKcajqg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.7153874561674027, 1.634057975825844, 2.9500450353202887),
            rot=(0.9980399332208615, 9.449359818760868e-09, -1.5069982365737077e-07, 0.06258028201019508),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/kcajqg/usd/kcajqg.usd"),
            visual_material_path="materials",
            scale=(0.9999616950374601, 1.000016811041665, 1.0000278503325635),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantNuhdae0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantNuhdae0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.1249451536112889, 6.982863784778412, 3.2748849644455604),
            rot=(0.7660444529585763, -9.705822780955213e-08, -1.1566948681653819e-07, -0.6427875979601448),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/nuhdae/usd/nuhdae.usd"),
            visual_material_path="materials",
            scale=(1.000016946880944, 1.0000219333734444, 0.99996211075564),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantNxvleg0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantNxvleg0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.0585791622837308, 5.618847184930743, 3.2582532872753123),
            rot=(0.9961946866639254, -1.3160167515402636e-08, -1.504212046824535e-07, -0.08715587336801045),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/nxvleg/usd/nxvleg.usd"),
            visual_material_path="materials",
            scale=(0.999961615123175, 1.0000164986379427, 1.0000278503325635),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantSfqnem0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantSfqnem0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.443099928663194, 0.0623420637529572, 3.685651445589919),
            rot=(0.6427875280052563, 1.1566951700627732e-07, -9.705821393898414e-08, 0.7660445116576905),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/sfqnem/usd/sfqnem.usd"),
            visual_material_path="materials",
            scale=(0.9999747325189626, 0.9999731636361153, 1.000030286123317),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantSfqnem1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantSfqnem1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.41135131129663666, 7.244562831171372, 4.133395586219898),
            rot=(0.996194692485941, 1.3160161374409227e-08, -1.5042120555405923e-07, 0.08715580682214326),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/sfqnem/usd/sfqnem.usd"),
            visual_material_path="materials",
            scale=(0.9999747325189626, 0.9999731636361153, 1.000030286123317),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantVoaeps0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantVoaeps0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.1419674784923733, 7.214120584882561, 4.170715585293415),
            rot=(0.996194692485941, 1.3160161374409234e-08, -1.5042120555405928e-07, 0.08715580682214326),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/voaeps/usd/voaeps.usd"),
            visual_material_path="materials",
            scale=(0.9999323810688248, 1.0000113943964093, 1.000029145347207),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantVoaeps1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantVoaeps1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.4126576995298805, 0.6156608330930609, 3.7229714446684197),
            rot=(0.6427875280052563, 1.1566951700627728e-07, -9.705821393898416e-08, 0.7660445116576905),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/voaeps/usd/voaeps.usd"),
            visual_material_path="materials",
            scale=(0.9999323810688248, 1.0000113943964093, 1.000029145347207),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantXfecjy0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantXfecjy0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.8871534807738857, 2.2942432782106885, 3.6520134142034957),
            rot=(0.9238795498316467, 0.0, 0.0, 0.3826833905500393),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/xfecjy/usd/xfecjy.usd"),
            visual_material_path="materials",
            scale=(0.9999467450370314, 1.0000122027136833, 1.0000425437167912),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantXfecjy1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantXfecjy1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.0290790524718747, 1.3579663382189773, 3.2199545763134956),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/xfecjy/usd/xfecjy.usd"),
            visual_material_path="materials",
            scale=(0.9999467450370314, 1.0000122027136833, 1.0000425437167912),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantXfecjy2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantXfecjy2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.648863427707016, 1.2586903099244084, 3.643665757953496),
            rot=(-0.3826834116234627, 0.0, 0.0, 0.9238795411027497),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/xfecjy/usd/xfecjy.usd"),
            visual_material_path="materials",
            scale=(0.9999467450370314, 1.0000122027136833, 1.0000425437167912),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantXfecjy3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantXfecjy3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.34552047229737, 0.09788987016305215, 3.6385075548284957),
            rot=(0.9848077445094436, 0.0, 0.0, 0.1736482258884967),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/xfecjy/usd/xfecjy.usd"),
            visual_material_path="materials",
            scale=(0.9999467450370314, 1.0000122027136833, 1.0000425437167912),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantXfecjy4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantXfecjy4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.318640590021868, -0.03435352848420467, 3.492394273578496),
            rot=(0.34202015414019765, 0.0, 0.0, 0.9396926168497417),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/xfecjy/usd/xfecjy.usd"),
            visual_material_path="materials",
            scale=(0.9999467450370314, 1.0000122027136833, 1.0000425437167912),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantXfecjy5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantXfecjy5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.322355681478977, -4.933300732161874, 3.6385075548284957),
            rot=(0.7071067811865477, 0.0, 0.0, 0.7071067811865474),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/xfecjy/usd/xfecjy.usd"),
            visual_material_path="materials",
            scale=(0.9999467450370314, 1.0000122027136833, 1.0000425437167912),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantXfecjy6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantXfecjy6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.318640601290531, -4.900357013293674, 3.2220256212334957),
            rot=(0.34202015414019765, 0.0, 0.0, 0.9396926168497417),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/xfecjy/usd/xfecjy.usd"),
            visual_material_path="materials",
            scale=(0.9999467450370314, 1.0000122027136833, 1.0000425437167912),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantXfecjy7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantXfecjy7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.322355681478977, 0.20718565700312555, 3.4667839220184953),
            rot=(0.7071067811865477, 0.0, 0.0, 0.7071067811865474),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/xfecjy/usd/xfecjy.usd"),
            visual_material_path="materials",
            scale=(0.9999467450370314, 1.0000122027136833, 1.0000425437167912),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantXfecjy8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantXfecjy8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.8872745056901232, 2.000033925731687, 1.8844504259234958),
            rot=(-0.13052668079343432, 0.0, 0.0, 0.9914447970517819),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/xfecjy/usd/xfecjy.usd"),
            visual_material_path="materials",
            scale=(0.9999467450370314, 1.0000122027136833, 1.0000425437167912),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantXfecjy9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantXfecjy9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.057767921691397, 1.8202903363181882, 3.6331591661584954),
            rot=(0.9238795498316467, 0.0, 0.0, 0.3826833905500393),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/xfecjy/usd/xfecjy.usd"),
            visual_material_path="materials",
            scale=(0.9999467450370314, 1.0000122027136833, 1.0000425437167912),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantXjcnky0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantXjcnky0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.4322522153665, -0.26906448562108093, 3.7058457174102233),
            rot=(0.6427875280052563, 1.1566951700627724e-07, -9.705821393898408e-08, 0.7660445116576902),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/xjcnky/usd/xjcnky.usd"),
            visual_material_path="materials",
            scale=(1.0000167447902404, 1.0000216577542564, 0.99996211075564),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantXjcnky1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantXjcnky1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.7427578740024595, 7.233715106410186, 4.153589858040229),
            rot=(0.996194692485941, 1.3160161374409224e-08, -1.5042120555405915e-07, 0.08715580682214326),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/xjcnky/usd/xjcnky.usd"),
            visual_material_path="materials",
            scale=(1.0000167447902404, 1.0000216577542564, 0.99996211075564),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantXwzycj0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantXwzycj0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.5890242516258328, 7.481014563822762, 4.131718532867323),
            rot=(0.996194692485941, 1.3160161374409239e-08, -1.5042120555405928e-07, 0.08715580682214326),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/xwzycj/usd/xwzycj.usd"),
            visual_material_path="materials",
            scale=(1.0000107906412194, 0.999937874620833, 1.0000195410708876),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantXwzycj1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantXwzycj1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.6795516699275534, 1.062717564163972, 3.6839743922423165),
            rot=(0.6427875280052563, 1.156695170062773e-07, -9.705821393898418e-08, 0.7660445116576905),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/xwzycj/usd/xwzycj.usd"),
            visual_material_path="materials",
            scale=(1.0000107906412194, 0.999937874620833, 1.0000195410708876),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantXzdszm0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantXzdszm0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.090131304125952, 7.0418402524789325, 3.2754945609059556),
            rot=(-0.04361990318388772, 1.5085209719160083e-07, 6.586423624875719e-09, 0.9990481990605886),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/xzdszm/usd/xzdszm.usd"),
            visual_material_path="materials",
            scale=(1.000020617999198, 1.0000509807913316, 1.0000334708055056),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantZlgfak0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantZlgfak0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(0.5315738560405229, 7.363086809515328, 2.6131548787336674),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/zlgfak/usd/zlgfak.usd"),
            visual_material_path="materials",
            scale=(0.9999899517435404, 1.0000344113878277, 0.9999862080153487),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantZlgfak1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantZlgfak1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.46760711639508, 2.9762060232825114, 2.9454107381136674),
            rot=(0.8191519943362758, 0.0, 0.0, -0.5735765076909112),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/zlgfak/usd/zlgfak.usd"),
            visual_material_path="materials",
            scale=(0.9999899517435404, 1.0000344113878277, 0.9999862080153487),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantZlgfak2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantZlgfak2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.1168542259431908, 1.526544904750368, 2.9454107381136674),
            rot=(0.8191519943362758, 0.0, 0.0, -0.5735765076909112),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/zlgfak/usd/zlgfak.usd"),
            visual_material_path="materials",
            scale=(0.9999899517435404, 1.0000344113878277, 0.9999862080153487),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantZlgfak3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantZlgfak3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.1935534839257165, 5.7833642549698325, 3.3498931599836674),
            rot=(0.8191519943362758, 0.0, 0.0, -0.5735765076909112),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/zlgfak/usd/zlgfak.usd"),
            visual_material_path="materials",
            scale=(0.9999899517435404, 1.0000344113878277, 0.9999862080153487),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantZlgfak4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantZlgfak4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.1935534839241095, 6.314003903404248, 3.3498931599836674),
            rot=(0.8191519943362758, 0.0, 0.0, -0.5735765076909112),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/zlgfak/usd/zlgfak.usd"),
            visual_material_path="materials",
            scale=(0.9999899517435404, 1.0000344113878277, 0.9999862080153487),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantZlgfak5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantZlgfak5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.1935534839257171, 6.844643551839833, 3.3498931599836674),
            rot=(0.8191519943362758, 0.0, 0.0, -0.5735765076909112),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/zlgfak/usd/zlgfak.usd"),
            visual_material_path="materials",
            scale=(0.9999899517435404, 1.0000344113878277, 0.9999862080153487),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hangingPlantZlgfak6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hangingPlantZlgfak6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.7096327666800833, 7.376195985476638, 2.633174409983668),
            rot=(0.887010822036624, 0.0, 0.0, 0.4617486346378434),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hanging_plant/zlgfak/usd/zlgfak.usd"),
            visual_material_path="materials",
            scale=(0.9999899517435404, 1.0000344113878277, 0.9999862080153487),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hookYfikis0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hookYfikis0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.3303602810894968, 7.350839271185164, 1.4224814247594486),
            rot=(-0.7071067215818997, 0.0, 0.0, 0.7071068407911903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hook/yfikis/usd/yfikis.usd"),
            visual_material_path="materials",
            scale=(0.9989219428831165, 1.0004075137441635, 1.0005718256143254),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hookYfikis1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hookYfikis1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.9639039822594961, 7.350839271185174, 1.6657093300344485),
            rot=(-0.7071067215818997, 0.0, 0.0, 0.7071068407911903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hook/yfikis/usd/yfikis.usd"),
            visual_material_path="materials",
            scale=(0.9989219428831165, 1.0004075137441635, 1.0005718256143254),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    hookYfikis2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/hookYfikis2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.1442384549194964, 7.350839271185165, 1.5139574989794484),
            rot=(-0.7071067215818997, 0.0, 0.0, 0.7071068407911903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/hook/yfikis/usd/yfikis.usd"),
            visual_material_path="materials",
            scale=(0.9989219428831165, 1.0004075137441635, 1.0005718256143254),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ladderVpmrlk0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ladderVpmrlk0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.637914667955511, -2.25348706829303, 0.7929689654113427),
            rot=(5.205485536564991e-07, 0.0, 0.0, 0.9999999999998646),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/ladder/vpmrlk/usd/vpmrlk.usd"),
            visual_material_path="materials",
            scale=(0.9999597582114205, 1.0000038131248044, 1.000016881923209),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    skeletalFrameCfqmqw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/skeletalFrameCfqmqw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.910854624725304, -1.0222271547008877, 2.7296456847180113),
            rot=(-0.7071067215818997, 0.0, 0.0, 0.7071068407911903),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/skeletal_frame/cfqmqw/usd/cfqmqw.usd"),
            visual_material_path="materials",
            scale=(1.000002119395442, 0.9999993191984132, 0.9999876467578239),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    skeletalFrameCvtaos0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/skeletalFrameCvtaos0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.3956963839530947, 1.9404270896874125, 2.3011710863113404),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/skeletal_frame/cvtaos/usd/cvtaos.usd"),
            visual_material_path="materials",
            scale=(1.0000105982860525, 1.0000024656696678, 1.0000040671139332),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    skeletalFrameGriwyu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/skeletalFrameGriwyu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.236626330516412, 1.1485363944180274, 1.944567879319135),
            rot=(4.013392641057306e-07, 0.0, 0.0, 0.9999999999999195),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/skeletal_frame/griwyu/usd/griwyu.usd"),
            visual_material_path="materials",
            scale=(0.9999987376057837, 0.9999982545991088, 0.9999861759310281),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    skeletalFrameHjudzd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/skeletalFrameHjudzd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.780767092103102, -0.8147267506878937, 4.682429326082262),
            rot=(2.8378972200554497e-07, 2.837897219569786e-07, 0.7071067811864905, 0.7071067811864907),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/skeletal_frame/hjudzd/usd/hjudzd.usd"),
            visual_material_path="materials",
            scale=(1.00000291898512, 0.9999911325330714, 0.9999995385189978),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    skeletalFrameNxyffe0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/skeletalFrameNxyffe0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.8356337013073742, -4.484570493773815, 1.7127935398808687),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/skeletal_frame/nxyffe/usd/nxyffe.usd"),
            visual_material_path="materials",
            scale=(0.9999988331258158, 0.9999976922934184, 0.9999953206825082),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfAdgrkb1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfAdgrkb1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.393412208812141, 5.869276327136529, 1.6301695238423202),
            rot=(-7.549790142485553e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/adgrkb/usd/adgrkb.usd"),
            visual_material_path="materials",
            scale=(1.0001185803085002, 0.9999852835865612, 1.0000042123543005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfAdgrkb3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfAdgrkb3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.393412208812126, 3.943934628286405, 1.6301695238423202),
            rot=(-7.549790142485553e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/adgrkb/usd/adgrkb.usd"),
            visual_material_path="materials",
            scale=(1.0001185803085002, 0.9999852835865612, 1.0000042123543005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfIbrbnl0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfIbrbnl0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.393412111188605, 6.798319944653327, 1.1058649695451817),
            rot=(-7.549790142485553e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/ibrbnl/usd/ibrbnl.usd"),
            visual_material_path="materials",
            scale=(1.0001184895645487, 1.0000445200028287, 1.0000037998621043),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfIbrbnl1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfIbrbnl1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.393412111188605, 4.872978147778327, 1.1058649695451817),
            rot=(-7.549790142485553e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/ibrbnl/usd/ibrbnl.usd"),
            visual_material_path="materials",
            scale=(1.0001184895645487, 1.0000445200028287, 1.0000037998621043),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfXrnzjv2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfXrnzjv2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.3934121144693, 7.047536403780889, 1.6250373481270735),
            rot=(-7.549790142485553e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/xrnzjv/usd/xrnzjv.usd"),
            visual_material_path="materials",
            scale=(1.0001187617964524, 0.9999105871779261, 1.0000042123543005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfXrnzjv3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfXrnzjv3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.3934121144693, 6.052310817840889, 2.1474598945170738),
            rot=(-7.549790142485553e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/xrnzjv/usd/xrnzjv.usd"),
            visual_material_path="materials",
            scale=(1.0001187617964524, 0.9999105871779261, 1.0000042123543005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfXrnzjv6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfXrnzjv6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.393412114469301, 5.122194606905889, 1.6250373481270735),
            rot=(-7.549790142485553e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/xrnzjv/usd/xrnzjv.usd"),
            visual_material_path="materials",
            scale=(1.0001187617964524, 0.9999105871779261, 1.0000042123543005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfXrnzjv7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfXrnzjv7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.393412114469319, 4.126969020965889, 2.1474598945170738),
            rot=(-7.549790142485553e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/xrnzjv/usd/xrnzjv.usd"),
            visual_material_path="materials",
            scale=(1.0001187617964524, 0.9999105871779261, 1.0000042123543005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfZadqqv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfZadqqv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.393412107747889, 6.582388914668018, 2.1539316740135517),
            rot=(-7.549790142485553e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/zadqqv/usd/zadqqv.usd"),
            visual_material_path="materials",
            scale=(1.000118671052468, 1.0000426497257662, 1.0000033873702485),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfZadqqv1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfZadqqv1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.3934121077478885, 4.657047117793017, 2.1539316740135517),
            rot=(-7.549790142485553e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/zadqqv/usd/zadqqv.usd"),
            visual_material_path="materials",
            scale=(1.000118671052468, 1.0000426497257662, 1.0000033873702485),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairHdibix0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairHdibix0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.9520766735076904, -5.60770320892334, 0.5464401841163635),
            rot=(-0.38913294672966003, -0.0023359954357147217, -0.006307624280452728, 0.92115718126297),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/hdibix/usd/hdibix.usd"),
            visual_material_path="materials",
            scale=(0.9999472744835299, 0.9999480634326798, 0.9999656717107583),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairHicyww0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairHicyww0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.428126573562622, -1.2391740083694458, 0.5573373436927795),
            rot=(0.7974214553833008, -0.0009268671274185181, 0.007043231278657913, 0.6033809781074524),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/hicyww/usd/hicyww.usd"),
            visual_material_path="materials",
            scale=(0.9999594450603323, 1.000006667150179, 1.000003554063924),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairHicyww1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairHicyww1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.227689743041992, -2.9982757568359375, 0.553017258644104),
            rot=(-0.04362449795007706, 2.866983413696289e-05, 5.353748565539718e-05, 0.9990480542182922),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/hicyww/usd/hicyww.usd"),
            visual_material_path="materials",
            scale=(0.9999594450603323, 1.000006667150179, 1.000003554063924),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairJdtdpa0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairJdtdpa0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.399846076965332, -2.085432529449463, 0.5535958409309387),
            rot=(-0.7074088454246521, 0.0006126761436462402, 0.0018731800373643637, 0.7068020701408386),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/jdtdpa/usd/jdtdpa.usd"),
            visual_material_path="materials",
            scale=(0.9999601106086295, 1.0000071950059266, 1.0000037441513476),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairJdtdpa1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairJdtdpa1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.741273880004883, -5.250157356262207, 1.308536410331726),
            rot=(0.08713536709547043, -0.0003413558006286621, -0.00021420378470793366, 0.9961965084075928),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/jdtdpa/usd/jdtdpa.usd"),
            visual_material_path="materials",
            scale=(0.9999601106086295, 1.0000071950059266, 1.0000037441513476),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairJdtdpa2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairJdtdpa2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.236894130706787, -1.2852110862731934, 0.553037703037262),
            rot=(0.7933465242385864, -0.0001893863081932068, 8.49405478220433e-05, 0.6087703108787537),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/jdtdpa/usd/jdtdpa.usd"),
            visual_material_path="materials",
            scale=(0.9999601106086295, 1.0000071950059266, 1.0000037441513476),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQyntri0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQyntri0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.288902282714844, -6.9994635581970215, 0.5364329814910889),
            rot=(0.9238797426223755, 1.4901161193847656e-08, 1.1175870895385742e-08, 0.38268327713012695),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qyntri/usd/qyntri.usd"),
            visual_material_path="materials",
            scale=(0.9999475960719759, 0.9999481407128383, 0.9999656717107583),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairQyntri1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairQyntri1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.357469081878662, -2.972979784011841, 0.5371880531311035),
            rot=(0.9990482926368713, 0.0, 2.0954757928848267e-08, 0.0436195470392704),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/qyntri/usd/qyntri.usd"),
            visual_material_path="materials",
            scale=(0.9999475960719759, 0.9999481407128383, 0.9999656717107583),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairRtbsof0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairRtbsof0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.738639831542969, -5.312719345092773, 0.5368825197219849),
            rot=(-0.04361946880817413, 0.0, 1.1175870895385742e-08, 0.9990483522415161),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/rtbsof/usd/rtbsof.usd"),
            visual_material_path="materials",
            scale=(1.0000239464498017, 0.9999680889993383, 0.9999900659391789),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairRtbsof1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairRtbsof1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.6306875348091125, 6.281875133514404, 0.5368825197219849),
            rot=(-0.04361960291862488, -2.9802322387695312e-08, 1.1175870895385742e-08, 0.9990483522415161),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/rtbsof/usd/rtbsof.usd"),
            visual_material_path="materials",
            scale=(1.0000239464498017, 0.9999680889993383, 0.9999900659391789),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairRtbsof2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairRtbsof2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.6306875348091125, 2.7783420085906982, 0.5368825197219849),
            rot=(-0.04361960291862488, -2.9802322387695312e-08, 1.1175870895385742e-08, 0.9990483522415161),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/rtbsof/usd/rtbsof.usd"),
            visual_material_path="materials",
            scale=(1.0000239464498017, 0.9999680889993383, 0.9999900659391789),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairRtbsof3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairRtbsof3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.676192283630371, -6.482883930206299, 0.5368825197219849),
            rot=(0.9990483522415161, 0.0, 2.421438694000244e-08, 0.0436195507645607),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/rtbsof/usd/rtbsof.usd"),
            visual_material_path="materials",
            scale=(1.0000239464498017, 0.9999680889993383, 0.9999900659391789),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairRtbsof4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairRtbsof4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-0.6306875348091125, 4.548674583435059, 0.5368825197219849),
            rot=(-0.04361960291862488, -2.9802322387695312e-08, 1.1175870895385742e-08, 0.9990483522415161),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/rtbsof/usd/rtbsof.usd"),
            visual_material_path="materials",
            scale=(1.0000239464498017, 0.9999680889993383, 0.9999900659391789),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairRtbsof5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairRtbsof5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.3758745193481445, -0.18370135128498077, 0.5368825197219849),
            rot=(0.9990483522415161, 0.0, 2.421438694000244e-08, 0.0436195507645607),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/rtbsof/usd/rtbsof.usd"),
            visual_material_path="materials",
            scale=(1.0000239464498017, 0.9999680889993383, 0.9999900659391789),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairRtbsof6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairRtbsof6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.63645601272583, -6.477816581726074, 0.5368825197219849),
            rot=(-0.04361946880817413, 0.0, 1.1175870895385742e-08, 0.9990483522415161),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/rtbsof/usd/rtbsof.usd"),
            visual_material_path="materials",
            scale=(1.0000239464498017, 0.9999680889993383, 0.9999900659391789),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairRtbsof7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairRtbsof7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.6488237380981445, -6.9054179191589355, 0.5368825197219849),
            rot=(0.3826841115951538, 0.0, -2.60770320892334e-08, 0.9238794445991516),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/rtbsof/usd/rtbsof.usd"),
            visual_material_path="materials",
            scale=(1.0000239464498017, 0.9999680889993383, 0.9999900659391789),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairUkuwuu0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairUkuwuu0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.405162811279297, -4.022551536560059, 0.5538764595985413),
            rot=(0.8036631941795349, 0.004488274455070496, -0.002112122718244791, 0.5950638055801392),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/ukuwuu/usd/ukuwuu.usd"),
            visual_material_path="materials",
            scale=(0.9999592786733964, 1.0000063504369978, 1.000003680788865),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairUkuwuu1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairUkuwuu1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.3876128196716309, -3.0469932556152344, 0.5530442595481873),
            rot=(-0.04362533614039421, 3.5375356674194336e-05, 5.966899334453046e-05, 0.9990479946136475),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/ukuwuu/usd/ukuwuu.usd"),
            visual_material_path="materials",
            scale=(0.9999592786733964, 1.0000063504369978, 1.000003680788865),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairUkuwuu2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairUkuwuu2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.4052042961120605, -0.2631646692752838, 0.553044319152832),
            rot=(-0.04362525790929794, 3.5136938095092773e-05, 5.9404876083135605e-05, 0.999048113822937),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/ukuwuu/usd/ukuwuu.usd"),
            visual_material_path="materials",
            scale=(0.9999592786733964, 1.0000063504369978, 1.000003680788865),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairUkuwuu3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairUkuwuu3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.247095108032227, -3.9722442626953125, 0.5562005639076233),
            rot=(0.8046442270278931, -0.004841253161430359, 0.0064937700517475605, 0.5937020182609558),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/ukuwuu/usd/ukuwuu.usd"),
            visual_material_path="materials",
            scale=(0.9999592786733964, 1.0000063504369978, 1.000003680788865),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairUkuwuu4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairUkuwuu4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.416379928588867, 0.693156898021698, 0.5533745288848877),
            rot=(-0.7085995078086853, 0.0006003230810165405, 0.0014226051280274987, 0.7056093215942383),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/ukuwuu/usd/ukuwuu.usd"),
            visual_material_path="materials",
            scale=(0.9999592786733964, 1.0000063504369978, 1.000003680788865),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairUkuwuu5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairUkuwuu5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.207663536071777, -0.2631644606590271, 0.5530439615249634),
            rot=(-0.04362471401691437, 3.5434961318969727e-05, 5.963072180747986e-05, 0.9990480542182922),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/ukuwuu/usd/ukuwuu.usd"),
            visual_material_path="materials",
            scale=(0.9999592786733964, 1.0000063504369978, 1.000003680788865),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairUkuwuu6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairUkuwuu6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.234480857849121, 0.7508211731910706, 0.5530436038970947),
            rot=(0.7071067690849304, 1.862645149230957e-05, -6.528527592308819e-05, -0.7071067690849304),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/ukuwuu/usd/ukuwuu.usd"),
            visual_material_path="materials",
            scale=(0.9999592786733964, 1.0000063504369978, 1.000003680788865),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    armchairUkuwuu7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/armchairUkuwuu7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.238499164581299, -2.0426883697509766, 0.5530382394790649),
            rot=(-0.7082135677337646, -4.2885541915893555e-05, -0.00018200199701823294, 0.7059983015060425),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/armchair/ukuwuu/usd/ukuwuu.usd"),
            visual_material_path="materials",
            scale=(0.9999592786733964, 1.0000063504369978, 1.000003680788865),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableHmzwxn0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableHmzwxn0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.727081775665283, -3.0029892921447754, 0.7034584879875183),
            rot=(0.999987781047821, 0.003516975324600935, -0.001377945183776319, 0.003219583071768284),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/hmzwxn/usd/hmzwxn.usd"),
            visual_material_path="materials",
            scale=(0.9999729843536455, 0.9999986058377597, 1.0000571683316166),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableHmzwxn1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableHmzwxn1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.43127965927124, -3.0070488452911377, 0.7031566500663757),
            rot=(0.9999927878379822, 0.0007684367010369897, -0.0022712599020451307, 0.002983852056786418),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/hmzwxn/usd/hmzwxn.usd"),
            visual_material_path="materials",
            scale=(0.9999729843536455, 0.9999986058377597, 1.0000571683316166),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableHmzwxn2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableHmzwxn2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.734970569610596, -0.27840983867645264, 0.7034998536109924),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/hmzwxn/usd/hmzwxn.usd"),
            visual_material_path="materials",
            scale=(0.9999729843536455, 0.9999986058377597, 1.0000571683316166),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableHmzwxn3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableHmzwxn3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.442842483520508, -0.282505601644516, 0.7034998536109924),
            rot=(1.0000001192092896, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/hmzwxn/usd/hmzwxn.usd"),
            visual_material_path="materials",
            scale=(0.9999729843536455, 0.9999986058377597, 1.0000571683316166),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableHmzwxn4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableHmzwxn4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.6055502891540527, -0.2721118927001953, 0.7031655311584473),
            rot=(0.9999907612800598, 0.000249211530899629, -0.003242229111492634, 0.002823297865688801),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/hmzwxn/usd/hmzwxn.usd"),
            visual_material_path="materials",
            scale=(0.9999729843536455, 0.9999986058377597, 1.0000571683316166),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableHmzwxn5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableHmzwxn5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.9015907049179077, -0.26564157009124756, 0.7045319080352783),
            rot=(0.9999901652336121, 0.0030374620109796524, -0.0012129254173487425, 0.0030377896036952734),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/hmzwxn/usd/hmzwxn.usd"),
            visual_material_path="materials",
            scale=(0.9999729843536455, 0.9999986058377597, 1.0000571683316166),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableHmzwxn6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableHmzwxn6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.8872019052505493, -3.049968957901001, 0.7014419436454773),
            rot=(0.9999966621398926, -3.1631738238502294e-05, 0.0011353854788467288, 0.0023474597837775946),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/hmzwxn/usd/hmzwxn.usd"),
            visual_material_path="materials",
            scale=(0.9999729843536455, 0.9999986058377597, 1.0000571683316166),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    breakfastTableHmzwxn7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/breakfastTableHmzwxn7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-2.591153383255005, -3.0558667182922363, 0.7013382315635681),
            rot=(0.9999973773956299, -2.947906068584416e-05, -0.0009171543060801923, 0.0021032223012298346),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/breakfast_table/hmzwxn/usd/hmzwxn.usd"),
            visual_material_path="materials",
            scale=(0.9999729843536455, 0.9999986058377597, 1.0000571683316166),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coffeeTableZisekv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coffeeTableZisekv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.858856439590454, 0.42007601261138916, 0.35392534732818604),
            rot=(1.0000001192092896, -1.406051069352543e-06, -7.721507427049801e-05, 2.682952242594183e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/zisekv/usd/zisekv.usd"),
            visual_material_path="materials",
            scale=(1.000029650030611, 0.9999764851575172, 1.0000138832683603),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    coffeeTableZisekv1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/coffeeTableZisekv1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.858860731124878, -3.1148228645324707, 0.3539256751537323),
            rot=(1.0000001192092896, 1.287653958570445e-06, -7.437776366714388e-05, -2.5247740609302127e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/coffee_table/zisekv/usd/zisekv.usd"),
            visual_material_path="materials",
            scale=(1.000029650030611, 0.9999764851575172, 1.0000138832683603),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    consoleTableTzkfqa0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/consoleTableTzkfqa0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.5981026887893677, 2.7888267040252686, 0.6056818962097168),
            rot=(2.7939677238464355e-07, 8.073158096522093e-05, -5.2202150982338935e-05, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/console_table/tzkfqa/usd/tzkfqa.usd"),
            visual_material_path="materials",
            scale=(0.999947774171722, 1.0000677313054498, 1.0000001646245142),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    consoleTableTzkfqa1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/consoleTableTzkfqa1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.5415167808532715, -6.4904584884643555, 0.6056817770004272),
            rot=(1.000000238418579, -3.3983669709414244e-05, -6.336279329843819e-05, -1.1560860002646223e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/console_table/tzkfqa/usd/tzkfqa.usd"),
            visual_material_path="materials",
            scale=(0.999947774171722, 1.0000677313054498, 1.0000001646245142),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    consoleTableTzkfqa2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/consoleTableTzkfqa2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.369626998901367, -5.242147445678711, 1.361181378364563),
            rot=(1.0000001192092896, -0.0001003557990770787, -0.00012793042697012424, -2.6454108592588454e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/console_table/tzkfqa/usd/tzkfqa.usd"),
            visual_material_path="materials",
            scale=(0.999947774171722, 1.0000677313054498, 1.0000001646245142),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    consoleTableTzkfqa3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/consoleTableTzkfqa3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.5981017351150513, 6.2983245849609375, 0.6056819558143616),
            rot=(-3.725290298461914e-09, 8.1649050116539e-05, -5.306370439939201e-05, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/console_table/tzkfqa/usd/tzkfqa.usd"),
            visual_material_path="materials",
            scale=(0.999947774171722, 1.0000677313054498, 1.0000001646245142),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    consoleTableTzkfqa4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/consoleTableTzkfqa4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.5981018543243408, 4.543574333190918, 0.6056819558143616),
            rot=(-7.078051567077637e-08, 8.157710544764996e-05, -5.295415030559525e-05, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/console_table/tzkfqa/usd/tzkfqa.usd"),
            visual_material_path="materials",
            scale=(0.999947774171722, 1.0000677313054498, 1.0000001646245142),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    consoleTableTzkfqa5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/consoleTableTzkfqa5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.5222887992858887, -6.254603862762451, 0.605681836605072),
            rot=(-0.42261838912963867, 7.213337812572718e-05, -3.921522875316441e-06, 0.9063078165054321),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/console_table/tzkfqa/usd/tzkfqa.usd"),
            visual_material_path="materials",
            scale=(0.999947774171722, 1.0000677313054498, 1.0000001646245142),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    consoleTableTzkfqa6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/consoleTableTzkfqa6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.873720169067383, -5.301921367645264, 0.6123960614204407),
            rot=(7.450580596923828e-08, 0.0, 2.764863893389702e-10, 1.000000238418579),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/console_table/tzkfqa/usd/tzkfqa.usd"),
            visual_material_path="materials",
            scale=(0.999947774171722, 1.0000677313054498, 1.0000001646245142),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    dessertStandXmwxow0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/dessertStandXmwxow0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.7835991382598877, 3.3875162601470947, 1.5142822265625),
            rot=(-3.8816688174847513e-07, -4.5726075768470764e-05, -2.2401793103199452e-05, 1.0000001192092896),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/dessert_stand/xmwxow/usd/xmwxow.usd"),
            visual_material_path="materials",
            scale=(1.00007397347001, 1.0000156709794197, 0.9999955557760783),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ottomanMjmkdw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ottomanMjmkdw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.6772675514221191, 0.3802041709423065, 0.24189750850200653),
            rot=(9.033828973770142e-08, -5.052432243246585e-05, 4.728378189611249e-05, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/ottoman/mjmkdw/usd/mjmkdw.usd"),
            visual_material_path="materials",
            scale=(0.9999790676263323, 0.9999735784878465, 1.0001044617435386),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ottomanMjmkdw1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ottomanMjmkdw1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.6772655248641968, -4.2189860343933105, 0.24189752340316772),
            rot=(1.2200325727462769e-06, -5.38418535143137e-05, 5.039694224251434e-05, 1.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/ottoman/mjmkdw/usd/mjmkdw.usd"),
            visual_material_path="materials",
            scale=(0.9999790676263323, 0.9999735784878465, 1.0001044617435386),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    ottomanMjmkdw2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/ottomanMjmkdw2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.572744846343994, -1.8057844638824463, 0.3211095929145813),
            rot=(0.7071067690849304, -6.184563972055912e-08, 6.183267942105886e-08, -0.70710688829422),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/ottoman/mjmkdw/usd/mjmkdw.usd"),
            visual_material_path="materials",
            scale=(0.9999790676263323, 0.9999735784878465, 1.0001044617435386),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaEwview0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaEwview0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.9731686115264893, -3.805691719055176, 0.2906183898448944),
            rot=(-6.123445928096771e-08, 0.00071750208735466, -8.053125930018723e-05, 0.9999998807907104),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/ewview/usd/ewview.usd"),
            visual_material_path="materials",
            scale=(0.9999731388949596, 0.999979640114896, 0.9999859768847899),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaEwview1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaEwview1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(3.97316837310791, -0.2707936763763428, 0.29061853885650635),
            rot=(-3.387685865163803e-08, 0.0007175467908382416, -8.051689655985683e-05, 0.9999998807907104),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/ewview/usd/ewview.usd"),
            visual_material_path="materials",
            scale=(0.9999731388949596, 0.999979640114896, 0.9999859768847899),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaKsbdlf0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaKsbdlf0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.929699420928955, -3.191732883453369, 0.2867558002471924),
            rot=(1.9883736968040466e-07, 0.7071068286895752, 0.7071067690849304, 2.5331974029541016e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/ksbdlf/usd/ksbdlf.usd"),
            visual_material_path="materials",
            scale=(0.9999896293223891, 0.9999726873690823, 0.9999765100133043),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    sofaKsbdlf1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/sofaKsbdlf1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.406490325927734, -0.42763492465019226, 0.2867558002471924),
            rot=(-2.5858753360807896e-07, -0.7071061134338379, 0.7071075439453125, 1.993030309677124e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/sofa/ksbdlf/usd/ksbdlf.usd"),
            visual_material_path="materials",
            scale=(0.9999896293223891, 0.9999726873690823, 0.9999765100133043),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    barJvkwcc0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/barJvkwcc0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.7669956071064443, 5.873109678518027, 0.682338336946416),
            rot=(-4.013392642053105e-07, 0.0, 0.0, 0.9999999999999195),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bar/jvkwcc/usd/jvkwcc.usd"),
            visual_material_path="materials",
            scale=(0.9999292382155989, 0.9999784005237479, 0.9999604656017789),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    barJvkwcc1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/barJvkwcc1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.054353944531973, 3.10400793785581, 0.682338336946416),
            rot=(0.7071067811865477, 0.0, 0.0, -0.7071067811865474),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bar/jvkwcc/usd/jvkwcc.usd"),
            visual_material_path="materials",
            scale=(0.9999292382155989, 0.9999784005237479, 0.9999604656017789),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    barJvkwcc2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/barJvkwcc2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.766995606618828, 3.844884092583027, 0.682338428496416),
            rot=(-5.205485537560791e-07, 0.0, 0.0, 0.9999999999998646),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bar/jvkwcc/usd/jvkwcc.usd"),
            visual_material_path="materials",
            scale=(0.9999292382155989, 0.9999784005237479, 0.9999604656017789),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    benchSihckt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/benchSihckt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.760802734380004, -1.672872436525001, 1.02226965332),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/bench/sihckt/usd/sihckt.usd"),
            visual_material_path="materials",
            scale=(0.999999985098839, 1.0000010578398464, 1.000000052361959),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    dressJmujjo0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/dressJmujjo0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.064545772397045, 7.2513167161342835, 1.0391198524384129),
            rot=(-0.6755901869956754, 0.0, 0.0, 0.7372773557048584),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/dress/jmujjo/usd/jmujjo.usd"),
            visual_material_path="materials",
            scale=(0.9999459107904055, 1.0000076664892015, 0.9999581242258413),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomDividerVwnumt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomDividerVwnumt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.130143880335027, -5.208757825104819, 1.8371867771712695),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_divider/vwnumt/usd/vwnumt.usd"),
            visual_material_path="materials",
            scale=(0.9999940390283732, 0.9999952227340292, 0.9999850993896752),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomDividerVwnumt1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomDividerVwnumt1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.130143880335027, -0.32531849405481983, 1.8371867771712695),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_divider/vwnumt/usd/vwnumt.usd"),
            visual_material_path="materials",
            scale=(0.9999940390283732, 0.9999952227340292, 0.9999850993896752),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightKtlgie0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightKtlgie0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.5983861554679315, -1.3913719971152838, 5.362362053717897),
            rot=(0.9999999999999716, 3.883971042523259e-10, -9.2601085723001e-17, -2.384182627411261e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/ktlgie/usd/ktlgie.usd"),
            visual_material_path="materials",
            scale=(0.9999885739657749, 0.9999877017888285, 0.9999866945507235),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightKtlgie1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightKtlgie1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.6918011945279465, -2.7022655823252837, 4.944259758792895),
            rot=(0.9999999999999716, 3.883971042523259e-10, -9.2601085723001e-17, -2.384182627411261e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/ktlgie/usd/ktlgie.usd"),
            visual_material_path="materials",
            scale=(0.9999885739657749, 0.9999877017888285, 0.9999866945507235),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightKtlgie2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightKtlgie2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.001580491407947, -0.7987650940452838, 5.580070061527895),
            rot=(0.9999999999999716, 3.883971042523259e-10, -9.2601085723001e-17, -2.384182627411261e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/ktlgie/usd/ktlgie.usd"),
            visual_material_path="materials",
            scale=(0.9999885739657749, 0.9999877017888285, 0.9999866945507235),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightKtlgie3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightKtlgie3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.352993577347945, -5.577265094045285, 5.229462883792896),
            rot=(0.9999999999999716, 3.883971042523259e-10, -9.2601085723001e-17, -2.384182627411261e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/ktlgie/usd/ktlgie.usd"),
            visual_material_path="materials",
            scale=(0.9999885739657749, 0.9999877017888285, 0.9999866945507235),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightKtlgie4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightKtlgie4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-8.028800950387948, -5.9773036682604, 4.509567864262896),
            rot=(0.9999999999999716, 3.883971042523259e-10, -9.2601085723001e-17, -2.384182627411261e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/ktlgie/usd/ktlgie.usd"),
            visual_material_path="materials",
            scale=(0.9999885739657749, 0.9999877017888285, 0.9999866945507235),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightKtlgie5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightKtlgie5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.646948655467947, -6.028393512010285, 4.944259758792895),
            rot=(0.9999999999999716, 3.883971042523259e-10, -9.2601085723001e-17, -2.384182627411261e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/ktlgie/usd/ktlgie.usd"),
            visual_material_path="materials",
            scale=(0.9999885739657749, 0.9999877017888285, 0.9999866945507235),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightKtlgie6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightKtlgie6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-7.5756342023429255, 0.2883715026347163, 4.944259758792896),
            rot=(0.9999999999999716, 3.883971042523259e-10, -9.2601085723001e-17, -2.384182627411261e-07),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/ktlgie/usd/ktlgie.usd"),
            visual_material_path="materials",
            scale=(0.9999885739657749, 0.9999877017888285, 0.9999866945507235),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightOcccxo0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightOcccxo0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.608525087277539, 2.8013074539866807, 2.007131750582086),
            rot=(0.7660444283313822, 0.0, 0.0, 0.6427876273097094),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/occcxo/usd/occcxo.usd"),
            visual_material_path="materials",
            scale=(0.9999833330270906, 1.0000634671671564, 0.9999624205461364),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightOcccxo1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightOcccxo1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.599359526327024, 6.307564790286677, 2.0071317505820865),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/occcxo/usd/occcxo.usd"),
            visual_material_path="materials",
            scale=(0.9999833330270906, 1.0000634671671564, 0.9999624205461364),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightOcccxo2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightOcccxo2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-1.6017742882413633, 4.552403305195766, 2.0071317505820865),
            rot=(0.9238795603683573, 0.0, 0.0, -0.38268336511216533),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/occcxo/usd/occcxo.usd"),
            visual_material_path="materials",
            scale=(0.9999833330270906, 1.0000634671671564, 0.9999624205461364),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightXaezsw0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightXaezsw0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.04010691894879, -0.27856634386037804, 3.4832633659836505),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/xaezsw/usd/xaezsw.usd"),
            visual_material_path="materials",
            scale=(0.9998985324047203, 1.0000175296343348, 1.0000130614922162),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightXaezsw1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightXaezsw1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.040106918948808, -4.833420012075377, 3.4832633659836505),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/xaezsw/usd/xaezsw.usd"),
            visual_material_path="materials",
            scale=(0.9998985324047203, 1.0000175296343348, 1.0000130614922162),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightXaezsw10 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightXaezsw10",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-4.6898824170938385, 2.0869842987128937, 3.4832634880586504),
            rot=(-0.7071066619772458, 0.0, 0.0, 0.7071069003958291),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/xaezsw/usd/xaezsw.usd"),
            visual_material_path="materials",
            scale=(0.9998985324047203, 1.0000175296343348, 1.0000130614922162),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightXaezsw2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightXaezsw2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.040106918948789, -3.6683127122703785, 3.4832633659836505),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/xaezsw/usd/xaezsw.usd"),
            visual_material_path="materials",
            scale=(0.9998985324047203, 1.0000175296343348, 1.0000130614922162),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightXaezsw3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightXaezsw3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.040106918948789, -2.443507780630378, 3.4832633659836505),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/xaezsw/usd/xaezsw.usd"),
            visual_material_path="materials",
            scale=(0.9998985324047203, 1.0000175296343348, 1.0000130614922162),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightXaezsw4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightXaezsw4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-10.040106918948787, -1.2548944993803781, 3.48326336598365),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/xaezsw/usd/xaezsw.usd"),
            visual_material_path="materials",
            scale=(0.9998985324047203, 1.0000175296343348, 1.0000130614922162),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightXaezsw5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightXaezsw5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.1354139257888107, 5.394141023079601, 3.4832634880586504),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/xaezsw/usd/xaezsw.usd"),
            visual_material_path="materials",
            scale=(0.9998985324047203, 1.0000175296343348, 1.0000130614922162),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightXaezsw6 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightXaezsw6",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.1354139257888107, 6.602445222299601, 3.4832634880586504),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/xaezsw/usd/xaezsw.usd"),
            visual_material_path="materials",
            scale=(0.9998985324047203, 1.0000175296343348, 1.0000130614922162),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightXaezsw7 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightXaezsw7",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.1354139257887894, 2.9885188306996007, 3.4832634880586504),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/xaezsw/usd/xaezsw.usd"),
            visual_material_path="materials",
            scale=(0.9998985324047203, 1.0000175296343348, 1.0000130614922162),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightXaezsw8 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightXaezsw8",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-3.1354139257888107, 4.196823151989601, 3.4832634880586504),
            rot=(0.9999999999999962, 0.0, 0.0, -8.688795409866118e-08),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/xaezsw/usd/xaezsw.usd"),
            visual_material_path="materials",
            scale=(0.9998985324047203, 1.0000175296343348, 1.0000130614922162),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    roomLightXaezsw9 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/roomLightXaezsw9",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-5.898186616313838, 2.0869842987128937, 3.4832634880586504),
            rot=(-0.7071066619772458, 0.0, 0.0, 0.7071069003958291),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/room_light/xaezsw/usd/xaezsw.usd"),
            visual_material_path="materials",
            scale=(0.9998985324047203, 1.0000175296343348, 1.0000130614922162),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    skeletalFrameTwalud0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/skeletalFrameTwalud0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-9.677564869935706, -7.445364244672147, 2.5388760925081226),
            rot=(1.0, 0.0, 0.0, 0.0),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/skeletal_frame/twalud/usd/twalud.usd"),
            visual_material_path="materials",
            scale=(0.9999999793676234, 0.9999976922934184, 0.9999944096108948),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfAdgrkb0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfAdgrkb0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.393412208812107, 5.869276547231406, 0.6033474413223202),
            rot=(-7.549790142485553e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/adgrkb/usd/adgrkb.usd"),
            visual_material_path="materials",
            scale=(1.0001185803085002, 0.9999852835865612, 1.0000042123543005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfAdgrkb2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfAdgrkb2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.3934122088121255, 3.943934750356405, 0.6033474413223202),
            rot=(-7.549790142485553e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/adgrkb/usd/adgrkb.usd"),
            visual_material_path="materials",
            scale=(1.0001185803085002, 0.9999852835865612, 1.0000042123543005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfCyckht0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfCyckht0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.2949067422846627, 7.268791478500774, 2.330496016997819),
            rot=(-0.7071067215818988, -3.090862017793444e-08, 3.090862020743312e-08, 0.70710684079119),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/cyckht/usd/cyckht.usd"),
            visual_material_path="materials",
            scale=(0.9998824047629864, 1.0001570307136232, 1.0000071635690475),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfHrfwyd0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfHrfwyd0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.9995000176450524, 7.270547599237459, 2.111663049666072),
            rot=(-0.7071067215818988, -3.090862017793442e-08, 3.090862020743312e-08, 0.70710684079119),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/hrfwyd/usd/hrfwyd.usd"),
            visual_material_path="materials",
            scale=(0.9997690284974537, 0.999822913368613, 1.000117181003771),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfHrfwyd1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfHrfwyd1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(1.9992825004882007, 7.269644769311044, 2.510849939311073),
            rot=(-0.7071067215818988, -3.090862017793442e-08, 3.090862020743312e-08, 0.70710684079119),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/hrfwyd/usd/hrfwyd.usd"),
            visual_material_path="materials",
            scale=(0.9997690284974537, 0.999822913368613, 1.000117181003771),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfQrmiur0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfQrmiur0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.1476161218102545, 7.279540203540003, 1.7643765575949624),
            rot=(-0.7071067215818988, -3.0908620177934405e-08, 3.090862020743313e-08, 0.70710684079119),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/qrmiur/usd/qrmiur.usd"),
            visual_material_path="materials",
            scale=(0.9997739319725689, 1.0000171132102034, 0.9997558420447699),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfXrnzjv0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfXrnzjv0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.393412114469301, 6.051971218235889, 1.1013565619920733),
            rot=(-7.549790142485553e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/xrnzjv/usd/xrnzjv.usd"),
            visual_material_path="materials",
            scale=(1.0001187617964524, 0.9999105871779261, 1.0000042123543005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfXrnzjv1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfXrnzjv1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.3934121144693, 7.0475366479208885, 0.5982149909520734),
            rot=(-7.549790142485553e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/xrnzjv/usd/xrnzjv.usd"),
            visual_material_path="materials",
            scale=(1.0001187617964524, 0.9999105871779261, 1.0000042123543005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfXrnzjv4 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfXrnzjv4",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.393412114469319, 4.126629299285889, 1.1013565619920733),
            rot=(-7.549790142485553e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/xrnzjv/usd/xrnzjv.usd"),
            visual_material_path="materials",
            scale=(1.0001187617964524, 0.9999105871779261, 1.0000042123543005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    wallMountedShelfXrnzjv5 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/wallMountedShelfXrnzjv5",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(4.393412114469301, 5.122194851045889, 0.5982149909520734),
            rot=(-7.549790142485553e-08, 0.0, 0.0, 0.9999999999999973),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/wall_mounted_shelf/xrnzjv/usd/xrnzjv.usd"),
            visual_material_path="materials",
            scale=(1.0001187617964524, 0.9999105871779261, 1.0000042123543005),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowYwetvt0 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowYwetvt0",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(-6.926475054343519, -7.983068772313492, 3.450400382519862),
            rot=(0.7071067811865477, 0.0, 0.0, 0.7071067811865474),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ywetvt/usd/ywetvt.usd"),
            visual_material_path="materials",
            scale=(0.9997733881311256, 1.0000004307887294, 1.0000082547980635),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowYwetvt1 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowYwetvt1",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(2.866141400736481, -7.983069748878492, 3.4532394938498627),
            rot=(0.7071067811865477, 0.0, 0.0, 0.7071067811865474),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ywetvt/usd/ywetvt.usd"),
            visual_material_path="materials",
            scale=(0.9997733881311256, 1.0000004307887294, 1.0000082547980635),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowYwetvt2 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowYwetvt2",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.376899844184777, -5.200246948271923, 3.450400504589862),
            rot=(5.205485536564991e-07, 0.0, 0.0, 0.9999999999998646),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ywetvt/usd/ywetvt.usd"),
            visual_material_path="materials",
            scale=(0.9997733881311256, 1.0000004307887294, 1.0000082547980635),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )

    windowYwetvt3 = AssetBaseCfg(
        prim_path="{ENV_REGEX_NS}/windowYwetvt3",
        init_state=AssetBaseCfg.InitialStateCfg(
            pos=(5.376899355899905, 0.12521221921307538, 3.4532393717798624),
            rot=(5.205485536564991e-07, 0.0, 0.0, 0.9999999999998646),
        ),
        spawn=UsdFileCfg(
            usd_path=os.path.expanduser("~/og_dataset/og_objects/window/ywetvt/usd/ywetvt.usd"),
            visual_material_path="materials",
            scale=(0.9997733881311256, 1.0000004307887294, 1.0000082547980635),
            rigid_props=RigidBodyPropertiesCfg(
                kinematic_enabled=True,
                rigid_body_enabled=False,
            ),
            # rigid_props=RigidBodyPropertiesCfg(),
        )
    )
