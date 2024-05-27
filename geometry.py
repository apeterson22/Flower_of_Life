import numpy as np

def flower_of_life_3d(radius, layers):
    points = []
    for i in range(layers):
        for j in range(layers):
            for k in range(layers):
                x = radius * (i - layers / 2)
                y = radius * (j - layers / 2)
                z = radius * (k - layers / 2)
                points.append((x, y, z))
    return points

def add_sacred_geometry(points, radius, layers):
    # Adding spheres and other geometrical shapes
    theta = np.linspace(0, 2*np.pi, 100)
    phi = np.linspace(0, np.pi, 100)
    theta, phi = np.meshgrid(theta, phi)
    for i in range(layers):
        r = radius * (i + 1)
        x = r * np.sin(phi) * np.cos(theta)
        y = r * np.sin(phi) * np.sin(theta)
        z = r * np.cos(phi)
        points.extend(list(zip(x.flatten(), y.flatten(), z.flatten())))
    return points
