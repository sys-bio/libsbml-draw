from pathlib import Path
import pkg_resources

from libsbml_draw.sbml_layout import SBMLlayout

#model_file_name = "GlycolysisOriginal_L3V1.xml"
#model_file_name = "GlycolysisOriginal-L3V1.xml"
model_file_name = "GlycolysisOriginal.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/libs/" + model_file_name))


sl = SBMLlayout(str(model_file))

sl.describeModel()

print("node font size: ", sl.getNodeFontSize("ATP"))

sl.drawNetwork("GlycolysisOriginal.pdf")

#sl.drawNetwork(figsize=(20,20))

#sl.setNodeFontSize("all", 8)

#sl.drawNetwork()

#for node in sl._SBMLlayout__network.nodes.values():
#    print("node id, name: ", node.id, node.name)
    
