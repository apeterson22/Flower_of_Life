import numpy as np

def flower_of_life_3d(radius, layers):
    points = []
    for i in range(-layers, layers+1):
        for j in range(-layers, layers+1):
            for k in range(-layers, layers+1):
                if (i**2 + j**2 + k**2) <= layers**2:  # Create a spherical boundary
                    x = i * radius * np.sqrt(3)
                    y = j * radius * np.sqrt(3)
                    z = k * radius * np.sqrt(3)
                    points.append((x, y, z))
    return points
