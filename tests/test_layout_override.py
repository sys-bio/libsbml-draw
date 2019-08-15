from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "BorisEJB.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))

sl = SBMLlayout(str(model_file), autoComputeLayout=True)

sl._describeModel()

sl.drawNetwork("boris_ejb_override.pdf")

sl.writeSBMLFile("test_layout_override.xml")

slr = SBMLlayout("test_layout_override.xml", autoComputeLayout=False)

slr.drawNetwork()

