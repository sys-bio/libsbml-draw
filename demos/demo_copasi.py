# from pathlib import Path
# import pkg_resources
import platform

from libsbml_draw.model.sbml_layout import SBMLlayout

if platform.system() == "Windows":
    model_dir = "C:\\tmp\\"
    model_file = "C:\\tmp\\copasi.xml"
elif platform.system() == "Linux":
    model_dir = "/home/radix/repos/libsbml-draw/model_files/"    
    model_file = "/home/radix/repos/libsbml-draw/model_files/copasi.xml"
else:
    model_dir = "/Users/natalieh/repos/libsbml-draw/model_files/"
    model_file = "/Users/natalieh/repos/libsbml-draw/model_files/copasi.xml"
#model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model_files/model.xml"))

print("model file: \n", model_file)

sl = SBMLlayout(model_file)


sl._describeModel()


print("node ids: ", sl.getNodeIds())
print("reaction ids: ", sl.getReactionIds())


sl.setNodeColor("S1", "lightpink")
sl.setNodeColor("S2", "lightgreen")


sl.drawNetwork()

new_model_file = model_dir + "render_sbml_pink_green.xml"
print("new model file: ", new_model_file)

sl.writeSBMLFile(new_model_file)


