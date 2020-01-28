"""
Draw the SBML model's network which consists of nodes and reactions.
"""
import numpy as np
from matplotlib.patches import BoxStyle, FancyArrowPatch, FancyBboxPatch
from matplotlib.path import Path
from matplotlib import pyplot as plt

import pathlib
import tempfile

import libsbml

import libsbml_draw.c_api.sbnw_c_api as sbnw

SBNW_NODE_WIDTH = 40
SBNW_NODE_HEIGHT = 20

MARGIN_EFFECT = 1

WIDTH_SHIFT = .25
HEIGHT_SHIFT = .25

try:
    __IPYTHON__
    from IPython import get_ipython
    ipython = get_ipython()
    ipython.magic("config InlineBackend.print_figure_kwargs = {'bbox_inches':None}")
except (NameError,ImportError):
    pass
    

def compute_figure_width_height_in_pixels(fig, ax):
    """Returns the width and height of the figure in pixels.

    Args:
        fig (matplotlib.figure.Figure): current figure
        ax (matplotlib.axes.Axes): current Axes instance

    Returns: tuple (int, int), (width, height)
    """

    fig_bbox = ax.get_window_extent(
            ).transformed(fig.dpi_scale_trans.inverted())

    fig_width_pixels = fig_bbox.width*fig.get_dpi()
    fig_height_pixels = fig_bbox.height*fig.get_dpi()

    return (fig_width_pixels, fig_height_pixels)


def compute_node_dimensions(text_length_points, text_height_points, fig_dpi,
                            fig_width_pixels, fig_height_pixels,
                            network_width_data_coords,
                            network_height_data_coords):
    """Returns the width and height needed in data coordinates for the text to
    fit inside the node given the figure dpi, figure size, and network size.

    Args:
        text_length_points (int): length of the node text in units of points
        text_height_points (int): height of the node text in units of points
        fig_dpi (int): the dots-per-inch setting for the figure
        fig_width_pixels (int): width of the figure in pixels
        fig_height_pixels (int): height of the figure in pixels
        network_width_data_coords (int): width of the network graph in data
            coordinates
        netowrk_height_data_coords (int): height of the network graph in data
            coordinates

    Returns: tuple (width, height)
        width (float): width of the node box in data coordinates
        height (float): height of node box in data coordinates
    """

    text_length_pixels = fig_dpi*text_length_points/72  # 1/72 inches per point

    text_height_pixels = fig_dpi*text_height_points/72  # 1/71

    network_width_to_height_ratio = (
            network_width_data_coords/network_height_data_coords)

    # horizontal figure, uses all the width available, not all of the height
    if network_width_to_height_ratio > 1:

        width = text_length_pixels*network_width_data_coords/fig_width_pixels

        used_fig_height_pixels = fig_width_pixels/network_width_to_height_ratio

        height = (text_height_pixels *
                  network_height_data_coords/used_fig_height_pixels)

    else:  # vertical figure, uses all the height available, not all the width

        used_fig_width_pixels = fig_height_pixels*network_width_to_height_ratio

        width = (text_length_pixels *
                 network_width_data_coords/used_fig_width_pixels)

        height = (text_height_pixels *
                  network_height_data_coords/fig_height_pixels)

    return (width, height)


def draw_compartments(compartments, fig, sf):
    """Create a list of FancyBbox Patches, one for each compartment.

    Args:
        compartments (iterable collection of Compartment): collection of
        compartments

    Returns: list of matplotlib.patches.FancyBboxPatch
    """
    compartment_patches = []

    for compartment in compartments:

        fbbp = FancyBboxPatch(
#            compartment.lower_left_point,
            [sf*compartment.lower_left_point[0]/72 + WIDTH_SHIFT, 
             sf*compartment.lower_left_point[1]/72 + HEIGHT_SHIFT],
            sf*compartment.width/72,
            sf*compartment.height/72,
            edgecolor=compartment.edge_color,
            facecolor=compartment.fill_color,
            linewidth=compartment.line_width,
            boxstyle=BoxStyle("round", pad=0, rounding_size=.6),
#            mutation_scale=10,
            transform=fig.dpi_scale_trans)

        compartment_patches.append(fbbp)

    return compartment_patches


