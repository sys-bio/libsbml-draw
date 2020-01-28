from pathlib import Path
import pkg_resources

from libsbml_draw.sbml_layout import SBMLlayout

model_file_name = "TCA_ecoli_glucose_BIOMD222_url.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/libs/" + model_file_name))


sl = SBMLlayout(str(model_file))

sl.describeModel()

sl.drawNetwork()
