import numpy as np

# Original field simulation functions
def magnetic_field_original(x, y, z, t, B0=1e-5):
    r = np.sqrt(x**2 + y**2 + z**2)
    Bx = B0 * (y**2 + z**2) / r**5
    By = B0 * (x**2 + z**2) / r**5
    Bz = B0 * (x**2 + y**2) / r**5
    return Bx, By, Bz

def electric_field_original(x, y, z, t, E0=1e-6):
    r = np.sqrt(x**2 + y**2 + z**2)
    Ex = E0 * x / r**3
    Ey = E0 * y / r**3
    Ez = E0 * z / r**3
    return Ex, Ey, Ez

def resonance_frequency(x, y, z, t, f0=1e3):
    r = np.sqrt(x**2 + y**2 + z**2)
    f = f0 / r
    return f

def solar_radiation_pressure(x, y, z, t, P0=1e-6):
    r = np.sqrt(x**2 + y**2 + z**2)
    P = P0 / r**2
    Px = P * x / r
    Py = P * y / r
    Pz = P * z / r
    return Px, Py, Pz

def vortex_field_original(x, y, z, t):
    Vx = -y * np.sin(t) * np.cos(z)
    Vy = x * np.sin(t) * np.cos(x)
    Vz = np.cos(z + t) * np.sin(y)
    return Vx, Vy, Vz

def wave_conjugation(x, y, z, t):
    f = resonance_frequency(x, y, z, t)
    return np.sin(f * t) * np.cos(f * t) * np.sin(f * t)

def update_positions_original(points, t):
    updated_points = []
    for x, y, z in points:
        Bx, By, Bz = magnetic_field_original(x, y, z, t)
        Ex, Ey, Ez = electric_field_original(x, y, z, t)
        Px, Py, Pz = solar_radiation_pressure(x, y, z, t)
        Vx, Vy, Vz = vortex_field_original(x, y, z, t)
        Wx = wave_conjugation(x, y, z, t)
        new_x = x + 0.1 * (Bx + Ex + Px + Vx + Wx)
        new_y = y + 0.1 * (By + Ey + Py + Vy + Wx)
        new_z = z + 0.1 * (Bz + Ez + Pz + Vz + Wx)
        updated_points.append((new_x, new_y, new_z))
    return updated_points

# Vortex field simulation functions
def vortex_force(x, y, z, t, vortex_params):
    forces = np.zeros(3)
    for params in vortex_params:
        x0, y0, z0, A, freq, phase = params
        r = np.sqrt((x - x0)**2 + (y - y0)**2 + (z - z0)**2)
        omega = 2 * np.pi * freq
        force_magnitude = A * np.exp(-r) * np.sin(omega * t + phase)
        direction = np.array([x - x0, y - y0, z - z0])
        direction = direction / np.linalg.norm(direction)
        forces += force_magnitude * direction
    return forces

def harmonic_resonance(x, y, z, t, freq=1.0):
    omega = 2 * np.pi * freq
    return np.array([
        np.sin(omega * t) * np.cos(y) * np.sin(z),
        np.cos(omega * t) * np.sin(x) * np.cos(z),
        np.sin(omega * t) * np.cos(x) * np.sin(y)
    ])

def magnetic_field_vortex(x, y, z, t, B0=1e-5):
    r = np.sqrt(x**2 + y**2 + z**2)
    Bx = B0 * (y**2 + z**2) / r**5
    By = B0 * (x**2 + z**2) / r**5
    Bz = B0 * (x**2 + y**2) / r**5
    return np.array([Bx, By, Bz])

def update_positions_vortex(points, t, vortex_params, freq=1.0):
    updated_points = []
    for x, y, z in points:
        Fv = vortex_force(x, y, z, t, vortex_params)
        Hr = harmonic_resonance(x, y, z, t, freq)
        Bx, By, Bz = magnetic_field_vortex(x, y, z, t)
        new_x = x + 0.1 * (Fv[0] + Hr[0] + Bx)
        new_y = y + 0.1 * (Fv[1] + Hr[1] + By)
        new_z = z + 0.1 * (Fv[2] + Hr[2] + Bz)
        updated_points.append((new_x, new_y, new_z))
    return updated_points
