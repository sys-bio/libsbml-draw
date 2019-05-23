"""
Draw the SBML model's network which consists of nodes and reactions.
"""
import numpy as np
from matplotlib.patches import BoxStyle, FancyArrowPatch, FancyBboxPatch
from matplotlib.path import Path
from matplotlib import pyplot as plt

import pathlib
import tempfile


def get_figure_width_height_in_pixels(fig):
    """Returns the width and height of the figure in pixels.
    
    Args: matplotlib.figure.Figure
        
    Returns: tuple (int, int), (width, height)
    """
#    ax = fig.get_axes()
    ax = plt.gca()
    
    fig_bbox = ax.get_window_extent(
            ).transformed(fig.dpi_scale_trans.inverted())

    fig_width_pixels = fig_bbox.width*fig.get_dpi()
    fig_height_pixels = fig_bbox.height*fig.get_dpi()
    
    print("extent w, h: ", fig_width_pixels, fig_height_pixels) 

    return (fig_width_pixels, fig_height_pixels)        
    

def get_node_dimensions(text_length_points, text_height_points, fig, 
                        network_width_data_coords, network_height_data_coords):
    """Returns the width and height needed in data coordinates for the text to
    fit inside the node.

    Args:

    Returns: 
    """
    
    text_length_pixels = fig.get_dpi()*text_length_points/72  # 1/72 inches per point

    text_height_pixels = fig.get_dpi()*text_height_points/72  # 1/71

    fig_width_pixels, fig_height_pixels = get_figure_width_height_in_pixels(fig)

    network_width_to_height_ratio = network_width_data_coords/network_height_data_coords

    
    if network_width_to_height_ratio > 1:  # horizontal figure, uses all the width available, not all of the height

        width = text_length_pixels*network_width_data_coords/fig_width_pixels

        used_fig_height_pixels = fig_width_pixels/network_width_to_height_ratio
        
        height = text_height_pixels*network_height_data_coords/used_fig_height_pixels

    else:  # vertical figure, used all the height available, not all of the width
        
        used_fig_width_pixels = fig_height_pixels*network_width_to_height_ratio

        width = text_length_pixels*network_width_data_coords/used_fig_width_pixels
        
        height = text_height_pixels*network_height_data_coords/fig_height_pixels

        
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


def draw_nodes(nodes, fig):
    """Create a list of FancyBbox Patches, one for each node.

    Args:
        nodes (iterable collection of Node): collection of nodes

    Returns: list of matplotlib.patches.FancyBboxPatch
    """ 
    
    fig_width_data_coords = (max([node.center.x for node in nodes])-
                            min([node.center.x for node in nodes]))

    fig_height_data_coords = (max([node.center.y for node in nodes])-
                             min([node.center.y for node in nodes])) 

    print("fig width data coords: ", fig_width_data_coords)
    print("fig height data coords: ", fig_height_data_coords)
      
    node_patches = []

    for node in nodes:

#        if fig_width_data_coords/fig_height_data_coords < 1: 
#            width = get_box_length(1.1*(len(node.name))*node.font_size, figwidth, figheight, fig_width_data_coords, fig_height_data_coords)[1]
#        else:
#            width = get_box_length(1.1*(len(node.name))*node.font_size, figwidth, figheight, fig_width_data_coords, fig_height_data_coords)[1]
#        height = get_box_length(node.font_size+4, figwidth, figheight, fig_width_data_coords, fig_height_data_coords)[1]

        width, height = get_node_dimensions(
                1.2*len(node.name)*node.font_size,
                1.2*node.font_size, 
                fig, 
                fig_width_data_coords, 
                fig_height_data_coords)
        
        print("node w, h: ", width, height)
        
        fbbp = FancyBboxPatch(
#            node.lower_left_point,
#            node.width,
#            node.height,
            [node.center.x-width/2, node.center.y-height/2],
#            [node.center.x-width/2, node.center.y-width/4],
            width,
            height,                        
#            width/2,
            edgecolor=node.edge_color,
            facecolor=node.fill_color,
            linewidth=node.edge_width,
            boxstyle=BoxStyle("round", pad=0.7, rounding_size=.8),
            mutation_scale=10
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


def createNetworkFigure(network, mutation_scale, figure_size=None, show=True):
    """Creates the figure, draws the nodes, draws the reactions, adds text to
    the nodes.

    Args:
        network (libsbml_draw.model.network.Network): the model's network which
            contains Nodes and Reactions.
        mutation_scale (dict): keys are roles (int), values are for
            matplotlib's mutation_scale parameter
        figure_size (tuple): (width, height) in inches
        show (bool): displays the figure if True

    Returns: matplotlib.figure.Figure
    """
    # SUPPRESS MAtPLOTLIB OUTPUT
    if running_ipython():
        from IPython.core.interactiveshell import InteractiveShell
        InteractiveShell.ast_node_interactivity = "last_expr"
    else:
        pass
    
#    MAX_FIGURE_DIM_TO_DISPLAY = 777 # inches
#    fig.set_dpi(72)

    # initialize figure
    if figure_size and len(figure_size) == 2:
        fig = plt.figure(figsize=figure_size);
    else:
        fig = plt.figure()

#    ax = plt.gca()
    
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)

    print("dn: fig_size: ", figure_size)
    
    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    width, height = bbox.width, bbox.height
    width *= fig.dpi
    height *= fig.dpi
    
    print("extent w, h: ", width, height) 
    
    # draw the compartments
    compartment_patches = draw_compartments(network.compartments.values())

    for compartment_patch in compartment_patches:
        ax.add_patch(compartment_patch)

#    figwidth = fig.get_dpi()*fig.get_figwidth()
#    figheight = fig.get_dpi()*fig.get_figheight()

    # draw the nodes
    node_patches = draw_nodes(network.nodes.values(), fig)
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
    