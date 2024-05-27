import pytest
from src.common.geometry import vortex_pattern, flower_of_life_3d, metatrons_cube, sphere

def test_vortex_pattern():
    points = vortex_pattern(100)
    assert len(points) == 100

def test_flower_of_life_3d():
    points = flower_of_life_3d(1, 3)
    assert len(points) > 0

def test_metatrons_cube():
    points = metatrons_cube(1)
    assert len(points) > 0

def test_sphere():
    points = sphere(1, 100)
    assert len(points) == 100
