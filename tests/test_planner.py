import numpy as np
from src.planner import ReactivePlanner

def test_planner_forward_when_clear():
    grid = np.zeros((10, 20), dtype=np.uint8)
    assert ReactivePlanner().plan(grid)[0] == "FORWARD"

def test_planner_turns_when_blocked():
    grid = np.zeros((10, 20), dtype=np.uint8)
    grid[:, 7:13] = 1
    assert ReactivePlanner().plan(grid)[0] in ("LEFT", "RIGHT")