def draw_nodes(nodes, node_padding, node_mutation_scale, fig, sf):
    """Create a list of FancyBbox Patches, one for each node.

    Args:
        nodes (iterable collection of _Node): collection of nodes

    Returns: list of matplotlib.patches.FancyBboxPatch
    """

    node_patches = []

    print("WIDTH_SHIFT, HEIGHT_SHIFT: ", WIDTH_SHIFT, HEIGHT_SHIFT)

    for node in nodes:

#        width = len(node.name)*node.font_size/72
#        height = node.font_size/72
#        node_center_x = node.center.x/72 + .5
#        node_center_y = node.center.y/72 + .5       
#        lower_left_point_x = node_center_x - node.width/2
#        lower_left_point_y = node_center_y - node.height/2
                
        fbbp = FancyBboxPatch(
#            node.lower_left_point,
#            node.width,
#            node.height,
            [sf*node.lower_left_point[0]/72 + WIDTH_SHIFT, 
             sf*node.lower_left_point[1]/72 + HEIGHT_SHIFT],
            sf*node.width/72,
            sf*node.height/72,
            edgecolor=node.edge_color,
            facecolor=node.fill_color,
            linewidth=node.edge_width,
            boxstyle=BoxStyle("round", 
                              pad=0,
#                              pad=node_padding if node_padding else 0.1,
                              rounding_size=.1),
#            mutation_scale=node_mutation_scale if node_mutation_scale else 1,
            transform=fig.dpi_scale_trans
            )

        node_patches.append(fbbp)

    return node_patches


def draw_reactions(reactions, mutation_scale, fig, sf):
    """Create a list of FancyArrow Patches, one for each curve in a reaction.

    Args:
        reactions (iterable collection of Reaction): collection of reactions

    Returns: list of matplotlib.patches.FancyArrowPatch
    """
    reaction_patches = []

    for reaction in reactions:

        curves = reaction.curves

        for curve in curves:

            start_point = np.array([sf*curve.start_point.x/72 + WIDTH_SHIFT,
                                    sf*curve.start_point.y/72 + HEIGHT_SHIFT])
            end_point = np.array([sf*curve.end_point.x/72 + WIDTH_SHIFT,
                                  sf*curve.end_point.y/72 + HEIGHT_SHIFT])
            control_point_1 = np.array([sf*curve.control_point_1.x/72 + WIDTH_SHIFT,
                                        sf*curve.control_point_1.y/72 + HEIGHT_SHIFT])
            control_point_2 = np.array([sf*curve.control_point_2.x/72 + WIDTH_SHIFT,
                                        sf*curve.control_point_2.y/72 + HEIGHT_SHIFT])

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
                    mutation_scale=mutation_scale.get(curve.role, 10),
                    path=cubic_bezier_curve_path,
                    transform=fig.dpi_scale_trans
                    )

            reaction_patches.append(fap)

    return reaction_patches


def add_labels(nodes, fig, sf):
    """Add text to the nodes.

    Args:
        nodes (iterable collection of _Node): collection of nodes

    Returns: None
    """
    for node in nodes:
        plt.text(sf*node.center.x/72 + WIDTH_SHIFT,
                 sf*node.center.y/72 + HEIGHT_SHIFT,
                 node.name,
                 fontsize=sf*node.font_size,
                 color=node.font_color,
                 fontname=node.font_family,
                 fontstyle=node.font_style,
                 horizontalalignment="center",
                 verticalalignment="center",
                 transform=fig.dpi_scale_trans)
#                 )

