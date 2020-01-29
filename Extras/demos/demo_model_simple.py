from pathlib import Path
import pkg_resources

from libsbml_draw.sbml_layout import SBMLlayout

model_file_name = "model.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/libs/" + model_file_name))

sl = SBMLlayout(str(model_file))

sl.describeModel()

print()
print("node ids: ", sl.getNodeIds())
print("reaction ids: ", sl.getReactionIds())


sl.drawNetwork()


#out_file = "model_out.xml"        
#sl.writeSBMLFile("model_out.xml")

#sl.getCurvesAttachedToNodes()



#sl2 = SBMLlayout(out_file)

#print("sl2 layoutSpecified: ", sl2._SBMLlayout__layoutSpecified)

#sl2.drawNetwork()

#sl2.setLayoutAlgorithm_k(10)

#sl2.regenerateLayout()

#sl2.drawNetwork()


#sl2.writeSBMLFile("model_out_render.xml")



sl.setReactionColor("_J0", "red", species="A")

sl.setReactionEdgeColor("_J3", "#0000ff30")

sl.setReactionEdgeColor("_J4", "pink", species="D")

# only applies to FancyArrowPatch arrowhead 
sl.setReactionFillColor("_J2", "lightgreen")

sl.setReactionCurveWidth("_J0", 5, role_name="product")
sl.setReactionCurveWidth("_J4", 10)
sl.setReactionCurveWidth(["_J1", "_J2", "_J3"], 15)

sl.setNodeFillColor("A", "pink")
sl.setNodeEdgeColor("all", "green")
sl.setNodeEdgeWidth(["D","X1","C"], 3)

sl.setNodeFontWeight(["X0","A","B","C","D","X1"], "bold")

sl.setNodeTextAnchor("X0", "right")
sl.setNodeTextAnchor("A", "left")
sl.setNodeVTextAnchor("B", "center")

sl.drawNetwork()

print("_J0 width: ", sl.getReactionCurveWidth("_J0"))

print("_J1 edge color: ", sl.getReactionEdgeColor("_J1"))
print("_J1 fill color: ", sl.getReactionFillColor("_J1"))

print("_J3 edge color: ", sl.getReactionEdgeColor("_J3"))
print("_J3 fill color: ", sl.getReactionFillColor("_J3"))

print("_J4 edge color: ", sl.getReactionEdgeColor("_J4"))
print("_J4 fill color: ", sl.getReactionFillColor("_J4"))

print("A: fill color: ", sl.getNodeFillColor("A"))
print("B: edge color: ", sl.getNodeEdgeColor("B"))
print("C: edge width: ", sl.getNodeEdgeWidth("C"))


print("X0: text anchor: ", sl.getNodeTextAnchor("X0"))
print("A: text anchor: ", sl.getNodeTextAnchor("A"))
print("B: vtext anchor: ", sl.getNodeVTextAnchor("B"))


sl.writeSBMLFile("model_simple_out.xml")




