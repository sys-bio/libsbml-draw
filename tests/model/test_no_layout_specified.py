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
    fig = SL.drawNetwork()
    assert isinstance(fig, Figure)
    
@pytest.mark.skip    
def test_style_changes():
    pass

@pytest.mark.skip    
def test_fr_alg_options_changes():
    pass
    