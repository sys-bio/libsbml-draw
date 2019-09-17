from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "BorisEJB.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))

sl = SBMLlayout(str(model_file), autoComputeLayout=False)


def test_boris_model_default_layout():
    assert sl.getNumberOfNodes() == 8
    assert sl.getNumberOfReactions() == 10


model_file_name = "test_layout_override.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))

slr = SBMLlayout(str(model_file), autoComputeLayout=False)


def test_boris_model_back_in():
    assert slr.getNumberOfNodes() == 8
    assert slr.getNumberOfReactions() == 10
