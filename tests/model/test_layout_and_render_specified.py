"""Test libsbml_draw on an SBML file which includes layout and render
information.
"""
from pathlib import Path
import pkg_resources

from matplotlib.figure import Figure

import pytest

from libsbml_draw.model.sbml_layout import SBMLlayout

MODEL_FILE_NAME = "largerpathway.xml"

MODEL_FILE = Path(pkg_resources.resource_filename(
        "libsbml_draw",
        "model/data/" + MODEL_FILE_NAME))

SL = SBMLlayout(str(MODEL_FILE))


def test_network_properties():
    """Test that the network was constructed as expected. 
    """
    assert SL.getNumberOfCompartments() == 0
    assert SL.getNumberOfNodes() == 6
    assert SL.getNumberOfReactions() == 5

    assert set(SL.getNodeIds()) == set(['ABCDEFG','B',
                                        'C', 'D', 'E', 'F'])

    assert set(SL.getReactionIds()) == set(['_J0', '_J1', '_J2',
                                            '_J3', '_J4'])
    
def test_draw_network():
    """Test that a call to drawNetwork() is successful 
    """       
    fig = SL.drawNetwork()
    assert isinstance(fig, Figure)