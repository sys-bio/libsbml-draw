"""Creates a Python interface to load, display and manipulate
models defined in an SBML file, making use of a c API and libsbml."""

from collections import namedtuple
import os

from matplotlib.colors import is_color_like

import libsbml

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
                 autoComputeLayout=False):

        self.__sbml_source = sbml_source
        self.__layout_number = layout_number
        self.__fitWindow = fitToWindow

        if self._validate_layout_alg_options(layout_alg_options):
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

            if SBMLlayout._validate_sbml_filename(self.__sbml_source):
                self.__h_model = sbnw.loadSBMLFile(self.__sbml_source)
            else:
                if self.__sbml_source.startswith("<?xml"):
                        self.__h_model = sbnw.loadSBMLString(
                                self.__sbml_source)
                else:
                    raise ValueError(f"File {self.__sbml_source} "
                                     f"does not exist.")

            if self.__h_model == 0:
                raise ValueError("SBML source cannot be parsed by libsbml.")

            self.__h_layout_info = sbnw.processLayout(self.__h_model)
            self.__h_network = sbnw.getNetworkp(self.__h_layout_info)
            self.__h_canvas = sbnw.getCanvasp(self.__h_layout_info)
            self.__layoutSpecified = True if sbnw.isLayoutSpecified(
                    self.__h_network) else False
            self.__autoComputeLayout = autoComputeLayout

            # create layout, if it doesn't already exist
            if not self.__layoutSpecified or self.__autoComputeLayout:
                self.__randomizeLayout()
                self.__doLayoutAlgorithm()

                # capture the render info here
                self.__doc = libsbml.readSBMLFromString(
                        self.__getSBMLWithLayoutString())

                self.__network = self.__createNetwork()
                self.__applyRenderInformation()

                # compute and set width and height for node boxes
                for node in self.__network.nodes.values():
                    # pad the width (default, 2 additional chars) and
                    # pad the height (default, 1 additional char)
                    width = (len(node.name) +
                             SBMLlayout.WIDTH_PADDING)*node.font_size
                    node_name_height = 1
                    height = (node_name_height +
                              SBMLlayout.HEIGHT_PADDING)*node.font_size
                    self.__setNodeWidth(node.id, width)
                    self.__setNodeHeight(node.id, height)

                self.regenerateLayout()

            else:
                if SBMLlayout._validate_sbml_filename(sbml_source):
                    self.__doc = libsbml.readSBMLFromFile(sbml_source)
                else:
                    self.__doc = libsbml.readSBMLFromString(sbml_source)

            if len(self.__fitWindow) == 4:
                self.__fitToWindow(self.__fitWindow[0], self.__fitWindow[1],
                                   self.__fitWindow[2], self.__fitWindow[3])
            else:
                pass

            sbnw.layout_alignToOrigin(self.__h_layout_info, 0, 0)

            print("canvas width: ", sbnw.canvas_getWidth(self.__h_canvas))
            print("canvas height: ", sbnw.canvas_getHeight(self.__h_canvas))

            self.__network = self.__createNetwork()

            self.__applyRenderInformation()

            self.__arrowhead_scale = {key: 10 for key in
                                      range(self.getNumberOfRoles())}

        else:  # User can separately load a file
            pass

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

    def setLayoutAlgorithmOptions(self, k=None, grav=None, baryx=None,
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
        if grav:
            self.__layout_alg_options.grav = grav
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
            k (float):

        Returns: None
        """
        self.__layout_alg_options.k = k

    def setLayoutAlgorithm_grav(self, gravity):
        """Set the Fruchterman-Reingold layout algorithm parameter 'grav'.

        Args:
            gravity (float):

        Returns: None
        """
        self.__layout_alg_options.grav = gravity

    def setLayoutAlgorithm_baryx(self, baryx):
        """Set the Fruchterman-Reingold layout algorithm parameter 'baryx'.

        Args:
            baryx (float):

        Returns: None
        """
        self.__layout_alg_options.baryx = baryx

    def setLayoutAlgorithm_baryy(self, baryy):
        """Set the Fruchterman-Reingold layout algorithm parameter 'baryy'.

        Args:
            baryy (float):

        Returns: None
        """
        self.__layout_alg_options.baryy = baryy

    def setLayoutAlgorithm_autobary(self, autobary):
        """Set the Fruchterman-Reingold layout algorithm parameter 'autobary'.

        Args:
            autobary (int):

        Returns: None
        """
        self.__layout_alg_options.autobary = autobary

    def setLayoutAlgorithm_padding(self, padding):
        """Set the Fruchterman-Reingold layout algorithm parameter 'padding'.

        Args:
            padding (float):

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
              "gravity ", self.__layout_alg_options.grav, "\n",
              "baryx ", self.__layout_alg_options.baryx, "\n",
              "baryy ", self.__layout_alg_options.baryy, "\n",
              "autobary ", self.__layout_alg_options.autobary, "\n",
              "padding ", self.__layout_alg_options.padding, "\n"
              )

    # Validation Methods

    def _validate_sbml_filename(sbml_filename):
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

    def _validate_layout_alg_options(self, layout_alg_options):
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

    def _validatePlotColor(plot_color):
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

    def _validateFontStyle(font_style):
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

        self.__doc = libsbml.readSBMLFromString(
            self.__getSBMLWithLayoutString())

        self.__network = self.__createNetwork()

        # apply render information, if any
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

        self.__doc = libsbml.readSBMLFromString(
                self.__getSBMLWithLayoutString())

        self.__updateNetworkLayout()

    def __randomizeLayout(self,):
        """Give the layout a starting point

        Args: None
        Returns: None
        """
        sbnw.randomizeLayout(self.__h_layout_info)

    def __doLayoutAlgorithm(self,):
        """Run the Fruchterman-Reingold Layout Algorithm

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

    def _describeModel(self,):
        """Provides a summary of the model built from the SBML file.

        Args: None
        Returns: None
        """
        print()
        # print("sbml filename: ", self.__sbml_source)
        print("layout number: ", self.__layout_number)
        print("layout is specified: ", self.__layoutSpecified)
        print("autoComputeLayout: ", self.__autoComputeLayout)
        print("number of Compartments: ", self.getNumberOfCompartments())
        print("number of Nodes: ", self.getNumberOfNodes())
        print("number of Reactions: ", self.getNumberOfReactions())

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
        return sbnw.nw_getNumNodes(self.__h_network)

    def getNumberOfReactions(self,):
        """Returns the number of reactions in the model.

        Args: None
        Returns: None
        """
        return sbnw.nw_getNumRxns(self.__h_network)

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
            self.__doc = libsbml.readSBMLFromString(
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
                alias_index = node_id.split("_")[1]
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
                alias_index = node_id.split("_")[1]
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

    def setNodeCentroid(self, node_id, x, y):
        """Sets the center point of the node.

        Args:
            node_id (str): id for the node
            x (float): new x coordinate
            y (float): new y coordinate

        Returns: None
        """
        if node_id in self.getNodeIds():

            node = self.__network.nodes[node_id]

            centroid = node.center
            centroid.x = x
            centroid.y = y

            # aliased nodes have the id of the original node
            if node.id in self.__network.aliasedNodes:

                alias_index = node_id.split("_")[1]
                h_node_id = node.id.encode('utf-8')
                h_node = sbnw.nw_getNodepFromId(self.__h_network, h_node_id)
                h_alias_node = sbnw.nw_getAliasInstancep(
                        self.__h_network,
                        h_node,
                        alias_index)
                sbnw.node_setCentroid(h_alias_node, centroid)
            # node is not an alias
            else:
                h_node_id = node_id.encode('utf-8')
                h_node = sbnw.nw_getNodepFromId(self.__h_network, h_node_id)
                sbnw.node_setCentroid(h_node, centroid)

            for nr in range(sbnw.nw_getNumRxns(self.__h_network)):
                # sbnw.nw_recenterJunctions(self.__h_network)
                h_reaction = sbnw.nw_getReactionp(self.__h_network, nr)
                if sbnw.reaction_hasSpec(h_reaction, h_node):
                    sbnw.reaction_recenter(h_reaction)
            sbnw.nw_rebuildCurves(self.__h_network)

            self.__updateNetworkLayout()
            self.__doc = libsbml.readSBMLFromString(
                        self.__getSBMLWithLayoutString())
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
        self.__addRenderInformation()
        libsbml.writeSBMLToFile(self.__doc, out_file_name)

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
        SBMLlayout._validatePlotColor(edge_color)

        if compartment_id == "all":
            for compartment in self.__network.compartments.values():
                compartment.edge_color = edge_color

        elif (isinstance(compartment_id, str) and
              compartment_id in self.getCompartmentIds()):
            self.__network.compartments[compartment_id].edge_color = edge_color

        elif isinstance(compartment_id, list):
            full_model_compartmentIds = self.getCompartmentIds()
            for this_id in compartment_id:
                if this_id in full_model_compartmentIds:
                    self.__network.compartments[this_id].edge_color = \
                        edge_color
                else:
                    raise ValueError(
                            f"Id {this_id} in the input list is invalid, "
                            f"so cannot set color for this id.")
        else:
            raise ValueError(f"Invalid input for compartment ids: "
                             f"{compartment_id}")

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
        SBMLlayout._validatePlotColor(fill_color)

        if compartment_id == "all":
            for compartment in self.__network.compartments.values():
                compartment.fill_color = fill_color

        elif (isinstance(compartment_id, str) and
              compartment_id in self.getCompartmentIds()):
            self.__network.compartments[compartment_id].fill_color = fill_color

        elif isinstance(compartment_id, list):
            full_model_compartmentIds = self.getCompartmentIds()
            for this_id in compartment_id:
                if this_id in full_model_compartmentIds:
                    self.__network.compartments[this_id].fill_color = \
                        fill_color
                else:
                    raise ValueError(
                            f"Id {this_id} in the input list is invalid, "
                            f"so cannot set color for this id.")
        else:
            raise ValueError(f"Invalid input for compartment ids: "
                             f"{compartment_id}")

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
        if compartment_id == "all":
            for compartment in self.__network.compartments.values():
                compartment.line_width = line_width

        elif (isinstance(compartment_id, str) and
              compartment_id in self.getCompartmentIds()):
            self.__network.compartments[compartment_id].line_width = line_width

        elif isinstance(compartment_id, list):
            full_model_compartmentIds = self.getCompartmentIds()
            for this_id in compartment_id:
                if this_id in full_model_compartmentIds:
                    self.__network.compartments[this_id].line_width = \
                        line_width
                else:
                    raise ValueError(
                            f"Id in the input list is invalid {this_id}, so "
                            f"cannot set compartment line width for this id.")
        else:
            raise ValueError(f"Invalid input for compartment ids: "
                             f"{compartment_id}")

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
        SBMLlayout._validatePlotColor(node_color)

        if (isinstance(node_id, str) and
                node_id.lower() in SBMLlayout.NODE_KEYWORDS):
            for node_id in self.getNodeKeywordIds(str(node_id).lower()):
                self.__network.nodes[node_id].edge_color = node_color
                self.__network.nodes[node_id].fill_color = node_color

        elif (isinstance(node_id, str) and
              node_id in self.getNodeIds()):
            self.__network.nodes[node_id].edge_color = node_color
            self.__network.nodes[node_id].fill_color = node_color

        elif isinstance(node_id, list):
            full_model_nodeIds = self.getNodeIds()
            for this_id in node_id:
                if this_id in full_model_nodeIds:
                    self.__network.nodes[this_id].edge_color = node_color
                    self.__network.nodes[this_id].fill_color = node_color
                else:
                    raise ValueError(
                            f"This id in the input list is invalid {this_id}, "
                            f"so cannot set color for this id.")
        else:
            raise ValueError(f"Invalid input for node_id: {node_id}. Node id"
                             f"must be a Species id, a list of Species ids, or"
                             f"a node keyword ({SBMLlayout.NODE_KEYWORDS}).")

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
        SBMLlayout._validatePlotColor(fill_color)

        if (isinstance(node_id, str) and
                node_id.lower() in SBMLlayout.NODE_KEYWORDS):
            for node_id in self.getNodeKeywordIds(str(node_id).lower()):
                self.__network.nodes[node_id].fill_color = fill_color

        elif (isinstance(node_id, str) and
              node_id in self.getNodeIds()):
            self.__network.nodes[node_id].fill_color = fill_color

        elif isinstance(node_id, list):
            full_model_nodeIds = self.getNodeIds()
            for this_id in node_id:
                if this_id in full_model_nodeIds:
                    self.__network.nodes[this_id].fill_color = fill_color
                else:
                    raise ValueError(
                            f"This id in the input list is invalid {this_id}, "
                            f"so cannot set node fill color for this id.")
        else:
            raise ValueError(f"Invalid input for node_id: {node_id}. "
                             f"Node id must be a Species id, a list of "
                             f"Species ids, or a node keyword "
                             f"({SBMLlayout.NODE_KEYWORDS} ).")

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
        SBMLlayout._validatePlotColor(edge_color)

        if (isinstance(node_id, str) and
                node_id.lower() in SBMLlayout.NODE_KEYWORDS):
            for node_id in self.getNodeKeywordIds(str(node_id).lower()):
                self.__network.nodes[node_id].edge_color = edge_color
        elif (isinstance(node_id, str) and
              node_id in self.getNodeIds()):
            self.__network.nodes[node_id].edge_color = edge_color
        elif isinstance(node_id, list):
            full_model_nodeIds = self.getNodeIds()
            for this_id in node_id:
                if this_id in full_model_nodeIds:
                    self.__network.nodes[this_id].edge_color = edge_color
                else:
                    raise ValueError(
                            f"This id in the input list is invalid {this_id}, "
                            f"so cannot set node edge color for this id.")
        else:
            raise ValueError(f"Invalid input for node_id: {node_id}. "
                             f"Node id must be a Species id, a list of "
                             f"Species ids, or a node keyword "
                             f"({SBMLlayout.NODE_KEYWORDS} ).")

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

        if (isinstance(node_id, str) and
                node_id.lower() in SBMLlayout.NODE_KEYWORDS):
            for node_id in self.getNodeKeywordIds(str(node_id).lower()):
                self.__network.nodes[node_id].edge_width = edge_width
        elif (isinstance(node_id, str) and
              node_id in self.getNodeIds()):
            self.__network.nodes[node_id].edge_width = edge_width
        elif isinstance(node_id, list):
            full_model_nodeIds = self.getNodeIds()
            for this_id in node_id:
                if this_id in full_model_nodeIds:
                    self.__network.nodes[this_id].edge_width = edge_width
                else:
                    raise ValueError(
                            f"This id in the input list is invalid {this_id}, "
                            f"so cannot set node edge width for this id.")
        else:
            raise ValueError(f"Invalid input for node_id: {node_id}. "
                             f"Node id must be a Species id, a list of "
                             f"Species ids, or a node keyword "
                             f"({SBMLlayout.NODE_KEYWORDS} ).")

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
            node_id (str): id for the node
            font_size (int or str): matplotlib acceptable values, which are:
                {size in points, 'xx-small', 'x-small', 'small', 'medium',
                'large', 'x-large', 'xx-large'}

        Returns: None
        """
        if (isinstance(node_id, str) and
                node_id.lower() in SBMLlayout.NODE_KEYWORDS):
            for node_id in self.getNodeKeywordIds(str(node_id).lower()):
                self.__network.nodes[node_id].font_size = font_size

        elif (isinstance(node_id, str) and
              node_id in self.getNodeIds()):
            self.__network.nodes[node_id].font_size = font_size

        elif isinstance(node_id, list):
            full_model_nodeIds = self.getNodeIds()
            for this_id in node_id:
                if this_id in full_model_nodeIds:
                    self.__network.nodes[this_id].font_size = font_size
                else:
                    raise ValueError(
                            f"This id in the input list is invalid {this_id}, "
                            f"so cannot set node font size for this id.")
        else:
            raise ValueError(f"Invalid input for node_id: {node_id}. "
                             f"Node id must be a Species id, a list of "
                             f"Species ids, or a node keyword "
                             f"({SBMLlayout.NODE_KEYWORDS} ).")

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
            node_id (str): id for the node
            font_name (str): value for font family (eg. 'serif')
            or font name (eg. 'Arial')

        Returns: None
        """
        if (isinstance(node_id, str) and
                node_id.lower() in SBMLlayout.NODE_KEYWORDS):
            for node_id in self.getNodeKeywordIds(str(node_id).lower()):
                self.__network.nodes[node_id].font_family = font_name

        elif (isinstance(node_id, str) and
              node_id in self.getNodeIds()):
            self.__network.nodes[node_id].font_family = font_name

        elif isinstance(node_id, list):
            full_model_nodeIds = self.getNodeIds()
            for this_id in node_id:
                if this_id in full_model_nodeIds:
                    self.__network.nodes[this_id].font_family = font_name
                else:
                    raise ValueError(
                            f"This id in the input list is invalid {this_id}, "
                            f"so cannot set node font family for this id.")
        else:
            raise ValueError(f"Invalid input for node_id: {node_id}. "
                             f"Node id must be a Species id, a list of "
                             f"Species ids, or a node keyword "
                             f"({SBMLlayout.NODE_KEYWORDS} ).")

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
            node_id (str): id for the node
            font_family (str): value for font family (eg. 'serif')
            or font name (eg. 'Arial')

        Returns: None
        """
        if (isinstance(node_id, str) and
                node_id.lower() in SBMLlayout.NODE_KEYWORDS):
            for node_id in self.getNodeKeywordIds(str(node_id).lower()):
                self.__network.nodes[node_id].font_family = font_family

        elif (isinstance(node_id, str) and
              node_id in self.getNodeIds()):
            self.__network.nodes[node_id].font_family = font_family

        elif isinstance(node_id, list):
            full_model_nodeIds = self.getNodeIds()
            for this_id in node_id:
                if this_id in full_model_nodeIds:
                    self.__network.nodes[this_id].font_family = font_family
                else:
                    raise ValueError(
                            f"This id in the input list is invalid {this_id}, "
                            f"so cannot set node font family for this id.")
        else:
            raise ValueError(f"Invalid input for node_id: {node_id}. "
                             f"Node id must be a Species id, a list of "
                             f"Species ids, or a node keyword "
                             f"({SBMLlayout.NODE_KEYWORDS} ).")

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
        SBMLlayout._validatePlotColor(font_color)

        if (isinstance(node_id, str) and
                node_id.lower() in SBMLlayout.NODE_KEYWORDS):
            for node_id in self.getNodeKeywordIds(str(node_id).lower()):
                self.__network.nodes[node_id].font_color = font_color

        elif (isinstance(node_id, str) and
              node_id in self.getNodeIds()):
            self.__network.nodes[node_id].font_color = font_color

        elif isinstance(node_id, list):
            full_model_nodeIds = self.getNodeIds()
            for this_id in node_id:
                if this_id in full_model_nodeIds:
                    self.__network.nodes[this_id].font_color = font_color
                else:
                    raise ValueError(
                            f"This id in the input list is invalid {this_id}, "
                            f"so cannot set node font color for this id.")
        else:
            raise ValueError(f"Invalid input for node_id: {node_id}. "
                             f"Node id must be a Species id, a list of "
                             f"Species ids, or a node keyword "
                             f"({SBMLlayout.NODE_KEYWORDS} ).")

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
        SBMLlayout._validateFontStyle(font_style)

        if (isinstance(node_id, str) and
                node_id.lower() in SBMLlayout.NODE_KEYWORDS):
            for node_id in self.getNodeKeywordIds(str(node_id).lower()):
                self.__network.nodes[node_id].font_style = font_style

        elif (isinstance(node_id, str) and
              node_id in self.getNodeIds()):
            self.__network.nodes[node_id].font_style = font_style

        elif isinstance(node_id, list):
            full_model_nodeIds = self.getNodeIds()
            for this_id in node_id:
                if this_id in full_model_nodeIds:
                    self.__network.nodes[this_id].font_style = font_style
                else:
                    raise ValueError(
                            f"This id in the input list is invalid {this_id}, "
                            f"so cannot set node font style for this id.")
        else:
            raise ValueError(f"Invalid input for node_id: {node_id}. "
                             f"Node id must be a Species id, a list of "
                             f"Species ids, or a node keyword "
                             f"({SBMLlayout.NODE_KEYWORDS} ).")

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

    def setReactionColor(self, reaction_id, reaction_color):
        """
        Sets the reaction edge color and fill color to the same value.

        Args:
            reaction_id (str): id of the reaction to change the color of one
                reaction, or 'all' to change the color of all the reactions
            reaction_color (str): id of the color

        Returns: None
        """
        SBMLlayout._validatePlotColor(reaction_color)

        if reaction_id == "all":
            for reaction in self.__network.reactions.values():
                reaction.fill_color = reaction_color
                reaction.edge_color = reaction_color

        elif (isinstance(reaction_id, str) and
              reaction_id in self.getReactionIds()):
            self.__network.reactions[reaction_id].edge_color = reaction_color
            self.__network.reactions[reaction_id].fill_color = reaction_color

        elif isinstance(reaction_id, list):
            full_model_reactionIds = self.getReactionIds()
            for this_id in reaction_id:
                if this_id in full_model_reactionIds:
                    self.__network.reactions[this_id].edge_color = \
                        reaction_color
                    self.__network.reactions[this_id].fill_color = \
                        reaction_color
                else:
                    raise ValueError(
                            f"This id in the input list is invalid {this_id}, "
                            f"so cannot set color for this id.")
        else:
            raise ValueError(f"Invalid input for reaction ids: {reaction_id}")

    def getReactionEdgeColor(self, reaction_id):
        """Returns the color id for the edge color of the reaction.

        Args:
            reaction_id (str): id for the reaction

        Returns: str
        """
        if reaction_id in self.__network.reactions:
            return self.__network.reactions[reaction_id].edge_color
        else:
            raise ValueError(f"Reaction {reaction_id} not found in network.")

    def setReactionEdgeColor(self, reaction_id, edge_color):
        """
        Sets the reaction edge color.

        Args:
            reaction_id (str): id of the reaction to change the color of one
                reaction, or 'all' to change the color of all the reactions
            edge_color (str): id of the color

        Returns: None
        """
        SBMLlayout._validatePlotColor(edge_color)

        if reaction_id == "all":
            for reaction in self.__network.reactions.values():
                reaction.edge_color = edge_color

        elif (isinstance(reaction_id, str) and
              reaction_id in self.getReactionIds()):
            self.__network.reactions[reaction_id].edge_color = edge_color

        elif isinstance(reaction_id, list):
            full_model_reactionIds = self.getReactionIds()
            for this_id in reaction_id:
                if this_id in full_model_reactionIds:
                    self.__network.reactions[this_id].edge_color = edge_color
                else:
                    raise ValueError(
                            f"This id in the input list is invalid {this_id}, "
                            f"so cannot set color for this id.")
        else:
            raise ValueError(f"Invalid input for reaction ids: {reaction_id}")

    def getReactionFillColor(self, reaction_id):
        """Returns the fill color for the reaction.

        Args:
            reaction_id (str): id for the reaction

        Returns: str
        """
        if reaction_id in self.__network.reactions:
            return self.__network.reactions[reaction_id].fill_color
        else:
            raise ValueError(f"Reaction {reaction_id} not found in network.")

    def setReactionFillColor(self, reaction_id, fill_color):
        """
        Sets the reaction fill color.

        Args:
            reaction_id (str): id of the reaction to change the color of one
                reaction, or 'all' to change the color of all the reactions
            fill_color (str): id of the color

        Returns: None
        """
        SBMLlayout._validatePlotColor(fill_color)

        if reaction_id == "all":
            for reaction in self.__network.reactions.values():
                reaction.fill_color = fill_color

        elif (isinstance(reaction_id, str) and
              reaction_id in self.getReactionIds()):
            self.__network.reactions[reaction_id].fill_color = fill_color

        elif isinstance(reaction_id, list):
            full_model_reactionIds = self.getReactionIds()
            for this_id in reaction_id:
                if this_id in full_model_reactionIds:
                    self.__network.reactions[this_id].fill_color = fill_color
                else:
                    raise ValueError(
                            f"This id in the input list is invalid {this_id}, "
                            f"so cannot set color for this id.")
        else:
            raise ValueError(f"Invalid input for reaction ids: {reaction_id}")

    def getReactionCurveWidth(self, reaction_id):
        """Returns the curve width for the given reaction.

        Args: reaction_id (str): id for the reaction

        Returns: int
        """
        if reaction_id in self.__network.reactions:
            return self.__network.reactions[reaction_id].curve_width
        else:
            raise ValueError(f"Reaction {reaction_id} not found in network.")

    def setReactionCurveWidth(self, reaction_id, curve_width):
        """
        Sets the width of the reaction curve.

        Args:
            reaction_id (str): id of the reaction to change the width of one
                reaction, or 'all' to change the width of all the reactions
            curve_width (int): numeric value representing the line width

        Returns: None
        """
        if reaction_id == "all":
            for reaction in self.__network.reactions.values():
                reaction.curve_width = curve_width

        elif (isinstance(reaction_id, str) and
              reaction_id in self.getReactionIds()):
            self.__network.reactions[reaction_id].curve_width = curve_width

        elif isinstance(reaction_id, list):
            full_model_reactionIds = self.getReactionIds()
            for this_id in reaction_id:
                if this_id in full_model_reactionIds:
                    self.__network.reactions[this_id].curve_width = curve_width
                else:
                    raise ValueError(
                            f"This id in the input list is invalid {this_id}, "
                            f"so cannot set reaction curve width for this id.")
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
        renderInfo.addRenderInformation(self.__network)
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

    def drawNetwork(self, save_file_name=None, bbox_inches="tight",
                    figsize=None, show=True, dpi=72, node_multiplier=1.0,
                    node_padding=0.6, node_mutation_scale=10,
                    compute_node_dims=True, use_all_fig_space=False):
        """Draws the network to screen.  The figure can be saved.

        Args:
            save_file_name (optional, str): save figure to this file
            bbox_inches (optional, str or matplotlib.transforms.Bbox): "tight",
                or a value for inches or a Bbox, used as a parameter in
                matplotlib's savefig()
            figsize (optional, tuple): (width, height) of the figure in inches,
                default value is (6, 4)
            show (optional, bool): if True, display the network on screen
            dpi (optional, int): desired dots-per-inch for the figure
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
        # %config InlineBackend.print_figure_kwargs = {'bbox_inches':None}

        fig = createNetworkFigure(self, self.__arrowhead_scale,
                                  figsize, show, dpi, node_multiplier,
                                  node_padding, node_mutation_scale,
                                  compute_node_dims, use_all_fig_space=False)
        if(save_file_name):
            fig.savefig(save_file_name)

        print("dn: fig w,h: ", fig.get_figwidth(), fig.get_figheight())

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
        return libsbml.SBMLToString(self.__doc)

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
