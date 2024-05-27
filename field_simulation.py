import numpy as np

def magnetic_field(x, y, z, t):
    Bx = np.sin(x + t)
    By = np.cos(y + t)
    Bz = np.sin(z + t)
    return Bx, By, Bz

def vortex_field(x, y, z, t):
    Vx = -y * np.sin(t)
    Vy = x * np.sin(t)
    Vz = np.cos(z + t)
    return Vx, Vy, Vz

def update_positions(points, t):
    updated_points = []
    for x, y, z in points:
        Bx, By, Bz = magnetic_field(x, y, z, t)
        Vx, Vy, Vz = vortex_field(x, y, z, t)
        new_x = x + 0.1 * (Bx + Vx)
        new_y = y + 0.1 * (By + Vy)
        new_z = z + 0.1 * (Bz + Vz)
        updated_points.append((new_x, new_y, new_z))
    return updated_points
