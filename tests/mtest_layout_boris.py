from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "BorisEJB.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))

sl = SBMLlayout(str(model_file), autoComputeLayout=False)

sl._describeModel()

assert sl.getNumberOfNodes() == 8
assert sl.getNumberOfReactions() == 10

sl.drawNetwork("boris_ejb_override.png")

sl.writeSBMLFile("ftest_layout_override.xml")

slr = SBMLlayout("ftest_layout_override.xml", autoComputeLayout=False)

slr._describeModel()

slr.drawNetwork()

assert sl.getNumberOfNodes() == 8
assert sl.getNumberOfReactions() == 10
