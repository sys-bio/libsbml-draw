from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

#chance glycolysis 1960
#model_file_name = "chance_glycolysis_1960.xml"
#model_file_name = "glycolysis_BIOMD12.xml"

model_file_name = "glycolysis_BIOMD176.xml"


model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/data/" + model_file_name))


sl = SBMLlayout(str(model_file))

sl._describeModel()

sl.drawNetwork(figsize=(16,16))





