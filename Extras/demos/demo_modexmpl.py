from pathlib import Path
import pkg_resources

from libsbml_draw.sbml_layout import SBMLlayout

model_file_name = "modexmpl.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/libs/" + model_file_name))

sl = SBMLlayout(str(model_file))

sl.describeModel()

fig = sl.drawNetwork()
#fig = sl.drawNetwork(node_mutation_scale=5)

#sl.setArrowheadScale(1, 15)
#sl.setArrowheadScale(4, 15)

#fig = sl.drawNetwork(node_mutation_scale=5)


