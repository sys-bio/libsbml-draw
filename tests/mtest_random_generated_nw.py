import site
site.addsitedir('../src/python')

from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "random_network.xml"

#model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/data/" + model_file_name))


sl = SBMLlayout(model_file_name, applyRender=False)

sl._describeModel()

sl.drawNetwork("random_4s_2r.pdf")


