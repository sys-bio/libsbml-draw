import sys
import os.path
from libsbml import readSBMLFromFile

inputFile = "C:\\tmp\\copasi.xml"
doc = readSBMLFromFile(inputFile)
model = doc.getModel(); 

layout_plugin = model.getPlugin("layout")
lol_plugin = layout_plugin.getListOfLayouts().getPlugin("render")

info_global = lol_plugin.getRenderInformation(0)

layout = layout_plugin.getLayout(0)
rPlugin = layout.getPlugin("render")   

rInfo = rPlugin.createLocalRenderInformation()



print("layout plugin type: ", type(layout_plugin))
print("lol_plugin type: ", type(lol_plugin))
print("layout type: ", type(layout))
print("rPlugin type: ", type(rPlugin))
print("rInfo type: ", type(rInfo))



