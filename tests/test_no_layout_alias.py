from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "model.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/data/" + model_file_name))

sl = SBMLlayout(str(model_file), applyRender=True)

sl._describeModel()

sl.drawNetwork()

sl.lockNode("X0")
sl.lockNode("A")    

sl.aliasNode("B")

sl.regenerateLayout()

sl.drawNetwork()    

print("node ids: ", sl.getNodeIds())
print()

#print("string: ", sl._SBMLlayout__getSBMLWithLayoutString())

sl.setNodeColor("B_1", "#00ff0030")

sl.lockNode("B_1")
sl.lockNode("D")
sl.unlockNode("X0")
sl.unlockNode("A")
sl.regenerateLayout()

sl.drawNetwork()

sl.setNodeEdgeColor("X1", "#00ff00")    
sl.setNodeFillColor("X1", "#ff0000")
sl.setNodeEdgeWidth("X1", 3)


sl.regenerateLayout()
                    
sl.drawNetwork("no_layout.png")
sl.drawNetwork("no_layout.pdf")

assert sl.getNodeEdgeColor("X1") == "#00ff00ff"    
assert sl.getNodeFillColor("X1") == "#ff0000ff"    
assert sl.getNodeEdgeWidth("X1") == 3

assert sl.getNodeEdgeColor("A") == "#0000ff"
assert sl.getNodeFillColor("A") == "#c9e0fb"

sl.writeSBMLFile("test_no_layout_alias.xml")


applyRender = True

sl2 = SBMLlayout("test_no_layout_alias.xml", applyRender=applyRender)

sl2._describeModel()

sl2.drawNetwork()

assert sl2.getNumberOfNodes() == 7
assert sl2.getNumberOfReactions() == 6

if applyRender:

    assert sl2.getNodeEdgeColor("X1") == "#00ff00ff"    
    assert sl2.getNodeFillColor("X1") == "#ff0000ff"    
    assert sl2.getNodeEdgeWidth("X1") == 3

else:

    assert sl2.getNodeEdgeColor("X1") == "#0000ff"    
    assert sl2.getNodeFillColor("X1") == "#c9e0fb"    
    assert sl2.getNodeEdgeWidth("X1") == 1
    
assert sl2.getNodeEdgeColor("A") == "#0000ff"
assert sl2.getNodeFillColor("A") == "#c9e0fb"

print("node ids: ", sl2.getNodeIds())




