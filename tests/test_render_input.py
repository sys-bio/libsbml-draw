from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout


model_file_name = "simple-L2-render-local.xml"
#model_file_name = "simple-L2-render-local-L3V1.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))

sl = SBMLlayout(str(model_file))

sl._describeModel()

sl.setCompartmentEdgeColor("vol1", "#0000ff")
sl.setCompartmentFillColor("vol1", "#ff000010")
sl.setCompartmentLineWidth("vol1", 5)

sl.drawNetwork("simple_render_local.pdf")


model_file_name = "simple-L2-render-global.xml"
#model_file_name = "simple-L2-render-global-L3V1.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))


sl = SBMLlayout(str(model_file))

sl._describeModel()

sl.drawNetwork("simple_render_global.pdf")


