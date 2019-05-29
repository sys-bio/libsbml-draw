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

def get_figure_width_height_in_pixels(fig=None):
    """Returns the width and height of the figure in pixels.
    
    Args: matplotlib.figure.Figure
        
    Returns: tuple (int, int), (width, height)
    """
#    ax = fig.get_axes()
    ax = plt.gca()
    
    if not fig:
        fig = plt.figure(frameon=False)
        plt.close(fig)
    else:
        pass
    
    fig_bbox = ax.get_window_extent(
            ).transformed(fig.dpi_scale_trans.inverted())

    fig_width_pixels = fig_bbox.width*fig.get_dpi()
    fig_height_pixels = fig_bbox.height*fig.get_dpi()
    
    print("extent w, h: ", fig_width_pixels, fig_height_pixels) 

    return (fig_width_pixels, fig_height_pixels)        
    

def get_node_dimensions(text_length_points, text_height_points, fig_dpi,
                        fig_width_pixels, fig_height_pixels,
                        network_width_data_coords, network_height_data_coords):
    """Returns the width and height needed in data coordinates for the text to
    fit inside the node.

    Args:
            
        
    Returns: 
        width (float): width of the node box in data coordinates
        height (float): height of node box in data coordinates    
    """
    
    text_length_pixels = fig_dpi*text_length_points/72  # 1/72 inches per point

    text_height_pixels = fig_dpi*text_height_points/72  # 1/71

#    fig_width_pixels, fig_height_pixels = get_figure_width_height_in_pixels(fig)

    network_width_to_height_ratio = network_width_data_coords/network_height_data_coords

#    print("nw w_to_h: ", network_width_to_height_ratio)

    if network_width_to_height_ratio > 1:  # horizontal figure, uses all the width available, not all of the height

        width = text_length_pixels*network_width_data_coords/fig_width_pixels

        used_fig_height_pixels = fig_width_pixels/network_width_to_height_ratio
        
        height = text_height_pixels*network_height_data_coords/used_fig_height_pixels

    else:  # vertical figure, used all the height available, not all of the width
        
        used_fig_width_pixels = fig_height_pixels*network_width_to_height_ratio

        width = text_length_pixels*network_width_data_coords/used_fig_width_pixels
        
        height = text_height_pixels*network_height_data_coords/fig_height_pixels

        print()
        print("text_length_pixels: ", text_length_pixels)
        print("used fig width pixels: ", used_fig_width_pixels)
        print("network_width_data_coords: ", network_width_data_coords)
        print("width: ", width)
        print()
        
    return (width, height)
         
    
#    dxy = pts_needed/72 # inches

#    tmp_x = ax.transData.transform([(0,0), (1,1)])
#    print("t w: ", tmp_x[1,0] - tmp_x[0,0])
#    tx = (tmp_x[1,0] - tmp_x[0,0])/fig_width_data_coords  # 1 unit in display coords
#    tx = figwidth/fig_width_data_coords
    
#    tmp_y = ax.transData.transform([(0,0), (1,1)])
#    print("t h: ", tmp_x[1,1] - tmp_x[0,1])
#    ty = (tmp_y[1,1] - tmp_y[0,1])/fig_height_data_coords  # 1 unit in display coords
#    ty = figheight/fig_height_data_coords
   
#    tmp_x = 1/tx  # 1 pixel in display coords
#    tmp_y = 1/ty
    
#    length_data_coords_width = tmp_x*dxy*ax.get_figure().get_dpi()  # shift pixels in display coords
    
#    length_data_coords_height = tmp_y*dxy*ax.get_figure().get_dpi()  # shift pixels in display coords
    
#    print()
#    print("figwidth, figheigth: ", figwidth, figheight)
#    print("pixels tmp: ", tmp_x)
#    print("pixels per data coord x: ", tx)
#    print("pixels per data coord y: ", ty)
#    print("data coord/pixel", tmp_x)
#    print("data coord/pixel", tmp_y)
#    #print("data coord/pixel * inch * pixel/inch: ", tmp)
#    print(f"length data coords for {pts_needed}", length_data_coords_width)
#    #print("data coord/pixel * inch * pixel/inch: ", tmp)
#    print(f"length data coords for {pts_needed}", length_data_coords_height)
#    print()

#    return (length_data_coords_width, length_data_coords_height)

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


