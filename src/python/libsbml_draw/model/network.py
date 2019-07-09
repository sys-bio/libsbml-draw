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


class Compartment():
    """Represents a compartment in the SBML model."""

    def __init__(self, h_compartment):

        self.width = sbnw.compartment_getWidth(h_compartment)
        self.height = sbnw.compartment_getHeight(h_compartment)
        self.min_corner = sbnw.compartment_getMinCorner(h_compartment)
        self.max_corner = sbnw.compartment_getMaxCorner(h_compartment)
        self.lower_left_point = [self.min_corner.x, self.min_corner.y]
        self.id = sbnw.compartment_getID(h_compartment)
        self.edge_color = "#0000ff30"  # 30% blue
        self.fill_color = "#0000ff05"  # 5% blue
        self.line_width = 3


class Node():
    """Represents a node in the SBMl model."""

    def __init__(self, h_node):

        self.width = sbnw.node_getWidth(h_node)
        self.height = sbnw.node_getHeight(h_node)
        self.center = sbnw.node_getCentroid(h_node)
        self.lower_left_point = [self.center.x - self.width/2,
                                 self.center.y - self.height/2]
        self.name = sbnw.node_getName(h_node)
        self.id = sbnw.node_getID(h_node)
        self.edge_width = 1
        self.edge_color = "#0000ff"
        self.fill_color = "#c9e0fb"
        self.font_size = 12
        self.font_family = "Arial"
        self.font_color = "#000000"
        self.font_style = "normal"
        self.text_anchor = "center"
        self.vtext_anchor = "center"

