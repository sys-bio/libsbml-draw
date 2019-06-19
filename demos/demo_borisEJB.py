from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "BorisEJB.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/data/" + model_file_name))


sl = SBMLlayout(str(model_file), autoComputeLayout=True)

sl._describeModel()

sl.drawNetwork()

sl2 = SBMLlayout(str(model_file))

sl2._describeModel()

sl2.drawNetwork()
