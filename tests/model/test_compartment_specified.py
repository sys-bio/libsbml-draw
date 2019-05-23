"""Test libsbml_draw on a file with a compartment specified. 
"""
from pathlib import Path
import pkg_resources

from matplotlib.figure import Figure

import pytest

from libsbml_draw.model.sbml_layout import SBMLlayout

MODEL_FILE_NAME_GLOBAL = "simple-L2-render-global.xml"

MODEL_FILE_GLOBAL = Path(pkg_resources.resource_filename(
        "libsbml_draw",
        "model/data/" + MODEL_FILE_NAME_GLOBAL))

SL_GLOBAL = SBMLlayout(str(MODEL_FILE_GLOBAL))

MODEL_FILE_NAME_LOCAL = "simple-L2-render-local.xml"

MODEL_FILE_LOCAL = Path(pkg_resources.resource_filename(
        "libsbml_draw",
        "model/data/" + MODEL_FILE_NAME_LOCAL))

SL_LOCAL = SBMLlayout(str(MODEL_FILE_LOCAL))

@pytest.mark.skip
def test_network_properties_global():
    """Test that the network was constructed as expected. 
    """
    assert SL_GLOBAL.getNumberOfCompartments() == 1
    assert SL_GLOBAL.getNumberOfNodes() == 2
    assert SL_GLOBAL.getNumberOfReactions() == 1

    assert set(SL_GLOBAL.getNodeIds()) == set(['Node0', 'Node1'])
    assert set(SL_GLOBAL.getReactionIds()) == set(['J0'])

@pytest.mark.skip
def test_draw_network_global():
    """Test that a call to drawNetwork() is successful 
    """       
    fig = SL_GLOBAL.drawNetwork()
    assert isinstance(fig, Figure)

@pytest.mark.skip
def test_network_properties_local():
    """Test that the network was constructed as expected. 
    """
    assert SL_LOCAL.getNumberOfCompartments() == 1
    assert SL_LOCAL.getNumberOfNodes() == 2
    assert SL_LOCAL.getNumberOfReactions() == 1

    assert set(SL_LOCAL.getNodeIds()) == set(['Node0', 'Node1'])
    assert set(SL_LOCAL.getReactionIds()) == set(['J0'])

@pytest.mark.skip    
def test_draw_network_local():
    """Test that a call to drawNetwork() is successful 
    """       
    fig = SL_LOCAL.drawNetwork()
    assert isinstance(fig, Figure)