def draw_nodes(nodes, node_padding, node_mutation_scale):
    """Create a list of FancyBbox Patches, one for each node.

    Args:
        nodes (iterable collection of Node): collection of nodes

    Returns: list of matplotlib.patches.FancyBboxPatch
    """

    node_patches = []

    for node in nodes:

        print("node w, h: ", node.width, node.height)

        fbbp = FancyBboxPatch(
            node.lower_left_point,
            node.width,
            node.height,
            edgecolor=node.edge_color,
            facecolor=node.fill_color,
            linewidth=node.edge_width,
            boxstyle=BoxStyle("round",
                              pad=node_padding if node_padding else 0.6,
                              rounding_size=.8),
            mutation_scale=node_mutation_scale if node_mutation_scale else 10
            )

        node_patches.append(fbbp)

    return node_patches


def draw_reactions(reactions, mutation_scale):
    """Create a list of FancyArrow Patches, one for each curve in a reaction.

    Args:
        reactions (iterable collection of Reaction): collection of reactions

    Returns: list of matplotlib.patches.FancyArrowPatch
    """
    reaction_patches = []

    for reaction in reactions:

        curves = reaction.curves

        for curve in curves:

            start_point = np.array([curve.start_point.x,
                                    curve.start_point.y])
            end_point = np.array([curve.end_point.x,
                                  curve.end_point.y])
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

            fap = FancyArrowPatch(
                    facecolor=reaction.fill_color,
                    edgecolor=reaction.edge_color,
                    arrowstyle=curve.curveArrowStyle,
                    clip_on=False,
                    linewidth=reaction.curve_width,
                    mutation_scale=mutation_scale.get(curve.role, 10),
                    path=cubic_bezier_curve_path
                    )

            reaction_patches.append(fap)

    return reaction_patches


def add_labels(nodes):
    """Add text to the nodes.

    Args:
        nodes (iterable collection of Node): collection of nodes

    Returns: None
    """
    for node in nodes:
        plt.text(node.center.x,
                 node.center.y,
                 node.name,
                 fontsize=node.font_size,
                 color=node.font_color,
                 fontname=node.font_family,
                 fontstyle=node.font_style,
                 horizontalalignment="center",
                 verticalalignment="center")

def update_node_dimensions(sbml_layout, fig_dpi, fig_width_pixels, 
                           fig_height_pixels, node_multiplier=1.0,
                           recompute_node_dims=True):
    """Increase the size of the node boxes, if necessary, to fit the text.
    
    Args:
        
    Returns: None    
    """
    nodes = sbml_layout._SBMLlayout__network.nodes.values()

    print("number of nodes: ", len(nodes), sbml_layout.getNodeIds())
    if len(nodes) == 8:
        for node_key in sbml_layout._SBMLlayout__network.nodes.keys():
            print("update node dims: ", 
                  node_key, sbml_layout._SBMLlayout__network.nodes[node_key].id)
    
    fig_width_data_coords = (
            max([node.center.x for node in nodes])-
            min([node.center.x for node in nodes]))

    fig_height_data_coords = (
            max([node.center.y for node in nodes])-
            min([node.center.y for node in nodes]))

    print("fig dpi: ", fig_dpi)
    print("fwdc fhdc: ", fig_width_data_coords, fig_height_data_coords)
    print("fig wh: ", fig_width_pixels, fig_height_pixels)
    print("node_multiplier", node_multiplier)

    needToRecomputeLayout = False
    
    for node in nodes:
                    
        width, height = get_node_dimensions(
            node_multiplier*(len(node.name)+0)*node.font_size,
            node_multiplier*(node.font_size+0),
            fig_dpi, fig_width_pixels, fig_height_pixels,
            fig_width_data_coords, fig_height_data_coords)

        print("computed w,h: ", width, height)        

        h_node_id = node.id.encode('utf-8')
        h_node = sbnw.nw_getNodepFromId(sbml_layout._SBMLlayout__h_network, 
                                        h_node_id)

        # is node big enough for font-size and figsize?
        if not sbml_layout._SBMLlayout__layoutSpecified or recompute_node_dims:
            needToRecomputeLayout = True
            sbnw.node_setWidth(h_node, width)
            node.width = width
            node.lower_left_point = [node.center.x - node.width/2,
                                     node.center.y - node.height/2]
        if not sbml_layout._SBMLlayout__layoutSpecified or recompute_node_dims:
            needToRecomputeLayout = True
            sbnw.node_setHeight(h_node, height)
            node.height = height
            node.lower_left_point = [node.center.x - node.width/2,
                                     node.center.y - node.height/2]                    
#    if False:
    if needToRecomputeLayout:
