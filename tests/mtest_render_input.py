import site
site.addsitedir('../src/python')

from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout


model_file_name = "simple-L2-render-local.xml"
#model_file_name = "simple-L2-render-local-L3V1.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))

sl = SBMLlayout(str(model_file))

sl._describeModel()

sl.drawNetwork()

sl.setCompartmentEdgeColor("vol1", "#0000ff")
sl.setCompartmentFillColor("vol1", "#ff000010")
sl.setCompartmentLineWidth("vol1", 5)

assert sl.getCompartmentEdgeColor("vol1") == "#0000ffff"
assert sl.getCompartmentFillColor("vol1") == "#ff000010"
assert sl.getCompartmentLineWidth("vol1") == 5

sl.drawNetwork("simple_render_local.png")

sl.writeSBMLFile("simple_render_local_out.xml")

slr = SBMLlayout("simple_render_local_out.xml")

slr.drawNetwork()


model_file_name = "simple-L2-render-global.xml"
#model_file_name = "simple-L2-render-global-L3V1.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))

sl = SBMLlayout(str(model_file))

sl._describeModel()

assert sl.getCompartmentEdgeColor("vol1") == "#ffa500"
assert sl.getCompartmentFillColor("vol1") == "#ffeeee"
assert sl.getCompartmentLineWidth("vol1") == 12

sl.drawNetwork("simple_render_global.png")

sl.writeSBMLFile("simple_render_global_out.xml")

slr = SBMLlayout("simple_render_global_out.xml")

slr.drawNetwork()


