import numpy as np
#from matplotlib.patches import BoxStyle, FancyArrowPatch, FancyBboxPatch
from matplotlib.path import Path
from matplotlib import pyplot as plt

from matplotlib.patches import RegularPolygon, Ellipse, PathPatch, Polygon
from matplotlib.collections import PatchCollection

fig, ax = plt.subplots()

# LE
# w=10, h=10
# s0,0												
# e100, 50														
# s100,50
# e0,100
# s 0,100
# e 33,50
# s 33,50
# e 0,0												

arrow1_center = np.array([15,10])
arrow1_points = arrow1_center + np.array([[0,0], [10,5], [10,5], [0,10], [0,10], [3.3,5], [3.3,5], [0,0]])

arrow1_patch = Polygon(arrow1_points, ec="black",fc="black", lw=1)

ax.add_patch(arrow1_patch)


points = []
codes = []
												
# SG
start_point = [20, 0]
end_point = [0, 20]
basePoint1 = [8.95430500338413, 0]
basePoint2 = [0, 8.95430500338413]

points.append(start_point)
points.append(basePoint1)
points.append(basePoint2)
points.append(end_point)

codes.append(Path.MOVETO)
codes.append(Path.CURVE4)
codes.append(Path.CURVE4)
codes.append(Path.CURVE4)

start_point = [0, 20]
end_point = [20, 40]
basePoint1 = [0, 31.0456949966159]
basePoint2 = [8.95430500338413, 40]

points.append(start_point)
points.append(basePoint1)
points.append(basePoint2)
points.append(end_point)

codes.append(Path.LINETO)
codes.append(Path.CURVE4)
codes.append(Path.CURVE4)
codes.append(Path.CURVE4)

start_point =  [20, 40]
end_point = [42, 40]

points.append(start_point)
points.append(end_point)

codes.append(Path.LINETO)
codes.append(Path.LINETO)

start_point = [42, 40]
end_point = [62, 20]
basePoint1 = [53.0456949966159, 40]
basePoint2 = [62, 31.0456949966159]

points.append(start_point)
points.append(basePoint1)
points.append(basePoint2)
points.append(end_point)

codes.append(Path.LINETO)
codes.append(Path.CURVE4)
codes.append(Path.CURVE4)
codes.append(Path.CURVE4)

start_point = [62, 20]
end_point = [42, 0]
basePoint1 = [62, 8.95430500338413]
basePoint2 = [53.0456949966159, 0]

points.append(start_point)
points.append(basePoint1)
points.append(basePoint2)
points.append(end_point)

codes.append(Path.LINETO)
codes.append(Path.CURVE4)
codes.append(Path.CURVE4)
codes.append(Path.CURVE4)

start_point = [42, 0]
end_point = [20, 0]

points.append(start_point)
points.append(end_point)

codes.append(Path.LINETO)
codes.append(Path.LINETO)


print("num points: ", len(points))
print("num codes: ", len(codes))

path = Path(points, codes)
patch = PathPatch(path, facecolor="#0000ff30", edgecolor="#0000ff")
ax.add_patch(patch)
													
plt.axis('equal')
plt.axis('off')											
plt.gca().invert_yaxis()
												
plt.show()





