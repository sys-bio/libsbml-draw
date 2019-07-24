"""
Draw the SBML model's network which consists of nodes and reactions.
"""
import numpy as np
from matplotlib.patches import BoxStyle, Ellipse, FancyArrowPatch, FancyBboxPatch, PathPatch, Polygon
from matplotlib.path import Path
from matplotlib import pyplot as plt


WIDTH_SHIFT = .25
HEIGHT_SHIFT = .25

INCHES_PER_POINT = 1/72

# without this, the image will get cut-off in the iPython Console
try:
    __IPYTHON__
    from IPython import get_ipython
    ipython = get_ipython()
    ipython.magic(
            "config InlineBackend.print_figure_kwargs = {'bbox_inches':None}")
except (NameError, ImportError):
    pass


def draw_compartments(compartments, fig, scaling_factor, nw_height_inches):
    """Create a list of FancyBbox Patches, one for each compartment.

    Args:
        compartments (iterable collection of Compartment): collection of
            compartments
        fig (matplotlib.figure.Figure): the figure of the network
        scaling_factor (float): scaling_factor to decrease or increase the
            figure size

    Returns: list of matplotlib.patches.FancyBboxPatch
    """
    compartment_patches = []

    for compartment in compartments:

        fbbp = FancyBboxPatch(
            [scaling_factor*compartment.lower_left_point[0]*INCHES_PER_POINT +
             WIDTH_SHIFT,
             scaling_factor*(nw_height_inches - 
             compartment.lower_left_point[1]*INCHES_PER_POINT -
             compartment.height*INCHES_PER_POINT) +
             HEIGHT_SHIFT],
            scaling_factor*compartment.width*INCHES_PER_POINT,
            scaling_factor*compartment.height*INCHES_PER_POINT,
            edgecolor=compartment.edge_color,
            facecolor=compartment.fill_color,
            linewidth=compartment.line_width,
            boxstyle=BoxStyle("round", pad=0, rounding_size=0.6),
            transform=fig.dpi_scale_trans)

        compartment_patches.append(fbbp)

    return compartment_patches


def draw_nodes(nodes, fig, scaling_factor, nw_height_inches):
    """Create a list of FancyBbox Patches, one for each node.

    Args:
        nodes (iterable collection of Node): collection of nodes
        fig (matplotlib.figure.Figure): the figure of the network
        scaling_factor (float): scaling_factor to decrease or increase the
            figure size

    Returns: list of matplotlib.patches.FancyBboxPatch
    """

    node_patches = []

    for node in nodes:
        
        print("node shape: ", node.shape)
        print("rect rounding: ", node.rectangle_rounding)

        if node.shape =="round_box" or node.shape == "polygon_pause":
        
            node_patch = FancyBboxPatch(
                [scaling_factor*node.lower_left_point[0]*INCHES_PER_POINT +
                 WIDTH_SHIFT,
                 scaling_factor*(nw_height_inches - 
                 node.lower_left_point[1]*INCHES_PER_POINT -
                 node.height*INCHES_PER_POINT) + HEIGHT_SHIFT],
                scaling_factor*node.width*INCHES_PER_POINT,
                scaling_factor*node.height*INCHES_PER_POINT,
                edgecolor=node.edge_color,
                facecolor=node.fill_color,
                linewidth=node.edge_width,
                boxstyle=BoxStyle("round",
                              pad=0,
                              rounding_size=node.rectangle_rounding),
                transform=fig.dpi_scale_trans
                )

        elif node.shape == "ellipse":
            
            node_patch = Ellipse(
                    (scaling_factor*node.center.x*INCHES_PER_POINT + WIDTH_SHIFT, 
                     scaling_factor*(nw_height_inches - node.center.y*INCHES_PER_POINT) + HEIGHT_SHIFT), 
                     scaling_factor*node.width*INCHES_PER_POINT, 
                     scaling_factor*node.height*INCHES_PER_POINT,
                     edgecolor=node.edge_color,
                     facecolor=node.fill_color,
                     linewidth=node.edge_width,
                     transform=fig.dpi_scale_trans
                    )

        elif node.shape == "polygon":

            node_points = _adjust_x_and_y_values(node.polygon_points, scaling_factor, nw_height_inches, node)

            node_points = np.array(node_points)

            print("type node_points: ", type(node_points), node_points.shape)
            
            # need to adjust the y's
            path = Path(node_points, node.polygon_codes)

            node_patch = PathPatch(
                    path, 
                    facecolor=node.fill_color, 
                    edgecolor=node.edge_color,
                    linewidth=node.edge_width,
                    transform=fig.dpi_scale_trans
                )
        else:
            pass

        node_patches.append(node_patch)

    return node_patches

