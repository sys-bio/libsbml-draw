# -*- coding: utf-8 -*-
from pathlib import Path
import pkg_resources

import libsbml

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "simple-L2-render-global.xml"
#model_file_name = "simple-L2-render-global-L3V1.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/data/" + model_file_name))
#model_file = Path(model_file_name)

sl = SBMLlayout(str(model_file))

sl._describeModel()

sl.drawNetwork()

print("Node0 font size: ", sl.getNodeFontSize("Node0"))
print("reaction ids: ", sl.getReactionIds())
print("Reaction curve width, edge color, fill color: ", sl.getReactionCurveWidth("J0"), sl.getReactionEdgeColor("J0"), sl.getReactionFillColor("J0"))

print("compartment ids: ", sl.getCompartmentIds())

sl.setCompartmentLineWidth("vol1", 12)

sl.drawNetwork()