#        print("Recomputing Layout")
#        for node in nodes:
#            sbml_layout.lockNode(node.id)
#        sbml_layout.regenerateLayout()    
#        for node in nodes:
#            sbml_layout.unlockNode(node.id)              
#        for nr in range(sbnw.nw_getNumRxns(sbml_layout._SBMLlayout__h_network)):
        sbnw.nw_recenterJunctions(sbml_layout._SBMLlayout__h_network)
#                h_reaction = sbnw.nw_getReactionp(self.__h_network, nr)
#                sbnw.reaction_recenter(h_reaction)
        sbnw.nw_rebuildCurves(sbml_layout._SBMLlayout__h_network)

        sbml_layout._SBMLlayout__updateNetworkLayout()
        sbml_layout._SBMLlayout__doc = libsbml.readSBMLFromString(
                sbml_layout._SBMLlayout__getSBMLWithLayoutString())
                
def createNetworkFigure(sbml_layout, mutation_scale, figsize=None,
                        show=True, dpi=None, node_multiplier=None, 
                        node_padding=None, node_mutation_scale=None, 
                        recompute_node_dims=None):
    """Creates the figure, draws the nodes, draws the reactions, adds text to
    the nodes.

    Args:
        network (libsbml_draw.model.network.Network): the model's network which
            contains Nodes and Reactions.
        mutation_scale (dict): keys are roles (int), values are for
            matplotlib's mutation_scale parameter
        figsize (tuple): (width, height) in inches
        show (bool): displays the figure if True

    Returns: matplotlib.figure.Figure
    """
    # SUPPRESS MAtPLOTLIB OUTPUT
#    if running_ipython():
#        from IPython.core.interactiveshell import InteractiveShell
#        InteractiveShell.ast_node_interactivity = "last_expr"
#    else:
#        pass
    
#    MAX_FIGURE_DIM_TO_DISPLAY = 777 # inches

    # initialize figure
    if figsize and len(figsize) == 2:
        fig = plt.figure(figsize=figsize, dpi=dpi);
    else:
        fig = plt.figure()

#    if dpi:   
#        fig.set_dpi(dpi)
#    else:
#        pass

    ax = plt.gca()

    # uses all of the figure space
    
#    ax = plt.Axes(fig, [0., 0., 1., 1.])
#    ax.set_axis_off()
#    fig.add_axes(ax)

    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    fig_width_pixels = bbox.width*fig.get_dpi()
    fig_height_pixels = bbox.height*fig.get_dpi()
    
    print("extent w, h: ", fig_width_pixels, fig_height_pixels) 
    
    
    network = sbml_layout._SBMLlayout__network
    
    update_node_dimensions(sbml_layout, fig.get_dpi(), fig_width_pixels, 
                           fig_height_pixels, node_multiplier, 
                           recompute_node_dims)
        
    # draw the compartments
    compartment_patches = draw_compartments(network.compartments.values())

    for compartment_patch in compartment_patches:
        ax.add_patch(compartment_patch)

#    figwidth = fig.get_dpi()*fig.get_figwidth()
#    figheight = fig.get_dpi()*fig.get_figheight()

    # draw the nodes
    node_patches = draw_nodes(network.nodes.values(), node_padding, 
                              node_mutation_scale)
    for node_patch in node_patches:
        ax.add_patch(node_patch)

    # draw the reactions
    reaction_patches = draw_reactions(
            network.reactions.values(),
            mutation_scale)
    for reaction_patch in reaction_patches:
        ax.add_patch(reaction_patch)

    # add labels
    add_labels(network.nodes.values())
    # No axes and size it just bigger than the data (i.e. tight)
    # ax.autoscale()
    
    # WHITE SPACE
    # plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    #fig.tight_layout()

    plt.axis("off")
#    plt.axis("tight")
    plt.axis("equal")

    if show:
#        if ((fig.get_figheight() > MAX_FIGURE_DIM_TO_DISPLAY or 
#             fig.get_figwidth() > MAX_FIGURE_DIM_TO_DISPLAY) and 
#            running_ipython()):
#
#            save_png_and_display_scaled_down_image(fig)
#
#            plt.close()
#
#        else:
        plt.show()
    else:
        plt.close()

    # SUPPRESS MAtPLOTLIB OUTPUT
    pass;

    return fig;

def save_png_and_display_scaled_down_image(figure):
    """Temporarily saves a figure as a png file, and then displays that png.

    Args:
        figure (matplotlib.figure.Figure): the figure to display

    Returns: None
    """
    NETWORK_IMAGE = "network_image.png"

    with tempfile.TemporaryDirectory() as tmpdirname:
        file_path = str(pathlib.Path(tmpdirname) / NETWORK_IMAGE)
        
        # print("filepath: ", file_path)
        
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
    