def _adjust_x_and_y_values(node_points, scaling_factor, nw_height_inches, node):
    """ """
    adjusted_node_points = []    

    for node_point in node_points:

        # x
        x = node_point[0] + node.lower_left_point[0]
        x = scaling_factor*x*INCHES_PER_POINT + WIDTH_SHIFT

        # y
        y = node_point[1] + node.lower_left_point[1]
        y = scaling_factor*(nw_height_inches - y*INCHES_PER_POINT) + HEIGHT_SHIFT    

        adjusted_node_points.append([x, y])
        
    return adjusted_node_points    

def _adjust_arrowhead_x_and_y_values(path_points, scaling_factor, nw_height_inches, center_point):
    """ """
    adjusted_points = []    

    print("nw height inches: ", nw_height_inches)

    for point in path_points:
           
        print("point x, y: ", point[0], point[1])

        # x
        x = point[0] + center_point.x
        x = scaling_factor*x*INCHES_PER_POINT + WIDTH_SHIFT

        # y
        y = point[1] + center_point.y
        y = scaling_factor*(nw_height_inches - y*INCHES_PER_POINT) + HEIGHT_SHIFT    

        print("adj point x, y: ", x, y)

        adjusted_points.append([x, y])
        
    return np.array(adjusted_points)    
    
def draw_reactions(reactions, mutation_scale, fig, scaling_factor, nw_height_inches, line_endings):
    """Create a list of FancyArrow Patches, one for each curve in a reaction.

    Args:
        reactions (iterable collection of Reaction): collection of reactions
        fig (matplotlib.figure.Figure): the figure of the network
        scaling_factor (float): scaling_factor to decrease or increase the
            figure size

    Returns: list of matplotlib.patches.FancyArrowPatch
    """
    reaction_patches = []

    for reaction in reactions:

        curves = reaction.curves

        for curve in curves:

            start_point = np.array([
                    scaling_factor*curve.start_point.x*INCHES_PER_POINT +
                    WIDTH_SHIFT,
                    scaling_factor*(nw_height_inches - curve.start_point.y*INCHES_PER_POINT) +
                    HEIGHT_SHIFT])
            end_point = np.array([
                    scaling_factor*curve.end_point.x*INCHES_PER_POINT +
                    WIDTH_SHIFT,
                    scaling_factor*(nw_height_inches - curve.end_point.y*INCHES_PER_POINT) +
                    HEIGHT_SHIFT])
            control_point_1 = np.array([
                    scaling_factor*curve.control_point_1.x*INCHES_PER_POINT +
                    WIDTH_SHIFT,
                    scaling_factor*(nw_height_inches - curve.control_point_1.y*INCHES_PER_POINT) +
                    HEIGHT_SHIFT])
            control_point_2 = np.array([
                    scaling_factor*curve.control_point_2.x*INCHES_PER_POINT +
                    WIDTH_SHIFT,
                    scaling_factor*(nw_height_inches - curve.control_point_2.y*INCHES_PER_POINT) +
                    HEIGHT_SHIFT])

            cubic_bezier_curve_path = Path(
                    [start_point,
                     control_point_1,
                     control_point_2,
                     end_point],
                    [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4])

            fap = FancyArrowPatch(
                    facecolor=curve.fill_color,
                    edgecolor=curve.edge_color,
                    arrowstyle=curve.curveArrowStyle,
                    clip_on=False,
                    linewidth=curve.curve_width,
                    mutation_scale=mutation_scale.get(curve.role, 10),
                    path=cubic_bezier_curve_path,
                    transform=fig.dpi_scale_trans
                    )

            reaction_patches.append(fap)

            if curve.role_name.lower() == "product":
                if "product" in line_endings:
                    arrow_path = line_endings["product"]   

                    print("arrow path type: ", type(arrow_path))
                    print("curve end point: ", curve.end_point.x, curve.end_point.y)

                    adjusted_arrow_path = _adjust_arrowhead_x_and_y_values(arrow_path, scaling_factor, nw_height_inches, curve.end_point)

                    print("adj arrow path: ", type(adjusted_arrow_path), adjusted_arrow_path)

                    arrow_patch = Polygon(
                            adjusted_arrow_path, edgecolor=curve.edge_color, 
                            facecolor=curve.fill_color, lw=1,
                            transform=fig.dpi_scale_trans) 

#                    codes = [Path.MOVETO, Path.LINETO, Path.LINETO, Path.LINETO, Path.LINETO]

#                    arrow_patch = PathPatch(Path(adjusted_arrow_path, codes), edgecolor="black", facecolor="black", lw=1, transform=fig.dpi_scale_trans)

                    reaction_patches.append(arrow_patch)

    return reaction_patches


