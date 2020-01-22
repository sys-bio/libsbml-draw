"""Creates a Python interface to load, display and manipulate
models defined in an SBML file, making use of a c API and libsbml."""

from collections import namedtuple
import os

from matplotlib.colors import is_color_like, to_hex

import tesbml

import libsbml_draw.c_api.sbnw_c_api as sbnw
from libsbml_draw.draw.draw_network import createNetworkFigure
from libsbml_draw.model.network import Network
from libsbml_draw.model.render import Render

BezierPoints = namedtuple("BezierPoints", ["start", "end",
                                           "control1", "control2"])


class SBMLlayout:
    """SBMLlayout represents the model in an SBML file."""

    LIBSBML_DRAW_VERSION = sbnw.getCurrentLibraryVersion()

    NODE_KEYWORDS = {"all", "boundary", "floating"}

    WIDTH_PADDING = 2  # number of additional characters in length node name
    HEIGHT_PADDING = 1  # number of additional characters in node name height

    def __init__(self, sbml_source=None, layout_alg_options=None,
                 layout_number=0, fitToWindow=tuple(),
                 autoComputeLayout=False, applyRender=True):

        self.__sbml_source = sbml_source
        self.__layout_number = layout_number
        self.__fitWindow = fitToWindow
        self.__applyRender = applyRender

        if self.__validate_layout_alg_options(layout_alg_options):
            self.__layout_alg_options = layout_alg_options
        else:
            self.__layout_alg_options = sbnw.fr_alg_options(
                20.0,        # k
                0,           # grav, has to be > 5 for effect
                500.0,       # baryx
                500.0,       # baryy
                1,           # autobary
                20.0         # padding
            )

        if isinstance(self.__sbml_source, str):

            if self.__validate_sbml_filename(self.__sbml_source):
                self.__h_model = sbnw.loadSBMLFile(self.__sbml_source)
            else:
                if self.__sbml_source.startswith("<?xml"):
                        self.__h_model = sbnw.loadSBMLString(
                                self.__sbml_source)
                else:
                    raise ValueError(f"File {self.__sbml_source} "
                                     f"does not exist, or the source string "
                                     f"is not a valid SBML file.")

            if self.__h_model == 0:
                raise ValueError("SBML source cannot be parsed by libsbml.")

            self.__h_layout_info = sbnw.processLayout(self.__h_model)
            self.__h_network = sbnw.getNetworkp(self.__h_layout_info)
            self.__h_canvas = sbnw.getCanvasp(self.__h_layout_info)
            self.__layoutSpecified = True if sbnw.isLayoutSpecified(
                    self.__h_network) else False
            self.__autoComputeLayout = autoComputeLayout

            # create layout, if it doesn't already exist or user requests it
            if not self.__layoutSpecified or self.__autoComputeLayout:
                self.__randomizeLayout()
                self.__doLayoutAlgorithm()

                # no render info here because auto-generating the layout
                self.__doc = tesbml.readSBMLFromString(
                        self.__getSBMLWithLayoutString())

                self.__network = self.__createNetwork()

                # compute and set width and height for node boxes
                for node in self.__network.nodes.values():
                    # pad the width (default, 2 additional chars) and
                    # pad the height (default, 1 additional char)
                    width = self.__computeNodeWidth(node)
                    height = self.__computeNodeHeight(node)
                    self.__setNodeWidth(node.id, width)
                    self.__setNodeHeight(node.id, height)

                self.regenerateLayout()

            else:
                if self.__validate_sbml_filename(sbml_source):
                    self.__doc = tesbml.readSBMLFromFile(sbml_source)
                else:
                    self.__doc = tesbml.readSBMLFromString(sbml_source)

            if len(self.__fitWindow) == 4:
                self.__fitToWindow(self.__fitWindow[0], self.__fitWindow[1],
                                   self.__fitWindow[2], self.__fitWindow[3])
            else:
                pass

            sbnw.layout_alignToOrigin(self.__h_layout_info, 0, 0)

            self.__network = self.__createNetwork()

            if self.__applyRender:
                self.__applyRenderInformation()

            self.__arrowhead_scale = {key: 15 for key in
                                      range(self.getNumberOfRoles())}

        else:  # User can separately load a file
            pass

    def __computeNodeWidth(self, node):
        """Computes the node width needed for the text to fit inside.

        Args:
            node (libsbml_draw.network.Node): the node of interest

        Returns: float
        """
        width = (len(node.name) + SBMLlayout.WIDTH_PADDING)*node.font_size

        return width

    def __computeNodeHeight(self, node):
        """Computes the node height needed for the text to fit inside.

        Args:
            node (libsbml_draw.network.Node): the node of interest

        Returns: float
        """
        node_name_height = 1
        height = (node_name_height + SBMLlayout.HEIGHT_PADDING)*node.font_size

        return height

    def loadSBMLFile(self, sbml_file):
        """Loads the SBML model into SBMLlayout.

        Args:
            sbml_string(str): name of file containing an SBML model

        Returns: None
        """
        self.__init__(sbml_file)

    def loadSBMLString(self, sbml_string):
        """Loads the SBML model into SBMLlayout.

        Args:
            sbml_string(str): SBML model in string format

        Returns: None
        """
        self.__init__(sbml_string)

    def setLayoutAlgorithmOptions(self, k=None, gravity=None, baryx=None,
                                  baryy=None, autobary=None, padding=None
                                  ):
        """
        Set values for the Fruchterman-Reingold layout algorithm parameters.

        Args:
            k (float):
            gravity (float):
            baryx (float):
            baryy (float):
            autobary (int):
            padding (float):

        Returns: None
        """
        if k:
            self.__layout_alg_options.k = k
        if gravity:
            self.__layout_alg_options.gravity = gravity
        if baryx:
            self.__layout_alg_options.baryx = baryx
        if baryy:
            self.__layout_alg_options.baryy = baryy
        if autobary:
            self.__layout_alg_options.autobary = autobary
        if padding:
            self.__layout_alg_options.padding = padding

    def setLayoutAlgorithm_k(self, k):
        """Set the Fruchterman-Reingold layout algorithm parameter 'k'.

        Args:
            k (float): stiffness parameter

        Returns: None
        """
        self.__layout_alg_options.k = k

    def setLayoutAlgorithm_gravity(self, gravity):
        """Set the Fruchterman-Reingold layout algorithm parameter 'gravity'.

        Args:
            gravity (float): strength of the gravity, must be greater than 5 to
                have an effect.

        Returns: None
        """
        self.__layout_alg_options.gravity = gravity

    def setLayoutAlgorithm_baryx(self, baryx):
        """Set the Fruchterman-Reingold layout algorithm parameter 'baryx'.

        Args:
            baryx (float): x value of the center of gravitational force

        Returns: None
        """
        self.__layout_alg_options.baryx = baryx

    def setLayoutAlgorithm_baryy(self, baryy):
        """Set the Fruchterman-Reingold layout algorithm parameter 'baryy'.

        Args:
            baryy (float): y value of the center of gravitational force

        Returns: None
        """
        self.__layout_alg_options.baryy = baryy

    def setLayoutAlgorithm_autobary(self, autobary):
        """Set the Fruchterman-Reingold layout algorithm parameter 'autobary'.
        This parameter determines if the barycenter is set automatically from
        layout info.

        Args:
            autobary (int): 1 = set barycenter automatically from layout info,
                0 means don't set it automatically

        Returns: None
        """
        self.__layout_alg_options.autobary = autobary

    def setLayoutAlgorithm_padding(self, padding):
        """Set the Fruchterman-Reingold layout algorithm parameter 'padding'.

        Args:
            padding (float): padding on compartments

        Returns: None
        """
        self.__layout_alg_options.padding = padding

    def getLayoutAlgorithmOptions(self,):
        """Get the Fruchterman-Reingold layout algorithm parameter values.

        Args: None

        Returns: instance of the fr_alg_options class
        """
        return self.__layout_alg_options

    def showLayoutAlgorithmOptions(self,):
        """Prints out the values of the Fruchterman-Reingold algorithm
        paramters, which are: k, grav, baryx, baryy, autobary, and padding.

        Args: None

        Returns: None
        """
        print("layout algorithm options: \n",
              "k ", self.__layout_alg_options.k, "\n",
              "gravity ", self.__layout_alg_options.gravity, "\n",
              "baryx ", self.__layout_alg_options.baryx, "\n",
              "baryy ", self.__layout_alg_options.baryy, "\n",
              "autobary ", self.__layout_alg_options.autobary, "\n",
              "padding ", self.__layout_alg_options.padding, "\n"
              )

    # Validation Methods

    def __validate_sbml_filename(self, sbml_filename):
        """
        Check if the file actually exists.

        Args:
            sbml_filename(str): name of a file

        Returns: bool
        """
        if sbml_filename and os.path.isfile(sbml_filename):
            return True
        else:
            return False

    def __validate_layout_alg_options(self, layout_alg_options):
        """
        Check if the user supplied an instance of fr_alg_options class.

        Args:
            layout_alg_options (sbnw.layout_alg_options): instance of the
            layout_alg_options class

        Returns: bool
        """
        if isinstance(layout_alg_options, sbnw.fr_alg_options):
            return True
        else:
            return False

    def __validatePlotColor(self, plot_color):
        """
        Check if the color supplied is a valid matplotlib color value.

        Args:
            plot_color(str): id for a color

        Returns: True or raises ValueError
        """
        if not is_color_like(plot_color):
            raise ValueError("Invalid color: ", plot_color)
        else:
            return True

    def __validateFontStyle(self, font_style):
        """ Check if the font style is a valid value for matplotlib.

        Args:
            font_style(str): name of a font style, which can be "normal",
                "italic", or "oblique"

        Return: True or raises ValueError
        """
        valid_font_styles = {"normal", "italic", "oblique"}

        if font_style in valid_font_styles:
            return True
        else:
            raise ValueError(f"Font Style, {font_style} is not valid, "
                             f"must be one of: {valid_font_styles}.")

    def __validateFontWeight(self, font_weight):
        """ Check if the font weight is a valid value for matplotlib and
        libsbml.

        Args:
            font_weight(str): name of a font weight, which can be "normal",
                or "bold"

        Return: True or raises ValueError
        """
        valid_font_weights = {"normal", "bold"}

        if font_weight in valid_font_weights:
            return True
        else:
            raise ValueError(f"Font Weight, {font_weight} is not valid, "
                             f"must be one of: {valid_font_weights}.")

    def __validateTextAnchor(self, text_anchor, anchor_type):
        """ Check if the text anchor is a valid value for matplotlib and
        libsbml.

        Args:
            text_anchor(str): location to anchor the text
            anchor_type(str): specifies "horizontal" or "vertical" anchor

        Return: True or raises ValueError
        """
        valid_text_anchors = {"center", "left", "right"}
        valid_vtext_anchors = {"center", "top", "bottom"}

        if anchor_type == "horizontal":
            if text_anchor in valid_text_anchors:
                return True
            else:
                raise ValueError(f"Text anchor, {text_anchor} is not valid, "
                                 f"must be one of: {valid_text_anchors}.")

        elif anchor_type == "vertical":
            if text_anchor in valid_vtext_anchors:
                return True
            else:
                raise ValueError(f"Text anchor, {text_anchor} is not valid, "
                                 f"must be one of: {valid_vtext_anchors}.")
        else:
            raise ValueError(f"anchor_type {anchor_type} must be either ",
                             "horizontal or vertical.")

    # Layout Methods

    def regenerateLayoutAndResetRenderInfo(self,):
        """Use this to generate a new layout, and reset the network's node
        and reaction layout and render values.

        Args: None

        Returns: None
        """
        self.__randomizeLayout()
        self.__doLayoutAlgorithm()

        if len(self.__fitWindow) == 4:
                self.__fitToWindow(self.__fitWindow[0], self.__fitWindow[1],
                                   self.__fitWindow[2], self.__fitWindow[3])
        else:
            pass

        sbnw.layout_alignToOrigin(self.__h_layout_info, 0, 0)

        self.__doc = tesbml.readSBMLFromString(
            self.__getSBMLWithLayoutString())

        self.__network = self.__createNetwork()

        # apply render information, if any
        if self.__applyRender:
            self.__applyRenderInformation()

    def regenerateLayout(self,):
        """Use this to generate a new layout, and update the network's node
        reaction, and compartment layout values.

        Args: None

        Returns: None
        """
        self.__randomizeLayout()
        self.__doLayoutAlgorithm()

        if len(self.__fitWindow) == 4:
                self.__fitToWindow(self.__fitWindow[0], self.__fitWindow[1],
                                   self.__fitWindow[2], self.__fitWindow[3])
        else:
            pass

        sbnw.layout_alignToOrigin(self.__h_layout_info, 0, 0)

        self.__doc = tesbml.readSBMLFromString(
                self.__getSBMLWithLayoutString())

        self.__updateNetworkLayout()

    def __randomizeLayout(self,):
        """Give the layout a starting point.

        Args: None
        Returns: None
        """
        sbnw.randomizeLayout(self.__h_layout_info)

    def __doLayoutAlgorithm(self,):
        """Run the Fruchterman-Reingold Layout Algorithm.

        Args: None
        Returns: None
        """
        sbnw.doLayoutAlgorithm(self.__layout_alg_options, self.__h_layout_info)

    # Model Methods

    def __createNetwork(self,):
        """Creates a network for this model based on the existing layout.

        Args: None
        Returns: libsbml_draw.Network
        """
        return Network(self.__h_network)

    def __updateNetworkLayout(self,):
        """Updates a network's layout values.

        Args: None
        Returns: None
        """
        network = self.__network
        network.updateNetwork()

    def describeModel(self, ):
        """Provides a summary of the model built from the SBML file.

        Args: None
        Returns: None
        """
        dct = {}
        dct["layout_number"] = self.__layout_number
        dct["layout_is_specified"] = self.__layoutSpecified
        dct["auto_compute_layout"] = self.__autoComputeLayout
        dct["number_of_compartments"] = self.getNumberOfCompartments()
        dct["number_of_nodes"] =self.getNumberOfNodes()
        dct["number_of_reactions"] = self.getNumberOfReactions()
        return dct


    def getNumberOfCompartments(self,):
        """Returns the number of compartments in the model.

        Args: None
        Returns: None
        """
        return sbnw.nw_getNumCompartments(self.__h_network)

    def getNumberOfNodes(self,):
        """Returns the number of nodes in the model.

        Args: None
        Returns: None
        """
        number_of_nodes = sbnw.nw_getNumNodes(self.__h_network)

        return number_of_nodes

    def getNumberOfReactions(self,):
        """Returns the number of reactions in the model.

        Args: None
        Returns: None
        """
        number_of_reactions = sbnw.nw_getNumRxns(self.__h_network)

        return number_of_reactions

    def __fitToWindow(self, left, top, right, bottom):
        """Constrains the (x,y) values for the layout to fall within this
        window.

        Args:
            left (int): left-most x value
            top (int):  top-most y value
            right (int): right-most x value
            bottom (int): bottom-most y value

        Returns: None
        """
        sbnw.fit_to_window(self.__h_layout_info, left, top, right, bottom)

    def setModelNamespace(self, level, version):
        """Specify the Model level and version.

        Args:
            level (int): model level
            version (int): model version

        Returns: None
        """
        sbnw.setModelNamespace(self.__h_layout_info, level, version)

    # Node Information

    def aliasNode(self, node_id):
        """Creates an alias of this node for each incoming and outgoing
        reaction.

        Args:
            node_id (str):

        Returns: None
        """
        if node_id in self.getNodeIds():

            h_node_id = node_id.encode('utf-8')
            h_node = sbnw.nw_getNodepFromId(self.__h_network, h_node_id)

            sbnw.node_make_alias(h_node, self.__h_network)

            self.__network._add_alias_nodes(node_id)
            self.__network._add_reactions_after_node_alias()
            self.__network._remove_node(node_id)
            self.__doc = tesbml.readSBMLFromString(
                        self.__getSBMLWithLayoutString())
        else:
            raise ValueError(f"species {node_id} is not in the network.")

    def getIsNodeAliased(self, node_id):
        """Returns True if this node is an alias of earlier node.

        Args:
            node_id (str):

        Returns: None
        """
        if node_id in self.getNodeIds():
            print("node id: ", node_id)
            node = self.__network.nodes[node_id]

            if node.id in self.__network.aliasedNodes:
                return True
            else:
                return False
        else:
            raise ValueError(f"species {node_id} is not in the network.")

    def getIsNodeLocked(self, node_id):
        """Returns True if this node is locked.

        Args:
            node_id(str): id for the node

        Returns: bool
        """
        if node_id in self.getNodeIds():

            node = self.__network.nodes[node_id]

            # aliased nodes have the id of the original node
            if node.id in self.__network.aliasedNodes:
                alias_index = int(node_id.split("_")[1])
                h_node_id = node.id.encode('utf-8')
                h_node = sbnw.nw_getNodepFromId(self.__h_network, h_node_id)
                h_alias_node = sbnw.nw_getAliasInstancep(
                        self.__h_network,
                        h_node,
                        alias_index)
                is_locked = sbnw.node_isLocked(h_alias_node)
            # node is not an alias
            else:
                h_node_id = node_id.encode('utf-8')
                h_node = sbnw.nw_getNodepFromId(self.__h_network, h_node_id)
                is_locked = sbnw.node_isLocked(h_node)

            if is_locked == 0:
                return False
            else:
                return True
        else:
            raise ValueError(f"species {node_id} is not in the network.")

    def lockNode(self, node_id):
        """Locks the node so that a new layout can be generated w/o moving
        this node.

        Args:
            node_id (str): id for the node

        Returns: None
        """
        if node_id in self.getNodeIds():

            node = self.__network.nodes[node_id]

            # aliased nodes have the id of the original node
            if node.id in self.__network.aliasedNodes:
                alias_index = int(node_id.split("_")[1])
                h_node_id = node.id.encode('utf-8')
                h_node = sbnw.nw_getNodepFromId(self.__h_network, h_node_id)
                h_alias_node = sbnw.nw_getAliasInstancep(
                        self.__h_network,
                        h_node,
                        alias_index)
                sbnw.node_lock(h_alias_node)
            # node is not an alias
            else:
                h_node_id = node.id.encode('utf-8')
                h_node = sbnw.nw_getNodepFromId(self.__h_network, h_node_id)
                sbnw.node_lock(h_node)
        else:
            raise ValueError(f"species {node_id} is not in the network.")

    def unlockNode(self, node_id):
        """Unlocks a previously locked node.

        Args:
            node_id (str): id for the node

        Returns: None
        """
        if node_id in self.getNodeIds():

            node = self.__network.nodes[node_id]

            # aliased nodes have the id of the original node
            if node.id in self.__network.aliasedNodes:
                alias_index = node_id.split("_")[1]
                h_node_id = node.id.encode('utf-8')
                h_node = sbnw.nw_getNodepFromId(self.__h_network, h_node_id)
                h_alias_node = sbnw.nw_getAliasInstancep(
                        self.__h_network,
                        h_node,
                        alias_index)
                sbnw.node_unlock(h_alias_node)
            # node is not an alias
            else:
                h_node_id = node.id.encode('utf-8')
                h_node = sbnw.nw_getNodepFromId(self.__h_network, h_node_id)
                sbnw.node_unlock(h_node)
        else:
            raise ValueError(f"species {node_id} is not in the network.")

    def setNetworkBackgroundColor(self, bg_color):
        """
        Sets the background color of the network.

        Args:
            bg_color (str): id of the color for the background

        Returns: None
        """
        self.__validatePlotColor(bg_color)

        self.__network.bg_color = bg_color

    def getNetworkBackgroundColor(self, ):
        """Returns the color id for the background color of the network.

        Args: None

        Returns: str
        """

        return self.__network.bg_color

    def getNodeCentroid(self, node_id):
        """Returns the center point of the node.

        Args:
            node_id (str): id for the node

        Returns: tuple, with x and y
        """
        if node_id in self.getNodeIds():

            centroid = self.__network.nodes[node_id].center

            return (centroid.x, centroid.y)
        else:
            raise ValueError(f"species {node_id} is not in the network.")

    # Reaction Information

    def getReactionCentroid(self, reaction_id):
        """Returns the centroid of the reaction.

        Args:
            reaction_id (str): id of the reaction

        Returns: tuple, with x and y
        """
        if reaction_id in self.getReactionIds():

            centroid = self.__network.reactions[reaction_id].centroid

            return (centroid.x, centroid.y)
        else:
            raise ValueError(f"reaction {reaction_id} is not in the network.")

    def _describeReaction(self, reaction_index):
        """Prints the number of species and number of curves in the reaction.

        Args: reaction_index (int): index of the reaction

        Returns: None
        """
        reaction_p = sbnw.nw_getReactionp(self.__h_network, reaction_index)
        reaction_id = sbnw.reaction_getID(reaction_p)
        numSpecies = sbnw.reaction_getNumSpec(reaction_p)
        numCurves = sbnw.reaction_getNumCurves(reaction_p)
        print("reaction index: ", reaction_index)
        print("reaction_id: ", reaction_id)
        print("numSpecies: ", numSpecies)
        print("numCurves: ", numCurves)

    # SBML IO Functions

    def __getSBMLWithLayoutString(self,):
        """Returns the SBML content, including layout, as a string.

        Args: None

        Returns: str
        """
        sbml_string = sbnw.getSBMLwithLayoutStr(self.__h_model,
                                                self.__h_layout_info, 1)
        return sbml_string

    def writeSBMLFile(self, out_file_name):
        """Writes the model as an SBML file.

        Args:
            out_file_name (str): name of the file to write

        Returns: None
        """
        level = self.__doc.getLevel()
        version = self.__doc.getVersion()

        layout_number = self.__layout_number
        layout_plugin = self.__doc.getModel().getPlugin("layout")

        layout = layout_plugin.getLayout(layout_number) if (
            layout_plugin and layout_plugin.getNumLayouts() > 0) else None

        if not layout.getNumSpeciesGlyphs():
            raise ValueError(f"""Cannot write file.  
            This level {level} version {version} document has no layout information.""")  # noqa

        self.__addRenderInformation()

        tesbml.writeSBMLToFile(self.__doc, out_file_name)

    # Compartment Methods

    def getCompartmentIds(self,):
        """Returns a list of compartment ids.

        Args: None

        Returns: list of str
        """
        return list(self.__network.compartments.keys())

    def setCompartmentEdgeColor(self, compartment_id, edge_color):
        """
        Sets the compartment edge color.

        Args:
            compartment_id (str): id of the compartment to change the color of
                one compartment, or 'all' to change the color of all the
                compartments
            edge_color (str): id of the color

        Returns: None
        """
        self.__validatePlotColor(edge_color)

        property_type = "edge"

        self.__setCompartmentProperty(
                compartment_id,
                edge_color,
                property_type)

    def getCompartmentEdgeColor(self, compartment_id):
        """Returns the color id for the compartment edge color.

        Args:
            compartment_id(str): id for the compartment

        Returns: str
        """
        if compartment_id in self.__network.compartments:
            return self.__network.compartments[compartment_id].edge_color
        else:
            raise ValueError(f"Compartment {compartment_id} not in network.")

    def __setCompartmentProperty(self, compartment_id, property_value,
                                 property_type):
        """Sets a property value on a compartment.

        Args:
            compartment_id (str): id of the compartment
            property_value (str or float): value for the property to be set,
            eg. "#0000ff"
            property_type (str): identifier for the property, eg. "fill"

        Returns: None
        """

        if property_type == "fill":
            self.__network.compartments[compartment_id].fill_color = to_hex(
                    property_value,
                    keep_alpha=True)
        elif property_type == "edge":
            self.__network.compartments[compartment_id].edge_color = to_hex(
                    property_value,
                    keep_alpha=True)
        elif property_type == "line_width":
            self.__network.compartments[
                    compartment_id].line_width = property_value
        else:
            raise ValueError("property_type is not valid: ",
                             property_type)

    def __setCompartmentBasedOnId(self, compartment_id, property_value,
                                  property_type):
        """Set the property on a compartment, based on the type of id list
        provided.

        Args:
            compartment_id (str or list of str): id of the compartment to
                change, or keyword 'all' to change the color of all the
                compartments of that type,
            property_value (str or float): value for the property to be set,
                eg. "#0000ff"
            property_type (str): identifier for the property, eg. "fill"

        Returns: None
        """

        if compartment_id == "all":
            for this_id in self.getCompartmentIds():

                self.__setCompartmentProperty(
                        this_id,
                        property_value,
                        property_type)

        elif (isinstance(compartment_id, str) and
              compartment_id in self.getCompartmentIds()):

            self.__setCompartmentProperty(
                    compartment_id,
                    property_value,
                    property_type)

        elif isinstance(compartment_id, list):
            full_model_compartmentIds = self.getCompartmentIds()
            for this_id in compartment_id:
                if this_id in full_model_compartmentIds:

                    self.__setCompartmentProperty(
                        this_id,
                        property_value,
                        property_type)

                else:
                    raise ValueError(
                            f"Id {this_id} in the input list is invalid, "
                            f"so cannot set color for this id.")
        else:
            raise ValueError(f"Invalid input for compartment ids: "
                             f"{compartment_id}")

    def setCompartmentFillColor(self, compartment_id, fill_color):
        """
        Sets the compartment fill color.

        Args:
            compartment_id (str): id of the compartment to change the color of
                one compartment, or 'all' to change the color of all the
                compartments
            fill_color (str): id of the color

        Returns: None
        """
        self.__validatePlotColor(fill_color)

        property_type = "fill"

        self.__setCompartmentProperty(
                compartment_id,
                fill_color,
                property_type)

    def getCompartmentFillColor(self, compartment_id):
        """Returns the color id for the compartment fill color.

        Args:
            compartment_id(str): id for the compartment

        Returns: str
        """
        if compartment_id in self.__network.compartments:
            return self.__network.compartments[compartment_id].fill_color
        else:
            raise ValueError(f"Compartment {compartment_id} not in network.")

    def getCompartmentLineWidth(self, compartment_id):
        """Returns the line width for the given compartment.

        Args: compartment_id (str): id for the compartment

        Returns: int
        """
        if compartment_id in self.__network.compartments:
            return self.__network.compartments[compartment_id].line_width
        else:
            raise ValueError(f"Reaction {compartment_id} not in network.")

    def setCompartmentLineWidth(self, compartment_id, line_width):
        """
        Sets the line width of the compartment.

        Args:
            compartment_id (str): id of the compartment to change the width of
                one compartment, or 'all' to change the width of all the
                compartments
            line_width (int): numeric value representing the line width

        Returns: None
        """
        property_type = "line_width"

        self.__setCompartmentProperty(
                compartment_id,
                line_width,
                property_type)

    # Node Methods

    def getNodeIds(self,):
        """Returns a list of node ids.

        Args: None

        Returns: list of str
        """
        return list(self.__network.nodes.keys())

    def getNodeColor(self, node_id):
        """Returns the id of the fill color for this node.

        Args:
            node_id (str): id for the node

        Returns: str
        """
        if node_id in self.__network.nodes:
            return self.__network.nodes[node_id].fill_color
        else:
            raise ValueError(f"Species {node_id} not found in network.")

    def getNodeKeywordIds(self, node_keyword):
        """Returns a list of node ids corresponding to the given keyword.

        Args:
            node_keyword(str): 'all', 'boundary', or 'floating'

        Returns: list of str
        """
        if node_keyword == "all":
            return self.getNodeIds()
        elif node_keyword == "boundary":
            return self.getBoundarySpeciesIds()
        elif node_keyword == "floating":
            return self.getFloatingSpeciesIds()
        else:
            return list()

    def __setNodeProperty(self, node_id, property_value, property_type):
        """Sets a property value on a node.

        Args:
            node_id (str): id of the node
            property_value (str or float): value for the property to be set,
            eg. "#0000ff"
            property_type (str): identifier for the property, eg. "fill"

        Returns: None
        """

        if property_type == "fill_and_edge":
            self.__network.nodes[node_id].edge_color = to_hex(
                    property_value,
                    keep_alpha=True)
            self.__network.nodes[node_id].fill_color = to_hex(
                    property_value,
                    keep_alpha=True)
        elif property_type == "fill":
            self.__network.nodes[node_id].fill_color = to_hex(
                    property_value,
                    keep_alpha=True)
        elif property_type == "edge":
            self.__network.nodes[node_id].edge_color = to_hex(
                    property_value,
                    keep_alpha=True)
        elif property_type == "edge_width":
            self.__network.nodes[node_id].edge_width = property_value
        elif property_type == "text_anchor":
            if property_value == "left":
                self.__network.nodes[node_id].text_anchor = "right"
            elif property_value == "right":
                self.__network.nodes[node_id].text_anchor = "left"
            else:
                self.__network.nodes[node_id].text_anchor = property_value
        elif property_type == "vtext_anchor":
            if property_value == "top":
                self.__network.nodes[node_id].vtext_anchor = "bottom"
            elif property_value == "bottom":
                self.__network.nodes[node_id].vtext_anchor = "top"
            else:
                self.__network.nodes[node_id].vtext_anchor = property_value
        elif property_type == "shape":
            self.__network.nodes[node_id].shape = property_value
        elif property_type == "font_size":
            self.__network.nodes[node_id].font_size = property_value
        elif property_type == "font_family":
            self.__network.nodes[node_id].font_family = property_value
        elif property_type == "font_color":
            self.__network.nodes[node_id].font_color = to_hex(
                    property_value,
                    keep_alpha=True)
        elif property_type == "font_style":
            self.__network.nodes[node_id].font_style = property_value
        elif property_type == "font_weight":
            self.__network.nodes[node_id].font_weight = property_value
        else:
            raise ValueError("property_type is not valid: ",
                             property_type)

    def __setKeywordNodesProperty(self, node_keyword, property_value,
                                  property_type):
        """Sets a property value on a node if the node is part of the
        node_keyword group. For example, with the keyword "all", the property
        will be set on all the nodes.

        Args:
            node_keyword (str): "all", "boundary" or "floating"
            property_value (str or float): value for the property to be set,
            eg. "#0000ff"
            property_type (str): identifier for the property, eg. "fill"

        Returns: None
        """
        for node_id in self.getNodeKeywordIds(str(node_keyword).lower()):

            self.__setNodeProperty(node_id, property_value, property_type)

    def __setListOfNodesProperty(self, node_ids, property_value,
                                 property_type):
        """Sets a property value on a list of nodes.

        Args:
            node_ids (list of str): ids of the nodes
            property_value (str or float): value for the property to be set,
            eg. "#0000ff"
            property_type (str): identifier for the property, eg. "fill"

        Returns: None
        """
        full_model_nodeIds = self.getNodeIds()

        for node_id in node_ids:
            if node_id in full_model_nodeIds:

                self.__setNodeProperty(node_id, property_value, property_type)

            else:
                raise ValueError(
                        f"This id in the input list is invalid {node_id}, "
                        f"so cannot set color for this id.")

    def __setNodeBasedOnId(self, node_id, property_value, property_type):
        """Set the property on a node, based on the type of id list provided.

        Args:
            node_id (str or list of str): id of the node to change,
                or keyword 'all', 'boundary', or 'floating' to change the color
                of all the nodes of that type, or a list of node ids to change.
            property_value (str or float): value for the property to be set,
            eg. "#0000ff"
            property_type (str): identifier for the property, eg. "fill"

        Returns: None
        """
        if (isinstance(node_id, str) and
                node_id.lower() in SBMLlayout.NODE_KEYWORDS):

            self.__setKeywordNodesProperty(
                    node_id,
                    property_value,
                    property_type)

        elif (isinstance(node_id, str) and
              node_id in self.getNodeIds()):

            self.__setNodeProperty(node_id, property_value, property_type)

        elif isinstance(node_id, list):

            self.__setListOfNodesProperty(
                    node_id,
                    property_value,
                    property_type)

        else:
            raise ValueError(f"Invalid input for node_id: {node_id}. Node id"
                             f"must be a Species id, a list of Species ids, or"
                             f"a node keyword ({SBMLlayout.NODE_KEYWORDS}).")

    def setNodeColor(self, node_id, node_color):
        """
        Sets the node edge color and fill color to the same value.

        Args:
            node_id (str or list of str): id of the node to change,
                or keyword 'all', 'boundary', or 'floating' to change the color
                of all the nodes of that type, or a list of node ids to change.
            node_color (str): id of the color

        Returns: None
        """
        self.__validatePlotColor(node_color)

        property_type = "fill_and_edge"

        self.__setNodeBasedOnId(node_id, node_color, property_type)

    def getNodeFillColor(self, node_id):
        """Returns the color id for the node fill color.

        Args: node_id(str): id of the node

        Returns: str
        """

        if node_id in self.__network.nodes:
            return self.__network.nodes[node_id].fill_color
        else:
            raise ValueError(f"Species {node_id} not found in network.")

    def setNodeFillColor(self, node_id, fill_color):
        """
        Sets the node fill color.

        Args:
            node_id (str or list of str): id of the node to change,
                or keyword 'all', 'boundary', or 'floating' to change the color
                of all the nodes of that type, or a list of node ids to change.
            fill_color (str): id of the color

        Returns: None
        """
        self.__validatePlotColor(fill_color)

        property_type = "fill"

        self.__setNodeBasedOnId(node_id, fill_color, property_type)

    def getNodeEdgeColor(self, node_id):
        """Returns the color id for the node edge color.

        Args:
            node_id(str): id for the node

        Returns: str
        """
        if node_id in self.__network.nodes:
            return self.__network.nodes[node_id].edge_color
        else:
            raise ValueError(f"Species {node_id} not found in network.")

    def setNodeEdgeColor(self, node_id, edge_color):
        """
        Sets the node edge color.

        Args:
            node_id (str or list of str): id of the node to change,
                or keyword 'all', 'boundary', or 'floating' to change the color
                of all the nodes of that type, or a list of node ids to change.
            edge_color (str): id of the color

        Returns: None
        """
        self.__validatePlotColor(edge_color)

        property_type = "edge"

        self.__setNodeBasedOnId(node_id, edge_color, property_type)

    def getNodeEdgeWidth(self, node_id):
        """Returns the line width for the node edge.

        Args:
            node_id(str): id for the node

        Returns: float
        """
        if node_id in self.__network.nodes:
            return self.__network.nodes[node_id].edge_width
        else:
            raise ValueError(f"Species {node_id} not found in network.")

    def setNodeEdgeWidth(self, node_id, edge_width):
        """
        Sets the line width of the node edge.

        Args:
            node_id (str or list of str): id of the node to change,
                or keyword 'all', 'boundary', or 'floating' to change the color
                of all the nodes of that type, or a list of node ids to change.
            edge_width (float): line width of the edge

        Returns: None
        """
        property_type = "edge_width"

        self.__setNodeBasedOnId(node_id, edge_width, property_type)

    def getNodeTextAnchor(self, node_id):
        """Returns the horizontal text anchor for the node.

        Args:
            node_id(str): id for the node

        Returns: str
        """
        if node_id in self.__network.nodes:
            return self.__network.nodes[node_id].text_anchor
        else:
            raise ValueError(f"Species {node_id} not found in network.")

    def setNodeTextAnchor(self, node_id, text_anchor):
        """
        Sets the horizontal text anchor for the node.

        Args:
            node_id (str or list of str): id of the node to change,
                or keyword 'all', 'boundary', or 'floating' to change the color
                of all the nodes of that type, or a list of node ids to change.
            text_anchor (str): "center", "left", "right"

        Returns: None
        """
        self.__validateTextAnchor(text_anchor, "horizontal")

        property_type = "text_anchor"

        self.__setNodeBasedOnId(node_id, text_anchor, property_type)

    def getNodeVTextAnchor(self, node_id):
        """Returns the vertical text anchor for the node.

        Args:
            node_id(str): id for the node

        Returns: str
        """
        if node_id in self.__network.nodes:
            return self.__network.nodes[node_id].vtext_anchor
        else:
            raise ValueError(f"Species {node_id} not found in network.")

    def setNodeVTextAnchor(self, node_id, vtext_anchor):
        """
        Sets the vertical text anchor for the node.

        Args:
            node_id (str or list of str): id of the node to change,
                or keyword 'all', 'boundary', or 'floating' to change the color
                of all the nodes of that type, or a list of node ids to change.
            vtext_anchor (str): "center", "bottom", "top"

        Returns: None
        """
        self.__validateTextAnchor(vtext_anchor, "vertical")

        property_type = "vtext_anchor"

        self.__setNodeBasedOnId(node_id, vtext_anchor, property_type)

    def getNodeFontSize(self, node_id):
        """Returns the font size of the node text.

        Args:
            node_id (str): id for the node

        Returns: int
        """
        if node_id in self.__network.nodes:
            return self.__network.nodes[node_id].font_size
        else:
            raise ValueError(f"Species {node_id} not found in network.")

    def setNodeFontSize(self, node_id, font_size):
        """Set the font size for the node.

        Args:
            node_id (str): id of the node to change,
                or keyword 'all', 'boundary', or 'floating' to change the color
                of all the nodes of that type, or a list of node ids to change.
            font_size (int or str): matplotlib acceptable values, which are:
                {size in points, 'xx-small', 'x-small', 'small', 'medium',
                'large', 'x-large', 'xx-large'}

        Returns: None
        """
        property_type = "font_size"

        self.__setNodeBasedOnId(node_id, font_size, property_type)

        if node_id == "all":
            node_ids = self.getNodeIds()
        elif node_id == "floating":
            node_ids = self.getFloatingSpeciesIds()
        elif node_id == "boundary":
            node_ids = self.getBoundarySpeciesIds()
        elif node_id in self.__network.nodes:
            node_ids = [node_id]
        else:
            raise ValueError(f"{node_id} not found in network, or is not one",
                             " of the valid id keywords {NODE_KEYWORDS}")

        for this_node_id in node_ids:
            node = self.__network.nodes[this_node_id]
            width = self.__computeNodeWidth(node)
            self.__setNodeWidth(this_node_id, width)
            height = self.__computeNodeHeight(node)
            self.__setNodeHeight(this_node_id, height)

        self.regenerateLayout()

    def getNodeFontName(self, node_id):
        """Returns the font family value, which can be the font family or
        font name.

        Args:
            node_id (str): id for the node

        Returns: str, eg. "Arial" or "serif"
        """
        if node_id in self.__network.nodes:
            return self.__network.nodes[node_id].font_family
        else:
            raise ValueError(f"Species {node_id} not found in network.")

    def setNodeFontName(self, node_id, font_name):
        """Sets the font family for the node, which can be a value for the
        family or name of the font.

        Args:
            node_id (str): id of the node to change,
                or keyword 'all', 'boundary', or 'floating' to change the color
                of all the nodes of that type, or a list of node ids to change.
            font_name (str): value for font family (eg. 'serif')
            or font name (eg. 'Arial')

        Returns: None
        """

        property_type = "font_family"

        self.__setNodeBasedOnId(node_id, font_name, property_type)

    def getNodeFontFamily(self, node_id):
        """Returns the font family value, which can be the font family or
        font name.
        """
        if node_id in self.__network.nodes:
            return self.__network.nodes[node_id].font_family
        else:
            raise ValueError(f"Species {node_id} not found in network.")

    def setNodeFontFamily(self, node_id, font_family):
        """Sets the font family for the node, which can be a value for either
        the family or name of the font.

        Args:
            node_id (str): id of the node to change,
                or keyword 'all', 'boundary', or 'floating' to change the color
                of all the nodes of that type, or a list of node ids to change.
            font_family (str): value for font family (eg. 'serif')
            or font name (eg. 'Arial')

        Returns: None
        """

        property_type = "font_family"

        self.__setNodeBasedOnId(node_id, font_family, property_type)

    def getNodeFontColor(self, node_id):
        """Returns the color of the node's text.

        Args:
            node_id (str): id for the node

        Returns: str
        """
        if node_id in self.__network.nodes:
            return self.__network.nodes[node_id].font_color
        else:
            raise ValueError(f"Species {node_id} not found in network.")

    def setNodeFontColor(self, node_id, font_color):
        """
        Sets the node font color.

        Args:
            node_id (str or list of str): id of the node to change,
                or keyword 'all', 'boundary', or 'floating' to change the color
                of all the nodes of that type, or a list of node ids to change.
            font_color (str): id of the color

        Returns: None
        """
        self.__validatePlotColor(font_color)

        property_type = "font_color"

        self.__setNodeBasedOnId(node_id, font_color, property_type)

    def getNodeFontStyle(self, node_id):
        """Returns the style of the font for the given node.

        Args:
            node_id (str): id for the node

        Returns: str, "italic", "normal", or "oblique"
        """
        if node_id in self.__network.nodes:
            return self.__network.nodes[node_id].font_style
        else:
            raise ValueError(f"Species {node_id} not found in network.")

    def setNodeFontStyle(self, node_id, font_style):
        """
        Sets the node font style.

        Args:
            node_id (str or list of str): id of the node to change,
                or keyword 'all', 'boundary', or 'floating' to change the color
                of all the nodes of that type, or a list of node ids to change.
            font_style (str): Available font styles are normal, italic, and
                oblique.

        Returns: None
        """
        self.__validateFontStyle(font_style)

        property_type = "font_style"

        self.__setNodeBasedOnId(node_id, font_style, property_type)

    def getNodeFontWeight(self, node_id):
        """Returns the weight of the font for the given node.

        Args:
            node_id (str): id for the node

        Returns: str, "bold" or "normal"
        """
        if node_id in self.__network.nodes:
            return self.__network.nodes[node_id].font_weight
        else:
            raise ValueError(f"Species {node_id} not found in network.")

    def setNodeFontWeight(self, node_id, font_weight):
        """
        Sets the node font weight.

        Args:
            node_id (str or list of str): id of the node to change,
                or keyword 'all', 'boundary', or 'floating' to change the color
                of all the nodes of that type, or a list of node ids to change.
            font_weight (str): Available font weights are normal or bold.

        Returns: None
        """
        self.__validateFontWeight(font_weight)

        property_type = "font_weight"

        self.__setNodeBasedOnId(node_id, font_weight, property_type)

    def getNodeWidth(self, node_id):
        """Returns the width of the node.

        Args:
            node_id (str): id for the node

        Returns: float
        """
        if node_id in self.__network.nodes:
            return self.__network.nodes[node_id].width
        else:
            raise ValueError(f"Species {node_id} not found in network.")

    def getNodeHeight(self, node_id):
        """Returns the height of the node.

        Args:
            node_id (str): id for the node

        Returns: float
        """
        if node_id in self.__network.nodes:
            return self.__network.nodes[node_id].height
        else:
            raise ValueError(f"Species {node_id} not found in network.")

    def __setNodeWidth(self, node_id, width):
        """Sets the width of the node.

        Args:
            node_id (str): id for the node
            width (float): width in data coordinates for the node

        Returns: None
        """
        if node_id in self.__network.nodes:
            node = self.__network.nodes[node_id]
            h_node_id = node_id.encode('utf-8')
            h_node = sbnw.nw_getNodepFromId(self.__h_network, h_node_id)
            sbnw.node_setWidth(h_node, width)
            node.width = width
            node.lower_left_point = [node.center.x - node.width/2,
                                     node.center.y - node.height/2]
        else:
            raise ValueError(f"Species {node_id} not found in network.")

    def __setNodeHeight(self, node_id, height):
        """Sets the height of the node.

        Args:
            node_id (str): id for the node
            height (float): height in data coordinates for the node

        Returns: None
        """
        if node_id in self.__network.nodes:
            node = self.__network.nodes[node_id]
            h_node_id = node_id.encode('utf-8')
            h_node = sbnw.nw_getNodepFromId(self.__h_network, h_node_id)
            sbnw.node_setHeight(h_node, height)
            node.height = height
            node.lower_left_point = [node.center.x - node.width/2,
                                     node.center.y - node.height/2]
        else:
            raise ValueError(f"Species {node_id} not found in network.")

    def getNodeName(self, node_id):
        """Returns the name of the node.

        Args:
            node_id (str): id for the node

        Returns: str
        """
        if node_id in self.__network.nodes:
            return self.__network.nodes[node_id].name
        else:
            raise ValueError(f"Species {node_id} not found in network.")

    def getNodeLowerLeftPoint(self, node_id):
        """Returns the point for the node's lower left corner.

        Args:
            node_id (str): id for the node

        Returns: point which has fields x and y
        """
        if node_id in self.__network.nodes:
            return self.__network.nodes[node_id].lower_left_point
        else:
            raise ValueError(f"Species {node_id} not found in network.")

    def getBoundarySpeciesIds(self,):
        """
        Gets the id values of the Species who have boundaryCondition set to
        True.

        Args:
            None

        Returns: list of Species ids
        """
        model = self.__doc.getModel()
        speciesList = model.getListOfSpecies()

        boundarySpeciesIds = list()

        for species in speciesList:
            if species.getBoundaryCondition() is True:
                boundarySpeciesIds.append(species.getId())

        return boundarySpeciesIds

    def getFloatingSpeciesIds(self,):
        """
        Gets the id values of the Species who have boundaryCondition set to
        False.

        Args:
            None

        Returns: list of Species ids
        """
        model = self.__doc.getModel()
        speciesList = model.getListOfSpecies()

        floatingSpeciesIds = list()

        for species in speciesList:
            if species.getBoundaryCondition() is False:
                floatingSpeciesIds.append(species.getId())

        return floatingSpeciesIds

    # Reaction Methods

    def getReactionIds(self,):
        """
        Gets the ids of the reactions in the model.

        Args: None

        Returns: list of Reaction ids
        """
        return list(self.__network.reactions.keys())

    def __setCurvePropertyByResolvingValueType(self, curve, value, value_type):
        """Generic function which sets a property value.

        Args:
            curve (libsbml_draw.network.Curve): the curve on which to set a
                property
            value (str or float): the value for the property to be set,
                eg. #0000ff for a color or 2 for a curve width
            value_type (str): an identifier for the property, eg. "fill"

        Returns: None
        """
        if value_type == "both" or value_type == "fill":
            curve.fill_color = to_hex(value, keep_alpha=True)
        if value_type == "both" or value_type == "edge":
            curve.edge_color = to_hex(value, keep_alpha=True)
        if value_type == "width":
            curve.curve_width = value

    def __setCurveProperty(self, curve, value, value_type, role_name, species):
        """Generic function which sets a property on a curve.  If role_name
        and/or species are given, the curve values for these properties must
        match in order for the property to be set.

        Args:
            curve (libsbml_draw.network.Curve): the curve on which to set a
                property
            value (str or float): the value for the property to be set,
                eg. #0000ff for a color or 2 for a curve width
            value_type (str): an identifier for the property, eg. "fill"
            role_name (optional, str): role of the curve in the reaction,
                for example, "product"
            species (optional, str): species to which the curve is connected,
                for example, "A" or "Node0"

        Returns: None
        """
        if role_name:
            if curve.role_name.lower() == role_name.lower():
                if species:
                    if curve.species.lower() == species.lower():
                        self.__setCurvePropertyByResolvingValueType(
                                curve,
                                value,
                                value_type)
                    else:
                        pass
                else:
                    self.__setCurvePropertyByResolvingValueType(
                            curve,
                            value,
                            value_type)
            else:
                pass

        elif species:

            if curve.species.lower() == species.lower():
                self.__setCurvePropertyByResolvingValueType(
                        curve,
                        value,
                        value_type)
            else:
                pass
        else:
            self.__setCurvePropertyByResolvingValueType(
                    curve,
                    value,
                    value_type)

    def setReactionColor(self, reaction_id, reaction_color, role_name=None,
                         species=None):
        """
        Sets the reaction edge color and fill color to the same value.  If the
        role or species args are set, then the color is set only for curves in
        a reaction which have that role or are connected to that species.

        Args:
            reaction_id (str): id of the reaction to change the color of one
                reaction, or 'all' to change the color of all the reactions
            reaction_color (str): id of the color
            role_name (optional, str): role of the curve in the reaction,
                for example, "product"
            species (optional, str): species to which the curve is connected,
                for example, "A" or "Node0"

        Returns: None
        """
        self.__validatePlotColor(reaction_color)

        edge_or_fill_color = "both"

        if reaction_id == "all":

            self.__setAllReactions(
                    reaction_color,
                    edge_or_fill_color,
                    role_name,
                    species)

        elif (isinstance(reaction_id, str) and
              reaction_id in self.getReactionIds()):

            self.__setOneReactionById(
                    reaction_id,
                    reaction_color,
                    edge_or_fill_color,
                    role_name,
                    species)

        elif isinstance(reaction_id, list):

            self.__setListOfReactions(
                    reaction_id,
                    reaction_color,
                    edge_or_fill_color,
                    role_name,
                    species)

        else:
            raise ValueError(f"Invalid input for reaction ids: {reaction_id}")

    def getReactionEdgeColor(self, reaction_id):
        """Returns the color id for the edge color of the reaction.

        Args:
            reaction_id (str): id for the reaction

        Returns: list of tuples of (curve species, curve role name, and curve
            color) for each curve in the reaction
        """
        property_type = "edge"

        return self.__getReactionCurveValues(reaction_id, property_type)

    def __setAllReactions(self, property_value, property_type, role_name,
                          species):
        """Sets a property value for all curves for all reactions in the
        network.  If role_name and/or species are given, the values on the
        curve for these must match, in order for the property to be set.

        Args:
            property_value (str or float): value of the property to be set
            property_type (str): identifier the property to be set, eg. "fill"
            role_name (optional, str): role of the curve in the reaction,
                for example, "product"
            species (optional, str): species to which the curve is connected,
                for example, "A" or "Node0"

        Returns: None
        """
        for reaction in self.__network.reactions.values():
            for curve in reaction.curves:
                self.__setCurveProperty(
                        curve,
                        property_value,
                        property_type,
                        role_name,
                        species)

    def __setOneReactionById(self, reaction_id, property_value, property_type,
                             role_name, species):
        """Sets a property value for all curves for one reaction in the
        network.  If role_name and/or species are given, the values on the
        curve for these must match, in order for the property to be set.

        Args:
            property_value (str or float): value of the property to be set
            property_type (str): identifier the property to be set, eg. "fill"
            role_name (optional, str): role of the curve in the reaction,
                for example, "product"
            species (optional, str): species to which the curve is connected,
                for example, "A" or "Node0"

        Returns: None
        """
        for curve in self.__network.reactions[reaction_id].curves:
            self.__setCurveProperty(
                    curve,
                    property_value,
                    property_type,
                    role_name,
                    species)

    def __setListOfReactions(self, reaction_ids, property_value, property_type,
                             role_name, species):
        """Sets a property value for all curves for a list of reactions in the
        network.  If role_name and/or species are given, the values on the
        curve for these must match, in order for the property to be set.

        Args:
            property_value (str or float): value of the property to be set
            property_type (str): identifier the property to be set, eg. "fill"
            role_name (optional, str): role of the curve in the reaction,
                for example, "product"
            species (optional, str): species to which the curve is connected,
                for example, "A" or "Node0"

        Returns: None
        """
        full_model_reactionIds = self.getReactionIds()

        for this_id in reaction_ids:

            if this_id in full_model_reactionIds:

                for curve in self.__network.reactions[this_id].curves:

                    self.__setCurveProperty(
                            curve,
                            property_value,
                            property_type,
                            role_name,
                            species)
            else:
                raise ValueError(
                        f"This id in the input list is invalid {this_id}, "
                        f"so cannot set color for this id.")

    def setReactionEdgeColor(self, reaction_id, edge_color, role_name=None,
                             species=None):
        """
        Sets the reaction edge color for all curves in the reaction.  If the
        role or species args are set, then the color is set only for curves in
        a reaction which have that role or are connected to that species.

        Args:
            reaction_id (str): id of the reaction to change the color of one
                reaction, or 'all' to change the color of all the reactions
            edge_color (str): id of the color
            role_name (optional, str): role of the curve in the reaction,
                for example, "product"
            species (optional, str): species to which the curve is connected,
                for example, "A" or "Node0"

        Returns: None
        """
        self.__validatePlotColor(edge_color)

        edge_or_fill_color = "edge"

        if reaction_id == "all":

            self.__setAllReactions(
                    edge_color,
                    edge_or_fill_color,
                    role_name,
                    species)

        elif (isinstance(reaction_id, str) and
              reaction_id in self.getReactionIds()):

            self.__setOneReactionById(
                    reaction_id,
                    edge_color,
                    edge_or_fill_color,
                    role_name,
                    species)

        elif isinstance(reaction_id, list):

            self.__setListOfReactions(
                    reaction_id,
                    edge_color,
                    edge_or_fill_color,
                    role_name,
                    species)

        else:
            raise ValueError(f"Invalid input for reaction ids: {reaction_id}")

    def __getReactionCurveValues(self, reaction_id, property_type):
        """Returns the values for the property_type for each curve of the
        reaction, for example, the "fill color" could be a property type.

        Args:
            reaction_id (str): id for the reaction
            property_type (str): specifies the curve property of interest

        Returns: list of tuples of (curve species, curve role name, and curve
            property_value) for each curve in the reaction
        """
        if reaction_id in self.__network.reactions:
            curve_colors = []

            for curve in self.__network.reactions[reaction_id].curves:

                if property_type == "fill":
                    property_value = curve.fill_color
                elif property_type == "edge":
                    property_value = curve.edge_color
                elif property_type == "width":
                    property_value = curve.curve_width
                else:
                    raise ValueError("Invalid property type: ", property_type)

                curve_colors.append((curve.species, curve.role_name,
                                     property_value))
        else:
            raise ValueError(f"Reaction {reaction_id} not found in network.")

        return curve_colors

    def getReactionFillColor(self, reaction_id):
        """Returns the color id for the fill color of the reaction.

        Args:
            reaction_id (str): id for the reaction

        Returns: list of tuples of (curve species, curve role name, and curve
            color) for each curve in the reaction
        """
        property_type = "fill"

        return self.__getReactionCurveValues(reaction_id, property_type)

    def setReactionFillColor(self, reaction_id, fill_color, role_name=None,
                             species=None):
        """
        Sets the reaction fill color for all curves in the reaction.  If the
        role or species args are set, then the color is set only for curves in
        a reaction which have that role or are connected to that species.

        Args:
            reaction_id (str): id of the reaction to change the color of one
                reaction, or 'all' to change the color of all the reactions
            fill_color (str): id of the color
            role_name (optional, str): role of the curve in the reaction,
                for example, "product"
            species (optional, str): species to which the curve is connected,
                for example, "A" or "Node0"

        Returns: None
        """
        self.__validatePlotColor(fill_color)

        property_type = "fill"

        if reaction_id == "all":

            self.__setAllReactions(
                    fill_color,
                    property_type,
                    role_name,
                    species)

        elif (isinstance(reaction_id, str) and
              reaction_id in self.getReactionIds()):

            self.__setOneReactionById(
                    reaction_id,
                    fill_color,
                    property_type,
                    role_name,
                    species)

        elif isinstance(reaction_id, list):

            self.__setListOfReactions(
                    reaction_id,
                    fill_color,
                    property_type,
                    role_name,
                    species)

        else:
            raise ValueError(f"Invalid input for reaction ids: {reaction_id}")

    def getReactionCurveWidth(self, reaction_id):
        """Returns the curve width for all curves of the reaction.

        Args:
            reaction_id (str): id for the reaction

        Returns: list of tuples of (curve species, curve role name, and curve
            width) for each curve in the reaction
        """
        property_type = "width"

        return self.__getReactionCurveValues(reaction_id, property_type)

    def setReactionCurveWidth(self, reaction_id, curve_width, role_name=None,
                              species=None):
        """
        Sets the line width of the curve for all curves in the reaction.  If
        the role or species args are set, then the color is set only for curves
        in a reaction which have that role or are connected to that species.

        Args:
            reaction_id (str): id of the reaction to change the width of one
                reaction, or 'all' to change the width of all the reactions
            curve_width (int): numeric value representing the line width
            role_name (optional, str): role of the curve in the reaction,
                for example, "product"
            species (optional, str): species to which the curve is connected,
                for example, "A" or "Node0"

        Returns: None
        """
        property_type = "width"

        if reaction_id == "all":

            self.__setAllReactions(
                    curve_width,
                    property_type,
                    role_name,
                    species)

        elif (isinstance(reaction_id, str) and
              reaction_id in self.getReactionIds()):

            self.__setOneReactionById(
                    reaction_id,
                    curve_width,
                    property_type,
                    role_name,
                    species)

        elif isinstance(reaction_id, list):

            self.__setListOfReactions(
                    reaction_id,
                    curve_width,
                    property_type,
                    role_name,
                    species)

        else:
            raise ValueError(f"Invalid input for reaction ids: {reaction_id}")

    # Render Methods

    def __addRenderInformation(self,):
        """Add render information to the model's libsbml.SBMLDocument.
        A LocalStyle element is added for each node, reaction, and compartment.
        If any of these elements already exist, they are first removed.

        Args: None

        Returns: None
        """
        renderInfo = Render(self.__doc, self.__layout_number)

        if (len(renderInfo.speciesToGlyphs) == 0 or
                len(renderInfo.reactionToGlyphs) == 0):
            pass

        else:
            renderInfo.addRenderInformation(self.__network)
            # update doc, it will be used to write new output xml file
            self.__doc = renderInfo.doc

    def __applyRenderInformation(self,):
        """Apply the render information in the SBML file to nodes, reactions,
        and compartments in the model's network.

        Args: None

        Returns: None
        """
        renderInfo = Render(self.__doc, self.__layout_number)
        renderInfo.applyRenderInformation(self.__network)

    # Plotting Methods

    def getArrowheadStyle(self, role):
        """Returns the arrowhead style for the given role.

        Args:
            role (int): which role

        Returns: int
        """
        return sbnw.arrowheadGetStyle(role)

    def setArrowheadStyle(self, role, style):
        """Set the arrowhead style for the given role.

        Args:
            role (int): which role
            style (int): which style

        Returns: None
        """
        sbnw.arrowheadSetStyle(role, style)

    def getArrowheadNumVerts(self, style):
        """Returns the number of vertices in the arrowhead of the given style.

        Args:
            style (int): which arrowhead style

        Returns:int
        """
        return sbnw.arrowheadStyleGetNumVerts(style)

    def getArrowheadVert(self, style, vertex_number):
        """Returns a point for the given vertex_number, given an arrowhead
        style.

        Args:
            style (int): which arrowhead style
            vertex_number (int): specify the vertex in the arrowhead

        Returns: point with fields x and y
        """
        number_of_arrowhead_styles = self.getArrowheadNumStyles()

        if style in range(number_of_arrowhead_styles):
            number_of_arrowhead_vertices = self.getArrowheadNumVerts(style)

            if vertex_number in range(number_of_arrowhead_vertices):
                return sbnw.arrowheadStyleGetVert(style, vertex_number)

            elif number_of_arrowhead_vertices == 0:
                    raise ValueError(f"style {style} has no vertices")
            else:
                raise ValueError(f"vertex_number must be in the range "
                                 f"0 - {number_of_arrowhead_vertices}")
        else:
            raise ValueError(f"style {style} must be in range "
                             f"0 - {number_of_arrowhead_styles}")

    def getArrowheadNumStyles(self,):
        """Returns the number of arrowhead styles available.

        Args: None

        Returns: int
        """
        return sbnw.arrowheadNumStyles()

    def drawNetwork(self, save_file_name=None, show=True, dpi=72,
                    width_shift=.25, height_shift=.25, scaling_factor=1):
        """Draws the network to screen.  The figure can be saved.

        Args:
            save_file_name (optional, str): save figure to this file
            show (optional, bool): if True, display the network on screen
            dpi (optional, int): desired dots-per-inch for the figure
            width_shift (optional, float): size in inches of the left and right
                borders
            height_shift (optional, float): size in inches of the bottom and
                top borders
            scaling_factor (option, float): decrease or increase the size of
                the figure using this factor; example, 0.5 results in reducing
                the figure size by one-half

        Returns: matplotlib.figure.Figure
        """
        fig = createNetworkFigure(self, self.__arrowhead_scale, show, dpi,
                                  width_shift, height_shift, scaling_factor)
        if(save_file_name):
            bg_color = self.__network.bg_color
            fig.savefig(save_file_name, facecolor=bg_color)

        return fig

    def __getLastError(self,):
        """Returns the last error from the c_api code.

        Args: None

        Returns: str
        """
        return sbnw.getLastError().decode('utf-8')

    def getSBMLString(self,):
        """Returns the SBML string for the model.

        Args: None

        Returns: str
        """
        return tesbml.SBMLToString(self.__doc)

    def setArrowheadScale(self, role, arrowhead_scale):
        """Set a value for matplotlib's mutation_scale to change the
        size of the arrowhead for a given role.  The default value is 10.
        Bigger values result in bigger arrowheads.

        Args:
            arrowhead_scale(int): passed on to matplotlib
            role(int): role of the reaction

        Returns: None
        """
        if role in range(self.getNumberOfRoles()):
            if isinstance(arrowhead_scale, int) and arrowhead_scale > 0:
                self.__arrowhead_scale[role] = arrowhead_scale
            else:
                raise ValueError(f"Arrowhead scale {arrowhead_scale} must be "
                                 f"an integer greater than 0.")
        else:
            raise ValueError(f"Role {role} is not in the allowable range: "
                             f"{self.getNumberOfRoles()}")

    def getArrowheadScale(self, role):
        """Returns the arrowhead scale for the given role.  Bigger values
        result in bigger arrowheads.

        Args: role(int)

        Returns: int
        """
        if role in self.__arrowhead_scale:
            return self.__arrowhead_scale[role]
        else:
            raise ValueError(f"Role {role} must be in the range 0 - "
                             f"{self.getNumberOfRoles() - 1}")

    def getNumberOfRoles(self,):
        """
        Args: None

        Returns: int
        """
        return len(sbnw.ROLES)

    def getReactionBezierPoints(self, reaction_id):
        """Returns a list of Bezier points (start, end, control1, control2) for
        each curve in the reaction.

        Args:
            reaction_id(str): id for the reaction

        Returns: list, of BezierPoints named tuple of tuples
        """
        bezier_points = list()

        if reaction_id in self.getReactionIds():

            for curve in self.__network.reactions[reaction_id].curves:

                bezier_points.append(BezierPoints(
                        (curve.start_point.x, curve.start_point.y),
                        (curve.end_point.x, curve.end_point.y),
                        (curve.control_point_1.x, curve.control_point_1.y),
                        (curve.control_point_2.x, curve.control_point_2.y)))
        else:
            raise ValueError(f"Reaction {reaction_id} is not in the network.")

        return bezier_points
