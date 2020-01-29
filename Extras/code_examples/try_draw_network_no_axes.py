"""
Draw the SBML model's network which consists of nodes and reactions.
"""
import numpy as np
from matplotlib.patches import BoxStyle, FancyArrowPatch, FancyBboxPatch
from matplotlib.path import Path
from matplotlib import pyplot as plt

def createGraph():
    fig = plt.figure()
    ax = plt.gca()

#plt.xlim, plt.ylim
#ax.autoscale()
#ax = fig.add_subplot(111, frameon=False) 

start_point = [0,0]
end_point = [1,1]
control_point_1 = [0.2,0.5]
control_point_2 = [0.8, 0.8]

vs = np.array(start_point)
vc1 = np.array(control_point_1)
vc2 = np.array(control_point_2)
ve = np.array(end_point)

cubic_bezier_curve_path = Path([vs, vc1, vc2, ve],
                               [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4])

fap = FancyArrowPatch(path=cubic_bezier_curve_path, 
                    arrowstyle="-|>",
                    clip_on=False,
                    linewidth=3,
                    color="red",
                    mutation_scale=100
                   )

ax.add_patch(fap)

lower_left_point = [1.6,.2]
width = 0.2
height = 0.2

fbbp = FancyBboxPatch(
        lower_left_point, 
        width, 
        height,
        boxstyle=BoxStyle("Round", pad=0.02))

ax.add_patch(fbbp)

plt.axis("off")
plt.axis("tight")

plt.show()
