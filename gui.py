import tkinter as tk
from tkinter import simpledialog
import numpy as np
from mayavi import mlab
from field_simulation import update_positions_with_conjugation
from geometry import flower_of_life_3d, add_sacred_geometry
from visualization import plot_flower_of_life_with_elements

def run_simulation(radius, layers, t_steps):
    points = flower_of_life_3d(radius, layers)
    points = add_sacred_geometry(points, radius, layers)
    
    for t in np.linspace(0, 2*np.pi, t_steps):
        updated_points = update_positions_with_conjugation(points, t)
        plot_flower_of_life_with_elements(updated_points)

def get_user_input():
    root = tk.Tk()
    root.withdraw()

    radius = simpledialog.askfloat("Input", "Enter the radius for the Flower of Life pattern:")
    layers = simpledialog.askinteger("Input", "Enter the number of layers:")
    t_steps = simpledialog.askinteger("Input", "Enter the number of time steps:")
    
    run_simulation(radius, layers, t_steps)

if __name__ == "__main__":
    get_user_input()
