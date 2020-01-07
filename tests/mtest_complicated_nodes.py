import site
site.addsitedir('../src/python')

from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

#model_file_name = "complicated_nodes-L3V1.xml"
model_file_name = "complicated_nodes.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))

sl = SBMLlayout(str(model_file))


sl._describeModel()


sl.drawNetwork("complicated_nodes.png")