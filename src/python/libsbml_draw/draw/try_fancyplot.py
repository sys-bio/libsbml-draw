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

head = (0,0.2)
tail = (1,1)

arrow_path = Path([(0,0), (.25,.25), (.5,.5)])

fap1 = FancyArrowPatch(head, tail,
                       facecolor="lightblue",
                       linewidth="1",
                       mutation_scale=20)

fap2 = FancyArrowPatch(
                      arrowstyle="-|>",
                      facecolor="red",
                      edgecolor="green",
                      linewidth="3",
                      mutation_scale=30,
                      path=arrow_path
                      )

print("fap2 face edge: ", fap2.get_facecolor(), ", ", fap2.get_edgecolor())

ax.add_patch(fbbp)
ax.add_patch(fap1)
ax.add_patch(fap2)

#plt.show()
