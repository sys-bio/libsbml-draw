# Extract the render information
import sys
import os.path
from libsbml import readSBMLFromFile

inputFile = "C:\\tmp\\copasi.xml"

doc = readSBMLFromFile(inputFile)

model = doc.getModel(); 

layout_plugin = model.getPlugin("layout")

print("num layouts: ", layout_plugin.getNumLayouts())

render_plugin = layout_plugin.getListOfLayouts().getPlugin("render")

print("num global info: ", render_plugin.getNumGlobalRenderInformationObjects()) 

info_global = render_plugin.getRenderInformation(0)

print("id: ", info_global.getId())
print("name: ", info_global.getName())
print("program name: ", info_global.getProgramName())
print("program version: ", info_global.getProgramVersion())
print("bg color: ", info_global.getBackgroundColor())

print("color definitions: ", info_global.getNumColorDefinitions())

for j in range(info_global.getNumColorDefinitions()):
    
    color = info_global.getColorDefinition(j)

    print("\tcolor: ", color.getId(), ", ", color.createValueString())

print("gradient definitions: ", info_global.getNumGradientDefinitions())

for j in range(info_global.getNumGradientDefinitions()):
    
    grad = info_global.getGradientDefinition(j)
    
    print("\tgradient: ", grad.getId(), ", ", grad.getElementName())

print("line endings: ", info_global.getNumLineEndings())

line_ending = info_global.getLineEnding(0)
print("line_ending dir:")
print(dir(line_ending))

for j in range(info_global.getNumLineEndings()):
    
    line_ending = info_global.getLineEnding(j)
    
    print("\tline ending: ", line_ending.getId())

print("styles: ", info_global.getNumStyles())
style = info_global.getStyle(0)
print("style dir:")
print(dir(style))

for j in range(info_global.getNumStyles()):
    
    style = info_global.getStyle(j)
    
    print("\tstyle: ", style.getId())
    print("\t\troles: ", style.createRoleString())
    print("\t\ttypes: ", style.createTypeString())
    
# Add render info to the layout

layout = layout_plugin.getLayout(0)

render_plugin = layout.getPlugin("render")    

print()    
print("num local render objects: ", render_plugin.getNumLocalRenderInformationObjects())    







