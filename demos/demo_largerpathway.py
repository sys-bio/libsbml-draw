from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

MODEL_FILE_NAME = "largerpathway.xml"

MODEL_FILE = Path(pkg_resources.resource_filename(
        "libsbml_draw",
        "model/data/" + MODEL_FILE_NAME))

print("model file: ", str(MODEL_FILE))

sl = SBMLlayout(str(MODEL_FILE))


#sl.describeModel()


sl.setNodeFontSize("all", 24)


sl.drawNetwork(figsize=(12,12))


print("node ids: ", sl.getNodeIds())
print("reaction ids: ", sl.getReactionIds())

