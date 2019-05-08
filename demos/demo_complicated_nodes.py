"""Test File: complicated_nodes.xml is causing problems during testing
"""
from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

#model_file_name = "complicated_nodes-L3V1.xml"
model_file_name = "complicated_nodes.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))


print("validate: ", SBMLlayout._validate_sbml_filename(str(model_file)))


sl = SBMLlayout(str(model_file))


sl._describeModel()

sl.drawNetwork(figure_size=(15,15))

#sl.setNodeFontSize("all", 6)

#sl.drawNetwork()


#for node in sl.getNodeIds():
#    centroid = sl.getNodeCentroid(node)
#    print("centroid: ", centroid[0], ", ", centroid[1])
#    print("width: ", sl.getNodeWidth(node))
#    print("height: ", sl.getNodeHeight(node))
    
#for node in sl._SBMLlayout__network.nodes.values():
#    print("edge_color: ", node.edge_color)    
#    print("fill_color: ", node.fill_color) 
    

#ss = sl.getSBMLString()

#sls = sl._SBMLlayout__getSBMLWithLayoutString()

#print("sls: \n", sls)

#out_file = "complicated_nodes_out.xml"    
    
#sl.writeSBMLFile("complicated_nodes_out.xml")


#sl2 = SBMLlayout(out_file)

#sl2._describeModel()

#sl2.drawNetwork()

#for node in sl2.getNodeIds():
#    centroid = sl2.getNodeCentroid(node)
#    print("centroid: ", centroid[0], ", ", centroid[1])
#    print("width: ", sl2.getNodeWidth(node))
#    print("height: ", sl2.getNodeHeight(node))
    
    
#for node in sl._SBMLlayout__network.nodes.values():
#    print("edge_color: ", node.edge_color)    
#    print("fill_color: ", node.fill_color)     