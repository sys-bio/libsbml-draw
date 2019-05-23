import platform

from libsbml_draw.model.sbml_layout import SBMLlayout


if platform.system() == "Windows":
    model_file = "C:\\tmp\\largerpathway.xml"
elif platform.system() == "Linux":    
    model_file = "/home/radix/repos/libsbml-draw/model_files/largerpathway.xml"
else:
    model_file = "/Users/natalieh/repos/libsbml-draw/model_files/largerpathway.xml"



sl = SBMLlayout(model_file)


#sl.describeModel()


sl.setNodeFontSize("all", 24)


sl.drawNetwork(figsize=(12,12))


print("node ids: ", sl.getNodeIds())
print("reaction ids: ", sl.getReactionIds())

