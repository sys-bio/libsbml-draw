import matplotlib.pyplot as plt
from matplotlib.patches import BoxStyle, FancyBboxPatch, FancyArrowPatch
from matplotlib.path import Path

import numpy as np

# Set-up the node libs

node_width_ABCDEFG = 116/72  # inches
node_height_ABCDEFG = 28/72  # inches
node_center_x_ABCDEFG = 0 + 58/72  # inches
node_center_y_ABCDEFG = 3 + 14/72  # inches
lower_left_corner_ABCDEFG = [node_center_x_ABCDEFG - node_width_ABCDEFG/2,
                       node_center_y_ABCDEFG - node_height_ABCDEFG/2]

node_width_F = 28/72  # inches
node_height_F = 28/72  # inches
node_center_x_F = 3 + 14/72  # inches
node_center_y_F = 0 + 14/72  # inches
lower_left_corner_F = [node_center_x_F - node_width_F/2,
                       node_center_y_F - node_height_F/2]

node_width_E = 28/72  # inches
node_height_E = 28/72  # inches
node_center_x_E = 5 + 14/72  # inches
node_center_y_E = 4 + 14/72  # inches
lower_left_corner_E = [node_center_x_E - node_width_E/2,
                       node_center_y_E - node_height_E/2]

node_width_C = 28/72  # inches
node_height_C = 28/72  # inches
node_center_x_C = 2.8 + 14/72  # inches
node_center_y_C = 4.4 + 14/72  # inches
lower_left_corner_C = [node_center_x_C - node_width_C/2,
                       node_center_y_C - node_height_C/2]

# Compute size parameters needed to create the figure

# left edge of box ABCDEFG to right edge of box E
network_width_inches = (
        (node_center_x_E + node_width_E/2) - 
        (node_center_x_ABCDEFG - node_width_ABCDEFG/2))

# top edge of box C to bottom edge of box F
network_height_inches = (
        (node_center_y_C + node_height_C/2) - 
        (node_center_y_F - node_height_F/2))

print("network width inches: ", network_width_inches)
print("network height inches: ", network_height_inches)

#WIDTH_SHIFT = .75  # width of left margin 
#HEIGHT_SHIFT = 0.5  # height of bottom margin

# when these are zero, the node boxes for ABCDEFG and F fall outside the axes
WIDTH_SHIFT = 0  
HEIGHT_SHIFT = 0

PORTION_OF_PLOT_INSIDE_THE_MARGINS = 1

fig_width_inches = network_width_inches/PORTION_OF_PLOT_INSIDE_THE_MARGINS
fig_height_inches = network_height_inches/PORTION_OF_PLOT_INSIDE_THE_MARGINS

# These enlargements are not big enough
# fig_width_inches = network_width_inches + 2*WIDTH_SHIFT
# fig_height_inches = network_height_inches + 2*HEIGHT_SHIFT

print("fig width inches: ", fig_width_inches)
print("fig height inches: ", fig_height_inches)

# Create the figure

fig = plt.figure(figsize=(fig_width_inches, fig_height_inches), dpi=72)

fig.subplots_adjust(0,0,1,1)

ax = plt.gca()

# Plotting in inches

# Create the reactions

start_point = np.array([node_center_x_ABCDEFG, node_center_y_ABCDEFG])

end_point = np.array([node_center_x_ABCDEFG + 1.3, node_center_y_ABCDEFG + .8])
            
control_point_1 = np.array([node_center_x_ABCDEFG + .1, node_center_y_ABCDEFG + .1])

control_point_2 = np.array([node_center_x_ABCDEFG + .2, node_center_y_ABCDEFG + .2])

cubic_bezier_curve_path = Path(
        [start_point,
         control_point_1,
         control_point_2,
         end_point],
         [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4])

