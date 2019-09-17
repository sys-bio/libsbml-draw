from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "model.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))


sl = SBMLlayout(str(model_file))

fr_alg = sl.getLayoutAlgorithmOptions()


def test_fr_alg_options_defaults():

    assert fr_alg.k == 20
    assert fr_alg.gravity == 0
    assert fr_alg.baryx == 500
    assert fr_alg.baryy == 500
    assert fr_alg.autobary == 1
    assert fr_alg.padding == 20


sl2 = SBMLlayout(str(model_file))

sl2.setLayoutAlgorithm_k(15)
sl2.setLayoutAlgorithm_gravity(20)
sl2.setLayoutAlgorithm_baryx(100)
sl2.setLayoutAlgorithm_baryy(250) 
sl2.setLayoutAlgorithm_padding(40)

fr_alg_2 = sl2.getLayoutAlgorithmOptions()


def test_fr_alg_options_set_k():
    assert fr_alg_2.k == 15


def test_fr_alg_options_set_gravity():
    assert fr_alg_2.gravity == 20


def test_fr_alg_options_set_bary():
    assert fr_alg_2.baryx == 100
    assert fr_alg_2.baryy == 250


def test_fr_alg_options_set_padding():
    assert fr_alg_2.padding == 40
