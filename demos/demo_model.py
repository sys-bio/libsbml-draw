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

sl._describeReaction(0)

sl.arrowheadGetVert(1,1)

centroid = sl.getNodeCentroid("X0")
print("centroid: ", centroid)

centroid = sl.getReactionCentroid("_J0")
print("rxn centroid: ", centroid)
centroid = sl.getReactionCentroid("J0")
print("rxn centroid: ", centroid)

print("X0", sl.getNodeColor("X0"))
print("X", sl.getNodeColor("X"))

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



