# from pathlib import Path
# import pkg_resources
import platform

from libsbml_draw.model.sbml_layout import SBMLlayout

if platform.system() == "Windows":
    model_dir = "C:\\Users\\nrhaw\\Documents\\repos\\libsbml-draw\\model_files\\"
    # model_file = "C:\\tmp\\copasi.xml"
    model_file = model_dir + "copasi.xml"
    #model_file = model_dir + "render_sbml_pink_green.xml"
elif platform.system() == "Linux":
    model_dir = "/home/radix/repos/libsbml-draw/model_files/"    
    model_file = "/home/radix/repos/libsbml-draw/model_files/copasi.xml"
else:
    model_dir = "/Users/natalieh/repos/libsbml-draw/model_files/"
    model_file = "/Users/natalieh/repos/libsbml-draw/model_files/copasi.xml"
#model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model_files/model.xml"))

print("model file: \n", model_file)

sl = SBMLlayout(model_file)

sl.describeModel()

## Draw Original copasi.xml
sl.drawNetwork()

print("node ids: ", sl.getNodeIds())
print("reaction ids: ", sl.getReactionIds())

sl.setNodeFontStyle("S1", "italic")
sl.setNodeColor("S1", "lightpink")
sl.setNodeColor("S2", "lightgreen")

sl.setNodeFontColor("S1", "white")
sl.setNodeFontStyle("S1", "italic")

sl.setReactionColor("_J0", "blue")
sl.setReactionCurveWidth("_J0", 1)

# Draw Pink and Green 
sl.drawNetwork()

new_model_file = model_dir + "render_sbml_pink_green.xml"
print("new model file: ", new_model_file)

sl.addRenderInformation()

sl.writeSBMLFile(new_model_file)

sl_apply = SBMLlayout(new_model_file)

# Read in and Draw Pink and Green
sl_apply.drawNetwork()

sl_apply.setNodeEdgeColor("S1", "black")
sl_apply.setNodeEdgeColor("S2", "black")

sl_apply.setReactionColor("_J0", "orange")

# Add edge color and change reaction color
sl_apply.drawNetwork()

local_model_file = model_dir + "render_had_local_already.xml"

sl_apply.addRenderInformation()

sl_apply.writeSBMLFile(local_model_file)

sl_local = SBMLlayout(local_model_file)

# Read in and Draw _Edge Color
sl_local.drawNetwork()

