from pathlib import Path
import pkg_resources
import pytest

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "BorisEJB.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))

sl = SBMLlayout(str(model_file), autoComputeLayout=True)

sl._describeModel()

sl.drawNetwork("boris_ejb_override.pdf")


def test_write_file_raises():

    with pytest.raises(ValueError):
        sl.writeSBMLFile("test_layout_override.xml")

# This will write if allowed, and when it is read back in, it displays as
# a single blob of garbage because everything is plotted with the same centers
# sl.writeSBMLFile("test_layout_override.xml")
# slr = SBMLlayout("test_layout_override.xml", autoComputeLayout=False)

slr = SBMLlayout(str(model_file), autoComputeLayout=False)

slr._describeModel()

slr.drawNetwork()

assert slr.getNodeTextAnchor("MKK_P") == "center"
# bottom means top in this situation
assert slr.getNodeVTextAnchor("MAPK") == "bottom"

assert slr.getNodeFontSize("MKK") == 11

assert slr.getNodeEdgeColor("MKKK") == "#969696"

assert slr.getNodeFillColor("MAPK_P") == "#c9e0fb"

assert slr.getReactionEdgeColor("J1") == [('MKKK_P', 'SUBSTRATE', '#ff9900'), 
                                          ('MKKK', 'PRODUCT', '#ff9900')]

assert slr.getReactionFillColor("J2") == [('MKK', 'SUBSTRATE', '#ff9900'), 
                                          ('MKK_P', 'PRODUCT', '#ff9900'), 
                                          ('MKKK_P', 'ACTIVATOR', '#ff9900')]



