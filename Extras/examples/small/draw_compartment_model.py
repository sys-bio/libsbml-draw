from libsbml_draw.model.sbml_layout import SBMLlayout

'''
critisism - What are the role names? What are their ids? 

When you set the node color after the node edge color, both
the properties get changed together. 

Change the seed on layout so dependent on time 
so you do not get deterministic layouts

regenerate layout causes network properties to revert 
back to default

setArrowheadScale funciton does not work, but changing the default
value does

Sometimes run into problems with a canvas which is too big (like in the schmerier 2008 model)

SBO term unexpected warning. Where does it come from 
'''

layout = SBMLlayout('2CompartmentModel.xml')
# print(layout.getNumberOfRoles())

layout.regenerateLayout()
layout.regenerateLayout()
layout.regenerateLayout()
layout.regenerateLayout()
layout.regenerateLayout()
layout.regenerateLayout()
layout.regenerateLayout()
layout.regenerateLayout()
layout.regenerateLayout()
layout.regenerateLayout()
[layout.setCompartmentEdgeColor(i, 'grey') for i in layout.getCompartmentIds()]
[layout.setCompartmentLineWidth(i, 10) for i in layout.getCompartmentIds()]
[layout.setNodeEdgeWidth(i, 10) for i in layout.getNodeIds()]
[layout.setNodeFontSize(i, 40) for i in layout.getNodeIds()]
[layout.setReactionEdgeColor(i, edge_color='black') for i in layout.getReactionIds()]
[layout.setReactionCurveWidth(i, 10) for i in layout.getReactionIds()]
[layout.setArrowheadScale(i, 50) for i in range(layout.getNumberOfRoles())]
[layout.setNodeColor(i, 'white') for i in layout.getNodeIds()]
[layout.setNodeEdgeColor(i, 'black') for i in layout.getNodeIds()]
layout.drawNetwork('compartment_network.png')

# layout.regenerateLayout()
# layout.regenerateLayout()
# layout.regenerateLayout()
# layout.regenerateLayout()
# layout.regenerateLayout()
# layout.drawNetwork('compartment_network.png')
#
# layout.writeSBMLFile('2CompartmentModelWithLayout.xml')
#
# from libsbml_draw.model.sbml_layout import SBMLlayout
#
# # Create a SBMLlayout object.
# layout = SBMLlayout('2CompartmentModel.xml')
#
# # Draw it and save to a png
# layout.drawNetwork('2CompartmentModelWithLayout.png')
#
# # save the SBML with render information
# layout.writeSBMLFile('2CompartmentModelWithLayout.xml')
#
# from libsbml_draw.model.sbml_layout import SBMLlayout
#
# # Create a SBMLlayout object.
# layout = SBMLlayout('Kholodenko2000.xml')
#
# # Draw it and save to a png
# layout.drawNetwork('Kholodenko2000WithLayout.png')
#
# # save the SBML with render information
# layout.writeSBMLFile('Kholodenko2000WithLayout.xml')
#
