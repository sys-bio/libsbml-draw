"""Test File: complicated_nodes.xml is causing problems during testing
"""
from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

#model_file_name = "complicated_nodes-L3V1.xml"
model_file_name = "complicated_nodes.xml"

model_file = Path(pkg_resources.resource_filename(
        "libsbml_draw", "model/data/" + model_file_name))

# https://stackoverflow.com/questions/33635439/matplotlib-patch-size-in-points

print("validate: ", SBMLlayout._validate_sbml_filename(str(model_file)))


sl = SBMLlayout(str(model_file))


sl._describeModel()

sl.drawNetwork(figure_size=(13,13))

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

out_file = "complicated_nodes_out.xml"    
    
sl.writeSBMLFile("complicated_nodes_out.xml")


#sl2 = SBMLlayout(out_file, fitToWindow=(0.,0.,500.,500.))
sl2 = SBMLlayout(out_file)

sl2._describeModel()

#sl2.drawNetwork(figure_size=(15,15))
sl2.drawNetwork(show=True)

#x = list()
#y = list()

#for node in sl2.getNodeIds():
#    centroid = sl2.getNodeCentroid(node)
#    x.append(centroid[0])
#    y.append(centroid[1])    
#    print("centroid: ", centroid[0], ", ", centroid[1])
#    print("width: ", sl2.getNodeWidth(node))
#    print("height: ", sl2.getNodeHeight(node))

#print()    
#print("min x, max x: ", min(x)-20, ", ", max(x)+20)
#print("min y, max y: ", min(y)-10, ", ", max(y)+10)
#print()
#print("width: ", max(x) - min(x))
#print("height: ", max(y) - min(y))

#    centroid = sl2.getNodeCentroid(node)
#    print("centroid: ", centroid[0], ", ", centroid[1])
#    print("width: ", sl2.getNodeWidth(node))
#    print("height: ", sl2.getNodeHeight(node))
    
    
#for node in sl._SBMLlayout__network.nodes.values():
#    print("edge_color: ", node.edge_color)    
#    print("fill_color: ", node.fill_color)     