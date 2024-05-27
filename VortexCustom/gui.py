import tkinter as tk
from tkinter import simpledialog
import numpy as np

def run_simulation(sim_type, t_steps, freq, vortex_params, use_vortex):
    if use_vortex:
        from field_simulation import update_positions_vortex as update_positions_with_conjugation
    else:
        from field_simulation import update_positions_original as update_positions_with_conjugation
    
    from visualization import plot_points_with_elements, plot_flower_of_life_with_elements

    if sim_type == 'flower':
        from common.geometry import flower_of_life_3d, add_sacred_geometry
        radius = simpledialog.askfloat("Input", "Enter the radius for the Flower of Life pattern:")
        layers = simpledialog.askinteger("Input", "Enter the number of layers:")
        points = flower_of_life_3d(radius, layers)
        points = add_sacred_geometry(points, radius, layers)
        for t in np.linspace(0, 2*np.pi, t_steps):
            updated_points = update_positions_with_conjugation(points, t, vortex_params, freq)
            plot_flower_of_life_with_elements(updated_points)
    else:
        points = np.random.rand(100, 3)
        for t in np.linspace(0, 2*np.pi, t_steps):
            updated_points = update_positions_with_conjugation(points, t, vortex_params, freq)
            plot_points_with_elements(updated_points)

def get_user_input():
    root = tk.Tk()
    root.withdraw()

    module_set = simpledialog.askstring("Module Set", "Enter 'original' for original modules or 'vortex' for vortex modules:")
    sim_type = simpledialog.askstring("Simulation Type", "Enter 'flower' for Flower of Life simulation or 'custom' for a custom simulation:")
    t_steps = simpledialog.askinteger("Input", "Enter the number of time steps:")
    freq = simpledialog.askfloat("Input", "Enter the frequency for the simulation:")
    
    use_vortex = (module_set.lower() == 'vortex')

    if sim_type == 'custom':
        vortex_params = [
            (0, 0, 1, 1.0, freq, 0),          # Primary vortex
            (1, -1, 0, 0.8, freq, np.pi/2),   # Secondary vortex 1
            (-1, 1, 0, 0.8, freq, np.pi),     # Secondary vortex 2
            (1, 1, 0, 0.8, freq, 3*np.pi/2)   # Secondary vortex 3
        ]
    else:
        vortex_params = []

    run_simulation(sim_type, t_steps, freq, vortex_params, use_vortex)

if __name__ == "__main__":
    get_user_input()
