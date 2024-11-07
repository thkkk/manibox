import os
import glob
import torch
from ManiBox.yolo_process_data import YoloProcessDataByTimeStep

# the directory of current file
# current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = "./data/"
# merge all integration_xxx.pkl

file_pattern = os.path.join(current_dir, 'integration_*.pkl')
files = glob.glob(file_pattern)

# image_data
all_image_data = []
all_qpos_data = []
all_action_data = []
all_reward = []
episode_begin = 3
episode_end = 90
image_data_dim = len(YoloProcessDataByTimeStep.objects_names) * 12
print(f"Using first {image_data_dim}-dim image-bbox information")

for file in files:
    data = torch.load(file)
    print(f"find shape of {file}: {data['image_data'].shape}")
    # extract epi_num from integration_*.pkl
    epi_num = int(file.split("_")[-1].split(".")[0])
    
    # if epi_num == 1600:
    #     # data['qpos_data'] shape: (25000, 120, 14)
    #     # find the first idx where qpos_data is all zero
    #     idx = -1
    #     for i in range(data['qpos_data'].shape[0]):
    #         if torch.sum(data['qpos_data'][i]) == 0:
    #             idx = i
    #             break
    #     import pdb; pdb.set_trace()
    # and then print idx to find the corresponding episode number
    
    baseline = 0  # The merged data may have been shifted, so the subscript needs to subtract the baseline
    if data['image_data'].shape[1] == episode_end - episode_begin:
        baseline = episode_begin
    if 'image_data' in data:
        print(f"{epi_num} image_data shape:", data['image_data'].shape)
        all_image_data.append(data['image_data'].cuda()[:epi_num, episode_begin-baseline: episode_end-baseline, :image_data_dim])
    if 'qpos_data' in data:
        all_qpos_data.append(data['qpos_data'].cuda()[:epi_num, episode_begin-baseline: episode_end-baseline, :])
    if 'action_data' in data:
        all_action_data.append(data['action_data'].cuda()[:epi_num, episode_begin-baseline:episode_end-baseline, :])
    if 'reward' in data:
        all_reward.append(data['reward'].cuda()[:epi_num, episode_begin-baseline:episode_end-baseline])
    # TODO: rewards

if all_image_data:
    combined_image_data = torch.cat(all_image_data, dim=0)
    combined_qpos_data = torch.cat(all_qpos_data, dim=0)
    combined_action_data = torch.cat(all_action_data, dim=0)
    if all_reward:
        combined_reward = torch.cat(all_reward, dim=0)
    # invalid_index = (torch.logical_or(combined_qpos_data[:, 30:, 6] > 3.7, combined_qpos_data[:, 30:, 6] < 2)).sum(dim=-1) > 0
    # print("qpos invalid number:", invalid_index.sum())
    # # import pdb; pdb.set_trace()
    # combined_qpos_data = combined_qpos_data[~invalid_index]
    # combined_image_data = combined_image_data[~invalid_index]
    # combined_action_data = combined_action_data[~invalid_index]
    
    # if combined_image_data[i, 0, 0:4] is all 0, then remove this episode
    # invalid_index = (combined_image_data[:, 0, 0:4] == 0).sum(dim=-1) == 4
    # print("img invalid number:", invalid_index.sum())
    # combined_qpos_data = combined_qpos_data[~invalid_index]
    # combined_image_data = combined_image_data[~invalid_index]
    # combined_action_data = combined_action_data[~invalid_index]
    
    all_index = torch.arange(combined_image_data.shape[0])
    # shuffle
    print("shuffle data")
    shuffled_index = torch.randperm(combined_image_data.shape[0])
    combined_image_data = combined_image_data[shuffled_index]
    combined_qpos_data = combined_qpos_data[shuffled_index]
    combined_action_data = combined_action_data[shuffled_index]
    if all_reward:
        combined_reward = combined_reward[shuffled_index]
    data = {
        "image_data": combined_image_data,  # Tensor, shape: (num_episodes, episode_len, 24)
        "image_depth_data": None,
        "qpos_data": combined_qpos_data,  # Tensor, shape: (num_episodes, episode_len, 14)
        "next_action_data": None,
        "next_action_is_pad": None,
        "action_data": combined_action_data,   # Tensor, shape: (num_episodes, episode_len, 14)
        "action_is_pad": None,
        "reward": combined_reward,
    }
    print("Combined image_data shape:", combined_image_data.shape)
    print("combined_reward", combined_reward.shape)
    dataset_dir = current_dir
    # if len(all_image_data) > 1:
    torch.save(data, os.path.join(dataset_dir, f"integration_{combined_image_data.shape[0]}.pkl"))
    print(f"Save data to {os.path.join(dataset_dir, f'integration_{combined_image_data.shape[0]}.pkl')}")
else:
    print("No image_data found in the files.")
