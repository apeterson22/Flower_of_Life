from mayavi import mlab
from elements import elements

def plot_flower_of_life_with_elements(points):
    mlab.figure(bgcolor=(1, 1, 1))
    element_keys = list(elements.keys())
    for i, point in enumerate(points):
        x, y, z = point
        element_key = element_keys[i % len(element_keys)]
        element = elements[element_key]
        mlab.points3d(x, y, z, scale_factor=element["size"], color=element["color"], mode='sphere')
    mlab.show()

def plot_points_with_elements(points):
    mlab.figure(bgcolor=(1, 1, 1))
    element_keys = list(elements.keys())
    for i, point in enumerate(points):
        x, y, z = point
        element_key = element_keys[i % len(element_keys)]
        element = elements[element_key]
        mlab.points3d(x, y, z, scale_factor=element["size"], color=element["color"], mode='sphere')
    mlab.show()
