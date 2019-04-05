# from pathlib import Path
# import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

#model_file = "C:\\tmp\\model.xml"
#model_file = "/home/radix/repos/libsbml-draw/model_files/model.xml"
model_file = "/Users/natalieh/repos/libsbml-draw/model_files/model.xml"
#model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model_files/model.xml"))

print("model file: \t", model_file)

sl = SBMLlayout(model_file)


sl._describeModel()


#sl.drawNetwork("C:\\tmp\\model_compute_layout.png")


print("node ids: ", sl.getNodeIds())
print("reaction ids: ", sl.getReactionIds())


sl.setNodeColor("all", "lightpink")
sl.setNodeEdgeColor("X0", "green")
sl.setNodeFillColor("X0", "yellow")

sl.setReactionCurveWidth("_J0", 2)
sl.setReactionColor("all", "purple")
sl.setReactionColor("_J0", "green")

# KeyError in setter
#sl.setReactionColor("_J", "green")
# ValueError in matplotlib
#sl.setReactionColor("_J1", "greene")

print("reaction edge: ", sl.getReactionEdgeColor("_J0"))
print("reaction fill: ", sl.getReactionFillColor("_J0"))

sl.drawNetwork()

