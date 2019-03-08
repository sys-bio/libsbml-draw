"""
Creates a python interface to the c API.
"""
import libsbml

import libsbml_draw.c_api.sbnw_c_api as sbnw
from libsbml_draw.draw.draw_network import createNetworkFigure
from libsbml_draw.model.network import Network

class SBMLlayout:
    """SBMLlayout represents the model in an SBML file, which already exists or
    which can be created from scratch."""       

    SBNW_version = sbnw.getCurrentLibraryVersion()
    
    def __init__ (self, sbml_filename=None, layout_alg_options=sbnw.fr_alg_options()):
        # note: the default values for the fr_alg_options are 0's
        # maybe need to change that?
        self.sbml_filename = sbml_filename
        self.layout_alg_options = layout_alg_options

        if sbml_filename:
            self.h_model = sbnw.loadSBML(self.sbml_filename)
            self.h_layout_info = sbnw.processLayout (self.h_model)                
            self.h_network = sbnw.getNetworkp(self.h_layout_info)
        else:
            print("No SBML filename given, creating a new model from scratch.")
            self.h_model = sbnw.SBMLModel_newp()
            # not sure if process layout does something default, our model is empty here
            self.h_layout_info = sbnw.processLayout (self.h_model)  
            self.h_network = sbnw.getNetworkp(self.h_layout_info)
            # add nodes
            # add reactions
            # add compartments
        self.numNodes = self.getNumberOfNodes()
        self.numReactions = self.getNumberOfReactions()
        self.numCompartments = self.getNumberOfCompartments()
        self.network = None
    
    # Give the layout a starting point
    def randomizeLayout(self,):
        sbnw.randomizeLayout(self.h_layout_info)

    # Run the FR Layout Algorithm
    def doLayoutAlgorithm (self,):
        sbnw.doLayoutAlgorithm(self.layout_alg_options, self.h_layout_info)

    # Sizing of the Layout
    def fitToWindow (self, left, top, right, bottom):
        sbnw.fit_to_window(self.h_layout_info, left, top, right, bottom)

    # Styling for the Curves
    def arrowheadGetStyle(self, role):
        return sbnw.arrowheadGetStyle(role) 
    
    def arrowheadSetStyle (self, role, style):
        sbnw.arrowheadSetStyle(role, style)

    # Specify the Model         
    def setModelNamespace(self, level, version):
        sbnw.setModelNamespace(self.h_layout_info, level, version)

    # Describe the model
    def describeModel(self,):
        print()
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
        node_p = sbnw.nw_getNodepFromId(self.h_network, node_id.encode('utf-8'))
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
    def getSBMLWithLayout(self,):
        sbml_string = sbnw.getSBMLwithLayoutStr(self.h_model, self.h_layout_info)
        return sbml_string 
    
    def writeSBMLWithLayout (self, output_filename):   
        filename = output_filename.encode('utf-8')
        result = sbnw.writeSBMLwithLayout(filename, self.h_model, self.h_layout_info)
        print("writeSBMLwithLayout result: ", result)
        # if result error, raise Exception?
        return result  

    def createNetwork(self,):
        self.network = Network(self.h_network)
    
    def drawNetwork(self,):
        createNetworkFigure(self.network)   
        print("network, num nodes: ", len(self.network.nodes))
        print("network, num edges: ", len(self.network.edges))
        print("network, num rxns: ", self.getNumberOfReactions()) 
        for edge in self.network.edges.values():
            print(len(edge.curves), "curves")
            for curve in edge.curves:
                print("role: ", curve.role)
        #for node in self.network.nodes:
            
    def get_node_ids(self,):
        return list(self.network.nodes.keys())   

    def get_reaction_ids(self,):
        return list(self.network.edges.keys())
    
    def change_node_color(self, node_id, node_color):
        self.network.nodes[node_id].fill_color = node_color     
                          
    def change_node_fontsize(self, node_id, fontsize):                      
        self.network.nodes[node_id].font_size = fontsize

    def change_node_fontname(self, node_id, fontname):                      
        self.network.nodes[node_id].font_name = fontname
        
    def change_node_fontcolor(self, node_id, fontcolor):                      
        self.network.nodes[node_id].font_color = fontcolor

    def change_node_fontstyle(self, node_id, fontstyle):                      
        self.network.nodes[node_id].font_style = fontstyle
                          
    def change_reaction_color(self, reaction_id, reaction_color):
        self.network.edges[reaction_id].fill_color = reaction_color

    def change_reaction_curve_width(self, reaction_id, curve_width):
        self.network.edges[reaction_id].curve_width = curve_width
        
    def addRenderInformation(self, sbml_file_name):
        #sbml_str = self.getSBMLWithLayout()
        #print("render in sbml_str: ", "render" in sbml_str)
        
        doc = libsbml.readSBMLFromFile(sbml_file_name)
        model = doc.getModel(); 
        layout_plugin = model.getPlugin("layout")
        #lol_plugin = layout_plugin.getListOfLayouts().getPlugin("render")
        #info_global = lol_plugin.getRenderInformation(0)
        
        print("num layouts: ", layout_plugin.getNumLayouts())

        # get first layout, there may be only 1
        layout = layout_plugin.getLayout(0)
        
        rPlugin = layout.getPlugin("render")   

        print("rPlugin type: " , type(rPlugin))
        
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
        
    def writeRenderSBML(self, sbml_file_name, render_sbml_file_name):
        doc = self.addRenderInformation(sbml_file_name)        
        print("writing render sbml file")
        libsbml.writeSBMLToFile(doc, render_sbml_file_name)
        print("finished writing render sbml file!")

    def applyRenderInformation(self,):
        self.color_definitions = {}

        doc = libsbml.readSBMLFromFile(self.sbml_filename)
        model = doc.getModel(); 
        layout_plugin = model.getPlugin("layout")
        print("num layouts: ", layout_plugin.getNumLayouts())
        layout = layout_plugin.getLayout(0)
        rPlugin = layout.getPlugin("render")
        render_plugin = layout_plugin.getListOfLayouts().getPlugin("render")
        print("num global info: ", render_plugin.getNumGlobalRenderInformationObjects()) 
        print("num local info: ", rPlugin.getNumLocalRenderInformationObjects())

        #globalInformation
            
        info_global = render_plugin.getRenderInformation(0)

        # -- add color definitions 

        for j in range(info_global.getNumColorDefinitions()):    
            color = info_global.getColorDefinition(j)
            self.color_definitions[color.getId()] = color.createValueString()
        
        # -- styles - rolelist, typelist
        print("styles: ", info_global.getNumStyles())

        for j in range(info_global.getNumStyles()):    
            style = info_global.getStyle(j)
    
            print("\tstyle: ", style.getId())
            print("\t\troles: ", style.createRoleString())
            print("\t\ttypes: ", style.createTypeString())
            
        #localInformation
            # styles - idlist
            #info_local = rPlugin.getRenderInformation(0)
            #for j in range(info_local.getNumStyles()):
            #    style = info_local.getStyle(j)
            #print("\t\tids: ", style.createIdString())

        
        
        
        
        


                