from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "GlycolysisOriginal.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))

sl = SBMLlayout(str(model_file))

sl._describeModel()



sl.drawNetwork("GlycolysisOriginal.pdf")

sl.writeSBMLFile("glycolysis_original.xml")

slr = SBMLlayout("glycolysis_original.xml")

slr.drawNetwork()



