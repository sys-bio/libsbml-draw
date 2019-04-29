# -*- coding: utf-8 -*-
from pathlib import Path
import pkg_resources

import libsbml

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "simple-L2-render-global.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/data/" + model_file_name))

sl = SBMLlayout(str(model_file))

#sl._describeModel()

#sl.drawNetwork()

model_file_name = "simple-L2-render-local.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/data/" + model_file_name))

sll = SBMLlayout(str(model_file))

#sll._describeModel()

#sll.drawNetwork()


# check libsbml API

doc = libsbml.readSBMLFromFile(str(model_file))

model = doc.getModel()

numCompartments = model.getNumCompartments()

print("numCompartments: ", numCompartments)

for index in range(numCompartments):
    compartment = model.getCompartment(index)
    print("id, name: ", compartment.getId(), ", ", compartment.getElementName())



