from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout


model_file_name = "simple-L2-render-local.xml"
#model_file_name = "simple-L2-render-local-L3V1.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))

sl = SBMLlayout(str(model_file))

sl.setCompartmentEdgeColor("vol1", "#0000ff")
sl.setCompartmentFillColor("vol1", "#ff000010")
sl.setCompartmentLineWidth("vol1", 5)


def test_render_local_set_commands():
    assert sl.getCompartmentEdgeColor("vol1") == "#0000ffff"
    assert sl.getCompartmentFillColor("vol1") == "#ff000010"
    assert sl.getCompartmentLineWidth("vol1") == 5


model_file_name = "simple-L2-render-global.xml"
#model_file_name = "simple-L2-render-global-L3V1.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))

slg = SBMLlayout(str(model_file))


def test_render_global_defaults():
    assert slg.getCompartmentEdgeColor("vol1") == "#ffa500"
    assert slg.getCompartmentFillColor("vol1") == "#ffeeee"
    assert slg.getCompartmentLineWidth("vol1") == 12

