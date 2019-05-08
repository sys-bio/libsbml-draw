"""
Draw the SBML model's network which consists of nodes and reactions.
"""
import numpy as np
from matplotlib.patches import BoxStyle, FancyArrowPatch, FancyBboxPatch
from matplotlib.path import Path
from matplotlib import pyplot as plt


def get_ratio():
    """
    """
    axes = plt.gca()
    t = axes.transAxes.transform([(0, 0), (1, 1)])
    print("t: ", type(t), ", ", len(t), ", ", t, ", ", t[1,1], ", ", t[0,1])
    print("dpi: ", axes.get_figure().get_dpi())
    ratio = float(axes.get_figure().get_dpi() / (t[1,1] - t[0,1]) / 72.)*100.
    
    return ratio


def draw_compartments(compartments):
    """Create a list of FancyBbox Patches, one for each compartment.

    Args:
        compartments (iterable collection of Compartment): collection of
        compartments

    Returns: list of matplotlib.patches.FancyBboxPatch
    """
    compartment_patches = []

    for compartment in compartments:

        fbbp = FancyBboxPatch(
            compartment.lower_left_point,
            compartment.width,
            compartment.height,
            edgecolor=compartment.edge_color,
            facecolor=compartment.fill_color,
            linewidth=compartment.line_width,
            boxstyle=BoxStyle("round", pad=0.2, rounding_size=.6),
            mutation_scale=10)

        compartment_patches.append(fbbp)

    return compartment_patches


def draw_nodes(nodes, ratio=1):
    """Create a list of FancyBbox Patches, one for each node.

    Args:
        nodes (iterable collection of Node): collection of nodes

    Returns: list of matplotlib.patches.FancyBboxPatch
    """
    node_patches = []
   
    print('ratio', ratio)

    for node in nodes:
        # https://stackoverflow.com/questions/33635439/matplotlib-patch-size-in-points
        #print('node width ', node.width)
        
#        if len(node.name) > 10:
#            node_width = max(0.045*((len(node.name)/2)+1), 0.13)*(node.font_size/20)
#            node_height = 0.20*(node.font_size/20)
#        else: 
#            node_width = max(0.045*(len(node.name)+1), 0.13)*(node.font_size/20)
#            node_height = 0.11*(node.font_size/20)
        
        fbbp = FancyBboxPatch(
            [x*ratio for x in node.lower_left_point],
            node.width*ratio,
            node.height*ratio,
#            node_width,
#            node_height,
            edgecolor=node.edge_color,
            facecolor=node.fill_color,
            boxstyle=BoxStyle("round", pad=0.2, rounding_size=.6),
            mutation_scale=20*ratio)

        node_patches.append(fbbp)

    return node_patches


def draw_reactions(reactions, mutation_scale, ratio=1):
    """Create a list of FancyArrow Patches, one for each curve in a reaction.

    Args:
        reactions (iterable collection of Reaction): collection of reactions

    Returns: list of matplotlib.patches.FancyArrowPatch
    """
    reaction_patches = []

    for reaction in reactions:

        curves = reaction.curves

        for curve in curves:

            start_point = np.array([curve.start_point.x*ratio, 
                                    curve.start_point.y*ratio])
            end_point = np.array([curve.end_point.x*ratio, 
                                  curve.end_point.y*ratio])
            control_point_1 = np.array([curve.control_point_1.x*ratio,
                                        curve.control_point_1.y*ratio])
            control_point_2 = np.array([curve.control_point_2.x*ratio,
                                        curve.control_point_2.y*ratio])

            cubic_bezier_curve_path = Path(
                    [start_point,
                     control_point_1,
                     control_point_2,
                     end_point],
                    [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4])

            fap = FancyArrowPatch(
                    facecolor=reaction.fill_color,
                    edgecolor=reaction.edge_color,
                    arrowstyle=curve.curveArrowStyle,
                    clip_on=False,
                    linewidth=reaction.curve_width,
                    mutation_scale=mutation_scale.get(curve.role, 25),
                    path=cubic_bezier_curve_path
                    )

            reaction_patches.append(fap)

    return reaction_patches


def add_labels(nodes, ratio=1):
    """Add text to the nodes.

    Args:
        nodes (iterable collection of Node): collection of nodes

    Returns: None
    """
    for node in nodes:
        plt.text(node.center.x*ratio,
                 node.center.y*ratio,
                 node.name,
                 fontsize=node.font_size,
                 color=node.font_color,
                 fontname=node.font_family,
                 fontstyle=node.font_style,
                 horizontalalignment="center",
                 verticalalignment="center")


def createNetworkFigure(network, mutation_scale, figure_size=None, show=True):
    """Creates the figure, draws the nodes, draws the reactions, adds text to
    the nodes.

    Args:
        network (libsbml_draw.model.network.Network): the model's network which
            contains Nodes and Reactions.

    Returns: matplotlib.figure.Figure
    """
    
    
    
    # initialize figure
    if figure_size and len(figure_size) == 2: 
        fig = plt.figure(figsize=figure_size)
    else:    
        fig = plt.figure() # figsize=(20,10)

    ax = plt.gca()
    
    ratio = get_ratio()
    #ratio = 1

    # draw the compartments
    compartment_patches = draw_compartments(network.compartments.values())

    for compartment_patch in compartment_patches:
        ax.add_patch(compartment_patch)

    # draw the nodes
    node_patches = draw_nodes(network.nodes.values(), ratio)
    for node_patch in node_patches:
        ax.add_patch(node_patch)

    # draw the reactions
    reaction_patches = draw_reactions(
            network.reactions.values(),
            mutation_scale, ratio)
    for reaction_patch in reaction_patches:
        ax.add_patch(reaction_patch)

    # add labels
    add_labels(network.nodes.values(), ratio)
    # No axes and size it just bigger than the data (i.e. tight)
    plt.axis("off")
    plt.axis("tight")
    plt.axis("equal")

    if show:
        plt.show()
        plt.close()
    else:
        plt.close()

    return fig
