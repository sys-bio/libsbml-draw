from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "model.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/data/" + model_file_name))

applyRender = True

sl = SBMLlayout(str(model_file), applyRender=applyRender)

sl.lockNode("X0")
sl.lockNode("A")    

sl.aliasNode("B")

sl.setNodeColor("B_1", "#00ff0030")
sl.setNodeColor("A", "#00ff0030")
                
sl.lockNode("B_1")
sl.lockNode("D")
sl.unlockNode("X0")
sl.unlockNode("A")


def test_node_locking():
    assert sl.getIsNodeLocked("D") == True
    assert sl.getIsNodeLocked("X0") == False
    assert sl.getIsNodeLocked("A") == False
    assert sl.getIsNodeLocked("C") == False


def test_node_aliasing():
    assert sl.getIsNodeAliased("B_1") == True
    assert sl.getIsNodeAliased("X1") == False    

model_file_name = "test_no_layout_alias.xml" 

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))

sl2 = SBMLlayout(str(model_file), applyRender=applyRender)


def test_alias_back_in():
    assert sl2.getNumberOfNodes() == 7
    assert sl2.getNumberOfReactions() == 6

