import os
import glob
import torch

# the directory of current file
current_dir = os.path.dirname(os.path.abspath(__file__))

# 获取所有匹配的文件名
file_pattern = os.path.join(current_dir, 'integration_*.pkl')
files = glob.glob(file_pattern)

# 初始化一个列表来存储所有的image_data
all_image_data = []
all_qpos_data = []
all_action_data = []
max_epi_len = 90

# 遍历所有文件并读取内容
for file in files:
    data = torch.load(file)
    print(f"find shape of {file}: {data['image_data'].shape}")
    # extract epi_num from integration_*.pkl
    epi_num = int(file.split("_")[-1].split(".")[0])
    
    if 'image_data' in data:
        all_image_data.append(data['image_data'].cuda()[:epi_num, :max_epi_len, :])
    if 'qpos_data' in data:
        all_qpos_data.append(data['qpos_data'].cuda()[:epi_num, :max_epi_len, :])
    if 'action_data' in data:
        all_action_data.append(data['action_data'].cuda()[:epi_num, :max_epi_len, :])

# 将所有image_data在第一维进行合并
if all_image_data:
    combined_image_data = torch.cat(all_image_data, dim=0)
    combined_qpos_data = torch.cat(all_qpos_data, dim=0)
    combined_action_data = torch.cat(all_action_data, dim=0)
    data = {
        "image_data": combined_image_data,  # Tensor, shape: (num_episodes, episode_len, 24)
        "image_depth_data": None,
        "qpos_data": combined_qpos_data,  # Tensor, shape: (num_episodes, episode_len, 14)
        "next_action_data": None,
        "next_action_is_pad": None,
        "action_data": combined_action_data,   # Tensor, shape: (num_episodes, episode_len, 14)
        "action_is_pad": None,
    }
    print("Combined image_data shape:", combined_image_data.shape)
    dataset_dir = current_dir
    if len(all_image_data) > 1:
        torch.save(data, os.path.join(dataset_dir, f"integration_{combined_image_data.shape[0]}.pkl"))
        print(f"Save data to {os.path.join(dataset_dir, f'integration_{combined_image_data.shape[0]}.pkl')}")
else:
    print("No image_data found in the files.")
