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

    # edge attributes
    s.edge.edgecolor = 'black'
    s.edge.fillcolor = 'black'
    s.edge.width = 15

    # font attributes
    s.font.color = 'black'
    s.font.size = 35
    s.font.weight = 'bold'

    # node attributes
    s.node.fillcolor = '#1fd6ff'
    s.node.edgewidth = 15

    # compartment attributes
    s.compartment.edgecolor = 'black'
    s.compartment.linewidth = 20

    # background attributes
    s.background.color = '#def9ff'

    # arrow attributes
    s.arrow.scale = 100

    return s


model_id = 'BIOMD0000000001'

fname = model_id + '.xml'

# download the model
biomodels_download(model_id, fname)

# Use a preconfigured style directly out of the box
s = SBMLlayout(fname, style=None, applyRender=False)

s.drawNetwork(model_id + ".png")


# x = s.getBoundarySpeciesIds()
# print(x)
# '''
# <species boundaryCondition="true" compartment="cell" hasOnlySubstanceUnits="true" id="R5P"
#     initialAmount="18" metaid="metaid_0000020" name="ribose-5-phosphate">
# '''
# expected = ['ribose-5-phosphate']
#
# # # draw the network
# s.drawNetwork(model_id + ".png")
#
# # write the newly generated layout and rendering information back to the
# # sbml model
# s.writeSBMLFile(fname)
























