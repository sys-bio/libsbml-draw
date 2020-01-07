import site
site.addsitedir('../src/python')

from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "model.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))


sl = SBMLlayout(str(model_file))

sl.drawNetwork()

sl.showLayoutAlgorithmOptions()

fr_alg = sl.getLayoutAlgorithmOptions()

assert fr_alg.k == 20
assert fr_alg.gravity == 0
assert fr_alg.baryx == 500
assert fr_alg.baryy == 500
assert fr_alg.autobary == 1
assert fr_alg.padding == 20

sl.setLayoutAlgorithm_k(15)

fr_alg = sl.getLayoutAlgorithmOptions()

assert fr_alg.k == 15

sl.regenerateLayout()

sl.drawNetwork()

sl.setLayoutAlgorithm_k(30)

fr_alg = sl.getLayoutAlgorithmOptions()

assert fr_alg.k == 30

sl.regenerateLayout()

sl.drawNetwork()

 
sl.setLayoutAlgorithm_k(20)
sl.setLayoutAlgorithm_gravity(20)

assert fr_alg.k == 20
assert fr_alg.gravity == 20


sl.regenerateLayout()

sl.drawNetwork()


sl.setLayoutAlgorithm_gravity(50)

sl.regenerateLayout()

sl.drawNetwork()


sl.setLayoutAlgorithm_autobary(0)
sl.regenerateLayout()
sl.drawNetwork()


sl.setLayoutAlgorithm_baryx(100)
sl.setLayoutAlgorithm_baryy(250)
 
sl.regenerateLayout()
sl.drawNetwork() 
 
sl.setLayoutAlgorithm_padding(40)

assert fr_alg.padding == 40





