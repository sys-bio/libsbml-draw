import os, site
site.addsitedir(os.path.dirname(__file__))
from tests.add_to_path import add_to_path
add_to_path()

import os
from libsbml_draw import SBMLlayout
from libsbml_draw.styles import Style, black_and_white
from libsbml_draw.utils import biomodels_download

def my_style():
    s = Style()
    s.edge.color = 'black'
    s.font.color = 'green'
    s.node.edgewidth = 15
    s.font.size = 30
    s.node.fillcolor = 'black'
    s.compartment.edgecolor = 'black'
    s.background.color = 'red'
    return s


model_id = 'BIOMD0000000112'

fname = model_id + '.xml'

# download the model
biomodels_download(model_id, fname)

# Use a preconfigured style directly out of the box
s = SBMLlayout(fname, style=my_style())
# s = SBMLlayout(fname, style=None)
# s.setNodeFontSize('all', 30)

# draw the network
# s.setNodeFontSize('receptor', 15)
s.drawNetwork(model_id + ".png")

# write the newly generated layout and rendering information back to the
# sbml model
# s.writeSBML(fname)




# s.setNodeColor('all', 'black')
# s.setNodeEdgeWidth('all', 10)
# s.setNodeFontColor('all', 'green')
# s.setNodeFontSize('all', 30)
# s.setReactionEdgeColor('all', 'orange')
# s.setCompartmentEdgeColor('cytoplasm', 'green')














