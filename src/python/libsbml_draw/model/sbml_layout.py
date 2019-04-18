"""Creates a Python interface to load, display and manipulate
models defined in an SBML file, making use of a c API and libsbml."""

import os

from matplotlib.colors import is_color_like

import libsbml

# from . import c_api.sbnw_c_api
# from libsbml_draw import (createNetworkFigure, Network, Render)

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
        if k: self.layout_alg_options.k = k
        if boundary: self.layout_alg_options.boundary = boundary
        if mag: self.layout_alg_options.mag = mag
        if grav: self.layout_alg_options.grav = grav
        if baryx: self.layout_alg_options.baryx = baryx
        if baryy: self.layout_alg_options.baryy = baryy
        if autobary: self.layout_alg_options.autobary = autobary
        if enable_comps: self.layout_alg_options.enable_comps
        if prerandom: self.layout_alg_options.prerandom = prerandom
        if padding: self.layout_alg_options.padding = padding
        
    def setLayoutAlgorithm_k(self, k):
        self.layout_alg_options.k = k

    def setLayoutAlgorithm_boundary(self, boundary):
        self.layout_alg_options.boundary = boundary

    def setLayoutAlgorithm_mag(self, magnitude):
        self.layout_alg_options.mag = magnitude

    def setLayoutAlgorithm_grav(self, gravity):
        self.layout_alg_options.grav = gravity
    
    def setLayoutAlgorithm_baryx(self, baryx):
        self.layout_alg_options.baryx = baryx
        
    def setLayoutAlgorithm_baryy(self, baryy):
        self.layout_alg_options.baryy = baryy

    def setLayoutAlgorithm_autobary(self, autobary):
        self.layout_alg_options.autobary = autobary
        
    def setLayoutAlgorithm_enable_comps(self, enable_comps):
        self.layout_alg_options.enable_comps = enable_comps        

    def setLayoutAlgorithm_prerandom(self, prerandom):
        self.layout_alg_options.prerandom = prerandom
        
    def setLayoutAlgorithm_padding(self, padding):
        self.layout_alg_options.padding = padding        
    
    def getLayoutAlgorithmOptions(self,):
        return self.layout_alg_options
    
    def showLayoutAlgorithmOptions(self,):
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
        if sbml_filename and os.path.isfile(sbml_filename):
            return True
        else:
            return False

    def _validate_layout_alg_options(self, layout_alg_options):
        if isinstance(layout_alg_options, sbnw.fr_alg_options):
            return True
        else:
            return False

    # Layout Methods

    def regenerateLayoutAndNetwork(self,):
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
        """Give the layout a starting point """
        sbnw.randomizeLayout(self.h_layout_info)

    def _doLayoutAlgorithm(self,):
        """Run the FR Layout Algorithm"""
        sbnw.doLayoutAlgorithm(self.layout_alg_options, self.h_layout_info)

    # Model Methods

    def _createNetwork(self,):
        return Network(self.h_network)

    def _describeModel(self,):
        print()
        print("sbml filename: ", self.sbml_filename)
        print("layout number: ", self.layout_number)
        print("layout is specified: ", self.layoutSpecified)
        print("number of Compartments: ", self.numCompartments)
        print("number of Nodes: ", self.numNodes)
        print("number of Reactions: ", self.numReactions)
        print("apply renderInfo, network type: ", type(self.network))

    def getNumberOfCompartments(self,):
        return sbnw.nw_getNumCompartments(self.h_network)

    def getNumberOfNodes(self,):
        return sbnw.nw_getNumNodes(self.h_network)

    def getNumberOfReactions(self,):
        return sbnw.nw_getNumRxns(self.h_network)

    def fitToWindow(self, left, top, right, bottom):
        sbnw.fit_to_window(self.h_layout_info, left, top, right, bottom)

    def setModelNamespace(self, level, version):
        """Specify the Model"""
        sbnw.setModelNamespace(self.h_layout_info, level, version)

    # Node Information

    def nodeGetCentroid(self, node_id):
        node_p = sbnw.nw_getNodepFromId(self.h_network,
                                        node_id.encode('utf-8'))
        return sbnw.node_getCentroid(node_p)

    def nodeGetHeight(self, node_index):
        node_p = sbnw.nw_getNodep(self.h_network, node_index)
        node_height = sbnw.node_getHeight(node_p)
        return node_height

    def nodeGetWidth(self, node_index):
        node_p = sbnw.nw_getNodep(self.h_network, node_index)
        node_width = sbnw.node_getWidth(node_p)
        return node_width

    # Reaction Information

    def reactionGetCentroid(self, reaction_index):
        reaction_p = sbnw.nw_getRxnp(self.h_network, reaction_index)
        centroid = sbnw.reaction_getCentroid(reaction_p)
        return centroid

    def describeReaction(self, reaction_index):
        reaction_p = sbnw.nw_getRxnp(self.h_network, reaction_index)
        numSpecies = sbnw.reaction_getNumSpecies(reaction_p)
        numCurves = sbnw.reaction_getNumCurves(reaction_p)
        print("reaction ", reaction_index, "numSpecies: ", numSpecies)
        print("reaction ", reaction_index, "numCurves: ", numCurves)

    # SBML IO Functions

    def getSBMLWithLayoutString(self,):
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
        libsbml.writeSBMLToFile(self.doc, out_file_name)
        print("wrote file: ", out_file_name)

    # Node Methods

    def getNodeIds(self,):
        return list(self.network.nodes.keys())

    def getNodeColor(self, node_id):
        return self.network.nodes[node_id].fill_color

    def _validateNodeColor(node_color):

        try:
            if not is_color_like(node_color):
                raise ValueError("Invalid color: ", node_color)
            else:
                return True
        except Exception as inst:
            print("ERROR: Cannot set node color: ", inst)
            print("TYPE of ERROR: ", type(inst).__name__)
            return False

    def getNodeKeywordIds(self, node_keyword):

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
            node_id (str): id of the node to change the color of one node,
                or 'all' to change the color of all the nodes

        Returns: None
        """
        SBMLlayout._validateNodeColor(node_color)

        if (isinstance(node_id, str) and
                node_id.lower() in SBMLlayout.NODE_KEYWORDS):
            for node_id in self.getNodeKeywordIds(str(node_id).lower()):
                self.network.nodes[node_id].edge_color = node_color
                self.network.nodes[node_id].fill_color = node_color

        elif (isinstance(node_id, str) and
              node_id.lower() in self.getNodeIds()):
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
        return self.network.nodes[node_id].fill_color

    def setNodeFillColor(self, node_id, node_color):
        self.network.nodes[node_id].fill_color = node_color

    def getNodeEdgeColor(self, node_id):
        return self.network.nodes[node_id].edge_color

    def setNodeEdgeColor(self, node_id, node_color):
        self.network.nodes[node_id].edge_color = node_color

    def getNodeFontSize(self, node_id):
        return self.network.nodes[node_id].font_size

    def setNodeFontSize(self, node_id, fontsize):
        self.network.nodes[node_id].font_size = fontsize

    def getNodeFontName(self, node_id):
        return self.network.nodes[node_id].font_family

    def setNodeFontName(self, node_id, fontname):
        self.network.nodes[node_id].font_family = fontname

    def getNodeFontFamily(self, node_id):
        return self.network.nodes[node_id].font_family

    def setNodeFontFamily(self, node_id, fontfamily):
        self.network.nodes[node_id].font_family = fontfamily

    def getNodeFontColor(self, node_id):
        return self.network.nodes[node_id].font_color

    def setNodeFontColor(self, node_id, fontcolor):
        self.network.nodes[node_id].font_color = fontcolor

    def getNodeFontStyle(self, node_id):
        return self.network.nodes[node_id].font_style

    def setNodeFontStyle(self, node_id, fontstyle):
        """Available font styles are normal, italic, and oblique"""
        self.network.nodes[node_id].font_style = fontstyle

    def getNodeWidth(self, node_id):
        return self.network.nodes[node_id].width

    def getNodeHeight(self, node_id):
        return self.network.nodes[node_id].height

    def getNodeName(self, node_id):
        return self.network.nodes[node_id].name

    def getNodeLowerLeftPoint(self, node_id):
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

        Returns: None
        """
        if reaction_id == "all":
            for reaction in self.network.reactions.values():
                reaction.fill_color = reaction_color
                reaction.edge_color = reaction_color
        elif reaction_id in self.getReactionIds():
            self.network.reactions[reaction_id].edge_color = reaction_color
            self.network.reactions[reaction_id].fill_color = reaction_color
        else:
            raise ValueError(f"Invalid input for reaction ids: {reaction_id}")

    def getReactionEdgeColor(self, reaction_id):
        return self.network.reactions[reaction_id].edge_color

    def setReactionEdgeColor(self, reaction_id, reaction_edge_color):
        self.network.reactions[reaction_id].edge_color = reaction_edge_color

    def getReactionFillColor(self, reaction_id):
        return self.network.reactions[reaction_id].fill_color

    def setReactionFillColor(self, reaction_id, reaction_fill_color):
        self.network.reactions[reaction_id].fill_color = reaction_fill_color

    def getReactionCurveWidth(self, reaction_id):
        return self.network.reactions[reaction_id].curve_width

    def setReactionCurveWidth(self, reaction_id, curve_width):
        self.network.reactions[reaction_id].curve_width = curve_width

    # Render Methods

    def addRenderInformation(self,):
        renderInfo = Render(self.sbml_filename, self.layout_number)
        renderInfo.addRenderInformation(self.network)
        self.doc = renderInfo.doc

    def _applyRenderInformation(self,):
        renderInfo = Render(self.sbml_filename, self.layout_number)
        renderInfo.applyGlobalRenderInformation(self.network)
        renderInfo.applyLocalRenderInformation(self.network)

    # Plotting Methods

    def arrowheadGetStyle(self, role):
        return sbnw.arrowheadGetStyle(role)

    def arrowheadSetStyle(self, role, style):
        sbnw.arrowheadSetStyle(role, style)

    def arrowheadGetNumVerts(self, style):
        return sbnw.arrowheadStyleGetNumVerts(style)

    def arrowheadGetVert(self, style, vertex_number):
        return sbnw.arrowheadStyleGetVert(style, vertex_number)

    def drawNetwork(self, save_file_name=None, bbox_inches="tight"):

        try:
            fig = createNetworkFigure(self.network)
            if(save_file_name):
                fig.savefig(save_file_name, bbox_inches=bbox_inches)
        except Exception as inst:
            print("Type of Error: ", type(inst))
            print("Description of Error: ", inst)

        return fig
