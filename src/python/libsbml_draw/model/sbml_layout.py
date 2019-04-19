"""Creates a Python interface to load, display and manipulate
models defined in an SBML file, making use of a c API and libsbml."""

import os

from matplotlib.colors import is_color_like

import libsbml

import libsbml_draw.c_api.sbnw_c_api as sbnw
from libsbml_draw.draw.draw_network import createNetworkFigure
from libsbml_draw.model.network import Network
from libsbml_draw.model.render import Render


class SBMLlayout:
    """SBMLlayout represents the model in an SBML file."""

    LIBSBML_DRAW_VERSION = sbnw.getCurrentLibraryVersion()

    NODE_KEYWORDS = {"all", "boundary", "floating"}

    def __init__(self, sbml_filename, layout_alg_options=None,
                 layout_number=0, fitWindow=tuple()):

        self.sbml_filename = sbml_filename
        self.layout_number = layout_number
        self.fitWindow = fitWindow

        if self._validate_layout_alg_options(layout_alg_options):
            self.layout_alg_options = layout_alg_options
        else:
            self.layout_alg_options = sbnw.fr_alg_options(
                20.0,        # k
                1,           # boundary
                0,           # mag
                0,           # grav
                500.0,       # baryx
                0.0,         # baryy
                1,           # autobary
                0,           # enable_comps
                0,           # prerandom
                0.0          # padding
            )

        if self._validate_sbml_filename(self.sbml_filename):

            self.h_model = sbnw.loadSBML(self.sbml_filename)
            self.h_layout_info = sbnw.processLayout(self.h_model)
            self.h_network = sbnw.getNetworkp(self.h_layout_info)
            self.layoutSpecified = True if sbnw.isLayoutSpecified(
                    self.h_network) else False

            # create layout, if it doesn't already exist
            if not self.layoutSpecified:
                self._randomizeLayout()
                self._doLayoutAlgorithm()
                self.doc = libsbml.readSBMLFromString(
                        self.getSBMLWithLayoutString())
            else:
                self.doc = libsbml.readSBMLFromFile(self.sbml_filename)

            if len(self.fitWindow) == 4:
                self.fitToWindow(self.fitWindow[0], self.fitWindow[1],
                                 self.fitWindow[2], self.fitWindow[3])

            self.network = self._createNetwork()

            # apply render information, if any
            self._applyRenderInformation()

        else:

            raise Exception(
                    f"The SBML file does not exist: {self.sbml_filename}")
            # self.h_model = sbnw.SBMLModel_newp()
            # not sure if process layout does something default,
            # our model is empty here
            # self.h_layout_info = sbnw.processLayout (self.h_model)
            # self.h_network = sbnw.getNetworkp(self.h_layout_info)
            # add nodes
            # add reactions
            # add compartments

        self.numNodes = self.getNumberOfNodes()
        self.numReactions = self.getNumberOfReactions()
        self.numCompartments = self.getNumberOfCompartments()

    def setLayoutAlgorithmOptions(self, k=None, boundary=None, mag=None,
                                  grav=None, baryx=None, baryy=None,
                                  autobary=None, enable_comps=None,
                                  prerandom=None, padding=None
                                  ):
        """
        Set values for the Fruchterman-Reingold layout algorithm parameters.

        Args:
            k (float):
            boundary (int):
            magnitude (int):
            gravity (float):
            baryx (float):
            baryy (float):
            autobary (int):
            enable_comps (int):
            prerandom (int):
            padding (float):

        Returns: None
        """
        if k:
            self.layout_alg_options.k = k
        if boundary:
            self.layout_alg_options.boundary = boundary
        if mag:
            self.layout_alg_options.mag = mag
        if grav:
            self.layout_alg_options.grav = grav
        if baryx:
            self.layout_alg_options.baryx = baryx
        if baryy:
            self.layout_alg_options.baryy = baryy
        if autobary:
            self.layout_alg_options.autobary = autobary
        if enable_comps:
            self.layout_alg_options.enable_comps
        if prerandom:
            self.layout_alg_options.prerandom = prerandom
        if padding:
            self.layout_alg_options.padding = padding

    def setLayoutAlgorithm_k(self, k):
        """Set the Fruchterman-Reingold layout algorithm parameter 'k'.

        Args:
            k (float):

        Returns: None
        """
        self.layout_alg_options.k = k

    def setLayoutAlgorithm_boundary(self, boundary):
        """Set the Fruchterman-Reingold layout algorithm parameter 'boundary'.

        Args:
            boundary (int):

        Returns: None
        """
        self.layout_alg_options.boundary = boundary

    def setLayoutAlgorithm_mag(self, magnitude):
        """Set the Fruchterman-Reingold layout algorithm parameter 'mag'.

        Args:
            mag (int):

        Returns: None
        """
        self.layout_alg_options.mag = magnitude

    def setLayoutAlgorithm_grav(self, gravity):
        """Set the Fruchterman-Reingold layout algorithm parameter 'grav'.

        Args:
            gravity (float):

        Returns: None
        """
        self.layout_alg_options.grav = gravity

    def setLayoutAlgorithm_baryx(self, baryx):
        """Set the Fruchterman-Reingold layout algorithm parameter 'baryx'.

        Args:
            baryx (float):

        Returns: None
        """
        self.layout_alg_options.baryx = baryx

    def setLayoutAlgorithm_baryy(self, baryy):
        """Set the Fruchterman-Reingold layout algorithm parameter 'baryy'.

        Args:
            baryy (float):

        Returns: None
        """
        self.layout_alg_options.baryy = baryy

    def setLayoutAlgorithm_autobary(self, autobary):
        """Set the Fruchterman-Reingold layout algorithm parameter 'autobary'.

        Args:
            autobary (int):

        Returns: None
        """
        self.layout_alg_options.autobary = autobary

    def setLayoutAlgorithm_enable_comps(self, enable_comps):
        """Set the Fruchterman-Reingold layout algorithm parameter
        'enable_comps'.

        Args:
            enable_comps (int):

        Returns: None
        """
        self.layout_alg_options.enable_comps = enable_comps

    def setLayoutAlgorithm_prerandom(self, prerandom):
        """Set the Fruchterman-Reingold layout algorithm parameter 'prerandom'.

        Args:
            prerandom (int):

        Returns: None
        """
        self.layout_alg_options.prerandom = prerandom

    def setLayoutAlgorithm_padding(self, padding):
        """Set the Fruchterman-Reingold layout algorithm parameter 'padding'.

        Args:
            padding (float):

        Returns: None
        """
        self.layout_alg_options.padding = padding

    def getLayoutAlgorithmOptions(self,):
        """Get the Fruchterman-Reingold layout algorithm parameter values.

        Args: None

        Returns: instance of the fr_alg_options class
        """
        return self.layout_alg_options

    def showLayoutAlgorithmOptions(self,):
        """Prints out the values of the Fruchterman-Reingold algorithm
        paramters, which are: k, boundary, mag, grav, baryx, baryy, autobary,
        enable_comps, prerandom, and padding.

        Args: None

        Returns: None
        """
        print("layout algorithm options: \n",
              "k ", self.layout_alg_options.k, "\n",
              "boundary ", self.layout_alg_options.boundary, "\n",
              "magnitude ", self.layout_alg_options.mag, "\n",
              "gravity ", self.layout_alg_options.grav, "\n",
              "baryx ", self.layout_alg_options.baryx, "\n",
              "baryy ", self.layout_alg_options.baryy, "\n",
              "autobary ", self.layout_alg_options.autobary, "\n",
              "enable_comps ", self.layout_alg_options.enable_comps, "\n",
              "prerandom ", self.layout_alg_options.prerandom, "\n",
              "padding ", self.layout_alg_options.padding, "\n"
              )

    # Validation Methods

    def _validate_sbml_filename(self, sbml_filename):
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
            raise ValueError(f"""Font Style, {font_style} is not valid, must be
                             one of: {valid_font_styles}.""")

    # Layout Methods

    def regenerateLayoutAndNetwork(self,):
        """Use this to generate a new layout, and update the network's node
        and reaction layout values.

        Args: None

        Returns: None
        """
        self._randomizeLayout()
        self._doLayoutAlgorithm()
        self.doc = libsbml.readSBMLFromString(self.getSBMLWithLayoutString())

        if len(self.fitWindow) == 4:
                self.fitToWindow(self.fitWindow[0], self.fitWindow[1],
                                 self.fitWindow[2], self.fitWindow[3])

        self.network = self._createNetwork()

        # apply render information, if any
        self._applyRenderInformation()

    def _randomizeLayout(self,):
        """Give the layout a starting point

        Args: None
        Returns: None
        """
        sbnw.randomizeLayout(self.h_layout_info)

    def _doLayoutAlgorithm(self,):
        """Run the Fruchterman-Reingold Layout Algorithm

        Args: None
        Returns: None
        """
        sbnw.doLayoutAlgorithm(self.layout_alg_options, self.h_layout_info)

    # Model Methods

    def _createNetwork(self,):
        """Creates a network for this model based on the existing layout.

        Args: None
        Returns: None
        """
        return Network(self.h_network)

    def _describeModel(self,):
        """Provides a summary of the model built from the SBML file.

        Args: None
        Returns: None
        """
        print()
        print("sbml filename: ", self.sbml_filename)
        print("layout number: ", self.layout_number)
        print("layout is specified: ", self.layoutSpecified)
        print("number of Compartments: ", self.numCompartments)
        print("number of Nodes: ", self.numNodes)
        print("number of Reactions: ", self.numReactions)

    def getNumberOfCompartments(self,):
        """Returns the number of compartments in the model.

        Args: None
        Returns: None
        """
        return sbnw.nw_getNumCompartments(self.h_network)

    def getNumberOfNodes(self,):
        """Returns the number of nodes in the model.

        Args: None
        Returns: None
        """
        return sbnw.nw_getNumNodes(self.h_network)

    def getNumberOfReactions(self,):
        """Returns the number of reactions in the model.

        Args: None
        Returns: None
        """
        return sbnw.nw_getNumRxns(self.h_network)

    def fitToWindow(self, left, top, right, bottom):
        """Constrains the (x,y) values for the layout to fall within this
        window.

        Args:
            left (int): left-most x value
            top (int):  top-most y value
            right (int): right-most x value
            bottom (int): bottom-most y value

        Returns: None
        """
        sbnw.fit_to_window(self.h_layout_info, left, top, right, bottom)

    def setModelNamespace(self, level, version):
        """Specify the Model level and version.

        Args:
            level (int): model level
            version (int): model version

        Returns: None
        """
        sbnw.setModelNamespace(self.h_layout_info, level, version)

    # Node Information

    def nodeGetCentroid(self, node_id):
        """Returns the center point of the node.

        Args:
            node_id (str): id for the node

        Returns: point, which has fields x and y
        """
        node_p = sbnw.nw_getNodepFromId(self.h_network,
                                        node_id.encode('utf-8'))
        return sbnw.node_getCentroid(node_p)

    def nodeGetHeight(self, node_index):
        """Returns the height of the node.

        Args:
            node_index(int): index of the node

        Returns: int
        """
        node_p = sbnw.nw_getNodep(self.h_network, node_index)
        node_height = sbnw.node_getHeight(node_p)
        return node_height

    def nodeGetWidth(self, node_index):
        """Returns the width of the node.

        Args:
            node_index(int): index of the node

        Returns: int
        """
        node_p = sbnw.nw_getNodep(self.h_network, node_index)
        node_width = sbnw.node_getWidth(node_p)
        return node_width

    # Reaction Information

    def reactionGetCentroid(self, reaction_index):
        """Returns the centroid of the reaction.

        Args:
            reaction_index(int): index of the reaction

        Returns: point, with fields x and y
        """
        reaction_p = sbnw.nw_getRxnp(self.h_network, reaction_index)
        centroid = sbnw.reaction_getCentroid(reaction_p)
        return centroid

    def describeReaction(self, reaction_index):
        """Prints the number of Species and number of curves in the reaction.

        Args: reaction_index(int): index of the reaction

        Returns: None
        """
        reaction_p = sbnw.nw_getRxnp(self.h_network, reaction_index)
        numSpecies = sbnw.reaction_getNumSpecies(reaction_p)
        numCurves = sbnw.reaction_getNumCurves(reaction_p)
        print("reaction ", reaction_index, "numSpecies: ", numSpecies)
        print("reaction ", reaction_index, "numCurves: ", numCurves)

    # SBML IO Functions

    def getSBMLWithLayoutString(self,):
        """Returns the SBML content, including layout, as a string.

        Args: None

        Returns: str
        """
        sbml_string = sbnw.getSBMLwithLayoutStr(self.h_model,
                                                self.h_layout_info)
        return sbml_string

    # def writeSBMLWithLayout(self, output_filename):
    #    filename = output_filename.encode('utf-8')
    #    result = sbnw.writeSBMLwithLayout(filename, self.h_model,
    #                                      self.h_layout_info)
    #    print("writeSBMLwithLayout result: ", result)
        # if result error, raise Exception?
    #    return result

    def writeSBMLFile(self, out_file_name):
        """Writes the model as an SBML file.

        Args:
            out_file_name (str): name of the file to write

        Returns: None
        """
        libsbml.writeSBMLToFile(self.doc, out_file_name)
        print("wrote file: ", out_file_name)

    # Node Methods

    def getNodeIds(self,):
        """Returns a list of node ids.

        Args: None

        Returns: list of str
        """
        return list(self.network.nodes.keys())

    def getNodeColor(self, node_id):
        """Returns the id of the color for this node.

        Args:
            node_id (str): id for the node

        Returns: str
        """
        return self.network.nodes[node_id].fill_color

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
                self.network.nodes[node_id].edge_color = node_color
                self.network.nodes[node_id].fill_color = node_color

        elif (isinstance(node_id, str) and
              node_id in self.getNodeIds()):
            self.network.nodes[node_id].edge_color = node_color
            self.network.nodes[node_id].fill_color = node_color

        elif isinstance(node_id, list):
            full_model_nodeIds = self.getNodeIds()
            for this_id in node_id:
                if this_id in full_model_nodeIds:
                    self.network.nodes[this_id].edge_color = node_color
                    self.network.nodes[this_id].fill_color = node_color
                else:
                    print(f"""This id in the input list is invalid {this_id},
                          so cannot set color for this id.""")
        else:
            raise ValueError(f"""Invalid input for node_id: {node_id}.
                             node_id must be a Species id, a list of Species
                             ids, or a node keyword (
                             {SBMLlayout.NODE_KEYWORDS} ).""")

    def getNodeFillColor(self, node_id):
        """Returns the color id for the node fill color.

        Args: node_id(str): id of the node

        Returns: str
        """
        return self.network.nodes[node_id].fill_color

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
                self.network.nodes[node_id].fill_color = fill_color

        elif (isinstance(node_id, str) and
              node_id in self.getNodeIds()):
            self.network.nodes[node_id].fill_color = fill_color

        elif isinstance(node_id, list):
            full_model_nodeIds = self.getNodeIds()
            for this_id in node_id:
                if this_id in full_model_nodeIds:
                    self.network.nodes[this_id].fill_color = fill_color
                else:
                    print(f"""This id in the input list is invalid {this_id},
                          so cannot set node fill color for this id.""")
        else:
            raise ValueError(f"""Invalid input for node_id: {node_id}.
                             node_id must be a Species id, a list of Species
                             ids, or a node keyword (
                             {SBMLlayout.NODE_KEYWORDS} ).""")

    def getNodeEdgeColor(self, node_id):
        """Returns the color id for the node edge color.

        Args:
            node_id(str): id for the node

        Returns: str
        """
        return self.network.nodes[node_id].edge_color

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
                self.network.nodes[node_id].edge_color = edge_color
        elif (isinstance(node_id, str) and
              node_id in self.getNodeIds()):
            self.network.nodes[node_id].edge_color = edge_color
        elif isinstance(node_id, list):
            full_model_nodeIds = self.getNodeIds()
            for this_id in node_id:
                if this_id in full_model_nodeIds:
                    self.network.nodes[this_id].edge_color = edge_color
                else:
                    print(f"""This id in the input list is invalid {this_id},
                          so cannot set node edge color for this id.""")
        else:
            raise ValueError(f"""Invalid input for node_id: {node_id}.
                             node_id must be a Species id, a list of Species
                             ids, or a node keyword (
                             {SBMLlayout.NODE_KEYWORDS} ).""")

    def getNodeFontSize(self, node_id):
        """Returns the font size of the node text.

        Args:
            node_id (str): id for the node

        Returns: int
        """
        return self.network.nodes[node_id].font_size

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
                self.network.nodes[node_id].font_size = font_size

        elif (isinstance(node_id, str) and
              node_id in self.getNodeIds()):
            self.network.nodes[node_id].font_size = font_size

        elif isinstance(node_id, list):
            full_model_nodeIds = self.getNodeIds()
            for this_id in node_id:
                if this_id in full_model_nodeIds:
                    self.network.nodes[this_id].font_size = font_size
                else:
                    print(f"""This id in the input list is invalid {this_id},
                          so cannot set node font size for this id.""")
        else:
            raise ValueError(f"""Invalid input for node_id: {node_id}.
                             node_id must be a Species id, a list of Species
                             ids, or a node keyword (
                             {SBMLlayout.NODE_KEYWORDS} ).""")

    def getNodeFontName(self, node_id):
        """Returns the font family value, which can be the font family or
        font name.

        Args:
            node_id (str): id for the node

        Returns: str, eg. "Arial" or "serif"
        """
        return self.network.nodes[node_id].font_family

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
                self.network.nodes[node_id].font_family = font_name

        elif (isinstance(node_id, str) and
              node_id in self.getNodeIds()):
            self.network.nodes[node_id].font_family = font_name

        elif isinstance(node_id, list):
            full_model_nodeIds = self.getNodeIds()
            for this_id in node_id:
                if this_id in full_model_nodeIds:
                    self.network.nodes[this_id].font_family = font_name
                else:
                    print(f"""This id in the input list is invalid {this_id},
                          so cannot set node font family for this id.""")
        else:
            raise ValueError(f"""Invalid input for node_id: {node_id}.
                             node_id must be a Species id, a list of Species
                             ids, or a node keyword (
                             {SBMLlayout.NODE_KEYWORDS} ).""")

    def getNodeFontFamily(self, node_id):
        """Returns the font family value, which can be the font family or
        font name.
        """
        return self.network.nodes[node_id].font_family

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
                self.network.nodes[node_id].font_family = font_family

        elif (isinstance(node_id, str) and
              node_id in self.getNodeIds()):
            self.network.nodes[node_id].font_family = font_family

        elif isinstance(node_id, list):
            full_model_nodeIds = self.getNodeIds()
            for this_id in node_id:
                if this_id in full_model_nodeIds:
                    self.network.nodes[this_id].font_family = font_family
                else:
                    print(f"""This id in the input list is invalid {this_id},
                          so cannot set node font family for this id.""")
        else:
            raise ValueError(f"""Invalid input for node_id: {node_id}.
                             node_id must be a Species id, a list of Species
                             ids, or a node keyword (
                             {SBMLlayout.NODE_KEYWORDS} ).""")

    def getNodeFontColor(self, node_id):
        """Returns the color of the node's text.

        Args:
            node_id (str): id for the node

        Returns: str
        """
        return self.network.nodes[node_id].font_color

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
                self.network.nodes[node_id].font_color = font_color

        elif (isinstance(node_id, str) and
              node_id in self.getNodeIds()):
            self.network.nodes[node_id].font_color = font_color

        elif isinstance(node_id, list):
            full_model_nodeIds = self.getNodeIds()
            for this_id in node_id:
                if this_id in full_model_nodeIds:
                    self.network.nodes[this_id].font_color = font_color
                else:
                    print(f"""This id in the input list is invalid {this_id},
                          so cannot set node font color for this id.""")
        else:
            raise ValueError(f"""Invalid input for node_id: {node_id}.
                             node_id must be a Species id, a list of Species
                             ids, or a node keyword (
                             {SBMLlayout.NODE_KEYWORDS} ).""")

    def getNodeFontStyle(self, node_id):
        """Returns the style of the font for the given node.

        Args:
            node_id (str): id for the node

        Returns: str, "italic", "normal", or "oblique"
        """
        return self.network.nodes[node_id].font_style

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
                self.network.nodes[node_id].font_style = font_style

        elif (isinstance(node_id, str) and
              node_id in self.getNodeIds()):
            self.network.nodes[node_id].font_style = font_style

        elif isinstance(node_id, list):
            full_model_nodeIds = self.getNodeIds()
            for this_id in node_id:
                if this_id in full_model_nodeIds:
                    self.network.nodes[this_id].font_style = font_style
                else:
                    print(f"""This id in the input list is invalid {this_id},
                          so cannot set node font style for this id.""")
        else:
            raise ValueError(f"""Invalid input for node_id: {node_id}.
                             node_id must be a Species id, a list of Species
                             ids, or a node keyword (
                             {SBMLlayout.NODE_KEYWORDS} ).""")

    def getNodeWidth(self, node_id):
        """Returns the width of the node.

        Args:
            node_id (str): id for the node

        Returns: int
        """
        return self.network.nodes[node_id].width

    def getNodeHeight(self, node_id):
        """Returns the height of the node.

        Args:
            node_id (str): id for the node

        Returns: int
        """
        return self.network.nodes[node_id].height

    def getNodeName(self, node_id):
        """Returns the name of the node.

        Args:
            node_id (str): id for the node

        Returns: str
        """
        return self.network.nodes[node_id].name

    def getNodeLowerLeftPoint(self, node_id):
        """Returns the point for the node's lower left corner.

        Args:
            node_id (str): id for the node

        Returns: point which has fields x and y
        """
        return self.network.nodes[node_id].lower_left_point

    def getBoundarySpeciesIds(self,):
        """
        Gets the id values of the Species who have boundaryCondition set to
        True.

        Args:
            None

        Returns: list of Species ids
        """
        model = self.doc.getModel()
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
        model = self.doc.getModel()
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
        return list(self.network.reactions.keys())

    def setReactionColor(self, reaction_id, reaction_color):
        """
        Sets the reaction edge color and fill color to the same value.

        Args:
            reaction_id (str): id of the reaction to change the color of one
                reaction, or 'all' to change the color of all the nodes
            reaction_color (str): id of the color

        Returns: None
        """
        SBMLlayout._validatePlotColor(reaction_color)

        if reaction_id == "all":
            for reaction in self.network.reactions.values():
                reaction.fill_color = reaction_color
                reaction.edge_color = reaction_color

        elif (isinstance(reaction_id, str) and
              reaction_id in self.getReactionIds()):
            self.network.reactions[reaction_id].edge_color = reaction_color
            self.network.reactions[reaction_id].fill_color = reaction_color

        elif isinstance(reaction_id, list):
            full_model_reactionIds = self.getReactionIds()
            for this_id in reaction_id:
                if this_id in full_model_reactionIds:
                    self.network.reactions[this_id].edge_color = reaction_color
                    self.network.reactions[this_id].fill_color = reaction_color
                else:
                    print(f"""This id in the input list is invalid {this_id},
                          so cannot set color for this id.""")
        else:
            raise ValueError(f"Invalid input for reaction ids: {reaction_id}")

    def getReactionEdgeColor(self, reaction_id):
        """Returns the color id for the edge color of the reaction.

        Args:
            reaction_id (str): id for the reaction

        Returns: str
        """
        return self.network.reactions[reaction_id].edge_color

    def setReactionEdgeColor(self, reaction_id, edge_color):
        """
        Sets the reaction edge color.

        Args:
            reaction_id (str): id of the reaction to change the color of one
                reaction, or 'all' to change the color of all the nodes
            edge_color (str): id of the color

        Returns: None
        """
        SBMLlayout._validatePlotColor(edge_color)

        if reaction_id == "all":
            for reaction in self.network.reactions.values():
                reaction.edge_color = edge_color

        elif (isinstance(reaction_id, str) and
              reaction_id in self.getReactionIds()):
            self.network.reactions[reaction_id].edge_color = edge_color

        elif isinstance(reaction_id, list):
            full_model_reactionIds = self.getReactionIds()
            for this_id in reaction_id:
                if this_id in full_model_reactionIds:
                    self.network.reactions[this_id].edge_color = edge_color
                else:
                    print(f"""This id in the input list is invalid {this_id},
                          so cannot set color for this id.""")
        else:
            raise ValueError(f"Invalid input for reaction ids: {reaction_id}")

    def getReactionFillColor(self, reaction_id):
        """Returns the fill color for the reaction.

        Args:
            reaction_id (str): id for the reaction

        Returns: str
        """
        return self.network.reactions[reaction_id].fill_color

    def setReactionFillColor(self, reaction_id, fill_color):
        """
        Sets the reaction fill color.

        Args:
            reaction_id (str): id of the reaction to change the color of one
                reaction, or 'all' to change the color of all the nodes
            fill_color (str): id of the color

        Returns: None
        """
        SBMLlayout._validatePlotColor(fill_color)

        if reaction_id == "all":
            for reaction in self.network.reactions.values():
                reaction.fill_color = fill_color

        elif (isinstance(reaction_id, str) and
              reaction_id in self.getReactionIds()):
            self.network.reactions[reaction_id].fill_color = fill_color

        elif isinstance(reaction_id, list):
            full_model_reactionIds = self.getReactionIds()
            for this_id in reaction_id:
                if this_id in full_model_reactionIds:
                    self.network.reactions[this_id].fill_color = fill_color
                else:
                    print(f"""This id in the input list is invalid {this_id},
                          so cannot set color for this id.""")
        else:
            raise ValueError(f"Invalid input for reaction ids: {reaction_id}")

    def getReactionCurveWidth(self, reaction_id):
        """Returns the curve width for the given reaction.

        Args: reaction_id (str): id for the reaction

        Returns: int
        """
        return self.network.reactions[reaction_id].curve_width

    def setReactionCurveWidth(self, reaction_id, curve_width):
        """
        Sets the width of the reaction curve.

        Args:
            reaction_id (str): id of the reaction to change the color of one
                reaction, or 'all' to change the color of all the nodes
            curve_width (int): numeric value representing the line width

        Returns: None
        """
        if reaction_id == "all":
            for reaction in self.network.reactions.values():
                reaction.curve_width = curve_width

        elif (isinstance(reaction_id, str) and
              reaction_id in self.getReactionIds()):
            self.network.reactions[reaction_id].curve_width = curve_width

        elif isinstance(reaction_id, list):
            full_model_reactionIds = self.getReactionIds()
            for this_id in reaction_id:
                if this_id in full_model_reactionIds:
                    self.network.reactions[this_id].curve_width = curve_width
                else:
                    print(f"""This id in the input list is invalid {this_id},
                          so cannot set reaction curve width for this id.""")
        else:
            raise ValueError(f"Invalid input for reaction ids: {reaction_id}")

    # Render Methods

    def addRenderInformation(self,):
        """Add render information to the model's libsbml.SBMLDocument.

        Args: None

        Returns: None
        """
        renderInfo = Render(self.sbml_filename, self.layout_number)
        renderInfo.addRenderInformation(self.network)
        self.doc = renderInfo.doc

    def _applyRenderInformation(self,):
        """Apply the render information in the SBML file to nodes and reactions
        in the model's network.

        Args: None

        Returns: None
        """
        renderInfo = Render(self.sbml_filename, self.layout_number)
        renderInfo.applyGlobalRenderInformation(self.network)
        renderInfo.applyLocalRenderInformation(self.network)

    # Plotting Methods

    def arrowheadGetStyle(self, role):
        """Returns the arrowhead style for the given role.

        Args:
            role (int): which role

        Returns: int
        """
        return sbnw.arrowheadGetStyle(role)

    def arrowheadSetStyle(self, role, style):
        """Set the arrowhead style for the given role.

        Args:
            role (int): which role
            style (int): which style

        Returns: None
        """
        sbnw.arrowheadSetStyle(role, style)

    def arrowheadGetNumVerts(self, style):
        """Returns the number of vertices in the arrowhead of the given style.

        Args:
            style (int): which arrowhead style

        Returns:int
        """
        return sbnw.arrowheadStyleGetNumVerts(style)

    def arrowheadGetVert(self, style, vertex_number):
        """Returns a point for the given vertex_number, given an arrowhead
        style.

        Args:
            style (int): which arrowhead style
            vertex_number (int): specify the vertex in the arrowhead

        Returns: point with fields x and y
        """
        return sbnw.arrowheadStyleGetVert(style, vertex_number)

    def drawNetwork(self, save_file_name=None, bbox_inches="tight"):
        """Draws the network to screen.  The figure can be saved.

        Args:
            save_file_name (str): save figure to this file
            bbox_inches (str or matplotlib.transforms.Bbox): "tight", or a
                value for inches or a Bbox.

        Returns: matplotlib.figure.Figure
        """
        try:
            fig = createNetworkFigure(self.network)
            if(save_file_name):
                fig.savefig(save_file_name, bbox_inches=bbox_inches)
        except Exception as inst:
            print("Type of Error: ", type(inst))
            print("Description of Error: ", inst)

        return fig
