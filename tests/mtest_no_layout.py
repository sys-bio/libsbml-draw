import site
site.addsitedir('../src/python')

from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "model.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))

applyRender = True

sl = SBMLlayout(str(model_file), applyRender=applyRender)

sl._describeModel()

sl.setReactionCurveWidth("all", 5)

assert sl.getReactionCurveWidth("_J0")[0] == ('X0', 'SUBSTRATE', 5)
assert sl.getReactionCurveWidth("_J0")[1] == ('A', 'PRODUCT', 5)

assert sl.getReactionCurveWidth("_J1")[0] == ("A", "SUBSTRATE", 5)
assert sl.getReactionCurveWidth("_J1")[1] == ("B", "PRODUCT", 5)

assert sl.getReactionCurveWidth("_J2")[0] == ('B', 'SUBSTRATE', 5)
assert sl.getReactionCurveWidth("_J2")[1] == ('D', 'PRODUCT', 5)
                              
assert sl.getReactionCurveWidth("_J5")[0] == ('D', 'SUBSTRATE', 5)
assert sl.getReactionCurveWidth("_J5")[1] == ('X1', 'PRODUCT', 5)

assert sl.getReactionCurveWidth("_J3")[0] == ('A', 'SUBSTRATE', 5)
assert sl.getReactionCurveWidth("_J3")[1] == ('C', 'PRODUCT', 5)

assert sl.getReactionCurveWidth("_J4")[0] == ('C', 'SUBSTRATE', 5)
assert sl.getReactionCurveWidth("_J4")[1] == ('D', 'PRODUCT', 5)

sl.drawNetwork(scaling_factor=0.75)

assert sl.getNumberOfNodes() == 6
assert sl.getNumberOfReactions() == 6

sl.setNodeEdgeColor("X1", "#ff0000")    
sl.setNodeFillColor("X1", "#ff000030")
sl.setNodeEdgeWidth("X1", 3)

assert sl.getNodeEdgeColor("X1") == "#ff0000ff"    
assert sl.getNodeFillColor("X1") == "#ff000030"    
assert sl.getNodeEdgeWidth("X1") == 3

assert sl.getNodeEdgeColor("A") == "#0000ff"
assert sl.getNodeFillColor("A") == "#c9e0fb"

sl.setNodeFontWeight(["A", "B", "C", "D"], "bold")

assert sl.getNodeFontWeight("B") == "bold"

sl.setReactionEdgeColor("_J0", "#ff0000", role_name="product")
sl.setReactionEdgeColor("_J1", "#ff00ff", role_name="substrate")
sl.setReactionEdgeColor("_J2", "#ff00ff", role_name="product")
sl.setReactionEdgeColor("_J5", "#00ff00", species="D")
sl.setReactionEdgeColor("_J3", "#ffff00", role_name="product")
sl.setReactionEdgeColor("_J4", "#00ffff")
                        
assert sl.getReactionEdgeColor("_J0")[0] == ('X0', 'SUBSTRATE', '#0000ff') 
assert sl.getReactionEdgeColor("_J0")[1] == ('A', 'PRODUCT', '#ff0000ff') 
                              
assert sl.getReactionEdgeColor("_J1")[0] == ("A", "SUBSTRATE", "#ff00ffff")
assert sl.getReactionEdgeColor("_J1")[1] == ("B", "PRODUCT", "#0000ff")

assert sl.getReactionEdgeColor("_J2")[0] == ('B', 'SUBSTRATE', '#0000ff')
assert sl.getReactionEdgeColor("_J2")[1] == ('D', 'PRODUCT', '#ff00ffff')
                              
assert sl.getReactionEdgeColor("_J5")[0] == ('D', 'SUBSTRATE', '#00ff00ff')
assert sl.getReactionEdgeColor("_J5")[1] == ('X1', 'PRODUCT', '#0000ff')

assert sl.getReactionEdgeColor("_J3")[0] == ('A', 'SUBSTRATE', '#0000ff')
assert sl.getReactionEdgeColor("_J3")[1] == ('C', 'PRODUCT', '#ffff00ff')

assert sl.getReactionEdgeColor("_J4")[0] == ('C', 'SUBSTRATE', '#00ffffff')
assert sl.getReactionEdgeColor("_J4")[1] == ('D', 'PRODUCT', '#00ffffff')
                        
sl.setReactionCurveWidth("_J0", 7, role_name="product")

assert sl.getReactionCurveWidth("_J0")[0] == ('X0', 'SUBSTRATE', 5)
assert sl.getReactionCurveWidth("_J0")[1] == ('A', 'PRODUCT', 7)
                              
sl.drawNetwork("model_simple_curve_colors.pdf")

sl.writeSBMLFile("ftest_no_layout.xml")

slr = SBMLlayout("ftest_no_layout.xml", applyRender=applyRender)

slr._describeModel()

slr.drawNetwork("model_simple_curve_colors_with_les.png")
    
if applyRender:

    assert slr.getNodeEdgeColor("X1") == "#ff0000ff"    
    assert slr.getNodeFillColor("X1") == "#ff000030"    
    assert slr.getNodeEdgeWidth("X1") == 3

else:

    assert slr.getNodeEdgeColor("X1") == "#0000ff"    
    assert slr.getNodeFillColor("X1") == "#c9e0fb"    
    assert slr.getNodeEdgeWidth("X1") == 1

assert slr.getNodeEdgeColor("A") == "#0000ff"
assert slr.getNodeFillColor("A") == "#c9e0fb"

slr.writeSBMLFile("ftest_no_layout_read_back_in.xml")
