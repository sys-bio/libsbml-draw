from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

#chance glycolysis 1960
#model_file_name = "chance_glycolysis_1960.xml"
#model_file_name = "repressilator_BIOMD12.xml"

model_file_name = "glycolysis_BIOMD176.xml"


model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/libs/" + model_file_name))


sl = SBMLlayout(str(model_file))

sl.describeModel()

sl.drawNetwork()

sl.aliasNode("ATP")
sl.aliasNode("ADP")
sl.drawNetwork()

sl.regenerateLayout()

sl.drawNetwork()

loo = sl.getLayoutAlgorithmOptions()

print(loo.k)

#sl.setLayoutAlgorithm_grav()

#sl.drawNetwork("glycolysis_bm12.png")

#sl.drawNetwork("glycolysis_bm12.pdf")
