"""Test libsbml_draw on an SBML file which does not specify a layout.
"""
from pathlib import Path
import pkg_resources

from matplotlib.figure import Figure

import pytest

from libsbml_draw.model.sbml_layout import SBMLlayout

MODEL_FILE_NAME = "model.xml"

MODEL_FILE = Path(pkg_resources.resource_filename(
        "libsbml_draw",
        "model/data/" + MODEL_FILE_NAME))

SL = SBMLlayout(str(MODEL_FILE))

def test_network_properties():
    """Test that the network was constructed as expected. 
    """
    assert SL.getNumberOfCompartments() == 0
    assert SL.getNumberOfNodes() == 6
    assert SL.getNumberOfReactions() == 6

    assert set(SL.getNodeIds()) == set(['X0', 'A', 'B',
                                        'D', 'C', 'X1'])

    assert set(SL.getReactionIds()) == set(['_J0', '_J1', '_J2',
                                            '_J3', '_J4', '_J5'])
    
def test_draw_network():
    """Test that a call to drawNetwork() is successful 
    """       
    fig = SL.drawNetwork(show=False)
    assert isinstance(fig, Figure)
    
def test_style_changes():
    SL.setNodeColor("all", "lightpink")
    SL.setNodeEdgeColor("all", "purple")
    SL.setNodeEdgeColor("X0", "green")
    SL.setNodeFillColor("X0", "yellow")
    SL.setNodeEdgeWidth("all", 2)
    SL.setNodeEdgeWidth("X1", 5)
    SL.setNodeEdgeWidth(["A","B","C"], 3)

    SL.setReactionCurveWidth("_J0", 3)
    SL.setReactionColor("all", "purple")
    SL.setReactionColor("_J0", "green")

    for node in SL._SBMLlayout__network.nodes.values():
        if node.id == "X0":
            assert node.fill_color == "yellow"
            assert node.edge_color == "green"
        if node.id != "X0":
            assert node.fill_color == "lightpink"
            assert node.edge_color == "purple"
        if node.id in ("X0", "D"):
            assert node.edge_width == 2
        if node.id in ("A", "B", "C"):
            assert node.edge_width == 3
        if node.id == "X1":
            assert node.edge_width == 5

    for reaction in SL._SBMLlayout__network.reactions.values():
        if reaction.id != "_J0":
            assert reaction.edge_color == "purple"
            assert reaction.fill_color == "purple"
        if reaction.id == "_J0":
            assert reaction.curve_width == 3
            assert reaction.edge_color == "green"
            assert reaction.fill_color == "green"

def test_fr_alg_options_changes():
    SL.setLayoutAlgorithmOptions(k=40, grav=20)
    fr_alg_options = SL.getLayoutAlgorithmOptions()
    assert fr_alg_options.k == 40
    assert fr_alg_options.grav == 20