def update_node_dimensions(sbml_layout, fig_dpi, fig_width_pixels,
                           fig_height_pixels, node_multiplier=1.0):
    """Increase the size of the node boxes, if necessary, to fit the text.

    Args:
        sbml_layout (libsbml_draw.model.SBMLlayout): current SBML model
        fig_dpi (int): dots-per-inch setting for the figure
        fig_width_pixels (int): width of the figure in pixels
        fig_height_pixels (int): height of the figure in pixels
        node_multiplier (optional, float): multiplier to achieve a width of
                the node box beyond what's needed for the text itself, eg. 1.1
                represents an extra 10%

    Returns: None
    """
    nodes = sbml_layout._SBMLlayout__network.nodes.values()

    nw_width_data_coords = (
            max([node.center.x for node in nodes]) -
            min([node.center.x for node in nodes])) + SBNW_NODE_WIDTH

    nw_height_data_coords = (
            max([node.center.y for node in nodes]) -
            min([node.center.y for node in nodes])) + SBNW_NODE_HEIGHT

    for node in nodes:

        width, height = compute_node_dimensions(
            node_multiplier*(len(node.name)+0)*node.font_size,
            node_multiplier*(node.font_size+0),
            fig_dpi, fig_width_pixels, fig_height_pixels,
            nw_width_data_coords, nw_height_data_coords)

        h_node_id = node.id.encode('utf-8')
        h_node = sbnw.nw_getNodepFromId(sbml_layout._SBMLlayout__h_network,
                                        h_node_id)

        sbnw.node_setWidth(h_node, width)
        node.width = width

        sbnw.node_setHeight(h_node, height)
        node.height = height

        node.lower_left_point = [node.center.x - node.width/2,
                                 node.center.y - node.height/2]

#    h_reaction = sbnw.nw_getReactionp(self.__h_network, nr)
#    sbnw.reaction_recenter(h_reaction)

#    sbnw.nw_recenterJunctions(sbml_layout._SBMLlayout__h_network)
#    sbnw.nw_rebuildCurves(sbml_layout._SBMLlayout__h_network)

#    sbml_layout._SBMLlayout__updateNetworkLayout()
    sbml_layout._SBMLlayout__doc = libsbml.readSBMLFromString(
            sbml_layout._SBMLlayout__getSBMLWithLayoutString())


def createNetworkFigure(sbml_layout, arrowhead_mutation_scale, figsize=None,
                        show=True, dpi=72, node_multiplier=None,
                        node_padding=None, node_mutation_scale=None,
                        compute_node_dims=None, use_all_fig_space=False):
    """Creates the figure, draws any compartments, draws the nodes,
    draws the reactions, adds text to the nodes.

    Args:
        sbml_layout (libsbml_draw.model.SBMLlayout): the SBML model
        arrowhead_mutation_scale (dict): keys are roles (int), values are for
            matplotlib's FancyArrowPatch mutation_scale parameter
        figsize (optional, tuple): (width, height) in inches
        show (optional, bool): displays the figure if True
        dpi (int): dots-per-inch setting for the figure
        node_multiplier (optional, float): multiplier to achieve a width of
            the node box beyond what's needed for the text itself, eg. 1.1
            represents an extra 10%
        node_padding (optional, float): passed to matplotlib for the
            FancyBboxPatch boxstyle pad parameter
        node_mutation_scale (optional, float): passed to matplotlib for the
            FancyBboxPatch mutation_scale parameter
        compute_node_dims (optional, bool): if True, the width and height
            of the node boxes will be computed so that the node text fits
            in the box given the font-size, figsize, and figure dpi.
            If False, the node width and height found in the SBML file or
            computed by the layout algorithm will be used.
        use_all_fig_space (optional, bool): if True, use all of the space
                available for the figure, with no borders

    Returns: matplotlib.figure.Figure
    """
    
    nodes = sbml_layout._SBMLlayout__network.nodes.values()
    reactions = sbml_layout._SBMLlayout__network.reactions.values()
    compartments = sbml_layout._SBMLlayout__network.compartments.values()

    for node in nodes:
        print("node: ", node.center.x/72, node.center.y/72, 
              node.center.x/72 - (node.width/2)/72, 
              node.center.y/72 - (node.height/2)/72, node.width, node.height, 
              node.id)
    print()
    for node in nodes:
        print("node: ", node.center.x, node.center.y, node.width, node.height, node.id)

    max_x_nodes = max([node.center.x + node.width/2 for node in nodes]) 
    min_x_nodes = min([node.center.x - node.width/2 for node in nodes])

    max_x_curves = max([max(curve.start_point.x, 
                         curve.end_point.x, 
                         curve.control_point_1.x,
                         curve.control_point_2.x) for reaction in reactions for curve in reaction.curves])

    min_x_curves = min([min(curve.start_point.x, 
                         curve.end_point.x, 
                         curve.control_point_1.x,
                         curve.control_point_2.x) for reaction in reactions for curve in reaction.curves])
        

    max_y_nodes = max([node.center.y + node.height/2 for node in nodes]) 
    min_y_nodes = min([node.center.y - node.height/2 for node in nodes])

    max_y_curves = max([max(curve.start_point.y, 
                         curve.end_point.y, 
                         curve.control_point_1.y,
                         curve.control_point_2.y) for reaction in reactions for curve in reaction.curves])

    min_y_curves = min([min(curve.start_point.y, 
                         curve.end_point.y, 
                         curve.control_point_1.y,
                         curve.control_point_2.y) for reaction in reactions for curve in reaction.curves])

    if compartments:

        max_x_compartments = max([compartment.max_corner.x 
                                  for compartment in compartments])
        min_x_compartments = min([compartment.min_corner.x 
                                  for compartment in compartments])

        max_y_compartments = max([compartment.max_corner.y 
                                  for compartment in compartments])
        min_y_compartments = min([compartment.min_corner.y 
                                  for compartment in compartments])
            
