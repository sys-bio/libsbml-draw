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
    s.node.edgewidth = 4
    s.font.size = 25
    s.font.color = 'green'
    s.node.color = 'red'
    s.edge.color = 'black'
    s.compartment.edgecolor = 'black'
    return s


model_id = 'BIOMD0000000112'

fname = model_id + '.xml'

# download the model
biomodels_download(model_id, fname)

# Use a preconfigured style directly out of the box
s = SBMLlayout(fname, style=my_style)

# draw the network
s.drawNetwork(model_id + ".png")

# write the newly generated layout and rendering information back to the
# sbml model
# s.writeSBML(fname)

















