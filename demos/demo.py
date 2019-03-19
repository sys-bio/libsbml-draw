#from libsbml import readSBMLFromFile, read`SBMLFromString

#import libsbml_draw.c_api.sbnw_c_api as sbnw
from libsbml_draw.model.sbml_layout import SBMLlayout

#model_file = "C:\\tmp\\model.xml"
#model_file = "C:\\tmp\\copasi.xml"
#model_file = "C:\\tmp\\render_sbml.xml"
#model_file = "C:\\tmp\\largerpathway.xml"
model_file = "C:\\tmp\\simple-L2-render-global.xml"

# read model
sl = SBMLlayout(model_file)

# generate layout
if not sl.layoutSpecified:
    sl._randomizeLayout()
    sl._doLayoutAlgorithm()

# describe network
print("num nodes: ", sl.getNumberOfNodes())
print("num reactions: ", sl.getNumberOfReactions())

# create network
sl._createNetwork()

# draw network
sl.drawNetwork()

# print node id's
print("node ids: ", sl.getNodeIds())

if "copasi" in model_file:
    # set node properties
    sl.setNodeColor("S1", "pink")
    sl.setNodeColor("S2", "green")
    sl.setNodeColor("S1", "Verdana")
    sl.setNodeColor("S1", "white")
    sl.setNodeFontsize("S1", 18)
    sl.setNodeFontstyle("S1", "italic")

    sl.setNodeFontsize("S2", 24)
    sl.setNodeFontstyle("S2", "oblique")
    sl.setNodeFontcolor("S2", "yellow")

# print reaction id's
print("reaction ids: ", sl.getReactionIds())

#sl.setReactionColor("_J0", "orange")
#sl.setReactionCurveWidth("_J0", 5)

# set reaction properties
sl.drawNetwork()

# update sl
#sl.change_node_color(node_id, color)

# draw network
#sl.drawNetwork()
render_sbml_file_name = "C:\\tmp\\render_sbml.xml"
sl.writeSBMLFile(render_sbml_file_name)

print("apply render info")
sl._applyRenderInformation()

sl.drawNetwork("C:\\tmp\\save_network.pdf")


