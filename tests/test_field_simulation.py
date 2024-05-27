import pytest
import numpy as np
from src.field_simulation import update_positions_original, update_positions_vortex

def test_update_positions_original():
    points = np.random.rand(10, 3)
    t = 0.1
    updated_points = update_positions_original(points, t)
    assert len(updated_points) == len(points)

def test_update_positions_vortex():
    points = np.random.rand(10, 3)
    t = 0.1
    vortex_params = [
        (0, 0, 1, 1.0, 1.0, 0),
        (1, -1, 0, 0.8, 1.0, np.pi/2),
        (-1, 1, 0, 0.8, 1.0, np.pi),
        (1, 1, 0, 0.8, 1.0, 3*np.pi/2)
    ]
    updated_points = update_positions_vortex(points, t, vortex_params, 1.0)
    assert len(updated_points) == len(points)
