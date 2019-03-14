from libsbml_draw.model.sbml_layout import SBMLlayout

model_file = "C:\\tmp\\model.xml"


sl = SBMLlayout(model_file)


#sl.describeModel()


sl.drawNetwork()


print("node ids: ", sl.getNodeIds())
print("reaction ids: ", sl.getReactionIds())


sl.setNodeColor("all", "lightpink")
sl.setNodeEdgeColor("X0", "green")
sl.setNodeFillColor("X0", "yellow")

sl.setReactionCurveWidth("_J0", 2)
sl.setReactionColor("all", "purple")
sl.setReactionColor("_J0", "green")

print("reaction edge: ", sl.getReactionEdgeColor("_J0"))
print("reaction fill: ", sl.getReactionFillColor("_J0"))

sl.drawNetwork()

