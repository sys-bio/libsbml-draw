"""Creates a user-friendly Python interface to load, display and manipulate
models defined in an SBML file, making use of a c API and libsbml."""

import os

import libsbml

import libsbml_draw.c_api.sbnw_c_api as sbnw
from libsbml_draw.draw.draw_network import createNetworkFigure
from libsbml_draw.model.network import Network


class SBMLlayout:
    """SBMLlayout represents the model in an SBML file, which already exists or
    which can be created from scratch."""

    LIBSBML_DRAW_version = sbnw.getCurrentLibraryVersion()

    def __init__(self, sbml_filename, layout_alg_options=None,
                 layout_number=0):

        self.sbml_filename = sbml_filename
        self.layout_number = layout_number

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
            self.network = self._createNetwork()
            # apply render information, if any
            self._applyRenderInformation()
            self.doc = None
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

    def _randomizeLayout(self,):
        """Give the layout a starting point """
        sbnw.randomizeLayout(self.h_layout_info)

    def _doLayoutAlgorithm(self,):
        """Run the FR Layout Algorithm"""
        sbnw.doLayoutAlgorithm(self.layout_alg_options, self.h_layout_info)

    def _createNetwork(self,):
        return Network(self.h_network)

    def describeModel(self,):
        print()
        print("layout is specified: ", self.layoutSpecified)
        print("number of Compartments: ", self.numCompartments)
        print("number of Nodes: ", self.numNodes)
        print("number of Reactions: ", self.numReactions)
        return (self.numCompartments, self.numNodes, self.numReactions)

    def getNumberOfCompartments(self,):
        return sbnw.nw_getNumCompartments(self.h_network)

    def getNumberOfNodes(self,):
        return sbnw.nw_getNumNodes(self.h_network)

    def getNumberOfReactions(self,):
        return sbnw.nw_getNumRxns(self.h_network)

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

    # SBML Functions
    def getSBMLWithLayoutString(self,):
        sbml_string = sbnw.getSBMLwithLayoutStr(self.h_model,
                                                self.h_layout_info)
        return sbml_string

    def writeSBMLWithLayout(self, output_filename):
        filename = output_filename.encode('utf-8')
        result = sbnw.writeSBMLwithLayout(filename, self.h_model,
                                          self.h_layout_info)
        print("writeSBMLwithLayout result: ", result)
        # if result error, raise Exception?
        return result

    def drawNetwork(self, save_file_name=None):
        fig = createNetworkFigure(self.network)
        if(save_file_name):
            fig.savefig(save_file_name)
        # print("network, num nodes: ", len(self.network.nodes))
        # print("network, num edges: ", len(self.network.edges))
        # print("network, num rxns: ", self.getNumberOfReactions())
        # for edge in self.network.edges.values():
        #    print(len(edge.curves), "curves")
        #    for curve in edge.curves:
        #        print("role: ", curve.role)

    def writeSBMLFile(self, out_file_name):
        libsbml.writeSBMLToFile(self.doc, out_file_name)

    def getNodeIds(self,):
        return list(self.network.nodes.keys())

    def getReactionIds(self,):
        return list(self.network.edges.keys())

    # Node Getters and Setters

    def getNodeColor(self, node_id):        
        return self.network.nodes[node_id].fill_color

    def setNodeColor(self, node_id, node_color):
        """
        Sets the node edge color and fill color to the same value.

        Args:
            node_id (str): id of the node to change the color of one node, 
                or 'all' to change the color of all the nodes

        Returns: None        
        """
        if node_id == "all":
            for node in self.network.nodes.values():
                node.fill_color = node_color
                node.edge_color = node_color
        else:
            self.network.nodes[node_id].edge_color = node_color
            self.network.nodes[node_id].fill_color = node_color
    
    def getNodeFillColor(self, node_id):
        return self.network.nodes[node_id].fill_color

    def setNodeFillColor(self, node_id, node_color):
        self.network.nodes[node_id].fill_color = node_color

    def getNodeEdgeColor(self, node_id):
        return self.network.nodes[node_id].edge_color

    def setNodeEdgeColor(self, node_id, node_color):
        self.network.nodes[node_id].edge_color = node_color

    def getNodeFontsize(self, node_id):
        return self.network.nodes[node_id].font_size

    def setNodeFontsize(self, node_id, fontsize):
        self.network.nodes[node_id].font_size = fontsize

    def getNodeFontname(self, node_id):
        return self.network.nodes[node_id].font_name

    def setNodeFontname(self, node_id, fontname):
        self.network.nodes[node_id].font_name = fontname

    def getNodeFontfamily(self, node_id):
        return self.network.nodes[node_id].font_family

    def setNodeFontfamily(self, node_id, fontfamily):
        self.network.nodes[node_id].font_family = fontfamily

    def getNodeFontcolor(self, node_id):
        return self.network.nodes[node_id].font_color

    def setNodeFontcolor(self, node_id, fontcolor):
        self.network.nodes[node_id].font_color = fontcolor

    def getNodeFontstyle(self, node_id):
        return self.network.nodes[node_id].font_style

    def setNodeFontstyle(self, node_id, fontstyle):
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

    # Reaction Getters and Setters

    def setReactionColor(self, reaction_id, reaction_color):
        """
        Sets the reaction edge color and fill color to the same value.

        Args:
            reaction_id (str): id of the reaction to change the color of one 
                reaction, or 'all' to change the color of all the nodes

        Returns: None        
        """
        if reaction_id == "all":
            for reaction in self.network.edges.values():
                reaction.fill_color = reaction_color
                reaction.edge_color = reaction_color
        else:
            self.network.edges[reaction_id].edge_color = reaction_color
            self.network.edges[reaction_id].fill_color = reaction_color

    def getReactionEdgeColor(self, reaction_id):
        return self.network.edges[reaction_id].edge_color

    def setReactionEdgeColor(self, reaction_id, reaction_edge_color):
        self.network.edges[reaction_id].edge_color = reaction_edge_color

    def getReactionFillColor(self, reaction_id):
        return self.network.edges[reaction_id].fill_color

    def setReactionFillColor(self, reaction_id, reaction_fill_color):
        self.network.edges[reaction_id].fill_color = reaction_fill_color

    def getReactionCurveWidth(self, reaction_id):
        return self.network.edges[reaction_id].curve_width

    def setReactionCurveWidth(self, reaction_id, curve_width):
        self.network.edges[reaction_id].curve_width = curve_width

    # Private Render Methods

    def _addRenderInformation(self, sbml_file_name):
        # sbml_str = self.getSBMLWithLayout()
        # print("render in sbml_str: ", "render" in sbml_str)
        doc = libsbml.readSBMLFromString(self.getSBMLWithLayoutString())
        # doc = libsbml.readSBMLFromFile(sbml_file_name)
        model = doc.getModel()
        layout_plugin = model.getPlugin("layout")
        # lol_plugin = layout_plugin.getListOfLayouts().getPlugin("render")
        # info_global = lol_plugin.getRenderInformation(0)

        print("num layouts: ", layout_plugin.getNumLayouts())

        # get first layout, there may be only 1
        layout = layout_plugin.getLayout(0)
        print("layout type: ", type(layout))
        print("layout num plugins: ", layout.getNumPlugins())

        rPlugin = layout.getPlugin("render")
        print("rPlugin type: ", type(rPlugin))

        if (rPlugin is not None and
                rPlugin.getNumLocalRenderInformationObjects() > 0):
            print("num local render info objects: ",
                  rPlugin.getNumLocalRenderInformationObjects())
        else:
            uri = libsbml.RenderExtension.getXmlnsL2() if doc.getLevel(
                    ) == 2 else libsbml.RenderExtension.getXmlnsL3V1V1()

            # enable render package
            doc.enablePackage(uri, "render", True)
            doc.setPackageRequired("render", False)

            rPlugin = layout.getPlugin("render")

            rInfo = rPlugin.createLocalRenderInformation()

            rInfo.setId("localRenderInfo")
            rInfo.setName("Fill_Color Render Information")
            # add color definitions
            # add linear gradients
            # add styles
            style = rInfo.createStyle("substrateStyle")
            style.getGroup().setFillColor("pink")
            style.getGroup().setStroke("black")
            style.getGroup().setStrokeWidth(2.0)
            style.addId("S1")
            style.addType("SPECIESGLYPH")

            style = rInfo.createStyle("productStyle")
            style.getGroup().setFillColor("green")
            style.getGroup().setStroke("black")
            style.getGroup().setStrokeWidth(2.0)
            style.addId("S2")
            style.addType("SPECIESGLYPH")

        return doc

    def _applyRenderInformation(self,):
        color_definitions = {}

        doc = libsbml.readSBMLFromFile(self.sbml_filename)
        model = doc.getModel()
        print("model type: ", type(model))
        layout_plugin = model.getPlugin("layout")

        if layout_plugin:
            print("num layouts: ", layout_plugin.getNumLayouts())
            layout = layout_plugin.getLayout(self.layout_number)
            rPlugin = layout.getPlugin("render")

            if rPlugin:
                render_plugin = layout_plugin.getListOfLayouts(
                        ).getPlugin("render")
                print("num global info: ",
                      render_plugin.getNumGlobalRenderInformationObjects())
                print("num local info: ",
                      rPlugin.getNumLocalRenderInformationObjects())

                # globalInformation
                info_global = render_plugin.getRenderInformation(0)

                if(info_global):
                    # -- add color definitions
                    for j in range(info_global.getNumColorDefinitions()):
                        color = info_global.getColorDefinition(j)
                        color_definitions[color.getId()
                                          ] = color.createValueString()
                    print("color definitions: ", len(color_definitions))

                    # -- styles - rolelist, typelist
                    print("styles: ", info_global.getNumStyles())

                    for j in range(info_global.getNumStyles()):
                        style = info_global.getStyle(j)

                        # print("\tstyle: ", style.getId())
                        # print("\t\troles: ", style.createRoleString())
                        # print("\t\ttypes string: ", style.createTypeString())
                        # types = style.getTypeList()
                        # print("\t\ttypes list: ", len(types))
                        if style.isInTypeList("SPECIESGLYPH"):
                            # print("\t\tApply this style to nodes.")
                            # print("\t\tFill is: ",
                            # style.getGroup().getFillColor())
                            if style.getGroup().isSetFillColor():
                                node_color = style.getGroup().getFillColor()
                                for node in self.network.nodes.values():
                                    node.fill_color = node_color
                                    print("set node color: ", node.fill_color)

                        if(style.isInTypeList("REACTIONGLYPH")):
                            # print("\t\tApply this style to reactions.")
                            for edge in self.network.edges.values():
                                if style.getGroup().isSetStroke():
                                    reaction_color = style.getGroup(
                                            ).getStroke()
                                    # print("\t\tStroke is: ", stroke_color)
                                    if reaction_color in color_definitions:
                                        reaction_color = color_definitions[
                                                reaction_color]
                                    edge.fill_color = reaction_color
                                if style.getGroup().isSetStrokeWidth():
                                    edge.curve_width = style.getGroup(
                                            ).getStrokeWidth()

                        if(style.isInTypeList("TEXTGLYPH")):
                            # print("\t\tApply this style to node text.")
                            # print("\t\tFont-family is: ",
                            # style.getGroup().getFontFamily
                            for node in self.network.nodes.values():
                                if(style.getGroup().isSetFontFamily()):
                                    node.font_name = style.getGroup(
                                            ).getFontFamily()
                                    print("set node font_name to: ",
                                          node.font_name)
                # localInformation
                # styles - idlist
                info_local = rPlugin.getRenderInformation(0)
                if(info_local):
                    for j in range(info_local.getNumStyles()):
                        style = info_local.getStyle(j)
                        print("\t\tids: ", style.createIdString())
                        print("\t\tfill color: ",
                              style.getGroup().getFillColor())

    def fitToWindow(self, left, top, right, bottom):
        sbnw.fit_to_window(self.h_layout_info, left, top, right, bottom)

    def arrowheadGetStyle(self, role):
        return sbnw.arrowheadGetStyle(role)

    def arrowheadSetStyle(self, role, style):
        sbnw.arrowheadSetStyle(role, style)

    def setModelNamespace(self, level, version):
        """Specify the Model"""
        sbnw.setModelNamespace(self.h_layout_info, level, version)