def add_labels(nodes, fig, scaling_factor, nw_height_inches):
    """Add text to the nodes.

    Args:
        nodes (iterable collection of Node): collection of nodes
        fig (matplotlib.figure.Figure): the figure of the network
        scaling_factor (float): scaling_factor to decrease or increase the
            figure size

    Returns: None
    """
    for node in nodes:
        plt.text(scaling_factor*node.center.x*INCHES_PER_POINT + WIDTH_SHIFT,
                 scaling_factor*(nw_height_inches - node.center.y*INCHES_PER_POINT) + HEIGHT_SHIFT,
                 node.name,
                 fontsize=scaling_factor*node.font_size,
                 color=node.font_color,
                 fontname=node.font_family,
                 fontstyle=node.font_style,
                 horizontalalignment=node.text_anchor,
                 verticalalignment=node.vtext_anchor,
                 transform=fig.dpi_scale_trans)


def get_network_dimensions(sbml_layout):
    """Compute the plotting width and height in inches needed for the given
       network.

    Args:
        sbml_layout (libsbml_draw.model.SBMLlayout): the SBML model

    Returns: tuple (float, float) of the (width, height)
    """
    nodes = sbml_layout._SBMLlayout__network.nodes.values()
    reactions = sbml_layout._SBMLlayout__network.reactions.values()
    compartments = sbml_layout._SBMLlayout__network.compartments.values()

    max_x_nodes = max([node.center.x + node.width/2 for node in nodes])

    max_x_curves = max([max(
                        curve.start_point.x,
                        curve.end_point.x,
                        curve.control_point_1.x,
                        curve.control_point_2.x)
                        for reaction in reactions
                        for curve in reaction.curves])

    max_y_nodes = max([node.center.y + node.height/2 for node in nodes])

    max_y_curves = max([max(curve.start_point.y,
                        curve.end_point.y,
                        curve.control_point_1.y,
                        curve.control_point_2.y)
                        for reaction in reactions
                        for curve in reaction.curves])

    if compartments:

        max_x_compartments = max([compartment.max_corner.x
                                  for compartment in compartments])
        max_y_compartments = max([compartment.max_corner.y
                                  for compartment in compartments])

        nw_width_points = max(max_x_nodes, max_x_curves, max_x_compartments)
        nw_height_points = max(max_y_nodes, max_y_curves, max_y_compartments)

    else:
        nw_width_points = max(max_x_nodes, max_x_curves)
        nw_height_points = max(max_y_nodes, max_y_curves)

    nw_width_inches = nw_width_points*INCHES_PER_POINT
    nw_height_inches = nw_height_points*INCHES_PER_POINT

    return (nw_width_inches, nw_height_inches)


def createNetworkFigure(sbml_layout, arrowhead_mutation_scale,
                        show=True, dpi=72, width_shift=.25, height_shift=.25,
                        scaling_factor=1):
    """Creates the figure, draws any compartments, draws the nodes,
    draws the reactions, adds text to the nodes.

    Args:
        sbml_layout (libsbml_draw.model.SBMLlayout): the SBML model
        arrowhead_mutation_scale (dict): keys are roles (int), values are for
            matplotlib's FancyArrowPatch mutation_scale parameter
        show (optional, bool): displays the figure if True
        dpi (int): dots-per-inch setting for the figure
        width_shift (optional, float): size in inches of the left and right
            borders
        height_shift (optional, float): size in inches of the bottom and
            top borders
        scaling_factor (option, float): decrease or increase the size of the
            figure using this factor; example, 0.5 results in reducing the
            figure size by one-half

    Returns: matplotlib.figure.Figure
    """

    (nw_width_inches, nw_height_inches) = get_network_dimensions(sbml_layout)

    fig_width_inches = nw_width_inches + 2*WIDTH_SHIFT
    fig_height_inches = nw_height_inches + 2*HEIGHT_SHIFT

    figsize = (scaling_factor*fig_width_inches,
               scaling_factor*fig_height_inches)

    fig = plt.figure(figsize=figsize, dpi=dpi)
    ax = plt.gca()
    
    fig.add_axes(ax)
    # create a figure without any margins
    fig.subplots_adjust(0, 0, 1, 1)

    network = sbml_layout._SBMLlayout__network

    fig.set_facecolor(network.bg_color)

    # draw the compartments
    compartment_patches = draw_compartments(
            network.compartments.values(), fig, scaling_factor, nw_height_inches)

    for compartment_patch in compartment_patches:
        ax.add_patch(compartment_patch)

    # draw the reactions
    reaction_patches = draw_reactions(
            network.reactions.values(),
            arrowhead_mutation_scale, fig, scaling_factor, nw_height_inches, network.line_endings)
    for reaction_patch in reaction_patches:
        ax.add_patch(reaction_patch)

    # draw the nodes
    node_patches = draw_nodes(network.nodes.values(), fig, scaling_factor, nw_height_inches)
    for node_patch in node_patches:
        ax.add_patch(node_patch)

    # add labels to the nodes
    add_labels(network.nodes.values(), fig, scaling_factor, nw_height_inches)

    plt.axis("off")
    plt.axis("equal")
#    plt.gca().invert_yaxis()

    if show:
        plt.show()
    else:
        plt.close()

    return fig
