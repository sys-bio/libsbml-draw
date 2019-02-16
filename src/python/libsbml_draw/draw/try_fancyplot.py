# -*- coding: utf-8 -*-

from matplotlib.patches import FancyArrowPatch, FancyBboxPatch
from matplotlib.path import Path
import matplotlib.pyplot as plt

# initialize figure
fig = plt.figure()
ax = plt.gca()

lower_left_corner = (0,0)
width = .5
height = .25

fbbp = FancyBboxPatch(lower_left_corner, 
                      width, 
                      height,
                      boxstyle="square",
                      color="red",
                      fill=False)

head = (0,0)
tail = (1,1)

arrow_path = Path([(0,0), (.25,.25), (.5,.5)])

fap1 = FancyArrowPatch(head, 
                      tail,
                      arrowstyle="-|>",
                      color="blue",
                      linewidth="5.0")

fap2 = FancyArrowPatch(path=arrow_path,
                      arrowstyle="-|>",
                      color="green",
                      linewidth="5.0")

ax.add_patch(fbbp)
ax.add_patch(fap1)
ax.add_patch(fap2)

#plt.show()
