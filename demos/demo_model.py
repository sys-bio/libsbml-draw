from pathlib import Path
import pkg_resources
# import platform

from libsbml_draw.model.sbml_layout import SBMLlayout

#from libsbml_draw import SBMLlayout

model_file_name = "model.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/data/" + model_file_name))


#if platform.system() == "Windows":
#    model_file = "C:\\tmp\\model.xml"
#elif platform.system() == "Linux":    
#    model_file = "/home/radix/repos/libsbml-draw/model_files/model.xml"
#else:
#    model_file = "/Users/natalieh/repos/libsbml-draw/model_files/model.xml"
#model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model_files/model.xml"))

print("model file: \n", model_file)

sl = SBMLlayout(str(model_file))


sl._describeModel()


#sl.drawNetwork("C:\\tmp\\model_compute_layout.png")


print("node ids: ", sl.getNodeIds())
print("reaction ids: ", sl.getReactionIds())

sl.drawNetwork()


sl.setNodeColor("all", "lightpink")
sl.setNodeEdgeColor("X0", "green")
sl.setNodeFillColor("X0", "yellow")

sl.setReactionCurveWidth("_J0", 3)
sl.setReactionColor("all", "purple")
sl.setReactionColor("_J0", "green")

# KeyError in setter
#sl.setReactionColor("_J", "green")
# ValueError in matplotlib
#sl.setReactionColor("_J1", "greene")

print("reaction edge: ", sl.getReactionEdgeColor("_J0"))
print("reaction fill: ", sl.getReactionFillColor("_J0"))

sl.drawNetwork()

sl.showLayoutAlgorithmOptions()

#sl.setLayoutAlgorithm_grav(20)

sl.setLayoutAlgorithmOptions(k=40, grav=20)

sl.showLayoutAlgorithmOptions()

sl.regenerateLayoutAndNetwork()

sl.drawNetwork()



