import platform

from libsbml_draw.model.sbml_layout import SBMLlayout

file_name = "veronica-network.xml"

if platform.system() == "Windows":
    model_dir = "C:\\Users\\nrhaw\\Documents\\repos\\libsbml-draw\\model_files\\"
elif platform.system() == "Linux":    
    model_dir = "/home/radix/repos/libsbml-draw/model_files/"
else:
    model_dir = "/Users/natalieh/repos/libsbml-draw/model_files/"
    
model_file = model_dir + file_name

print("model file: \n", model_file)



sl = SBMLlayout(model_file)

sl._describeModel()

my_fig = sl.drawNetwork()

color1 = ["S6", "S7", "S5", "S4", "S8"]
color2 = ["S0", "S1", "S2", "S3", "S9", "S10", "S11"]

for node in color1:
    sl.setNodeFillColor(node, "lightblue")
    
for node in color2: 
    sl.setNodeFillColor(node, "lightgreen")

for reaction in sl.getReactionIds():
    sl.setReactionCurveWidth(reaction, 2)    

sl.drawNetwork()

    
    

