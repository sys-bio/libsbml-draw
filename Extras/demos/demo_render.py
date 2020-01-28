#import libsbml

from libsbml_draw.model.sbml_layout import SBMLlayout
#from libsbml_draw.model.render import Render


#model_file = "C:\\tmp\\copasi.xml"
model_file = "C:\\tmp\\largerpathway.xml"

#doc = libsbml.readSBMLFromFile(model_file)
#model = doc.getModel()
#layout_plugin = model.getPlugin("layout")

#if layout_plugin:
#    print("num layouts: ", layout_plugin.getNumLayouts())


sl = SBMLlayout(model_file)

sl.describeModel()

sl.drawNetwork()
#r = Render(model_file, sl.layout_number)
#r._describeRenderInfo()

#print("render: ", type(r))
#print("num layouts: ", r.layout_plugin.getNumLayouts())

#sl._applyRenderInformation(None)

#a0e0a030

reactionIds = sl.getReactionIds()

sl.setNodeColor("all", "#0000ff30")
sl.setReactionColor("all", "blue")

sl.setNodeEdgeColor("F", "blue")
sl.setNodeFillColor("F", "lightgreen")
sl.setNodeFontFamily("ABCDEFG", "Elephant")
sl.setNodeFontColor("ABCDEFG", "green")
sl.setNodeEdgeColor("ABCDEFG", "blue")

for reactionId in reactionIds: 
    sl.setReactionCurveWidth(reactionId, 1)
    sl.setReactionFillColor(reactionId, "red")


sl.drawNetwork(save_file_name="C:\\tmp\\larger_pathway_set_changes_tight.png", bbox_inches="tight")
