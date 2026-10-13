class SafetyMonitor:
    def __init__(self, max_obstacle_ratio=0.5):
        self.max_ratio = max_obstacle_ratio

    def check(self, obstacle_grid):
        ratio = obstacle_grid.mean()
        if ratio > self.max_ratio:
            return "EMERGENCY_STOP", ratio
        if ratio > 0.3:
            return "SLOW_DOWN", ratio
        return "OK", ratio
