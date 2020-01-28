from pathlib import Path
import pkg_resources


from libsbml_draw.model.sbml_layout import SBMLlayout


model_file_name = "simple-L2-render-local-L3V1-fixed.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/data/" + model_file_name))


sl = SBMLlayout(str(model_file))

sl.describeModel()

sl.drawNetwork()


sl.writeSBMLFile("fixed.xml")



