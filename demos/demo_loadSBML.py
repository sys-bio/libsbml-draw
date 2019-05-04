from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "model.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/data/" + model_file_name))



sl = SBMLlayout()

sl.loadSBMLFile(str(model_file))

sl._describeModel()

sl.drawNetwork()

sl_str = sl.getSBMLString()



ss = SBMLlayout()

ss.loadSBMLString(sl_str)

ss._describeModel()

ss.drawNetwork()
