import numpy as np

def vortex_pattern(num_points):
    points = []
    for i in range(num_points):
        angle = 3 * i * (np.pi / 180)  # converting degrees to radians
        radius = i / num_points
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        z = radius * np.sin(3 * angle)  # adding a third dimension
        points.append((x, y, z))
    return points

def flower_of_life_3d(radius, layers):
    points = []
    for layer in range(layers):
        for angle in np.arange(0, 2 * np.pi, np.pi / 6):
            x = radius * layer * np.cos(angle)
            y = radius * layer * np.sin(angle)
            z = 0
            points.append((x, y, z))
            for secondary_angle in np.arange(0, 2 * np.pi, np.pi / 6):
                x2 = x + radius * np.cos(secondary_angle)
                y2 = y + radius * np.sin(secondary_angle)
                points.append((x2, y2, z))
    return points

def metatrons_cube(radius):
    points = []
    angles = [0, 2*np.pi/3, 4*np.pi/3]
    for angle in angles:
        x = radius * np.cos(angle)
        y = radius * np.sin(angle)
        points.append((x, y, 0))
        for angle2 in angles:
            x2 = x + radius * np.cos(angle2)
            y2 = y + radius * np.sin(angle2)
            points.append((x2, y2, 0))
    # Add third dimension points
    for point in points[:]:
        points.append((point[0], point[1], radius))
        points.append((point[0], point[1], -radius))
    return points

def sphere(radius, num_points):
    points = []
    indices = np.arange(0, num_points, dtype=float) + 0.5
    phi = np.arccos(1 - 2*indices/num_points)
    theta = np.pi * (1 + 5**0.5) * indices

    x = radius * np.cos(theta) * np.sin(phi)
    y = radius * np.sin(theta) * np.sin(phi)
    z = radius * np.cos(phi)
    
    points = np.vstack((x, y, z)).T
    return points

def initialize_geometry_pattern(pattern, **kwargs):
    if pattern == 'vortex':
        return vortex_pattern(kwargs.get('num_points', 100))
    elif pattern == 'flower_of_life':
        return flower_of_life_3d(kwargs.get('radius', 1), kwargs.get('layers', 3))
    elif pattern == 'metatrons_cube':
        return metatrons_cube(kwargs.get('radius', 1))
    elif pattern == 'sphere':
        return sphere(kwargs.get('radius', 1), kwargs.get('num_points', 100))
    else:
        raise ValueError("Unknown pattern")
