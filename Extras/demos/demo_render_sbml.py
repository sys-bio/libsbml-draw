import platform

from libsbml_draw.sbml_layout import SBMLlayout


if platform.system() == "Windows":
    model_file = "C:\\Users\\nrhaw\\Documents\\repos\\libsbml-draw\\model_files\\render_sbml_pink_green.xml"
elif platform.system() == "Linux":    
    model_file = "/home/radix/repos/libsbml-draw/model_files/render_sbml.xml"
else:
    model_file = "/Users/natalieh/repos/libsbml-draw/model_files/render_sbml.xml"



sl = SBMLlayout(model_file)


#sl.describeModel()


sl.drawNetwork()


print("node ids: ", sl.getNodeIds())
print("reaction ids: ", sl.getReactionIds())

