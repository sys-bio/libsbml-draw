"""Represent the network as a collection of nodes and reactions.
"""
from enum import IntEnum

from matplotlib.patches import ArrowStyle

import libsbml_draw.c_api.sbnw_c_api as sbnw


class Role(IntEnum):
    SUBSTRATE = 0
    PRODUCT = 1
    SIDESUBSTRATE = 2
    SIDEPRODUCT = 3
    MODIFIER = 4
    ACTIVATOR = 5
    INHIBITOR = 6


class Node():
    """ """
    def __init__(self, h_node):

        self.width = sbnw.node_getWidth(h_node)
        self.height = sbnw.node_getHeight(h_node)
        self.center = sbnw.node_getCentroid(h_node)
        self.lower_left_point = [self.center.x - self.width/2,
                                 self.center.y - self.height/2]
        self.name = sbnw.node_getName(h_node)
        self.id = sbnw.node_getID(h_node)
        self.edge_color = "#0000ff30"
        self.fill_color = "#0000ff30"
        self.font_size = 12
        self.font_family = "Arial"
        self.font_color = "black"
        self.font_style = "normal"


class Curve():
    """ """

    role_arrowstyles = ["-",                                  # SUBSTRATE
                        "-|>",                                # PRODUCT
                        "-",                                  # SIDESUBSTRATE
                        "-|>",                                # SIDEPRODUCT
                        ArrowStyle("|-|",
                                   widthA=0, angleA=None,
                                   widthB=1.0, angleB=None),  # MODIFIER
                        "-|>",                                # ACTIVATOR
                        ArrowStyle("|-|",
                                   widthA=0, angleA=None,
                                   widthB=1.0, angleB=None)   # INHIBITOR
                        ]

    def __init__(self, h_curve):

        curveCPs = sbnw.getCurveCPs(h_curve)
        self.start_point = curveCPs.start
        self.end_point = curveCPs.end
        self.control_point_1 = curveCPs.control_point_1
        self.control_point_2 = curveCPs.control_point_2
        self.role = sbnw.curve_getRole(h_curve)
        # what if role isn't defined?
        self.curveArrowStyle = Curve.role_arrowstyles[self.role]
    

class Reaction():
    """ """
    def __init__(self, h_reaction):
        self.curves = []
        for curve_index in range(sbnw.reaction_getNumCurves(h_reaction)):
            h_curve = sbnw.reaction_getCurvep(h_reaction, curve_index)
            self.curves.append(Curve(h_curve))
        self.id = sbnw.reaction_getID(h_reaction)
        self.edge_color = "blue"
        self.fill_color = "blue"
        self.curve_width = 1


class Network():
    """ """
    def __init__(self, h_network):
        self.h_network = h_network
        self.nodes = {}
        self.reactions = {}
        self._add_nodes(self.h_network)
        self._add_reactions(self.h_network)

    def _add_nodes(self, h_network):
        for node_index in range(sbnw.nw_getNumNodes(h_network)):
            h_node = sbnw.nw_getNodep(h_network, node_index)
            node_id = sbnw.node_getID(h_node)
            self.nodes[node_id] = Node(h_node)

    def _add_reactions(self, h_network):
        for reaction_index in range(sbnw.nw_getNumRxns(h_network)):
            h_reaction = sbnw.nw_getReactionp(h_network, reaction_index)
            reaction_id = sbnw.reaction_getID(h_reaction)
            self.reactions[reaction_id] = Reaction(h_reaction)