#        nw_width_points = (max(max_x_nodes, max_x_curves, max_x_compartments) - 
#                           min(min_x_nodes, min_x_curves, min_x_compartments))

#        nw_height_points = (max(max_y_nodes, max_y_curves, max_y_compartments) - 
#                            min(min_y_nodes, min_y_curves, min_y_compartments))

        nw_width_points = max(max_x_nodes, max_x_curves, max_x_compartments)

        nw_height_points = max(max_y_nodes, max_y_curves, max_y_compartments)

    else:
    
#        nw_width_points = (max(max_x_nodes, max_x_curves) - 
#                           min(min_x_nodes, min_x_curves))

#        nw_height_points = (max(max_y_nodes, max_y_curves) - 
#                            min(min_y_nodes, min_y_curves))

        nw_width_points = max(max_x_nodes, max_x_curves)

        nw_height_points = max(max_y_nodes, max_y_curves)
        
    print("max_x, max_y: ", max_x_nodes, max_x_curves, max_y_nodes, max_y_curves)
    print("min_x, min_y: ", min_x_nodes, min_x_curves, min_y_nodes, min_y_curves)

#    nw_width_inches = nw_width_points/72 + 5*SHIFT    
#    nw_height_inches = nw_height_points/72 + 5*SHIFT

    nw_width_inches = nw_width_points/72    
    nw_height_inches = nw_height_points/72

#    if compartments:
#        max_compartment_width = max([compartment.width for compartment in compartments])/72
#        max_compartment_height = max([compartment.height for compartment in compartments])/72
#    else:
#        max_compartment_width = 0
#        max_compartment_height = 0

#    ax = plt.gca()
#    ax_win = ax.transData.transform([(0,0), (1,1)]) 
#    print("transData: ", ax_win[0,0], ax_win[0,1])   
#    global WIDTH_SHIFT    
#    global HEIGHT_SHIFT
#    WIDTH_SHIFT = ax_win[0,0]/dpi    
#    HEIGHT_SHIFT = ax_win[0,1]/dpi   

    SF = .5

    fig_width_inches = SF*nw_width_inches + 2*WIDTH_SHIFT
    fig_height_inches = SF*nw_height_inches + 2*HEIGHT_SHIFT

