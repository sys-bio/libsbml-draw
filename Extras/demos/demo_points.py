import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots(figsize=(6, 6))


x, y = 10*np.random.rand(2, 1000)


ax.plot(x, y*10., 'go', alpha=0.2)  # plot some libs in libs coordinates


# add a circle in fixed-units
circ = mpatches.Circle((2.5, 2), 1.0, transform=fig.dpi_scale_trans,
                       facecolor='blue', alpha=0.75)


ax.add_patch(circ)


plt.text(2.5, 2, "hello", color="white", fontsize=12, transform=fig.dpi_scale_trans, verticalalignment="center", horizontalalignment="center")

plt.show()

