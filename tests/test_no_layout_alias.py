from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "model.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/data/" + model_file_name))

applyRender = True

sl = SBMLlayout(str(model_file), applyRender=applyRender)

sl._describeModel()

sl.drawNetwork()

sl.lockNode("X0")
sl.lockNode("A")    

sl.aliasNode("B")

sl.regenerateLayout()

sl.drawNetwork("model_simple_alias_B_lock_A_X0.pdf")    

print("node ids: ", sl.getNodeIds())
print()

#print("string: ", sl._SBMLlayout__getSBMLWithLayoutString())

sl.setNodeColor("B_1", "#00ff0030")
sl.setNodeColor("A", "#00ff0030")
                
sl.lockNode("B_1")
sl.lockNode("D")
sl.unlockNode("X0")
sl.unlockNode("A")
sl.regenerateLayout()

sl.drawNetwork()

sl.regenerateLayout()

sl.writeSBMLFile("test_no_layout_alias.xml")

sl2 = SBMLlayout("test_no_layout_alias.xml", applyRender=applyRender)

sl2._describeModel()

sl2.drawNetwork()

assert sl2.getNumberOfNodes() == 7
assert sl2.getNumberOfReactions() == 6



print("node ids: ", sl2.getNodeIds())




