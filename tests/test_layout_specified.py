from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

MODEL_FILE_NAME = "largerpathway.xml"

MODEL_FILE = Path(pkg_resources.resource_filename(
        "libsbml_draw",
        "model/data/" + MODEL_FILE_NAME))

sl = SBMLlayout(str(MODEL_FILE))


def test_layout_specified():
    assert sl.getNumberOfNodes() == 6
    assert sl.getNumberOfReactions() == 5

    assert sl.getNodeFontSize("ABCDEFG") == 12
    assert sl.getNodeFontWeight("F") == "normal"

    assert sl.getNodeFillColor("E") == "#a0e0a030"


MODEL_FILE_NAME = "test_larger_pathway.xml"

MODEL_FILE = Path(pkg_resources.resource_filename(
        "libsbml_draw",
        "model/data/" + MODEL_FILE_NAME))


slr =  SBMLlayout(str(MODEL_FILE))


def test_layout_specified_back_in():

    assert sl.getNumberOfNodes() == 6
    assert sl.getNumberOfReactions() == 5

    assert sl.getReactionCurveWidth("_J2") == [('C', 'SUBSTRATE', 3.0), 
                                               ('ABCDEFG', 'PRODUCT', 3.0)]

    assert sl.getReactionEdgeColor("_J1") == [('B', 'SUBSTRATE', '#000000a0'), 
                                              ('C', 'PRODUCT', '#000000a0'), 
                                              ('D', 'PRODUCT', '#000000a0')]
