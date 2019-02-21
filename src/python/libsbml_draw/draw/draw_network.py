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
    
        lower_left_point = node.lower_left_point
        width = node.width
        height = node.height
    
        fbbp = FancyBboxPatch(
            lower_left_point, 
            width, 
            height,
            boxstyle=BoxStyle("Round", pad=0.02))

        node_patches.append(fbbp)  
       
    return node_patches


def draw_edges(edges):
    """Create a list of FancyArrow Patches, one for each edge
    """
    edge_patches = []

    for edge in edge_patches:
    
        start_point = np.array(edge.start_point)
        end_point = np.array(edge.end_point)
        control_point_1 = np.array(edge.control_point_1)
        control_point_2 = np.array(edge.control_point_2)
    
        cubic_bezier_curve_path = Path(
                [start_point, 
                 control_point_1, 
                 control_point_2, 
                 end_point],
                [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4])

        fap = FancyArrowPatch(path=cubic_bezier_curve_path, 
                    arrowstyle="-|>",
                    clip_on=False,
                    linewidth=3,
                    color="red",
                    mutation_scale=100
                   )

        edge_patches.append(fap)

    return edge_patches


def createGraph(network):
    # initialize figure
    fig = plt.figure()
    ax = plt.gca()

    # draw the nodes
    node_patches = draw_nodes(network.nodes)
    for node_patch in node_patches:
        ax.add_patch(node_patch)

    # draw the edges
    edge_patches = draw_edges(network.edges)
    for edge_patch in edge_patches:
        ax.add_patch(edge_patch)

    # add labels

    # No axes and size it just bigger than the data (i.e. tight)
    plt.axis("off")
    plt.axis("tight")

    plt.show()

    return fig

