"""
Creates a python interface to the c API.
"""
import libsbml_draw.c_api.sbnw_c_api as sbnw


class SBMLlayout:
    """SBMLlayout represents the model in an SBML file, which already exists or
    which can be created from scratch."""       

    SBNW_version = sbnw.getCurrentLibraryVersion().decode('utf-8')
    
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
        sbml_string = sbnw.getSBMLwithLayoutStr(self.h_model, self.h_layout_info).decode('utf-8')
        return sbml_string 
    
    def writeSBMLWithLayout (self, output_filename):   
        filename = output_filename.encode('utf-8')
        result = sbnw.writeSBMLwithLayout(filename, self.h_model, self.h_layout_info)
        print("writeSBMLwithLayout result: ", result)
        # if result error, raise Exception?
        return result  
		