from pathlib import Path
import pkg_resources

from libsbml_draw.sbml_layout import SBMLlayout


model_file_name = "simple-L2-render-local.xml"
#model_file_name = "simple-L2-render-local-L3V1.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/libs/" + model_file_name))

sl = SBMLlayout(str(model_file))

sl.describeModel()

sl.drawNetwork()

for node in sl._SBMLlayout__network.nodes.values():
    print("node: ", node.id, node.name, node.font_size)

for reaction in sl._SBMLlayout__network.reactions.values():
    print("reaction: ", reaction.id)


