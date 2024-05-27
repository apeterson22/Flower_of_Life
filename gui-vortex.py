import tkinter as tk
from tkinter import simpledialog
import numpy as np
from mayavi import mlab
from field_simulation import update_positions_with_conjugation
from geometry import flower_of_life_3d, add_sacred_geometry
from visualization import plot_flower_of_life_with_elements, plot_points_with_elements

def run_custom_simulation(t_steps, freq, vortex_params):
    points = np.random.rand(100, 3)
    for t in np.linspace(0, 2*np.pi, t_steps):
        updated_points = update_positions_with_conjugation(points, t, vortex_params, freq)
        plot_points_with_elements(updated_points)

def get_user_input():
    root = tk.Tk()
    root.withdraw()

    sim_type = simpledialog.askstring("Simulation Type", "Enter 'flower' for Flower of Life simulation or 'custom' for a custom simulation:")
    t_steps = simpledialog.askinteger("Input", "Enter the number of time steps:")
    freq = simpledialog.askfloat("Input", "Enter the frequency for the simulation:")
    
    if sim_type.lower() == 'flower':
        radius = simpledialog.askfloat("Input", "Enter the radius for the Flower of Life pattern:")
        layers = simpledialog.askinteger("Input", "Enter the number of layers:")
        run_flower_of_life_simulation(radius, layers, t_steps, freq)
    elif sim_type.lower() == 'custom':
        # Example vortex parameters for the Lynchpin configuration
        vortex_params = [
            (0, 0, 1, 1.0, freq, 0),      # Primary vortex
            (1, -1, 0, 0.8, freq, np.pi/2),   # Secondary vortex 1
            (-1, 1, 0, 0.8, freq, np.pi),     # Secondary vortex 2
            (1, 1, 0, 0.8, freq, 3*np.pi/2)   # Secondary vortex 3
        ]
        run_custom_simulation(t_steps, freq, vortex_params)
    else:
        print("Invalid simulation type")

if __name__ == "__main__":
    get_user_input()
