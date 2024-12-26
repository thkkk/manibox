# ManiBox: Enhancing Spatial Grasping Generalization via Scalable Simulation Data Generation

- 📝[Paper](https://arxiv.org/pdf/2411.01850)
- 🌍[Project Page](https://thkkk.github.io/manibox)
- 🛢️[Dataset](https://ml.cs.tsinghua.edu.cn/~hengkai/20240923_41_30_28_integration_38150.pkl)
- 👏Contributors: [Hengkai Tan](https://github.com/thkkk), [Xuezhou Xu](https://github.com/xuxuezhou), [Chengyang Ying](https://github.com/yingchengyang), [Xinyi Mao](https://github.com/shhmxy2)

**The code of the simulator part** (including teacher policy and data generation) could be seen in **[sim branch](https://github.com/thkkk/manibox/tree/sim)**.

## Installation Instructions

```bash
conda deactivate
conda create -n manibox python=3.9
conda activate manibox

pip install -e .

# for student inference code, you should install these in `isaac lab conda env`:
pip install einops
```

## Dataset

The full space version dataset is in 🛢️[Download link](https://ml.cs.tsinghua.edu.cn/~hengkai/20240923_41_30_28_integration_38150.pkl). It has a total of 38,150 trajectories, which you should rename to integration.pkl in any directory.

## Student Training Instructions

The `train.py` will will read `integration.pkl` in the `--dataset` directory as a dataset. `integration.pkl` is a dict containing three keys, `image_data`, `qpos_data`, `action_data`, with shape `(num_episodes, episode_len , dim)`.

```bash

# BBOX RNN
python ManiBox/train.py --policy_class RNN --batch_size 128 --dataset ../ --num_episodes 38000  --loss_function l1  --rnn_layers 3 --rnn_hidden_dim 512 --actor_hidden_dim 512 --num_epochs 50 --lr 2e-3 --gradient_accumulation_steps 1 > train.log 2>&1
```

## Deployment Instructions

```bash
python ManiBox/inference_real_world.py  --ckpt_dir /PATH/TO/ManiBox/ckpt/2024-xx-xx_xx-xx-xxRNN --policy_class RNN --ckpt_name policy_best.ckpt
```

## Other Instructions

### Teacher Policy Training Instructions
```bash

# PPO Training
python source/standalone/workflows/rsl_rl/train.py --task Isaac-Lift-Cube-MobileAloha-v0  --num_envs 4096  --headless
```

### Data Collection Instructions
```bash

# Collect data in simulator
python source/standalone/workflows/rsl_rl/play_collect_data.py --task Isaac-Lift-Cube-MobileAloha-Play-v0 \
--num_envs 40  --load_run  2024-09-12_17-42-24 --headless --enable_cameras
```

### Simulator Inference Instruction
```bash

# Student policy inference in simulator
python source/standalone/workflows/rsl_rl/student_inference_orbit_multi_envs.py --task Isaac-Lift-Cube-MobileAloha-Play-v0 \
--ckpt_dir "\PATH\TO\Your\CKPT" --policy_class "RNN" --ckpt_name policy_best.ckpt --nheads 48 --num_train_step 38000 --seed 0
```

## Acknowledgement

- [cobot magic](https://github.com/agilexrobotics/cobot_magic)
- [mobile aloha](https://github.com/MarkFzp/mobile-aloha)

## BibTeX
If you find our work useful for your project, please consider citing the following paper.

```
@article{tan2024manibox,
  title={ManiBox: Enhancing Spatial Grasping Generalization via Scalable Simulation Data Generation},
  author={Tan, Hengkai and Xu, Xuezhou and Ying, Chengyang and Mao, Xinyi and Liu, Songming and Zhang, Xingxing and Su, Hang and Zhu, Jun},
  journal={arXiv preprint arXiv:2411.01850},
  year={2024}
}
```
