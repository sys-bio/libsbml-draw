from libsbml import readSBMLFromFile, readSBMLFromString

import libsbml_draw.c_api.sbnw_c_api as sbnw
from libsbml_draw.model.sbml_layout import SBMLlayout

model_file = "C:\\tmp\\model.xml"

layout_alg_options = sbnw.fr_alg_options(
            20.0,        # k
            1,           # boundary
            0,           # mag
            0,           # grav
            500.0,       # baryx
            0.0,         # baryy
            1,           # autobary
            0,           # enable_comps
            0,           # prerandom
            0.0          # padding
            )    

# read model
sl = SBMLlayout(model_file, layout_alg_options)

# generate layout
sl.randomizeLayout()
sl.doLayoutAlgorithm()

# describe network
print("num nodes: ", sl.getNumberOfNodes())
print("num reactions: ", sl.getNumberOfReactions())

# create network
sl.createNetwork()

# draw network
sl.drawNetwork()

# set node properties


# set reaction properties


# update sl
#sl.change_node_color(node_id, color)

# draw network
#sl.drawNetwork()
