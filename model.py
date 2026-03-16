# D:\Minor Project\model.py

import torch.nn as nn
import torchvision.models as models

class DeepfakeModel(nn.Module):
    def __init__(self):
        super(DeepfakeModel, self).__init__()
        # ✅ Load pretrained ResNet50
        self.base_model = models.resnet50(pretrained=True)

        # ✅ Change final layer to output 2 classes (Real/Fake)
        self.base_model.fc = nn.Linear(self.base_model.fc.in_features, 2)

    def forward(self, x):
        return self.base_model(x)
