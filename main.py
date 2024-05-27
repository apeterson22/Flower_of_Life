import numpy as np
from geometry import flower_of_life_3d, add_sacred_geometry
from field_simulation import update_positions_with_conjugation
from visualization import plot_flower_of_life_with_elements

# Define parameters
radius = 1.0
layers = 5
points = flower_of_life_3d(radius, layers)
points = add_sacred_geometry(points, radius, layers)

# Plot the Flower of Life pattern with dynamic update and elements
for t in np.linspace(0, 2*np.pi, 100):
    updated_points = update_positions_with_conjugation(points, t)
    plot_flower_of_life_with_elements(updated_points)
