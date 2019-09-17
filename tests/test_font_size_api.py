from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "model.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))


sl = SBMLlayout(str(model_file))
sl.setNodeFontSize("X0", 24)


def test_font_size_api_singles():

    assert sl.getNodeFontSize("A") == 10
    assert sl.getNodeFontSize("X0") == 24


sl2 = SBMLlayout(str(model_file))
sl2.setNodeFontSize("all", 18)


def test_font_size_api_all():

    assert sl2.getNodeFontSize("X0") == 18
    assert sl2.getNodeFontSize("A") == 18
    assert sl2.getNodeFontSize("B") == 18
    assert sl2.getNodeFontSize("C") == 18
    assert sl2.getNodeFontSize("D") == 18
    assert sl2.getNodeFontSize("X1") == 18



