#!/bin/bash

# Download official assets package from 'https://docs.isaacsim.omniverse.nvidia.com/latest/installation/download.html'
# For ManiBox, the following assets are not necessary

# mkdir manibox_dataset

# unzip ~/isaac-sim-assets-1@4.2.0-rc.18+release.16044.3b2ed111.zip -d ~/manibox_dataset/assets_1
# unzip ~/isaac-sim-assets-2@4.2.0-rc.18+release.16044.3b2ed111.zip -d ~/manibox_dataset/assets_2
# unzip ~/isaac-sim-assets-3@4.2.0-rc.18+release.16044.3b2ed111.zip -d ~/manibox_dataset/assets_3
# unzip ~/isaac-sim-assets-4@4.2.0-rc.18+release.16044.3b2ed111.zip -d ~/manibox_dataset/assets_4

unzip ~/manibox/manibox-sim-usd-urdf.zip -d ~/manibox

mkdir -p ~/manibox_dataset/Assets/Isaac/4.2/NVIDIA/Assets/ArchVis/Residential/Food/Fruit/
mkdir -p ~/manibox_dataset/assets_2/Assets/Isaac/4.2/Isaac/Robots/MobileAloha/
mkdir -p ~/manibox_dataset/assets_1/Assets/Isaac/4.2/Isaac/Environments/Simple_Room/
mkdir -p ~/manibox_dataset/assets_3/Assets/Isaac/4.2/NVIDIA/Assets/ArchVis/Residential/Decor/TableCloth/

# Green Apple
mv ~/manibox/green_apple.usd \
   ~/manibox_dataset/Assets/Isaac/4.2/NVIDIA/Assets/ArchVis/Residential/Food/Fruit/

# Mobile Aloha
mv ~/manibox/Links_allFront_Joints_fl.usd \
   ~/manibox_dataset/assets_2/Assets/Isaac/4.2/Isaac/Robots/MobileAloha/

# Cube Room
mv ~/manibox/CubeRoom.usda \
   ~/manibox_dataset/assets_1/Assets/Isaac/4.2/Isaac/Environments/Simple_Room/

# Orange Tablecloth
mv ~/manibox/orange_tablecloth_without_ref_tem.usd \
   ~/manibox_dataset/assets_3/Assets/Isaac/4.2/NVIDIA/Assets/ArchVis/Residential/Decor/TableCloth/
