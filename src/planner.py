import numpy as np

class ReactivePlanner:
    """Выбирает безопасное направление по obstacle map."""
    def __init__(self, danger_zone_ratio=0.4):
        self.danger = danger_zone_ratio

    def plan(self, obstacle_grid):
        h, w = obstacle_grid.shape
        center = obstacle_grid[:, w//3: 2*w//3]
        if center.mean() < 0.2:
            return "FORWARD", 0.0
        left = obstacle_grid[:, :w//2]
        right = obstacle_grid[:, w//2:]
        if left.mean() < right.mean():
            return "LEFT", 0.5
        return "RIGHT", 0.5
