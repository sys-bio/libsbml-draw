from pathlib import Path
import pkg_resources

from libsbml_draw.sbml_layout import SBMLlayout

model_file_name = "BorisEJB.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/libs/" + model_file_name))


sl = SBMLlayout(str(model_file), autoComputeLayout=True)

sl.describeModel()

sl.drawNetwork("Boris_EJB.png")
sl.drawNetwork("Boris_EJB.pdf")


sl2 = SBMLlayout(str(model_file))

sl2.describeModel()

sl2.drawNetwork()