fap = FancyArrowPatch(
                    facecolor="black",
                    edgecolor="black",
                    arrowstyle="-|>",
                    clip_on=False,
                    linewidth=2,
                    mutation_scale=15,
                    path=cubic_bezier_curve_path,
                    transform=fig.dpi_scale_trans
                    )


# Create the node boxes

node_patch_ABCDEFG = FancyBboxPatch(
            [lower_left_corner_ABCDEFG[0] + WIDTH_SHIFT, 
             lower_left_corner_ABCDEFG[1] + HEIGHT_SHIFT],
            node_width_ABCDEFG,
            node_height_ABCDEFG,
            edgecolor="blue",
            facecolor="lightblue",
            linewidth=1,
            boxstyle=BoxStyle("round", 
                              pad=0,
                              rounding_size=.1),
            transform=fig.dpi_scale_trans
            )

node_patch_C = FancyBboxPatch(
            [lower_left_corner_C[0] + WIDTH_SHIFT, 
             lower_left_corner_C[1] + HEIGHT_SHIFT],
            node_width_C,
            node_height_C,
            edgecolor="blue",
            facecolor="lightblue",
            linewidth=1,
            boxstyle=BoxStyle("round", 
                              pad=0,
                              rounding_size=.1),
            transform=fig.dpi_scale_trans
            )
            
node_patch_E = FancyBboxPatch(
            [lower_left_corner_E[0] + WIDTH_SHIFT, 
             lower_left_corner_E[1] + HEIGHT_SHIFT],
            node_width_E,
            node_height_E,
            edgecolor="blue",
            facecolor="lightblue",
            linewidth=1,
            boxstyle=BoxStyle("round", 
                              pad=0,
                              rounding_size=.1),
            transform=fig.dpi_scale_trans
            )            

node_patch_F = FancyBboxPatch(
            [lower_left_corner_F[0] + WIDTH_SHIFT, 
             lower_left_corner_F[1] + HEIGHT_SHIFT],
            node_width_F,
            node_height_F,
            edgecolor="blue",
            facecolor="lightblue",
            linewidth=1,
            boxstyle=BoxStyle("round", 
                              pad=0,
                              rounding_size=.1),
            transform=fig.dpi_scale_trans
            )
            
ax.add_patch(fap)            
ax.add_patch(node_patch_ABCDEFG)
ax.add_patch(node_patch_C)
ax.add_patch(node_patch_E)
ax.add_patch(node_patch_F)


# Add text labels for the nodes

plt.text(
        node_center_x_ABCDEFG + WIDTH_SHIFT,
        node_center_y_ABCDEFG + HEIGHT_SHIFT,
        "ABCDEFG",
        fontsize=12,
        color="black",
        fontname="Verdana",
        fontstyle="normal",
        horizontalalignment="center",
        verticalalignment="center",
        transform=fig.dpi_scale_trans
        )

plt.text(
        node_center_x_C + WIDTH_SHIFT,
        node_center_y_C + HEIGHT_SHIFT,
        "C",
        fontsize=12,
        color="black",
        fontname="Verdana",
        fontstyle="normal",
        horizontalalignment="center",
        verticalalignment="center",
        transform=fig.dpi_scale_trans
        )

plt.text(
        node_center_x_E + WIDTH_SHIFT,
        node_center_y_E + HEIGHT_SHIFT,
        "E",
        fontsize=12,
        color="black",
        fontname="Verdana",
        fontstyle="normal",
        horizontalalignment="center",
        verticalalignment="center",
        transform=fig.dpi_scale_trans
        )

plt.text(
        node_center_x_F + WIDTH_SHIFT,
        node_center_y_F + HEIGHT_SHIFT,
        "F",
        fontsize=12,
        color="black",
        fontname="Verdana",
        fontstyle="normal",
        horizontalalignment="center",
        verticalalignment="center",
        transform=fig.dpi_scale_trans
        )
                
plt.axis("equal")

plt.axis("off")

plt.show()

fig.savefig("node_example_subplots_adjust.png")