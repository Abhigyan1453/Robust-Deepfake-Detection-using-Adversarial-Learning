import torch
from model import DeepfakeModel

model = DeepfakeModel()
torch.save(model.state_dict(), "model.pth")
