from torchvision import transforms
from model import DeepfakeModel
from utils import extract_frames
import torch

# Inside your process_video function or at the top of detect.py

from torchvision import transforms

transform = transforms.Compose([
    transforms.ToPILImage(),
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])



def process_video(video_path):
    model = DeepfakeModel()
    model.eval()  # using pretrained ResNet50 (no need to load .pth)

    frames = extract_frames(video_path, num_frames=10)
    predictions = []

    for frame in frames:
        img_tensor = transform(frame).unsqueeze(0)
        with torch.no_grad():
            output = model(img_tensor)
        prediction = torch.argmax(output, dim=1).item()
        predictions.append(prediction)

    fake_ratio = sum(predictions) / len(predictions)
    return "Fake" if fake_ratio > 0.5 else "Real"
