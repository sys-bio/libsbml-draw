# -*- coding: utf-8 -*-
from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "simple-L2-render-global.xml"
#model_file_name = "simple-L2-render-global-L3V1.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/data/" + model_file_name))
#model_file = Path(model_file_name)

sl = SBMLlayout(str(model_file))

sl.describeModel()

sl.drawNetwork()

for node in sl._SBMLlayout__network.nodes.values():
    print("node: ", node.font_size)

