import numpy as np

class ObstacleMap:
    def __init__(self, grid_w=20, grid_h=10, threshold=0.7):
        self.grid_w = grid_w
        self.grid_h = grid_h
        self.threshold = threshold

    def from_depth(self, depth):
        h, w = depth.shape
        cw, ch = w // self.grid_w, h // self.grid_h
        grid = np.zeros((self.grid_h, self.grid_w))
        for i in range(self.grid_h):
            for j in range(self.grid_w):
                cell = depth[i*ch:(i+1)*ch, j*cw:(j+1)*cw]
                grid[i, j] = cell.mean()
        return (grid > self.threshold).astype(np.uint8)
