from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "model.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/data/" + model_file_name))

sl = SBMLlayout(str(model_file))

sl._describeModel()


print("node ids: ", sl.getNodeIds())
print("reaction ids: ", sl.getReactionIds())


sl.drawNetwork()


out_file = "model_out.xml"        
sl.writeSBMLFile("model_out.xml")

sl2 = SBMLlayout(out_file)

print("sl2 layoutSpecified: ", sl2._SBMLlayout__layoutSpecified)

sl2.drawNetwork()

sl2.setLayoutAlgorithm_k(10)

sl2.regenerateLayout()

sl2.drawNetwork()





