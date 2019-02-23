"""Represent the network as a collection of nodes and edges.
"""
import libsbml_draw.c_api.sbnw_c_api as sbnw

class Node():
    """ """
    def __init__ (self, h_node):

        self.width = sbnw.node_getWidth(h_node)
        self.height = sbnw.node_getHeight(h_node)
        self.center = sbnw.node_getCentroid(h_node)
        self.lower_left_point = [self.center.x - self.width/2,
                                 self.center.y - self.height/2]
        self.name = sbnw.node_getName(h_node)


class Curve():
    """ """
    def __init__ (self, h_curve):
    
        curveCPs = sbnw.getCurveCPs(h_curve)
        self.start_point = curveCPs.start
        self.end_point = curveCPs.end
        self.control_point_1 = curveCPs.control_point_1
        self.control_point_2 = curveCPs.control_point_2         
        self.curveArrowStyle = "-"

class Edge():
    """ """
    def __init__ (self, h_reaction):
        self.curves = []        
        for curve_index in range(sbnw.reaction_getNumCurves(h_reaction)):
            h_curve = sbnw.reaction_getCurvep(h_reaction, curve_index)  
            self.curves.append(Curve(h_curve))

        
class Network():
    """ """
    def __init__ (self, h_network):
        self.h_network = h_network
        self.nodes = []
        self.edges = []
        self._add_nodes(self.h_network)
        self._add_edges(self.h_network)
         
    def _add_nodes(self, h_network):
        for node_index in range(sbnw.nw_getNumNodes(h_network)):
            h_node = sbnw.nw_getNodep(h_network, node_index)
            self.nodes.append(Node(h_node))
          
    def _add_edges(self, h_network):
        for reaction_index in range(sbnw.nw_getNumRxns(h_network)):
            h_reaction = sbnw.nw_getReactionp(h_network, reaction_index)                   
            self.edges.append(Edge(h_reaction))        
            
            