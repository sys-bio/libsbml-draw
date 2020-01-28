#import numpy as np
#from matplotlib.patches import BoxStyle, FancyArrowPatch, FancyBboxPatch
from matplotlib.path import Path
from matplotlib import pyplot as plt

from matplotlib.patches import RegularPolygon, Ellipse, PathPatch
from matplotlib.collections import PatchCollection

fig, ax = plt.subplots()

ax.set_facecolor("#ff000010")
fig.set_facecolor("#0000ff10")
                       
patches = []

# add a Polygon
polygon = RegularPolygon((0,0), 5, 0.1)
patches.append(polygon)

# add an Ellipse
ellipse = Ellipse((1,0), 0.2, 0.1)
patches.append(ellipse)

# add a path patch
path_data = [
    (Path.MOVETO, [0.018, -0.11]),
    (Path.CURVE4, [-0.031, -0.051]),
    (Path.CURVE4, [-0.115, 0.073]),
    (Path.CURVE4, [-0.03, 0.073]),
    (Path.LINETO, [-0.011, 0.039]),
    (Path.CURVE4, [0.043, 0.121]),
    (Path.CURVE4, [0.075, -0.005]),
    (Path.CURVE4, [0.035, -0.027]),
    (Path.CLOSEPOLY, [0.018, -0.11])]

#cubic_bezier_curve_path = Path(
#                    [start_point,
#                     control_point_1,
#                     control_point_2,
#                     end_point],
#                    [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4])

codes, verts = zip(*path_data)

print("codes: ", type(codes), codes)
print("verts: ", type(verts), verts)
print("type zip path: ", type(path_data), len(path_data))

path = Path(verts, codes)

patch = PathPatch(path)

patches.append(patch)

collection = PatchCollection(patches, cmap=plt.cm.hsv, alpha=0.3)

ax.add_collection(collection)

#ax.set_axis_bgcolor("#ff000030")

plt.axis('equal')
plt.axis('off')

plt.show()

# regular polygon: center, number of points, distance from center to each point
# ellipse: center, width, height
# 
  

