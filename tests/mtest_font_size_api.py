from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "model.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))

applyRender = True

sl = SBMLlayout(str(model_file), applyRender=applyRender)

sl._describeModel()

sl.drawNetwork()

assert sl.getNodeFontSize("X0") == 10

sl.setNodeFontSize("X0", 24)

assert sl.getNodeFontSize("X0") == 24

sl.drawNetwork()

sl.regenerateLayout()

sl.drawNetwork()

sl.setNodeFontSize("all", 18)

sl.drawNetwork()

assert sl.getNodeFontSize("X0") == 18
assert sl.getNodeFontSize("A") == 18
assert sl.getNodeFontSize("B") == 18
assert sl.getNodeFontSize("C") == 18
assert sl.getNodeFontSize("D") == 18
assert sl.getNodeFontSize("X1") == 18



