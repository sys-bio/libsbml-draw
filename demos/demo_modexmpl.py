from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "modexmpl.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/data/" + model_file_name))

sl = SBMLlayout(str(model_file))

sl._describeModel()

fig = sl.drawNetwork()

sl.setArrowheadScale(1, 25)
sl.setArrowheadScale(4, 25)

fig = sl.drawNetwork()


