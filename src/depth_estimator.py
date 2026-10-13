import torch
import cv2
import numpy as np

class MiDaSDepth:
    def __init__(self, device="cuda"):
        self.device = device
        self.model = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")
        self.model.to(device).eval()
        self.transform = torch.hub.load("intel-isl/MiDaS", "transforms").small_transform

    def estimate(self, frame):
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        inp = self.transform(img).to(self.device)
        with torch.no_grad():
            pred = self.model(inp)
            pred = torch.nn.functional.interpolate(
                pred.unsqueeze(1), size=img.shape[:2],
                mode="bicubic", align_corners=False).squeeze()
        depth = pred.cpu().numpy()
        depth = (depth - depth.min()) / (depth.max() - depth.min() + 1e-6)
        return depth
