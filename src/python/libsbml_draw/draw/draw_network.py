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
            boxstyle=BoxStyle("circle", pad=0.02))

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
            control_point_1 = np.array([curve.control_point_1.x, curve.control_point_1.y])
            control_point_2 = np.array([curve.control_point_2.x, curve.control_point_2.y])
    
            cubic_bezier_curve_path = Path(
                    [start_point, 
                     control_point_1, 
                     control_point_2, 
                     end_point],
                    [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4])

        #print("bezier_path: ", cubic_bezier_curve_path)

            fap = FancyArrowPatch(path=cubic_bezier_curve_path, 
                    arrowstyle=curve.curveArrowStyle,
                    clip_on=False,
                    linewidth=1,
                    color="red",
                    mutation_scale=10
                   )

            edge_patches.append(fap)

    return edge_patches


def add_labels(nodes):
    for node in nodes:
        width_shift = node.width/4
        height_shift = node.height/4
        plt.text(node.center.x-width_shift, 
                 node.center.y-height_shift, 
                 node.name,
                 fontsize="xx-small",
                 color="black")


def createNetworkFigure(network):
    # initialize figure
    fig = plt.figure()
    ax = plt.gca()

    print("drawing the nodes")
    # draw the nodes
    node_patches = draw_nodes(network.nodes)
    for node_patch in node_patches:
        ax.add_patch(node_patch)

    print("drawing the edges")
    # draw the edges
    print(len(network.edges), "nw edges")
    edge_patches = draw_edges(network.edges)
    print(len(edge_patches), " edge patches")
    for edge_patch in edge_patches:
        ax.add_patch(edge_patch)

    print("adding the labels")
    # add labels
    add_labels(network.nodes)
    
    # No axes and size it just bigger than the data (i.e. tight)
    plt.axis("off")
    plt.axis("tight")
    plt.axis("equal")

    plt.show()

    return fig

