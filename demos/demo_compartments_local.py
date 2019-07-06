from pathlib import Path
import pkg_resources

import libsbml

from libsbml_draw.model.sbml_layout import SBMLlayout


model_file_name = "simple-L2-render-local.xml"
#model_file_name = "simple-L2-render-local-L3V1.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/data/" + model_file_name))

sll = SBMLlayout(str(model_file))

sll._describeModel()

sll.drawNetwork()

sll.setCompartmentEdgeColor("vol1", "blue")
sll.setCompartmentFillColor("vol1", "lightpink")
sll.setCompartmentLineWidth("vol1", 5)

sll.drawNetwork()

print(sll.getCompartmentEdgeColor("vol1"))
print(sll.getCompartmentFillColor("vol1"))
print(sll.getCompartmentLineWidth("vol1"))

# check libsbml API

doc = libsbml.readSBMLFromFile(str(model_file))

model = doc.getModel()

numCompartments = model.getNumCompartments()

print("numCompartments: ", numCompartments)

for index in range(numCompartments):
    compartment = model.getCompartment(index)
    print("id, name: ", compartment.getId(), ", ", compartment.getElementName())


for reaction in sll._SBMLlayout__network.reactions.values():
    for curve in reaction.curves:
        print("curve role: ", curve.role, curve.role_name, curve.role_name.lower()=="substrate")
        
for node in sll._SBMLlayout__network.nodes.values():
    print("node, font_size: ", node.font_size)        
        