#    fig_width_inches = (max(nw_width_inches, max_compartment_width) + WIDTH_SHIFT)
#    fig_height_inches = (max(nw_height_inches, max_compartment_height) + 2*HEIGHT_SHIFT)

    print("nw width, height points: ", nw_width_points, nw_height_points)
    print("nw width, height inches: ", nw_width_inches, nw_height_inches)
#    print("max compartment width: ", max_compartment_width)
#    print("max compartment height: ", max_compartment_height)
    print("WIDTH SHIFT, HEIGHT SHIFT: ", WIDTH_SHIFT, HEIGHT_SHIFT)

    # initialize figure
#    if figsize and len(figsize) == 2:
#        fig = plt.figure(figsize=figsize, dpi=dpi)
#    else:
#        figsize = (fig_width_inches, fig_height_inches)
#        fig = plt.figure(figsize=figsize)

    figsize = (fig_width_inches, fig_height_inches)

    
#    print("window extent: ", ax.get_window_extent())
#    fig_bbox = ax.get_window_extent(
#            ).transformed(fig.dpi_scale_trans.inverted())
       
    fig = plt.figure(figsize=figsize, dpi=dpi)
    ax = plt.gca()
    fig.add_axes(ax)
    fig.subplots_adjust(0,0,1,1)

#    ax = plt.subplot(111, aspect = 'equal')
#    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)

    print("fig dpi: ", fig.dpi, fig.get_dpi())
    print("fig width, height: ", fig.get_figwidth(), fig.get_figheight())

    # uses all of the figure space
#    if use_all_fig_space:
#        ax = plt.Axes(fig, [0., 0., 1., 1.])
#        ax.set_axis_off()
#        fig.add_axes(ax)
#    else:  # figure will have border space
#        ax = plt.gca()
#        fig.add_axes(ax)

#    fig_width_pixels, fig_height_pixels = \
#        compute_figure_width_height_in_pixels(fig, ax)

    network = sbml_layout._SBMLlayout__network

    # ensure that the node text will fit in the node box
#    if compute_node_dims:
#        update_node_dimensions(sbml_layout, fig.get_dpi(), fig_width_pixels,
#                               fig_height_pixels, node_multiplier)
#    else:  # use node dimensions given in SBML or returned by the layout alg
#        pass

    # draw the compartments
    compartment_patches = draw_compartments(network.compartments.values(), fig, SF)

    for compartment_patch in compartment_patches:
        ax.add_patch(compartment_patch)

    # draw the reactions
    reaction_patches = draw_reactions(
            network.reactions.values(),
            arrowhead_mutation_scale, fig, SF)
    for reaction_patch in reaction_patches:
        ax.add_patch(reaction_patch)

    # draw the nodes
    node_patches = draw_nodes(network.nodes.values(), node_padding,
                              node_mutation_scale, fig, SF)
    for node_patch in node_patches:
        ax.add_patch(node_patch)

    # add labels to the nodes
    add_labels(network.nodes.values(), fig, SF)

#    plt.text(0,0, "A", transform=fig.dpi_scale_trans)
#    plt.text(1,0, "B", transform=fig.dpi_scale_trans)

#    ax.autoscale()
#    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
#    plt.axis("tight")

    plt.axis("off")
    plt.axis("equal")

    if show:
        plt.show()
    else:
        plt.close()

    return fig


def save_png_and_display_scaled_down_image(figure):
    """Temporarily saves a figure as a png file, and then displays that png.

    Args:
        figure (matplotlib.figure.Figure): the figure to display

    Returns: None
    """
    NETWORK_IMAGE = "network_image.png"

    with tempfile.TemporaryDirectory() as tmpdirname:
        file_path = str(pathlib.Path(tmpdirname) / NETWORK_IMAGE)
        figure.savefig(file_path)
        from IPython.display import Image
        from IPython.display import display
        im = Image(filename=file_path, width=500, height=500)
        display(im)


def running_ipython():
    """Check if the user is running in iPython

    Args: None

    Returns: bool, True if running in iPython
    """
    try:
        __IPYTHON__
        return True
    except NameError:
        return False
