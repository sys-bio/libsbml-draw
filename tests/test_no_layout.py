from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "model.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/data/" + model_file_name))

sl = SBMLlayout(str(model_file), applyRender=True)

sl._describeModel()

sl.drawNetwork()

assert sl.getNumberOfNodes() == 6
assert sl.getNumberOfReactions() == 6

sl.writeSBMLFile("test_no_layout.xml")

#slr = SBMLlayout("test_no_layout.xml", applyRender=True)
#slr._describeModel()
#slr.drawNetwork()
    

import libsbml

print("OP SUCCESS: ", libsbml.LIBSBML_OPERATION_SUCCESS)
print("OP FAIL: ", libsbml.LIBSBML_OPERATION_FAILED)
print("INVALID OBJ: ", libsbml.LIBSBML_INVALID_OBJECT)
print("LEVEL MISMATCH: ", libsbml.LIBSBML_LEVEL_MISMATCH)
print("LIBSBML_VERSION_MISMATCH: ", libsbml.LIBSBML_VERSION_MISMATCH) 
print("PKG VERSION MISMATCH: ", libsbml.LIBSBML_PKG_VERSION_MISMATCH)
print("dup obj id: ", libsbml.LIBSBML_DUPLICATE_OBJECT_ID)





