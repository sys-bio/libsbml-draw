from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "GlycolysisOriginal.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))

sl = SBMLlayout(str(model_file))

sl._describeModel()

assert sl.getNumberOfNodes() == 23
assert sl.getNumberOfReactions() == 11

sl.drawNetwork("GlycolysisOriginal.pdf")


assert sl.getNodeEdgeWidth("External_glucose") == 3
assert sl.getNodeEdgeWidth("Glucose") == 1
# in this case, bottom means top
assert sl.getNodeVTextAnchor("pyruvate") == "bottom"
assert sl.getNodeVTextAnchor("ADP") == "bottom"

assert sl.getNodeFillColor("NAD") == "#7fff55"
assert sl.getNodeFillColor("NADH") == "#d4ffaa"

assert sl.getNodeFillColor("ATP") == "#ff7faa"
assert sl.getNodeFillColor("ADP") == "#ffd4d4"

assert sl.getNodeEdgeColor("glycerate_3_phosphate") == "#969696"

sl.writeSBMLFile("glycolysis_original.xml")

slr = SBMLlayout("glycolysis_original.xml")

slr.drawNetwork()

assert slr.getNumberOfNodes() == 23
assert slr.getNumberOfReactions() == 11

assert slr.getReactionCurveWidth("J9") == [('ATP', 'SUBSTRATE', 2.0), 
                                           ('ADP', 'PRODUCT', 2.0)]

assert slr.getReactionEdgeColor("J10") == [('External_acetaldehyde', 
                                            'SUBSTRATE', '#ff9900'), 
                                           ('Sink', 'PRODUCT', '#ff9900')]

assert slr.getReactionFillColor("J0") == [('External_glucose', 
                                           'SUBSTRATE', '#ff9900'), 
                                          ('Glucose', 'PRODUCT', '#ff9900')]

