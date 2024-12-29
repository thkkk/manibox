import torch

from ..rigid_object import RigidObjectData



class RandomRigidObjectData(RigidObjectData):
    # chosen_index: torch.Tensor = None
    root_scales: torch.Tensor = None
    pass