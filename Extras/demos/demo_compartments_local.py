from pathlib import Path
import pkg_resources

import libsbml

from libsbml_draw.sbml_layout import SBMLlayout


model_file_name = "simple-L2-render-local.xml"
#model_file_name = "simple-L2-render-local-L3V1.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/libs/" + model_file_name))

sll = SBMLlayout(str(model_file))

sll.describeModel()

sll.drawNetwork()

sll.setCompartmentEdgeColor("vol1", "#0000ff")
sll.setCompartmentFillColor("vol1", "#ff000010")
sll.setCompartmentLineWidth("vol1", 5)

for node in sll._SBMLlayout__network.nodes.values():
    print("_Node shape points: ", node.shape, len(node.polygon_points), len(node.polygon_codes))
    for point in node.polygon_points:
        print("point: ", point)
    for code in node.polygon_codes:
        print("code: ", code)

sll.drawNetwork()

sll.writeSBMLFile("simple_local_out.xml")

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
        