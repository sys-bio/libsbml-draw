import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
x_tail = 0.1
y_tail = 0.1
x_head = 0.9
y_head = 0.9
dx = x_head - x_tail
dy = y_head - y_tail

fig, axs = plt.subplots(nrows=2)
arrow = mpatches.FancyArrowPatch((x_tail, y_tail), (dx, dy),
                                 mutation_scale=100)
axs[0].add_patch(arrow)

arrow = mpatches.FancyArrowPatch((x_tail, y_tail), (dx, dy),
                                 mutation_scale=100, 
                                 facecolor="orange", 
                                 edgecolor="green")
axs[1].add_patch(arrow)
axs[1].set_xlim(0, 2)
axs[1].set_ylim(0, 2)