class Curve():
    """Part of a complete reaction curve. As an example, a reaction between a
    substrate and a product usually consists of two curves.  The first curve
    has no arrowhead (i.e. has arrowstyle '-') and the second has an arrowhead
    pointing to the product."""

    role_arrowstyles = ["-",                                  # SUBSTRATE
                        "-|>",                                # PRODUCT
                        "-",                                  # SIDESUBSTRATE
                        "-|>",                                # SIDEPRODUCT
                        "-|>",                                # MODIFIER
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
        self.role_name = Role(self.role).name
        self.curveArrowStyle = Curve.role_arrowstyles[self.role]


class Reaction():
    """Represents a reaction in the SBML model."""
    def __init__(self, h_reaction):
        self.curves = []
        for curve_index in range(sbnw.reaction_getNumCurves(h_reaction)):
            h_curve = sbnw.reaction_getCurvep(h_reaction, curve_index)
            self.curves.append(Curve(h_curve))
        self.id = sbnw.reaction_getID(h_reaction)
        self.edge_color = "blue"
        self.fill_color = "blue"
        self.curve_width = 1
        self.centroid = sbnw.reaction_getCentroid(h_reaction)


class Network():
    """Represents a network in the SBML model, and consists of nodes and
    reactions."""
    def __init__(self, h_network):
        self.h_network = h_network
        self.compartments = {}
        self.nodes = {}
        self.reactions = {}
        self._add_nodes()
        self._add_reactions()
        self._add_compartments()
        self.aliasedNodes = {}

    def _remove_node(self, node_id):
        """Remove a node from the network.

        Args:
            node_id (str): id for the node

        Returns: None
        """
        if node_id in self.nodes:
            del self.nodes[node_id]
        else:
            raise ValueError(f"species {node_id} is not in the network.")

    def _add_alias_nodes(self, node_id):
        """Add alias nodes to the network for the given node.

        Args:
            node_id (str): id for the node

        Returns: None
        """
        if node_id in self.nodes:

            aliased_node = self.nodes[node_id]

            h_node_id = node_id.encode('utf-8')
            h_node = sbnw.nw_getNodepFromId(self.h_network, h_node_id)
            num_aliases = sbnw.nw_getNumAliasInstances(self.h_network, h_node)

            alias_ids = list()

            for alias_index in range(num_aliases):
                h_alias_node = sbnw.nw_getAliasInstancep(self.h_network,
                                                         h_node, alias_index)

                alias_node_id = sbnw.node_getID(
                        h_alias_node) + "_" + str(alias_index)

                self.nodes[alias_node_id] = Node(h_alias_node)

                self.nodes[alias_node_id].edge_width = aliased_node.edge_width
                self.nodes[alias_node_id].edge_color = aliased_node.edge_color
                self.nodes[alias_node_id].fill_color = aliased_node.fill_color
                self.nodes[alias_node_id].font_size = aliased_node.font_size
                self.nodes[alias_node_id].font_family = aliased_node.font_family  # noqa
                self.nodes[alias_node_id].font_color = aliased_node.font_color
                self.nodes[alias_node_id].font_style = aliased_node.font_style

                alias_ids.append(alias_node_id)

            self.aliasedNodes[node_id] = alias_ids
        else:
            raise ValueError(f"species {node_id} is not in the network.")

    def _add_compartments(self,):
        """Populates the collection of compartments.

        Args: None

        Returns: None
        """
        for compartment_index in range(
                sbnw.nw_getNumCompartments(self.h_network)):
            h_compartment = sbnw.nw_getCompartmentp(self.h_network,
                                                    compartment_index)
            compartment_id = sbnw.compartment_getID(h_compartment)
            self.compartments[compartment_id] = Compartment(h_compartment)

    def _add_nodes(self,):
        """Populates the collection of nodes.

        Args: None

        Returns: None
        """
        for node_index in range(sbnw.nw_getNumNodes(self.h_network)):
            h_node = sbnw.nw_getNodep(self.h_network, node_index)
            node_id = sbnw.node_getID(h_node)
            num_aliases = sbnw.nw_getNumAliasInstances(self.h_network, h_node)

            if node_id in self.nodes:
                for i in range(num_aliases):
                    alias_node_id = node_id + "_" + str(i)
                    if alias_node_id not in self.nodes:
                        self.nodes[alias_node_id] = Node(h_node)
                        break
            else:
                self.nodes[node_id] = Node(h_node)

    def _add_reactions_after_node_alias(self,):
        """Updates the reactions in the network after a node has been aliased.

        Args: None

        Returns: None
        """
        existing_reactions = [reaction for reaction in self.reactions.values()]

        # Acquire new curve layout data for the reactions
        self._add_reactions()

        # Restore the current render data for the reactions
        for reaction in existing_reactions:
            self.reactions[reaction.id].edge_color = reaction.edge_color
            self.reactions[reaction.id].fill_color = reaction.fill_color
            self.reactions[reaction.id].curve_width = reaction.curve_width

    def _add_reactions(self,):
        """Populates the collection of reactions.

        Args: None

        Returns: None
        """
        for reaction_index in range(sbnw.nw_getNumRxns(self.h_network)):
            h_reaction = sbnw.nw_getReactionp(self.h_network, reaction_index)
            reaction_id = sbnw.reaction_getID(h_reaction)
            self.reactions[reaction_id] = Reaction(h_reaction)

    def _update_compartments_layout(self,):
        """Updates the layout information for the compartments.

        Args: None

        Returns: None
        """
        for compartment_index in range(
                sbnw.nw_getNumCompartments(self.h_network)):
            h_compartment = sbnw.nw_getCompartmentp(self.h_network,
                                                    compartment_index)
            compartment_id = sbnw.compartment_getID(h_compartment)
            compartment = self.compartments[compartment_id]

            compartment.width = sbnw.compartment_getWidth(h_compartment)
            compartment.height = sbnw.compartment_getHeight(h_compartment)

            compartment.min_corner = sbnw.compartment_getMinCorner(
                    h_compartment)
            compartment.max_corner = sbnw.compartment_getMaxCorner(
                    h_compartment)
            compartment.lower_left_point = [compartment.min_corner.x,
                                            compartment.min_corner.y]

    def _update_nodes_layout(self,):
        """Updates the layout information for the nodes.

        Args: None

        Returns: None
        """
        for node_index in range(sbnw.nw_getNumNodes(self.h_network)):
            h_node = sbnw.nw_getNodep(self.h_network, node_index)
            node_id = sbnw.node_getID(h_node)

            if node_id in self.aliasedNodes:

                num_aliases = sbnw.nw_getNumAliasInstances(self.h_network,
                                                           h_node)

                for alias_index in range(num_aliases):

                    h_alias_node = sbnw.nw_getAliasInstancep(
                            self.h_network,
                            h_node,
                            alias_index)

                    alias_node_id = self.aliasedNodes[node_id][alias_index]
                    node = self.nodes[alias_node_id]
                    node.center = sbnw.node_getCentroid(h_alias_node)
                    node.lower_left_point = [node.center.x - node.width/2,
                                             node.center.y - node.height/2]
            else:
                node = self.nodes[node_id]
                node.center = sbnw.node_getCentroid(h_node)
                node.lower_left_point = [node.center.x - node.width/2,
                                         node.center.y - node.height/2]

    def _update_reactions_layout(self,):
        """Updates the layout information for the reactions.

        Args: None

        Returns: None
        """
        for reaction_index in range(sbnw.nw_getNumRxns(self.h_network)):
            h_reaction = sbnw.nw_getReactionp(self.h_network, reaction_index)
            reaction_id = sbnw.reaction_getID(h_reaction)
            reaction = self.reactions[reaction_id]

            reaction.centroid = sbnw.reaction_getCentroid(h_reaction)

            reaction.curves = []
            for curve_index in range(sbnw.reaction_getNumCurves(h_reaction)):
                h_curve = sbnw.reaction_getCurvep(h_reaction, curve_index)
                reaction.curves.append(Curve(h_curve))

    def updateNetwork(self,):
        """Updates the layout position values for the compartments, nodes,
        reactions (and the curves making up each reaction).

        Args: None

        Returns: None
        """
        self._update_compartments_layout()
        self._update_nodes_layout()
        self._update_reactions_layout()
