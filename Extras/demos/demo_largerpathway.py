from pathlib import Path
import pkg_resources

from libsbml_draw.sbml_layout import SBMLlayout

MODEL_FILE_NAME = "largerpathway.xml"

MODEL_FILE = Path(pkg_resources.resource_filename(
        "libsbml_draw",
        "model/libs/" + MODEL_FILE_NAME))

print("model file: ", str(MODEL_FILE))

sl = SBMLlayout(str(MODEL_FILE))


#sl.describeModel()

sl.setReactionColor("all", "#0000ff50")  
sl.setNodeColor("all", "#00ff0030")
                    
#sl.setNodeFontSize("all", 24)

sl.drawNetwork("largerpathway.png")

#sl.drawNetwork(figsize=(12,12))


print("node ids: ", sl.getNodeIds())
print("reaction ids: ", sl.getReactionIds())
print()

for node in sl._SBMLlayout__network.nodes.values():
    print("node fs: ", node.font_size, node.font_family)
      
    
sl.writeSBMLFile("largerpathway_out.xml")
    
#sl.drawNetwork(scaling_factor=.5)
    