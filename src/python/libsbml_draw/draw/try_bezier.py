# -*- coding: utf-8 -*-

#You avoid most rounding errors by using

#Control1 = (Start + 2 * Control) / 3
#Control2 = (End   + 2 * Control) / 3
#Note that line segments are also convertible to cubic Bezier curves using:

#Control1 = Start
#Control2 = End

# https://stackoverflow.com/questions/50871343/connectionstyle-arc3-fancyarrowpatch-and-path-curve3-two-quadratic-bezier-cu

from matplotlib.patches import Circle, FancyArrowPatch, PathPatch
from matplotlib import pyplot as plt

fig = plt.figure(frameon=False)
ax = fig.add_subplot(111, frameon=False) 

rad = 0.3
shrink = 0

size = 0.1
n1 = Circle([0,0], radius=size, alpha=0., fill=False, linewidth=0.1)
n2 = Circle([1,1], radius=size, alpha=0., fill=False, linewidth=0.1)

ax.add_patch(n1)
ax.add_patch(n2)

print("n1.center: ", n1.center, "type: ", type(n1.center))

e = FancyArrowPatch(n1.center, n2.center, 
                    connectionstyle="arc3, rad=%s" % rad,
                    arrowstyle="-|>",
                    clip_on=False,
                    linewidth=2.,
                    mutation_scale=100
                    )

ax.add_patch(e)

# Calculate Distance
#import math  
#def calculateDistance(x1,y1,x2,y2):  
#     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
#     return dist  
#print calculateDistance(x1, y1, x2, y2)  
import numpy

vs = numpy.asarray(n1.center)
ve = numpy.asarray(n2.center)

vD=ve-vs
vp=numpy.asarray([vD[1], -vD[0]])

vc = vs+0.5*vD+rad*vp

print("vs: ", vs, "type: ", type(vs))
print(ve)
print(vD)
print(vp)
print(vc)

from matplotlib.path import Path

pp1 = PathPatch(Path([vs, vc, ve],
                     [Path.MOVETO, Path.CURVE3, Path.CURVE3]),
                color="red",
                transform=ax.transData,
                fc="None"
               )

ax.add_patch(pp1)



