from libsbml_draw.model.sbml_layout import SBMLlayout

model_file = "C:\\tmp\\modexmpl.xml"


sl = SBMLlayout(model_file)


#sl.describeModel()


sl.drawNetwork()


print("node ids: ", sl.getNodeIds())
print("reaction ids: ", sl.getReactionIds())
