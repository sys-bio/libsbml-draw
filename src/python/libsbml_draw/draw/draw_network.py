"""
Draw the SBML model's network which consists of nodes and reactions.
"""
import numpy as np
from matplotlib.patches import BoxStyle, FancyArrowPatch, FancyBboxPatch
from matplotlib.path import Path
from matplotlib import pyplot as plt


def draw_nodes(nodes):
    """Create a list of FancyBbox Patches, one for each node
    """
    node_patches = []

    for node in nodes:

        fbbp = FancyBboxPatch(
            node.lower_left_point,
            node.width,
            node.height,
            edgecolor=node.edge_color,
            facecolor=node.fill_color,
            boxstyle=BoxStyle("round", pad=0.2, rounding_size=.6),
            mutation_scale=10)

        node_patches.append(fbbp)

    return node_patches


def draw_edges(edges):
    """Create a list of FancyArrow Patches, one for each edge
    """
    edge_patches = []

    for edge in edges:

        curves = edge.curves

        for curve in curves:

            start_point = np.array([curve.start_point.x, curve.start_point.y])
            end_point = np.array([curve.end_point.x, curve.end_point.y])
            control_point_1 = np.array([curve.control_point_1.x,
                                        curve.control_point_1.y])
            control_point_2 = np.array([curve.control_point_2.x,
                                        curve.control_point_2.y])

            cubic_bezier_curve_path = Path(
                    [start_point,
                     control_point_1,
                     control_point_2,
                     end_point],
                    [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4])

        # print("bezier_path: ", cubic_bezier_curve_path)

            fap = FancyArrowPatch(facecolor=edge.fill_color,
                                  edgecolor=edge.edge_color,
                                  arrowstyle=curve.curveArrowStyle,
                                  clip_on=False,
                                  linewidth=edge.curve_width,                                  
                                  mutation_scale=15,
                                  path=cubic_bezier_curve_path
                                  )

            edge_patches.append(fap)

    return edge_patches


def add_labels(nodes):
    for node in nodes:
        plt.text(node.center.x,
                 node.center.y,
                 node.name,
                 fontsize=node.font_size,
                 # fontsize="xx-small",
                 color=node.font_color,
                 fontname=node.font_name,
                 fontstyle=node.font_style,
                 horizontalalignment="center",
                 verticalalignment="center")


def createNetworkFigure(network):
    # initialize figure
    fig = plt.figure()
    ax = plt.gca()

    print("drawing the nodes")
    # draw the nodes
    node_patches = draw_nodes(network.nodes.values())
    for node_patch in node_patches:
        ax.add_patch(node_patch)

    print("drawing the edges")
    # draw the edges
    print(len(network.edges), "nw edges")
    edge_patches = draw_edges(network.edges.values())
    print(len(edge_patches), " edge patches")
    for edge_patch in edge_patches:
        ax.add_patch(edge_patch)

    print("adding the labels")
    # add labels
    add_labels(network.nodes.values())
    print("finishing plot")
    # No axes and size it just bigger than the data (i.e. tight)
    plt.axis("off")
    plt.axis("tight")
    plt.axis("equal")

    plt.show()

    return fig
