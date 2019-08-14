from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

MODEL_FILE_NAME = "largerpathway.xml"

MODEL_FILE = Path(pkg_resources.resource_filename(
        "libsbml_draw",
        "model/data/" + MODEL_FILE_NAME))


sl = SBMLlayout(str(MODEL_FILE))

sl._describeModel()


sl.drawNetwork("larger_pathway.png")


sl.writeSBMLFile("test_larger_pathway.xml")


slr =  SBMLlayout("test_larger_pathway.xml")

slr.drawNetwork()


