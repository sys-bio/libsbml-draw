import site
site.addsitedir('../src/python')

from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "modexmpl.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))

sl = SBMLlayout(str(model_file))

sl._describeModel()

sl.drawNetwork("ftest_line_endings.pdf")

