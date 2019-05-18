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

sl.setNodeEdgeWidth("all", 2)

out_file = "model_out.xml"        
sl.writeSBMLFile("model_out.xml")
sl2 = SBMLlayout(out_file)
sl2.drawNetwork()

sl.getArrowheadVert(1,1)

centroid = sl.getNodeCentroid("X0")
print("centroid: ", centroid)

centroid = sl.getReactionCentroid("_J0")
print("rxn centroid: ", centroid)
#centroid = sl.getReactionCentroid("J0")
#print("rxn centroid: ", centroid)

print("X0", sl.getNodeColor("X0"))
#print("X", sl.getNodeColor("X"))

sl.setNodeColor("all", "lightpink")
sl.setNodeEdgeColor("all", "purple")
sl.setNodeEdgeColor("X0", "green")
sl.setNodeFillColor("X0", "yellow")
sl.setNodeEdgeWidth("all", 2)
sl.setNodeEdgeWidth("X1", 5)
sl.setNodeEdgeWidth(["A","B","C"], 3)

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

#sl.setLayoutAlgorithmOptions(mag=1)

sl.showLayoutAlgorithmOptions()

sl.regenerateLayoutAndNetwork()

sl.drawNetwork()

print("node centroid: ", sl.getNodeCentroid("X0"))
print("rxn centroid: ", sl.getReactionCentroid("_J0"))

print("Bezier Points: ", sl.getReactionBezierPoints("_J0"))


sl.setNodeCentroid("X0", 200, 300)

sl.drawNetwork()

print("node centroid: ", sl.getNodeCentroid("X0"))

print("X1 locked, False: ", sl.getIsNodeLocked("X1"))

sl.lockNode("X1")

print("X1 locked, True: ", sl.getIsNodeLocked("X1"))


sl.regenerateLayoutAndNetwork()
sl.drawNetwork()

sl.regenerateLayoutAndNetwork()
sl.drawNetwork()

sl.unlockNode("X1")

print("X1 locked, False: ", sl.getIsNodeLocked("X1"))


sl.aliasNode("A")

#print("A aliased? ", sl.getIsNodeAliased("A"))

sl.drawNetwork()

print(sl.getNodeIds())

x = list()
y = list()

for node in sl.getNodeIds():
    centroid = sl.getNodeCentroid(node)
    x.append(centroid[0])
    y.append(centroid[1])    
    print("centroid: ", centroid[0], ", ", centroid[1])
    print("width: ", sl.getNodeWidth(node))
    print("height: ", sl.getNodeHeight(node))

print()    
print("min x, max x: ", min(x)-20, ", ", max(x)+20)
print("min y, max y: ", min(y)-10, ", ", max(y)+10)
print()
print("width: ", max(x) - min(x))
print("height: ", max(y) - min(y))
print()


