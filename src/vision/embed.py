import torch
from torchvision import models, transforms
from PIL import Image
from pathlib import Path

device = "cuda" if torch.cuda.is_available() else "cpu"

model = models.resnet18(weights=models.ResNet18_Weights.DEFAULT)
model.fc = torch.nn.Identity()
model = model.to(device).eval()

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485,0.456,0.406],
        std=[0.229,0.224,0.225]
    )
])

@torch.no_grad()
def embed_image(path: str):
    img = Image.open(Path(path)).convert("RGB")
    x = transform(img).unsqueeze(0).to(device)
    emb = model(x)
    return emb.cpu().numpy().flatten()
