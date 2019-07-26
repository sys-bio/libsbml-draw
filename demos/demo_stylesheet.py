import libsbml

from pathlib import Path
import pkg_resources

STYLESHEET_FILE_NAME = "render-stylesheet_global.xml"
#STYLESHEET_FILE_NAME = "SBGNstyles.xml"

SS_FILE = Path(pkg_resources.resource_filename(
        "libsbml_draw",
        "model/data/" + STYLESHEET_FILE_NAME))

doc = libsbml.readSBMLFromFile(str(SS_FILE))

print("num errors: ", doc.getNumErrors())

for i in range(doc.getNumErrors()):
    error = doc.getError(i).getErrorId()

    print("error: ", error)

    print("error log: ", doc.getErrorLog())


    if error == libsbml.XMLFileUnreadable:
        print("XMLFileUnreadable")    
    elif error == libsbml.XMLFileOperationError:
        print("XMLFileOperationError")
    else:
        print("Other Error")
        
## Get Plugin
num_d_plugin = doc.getNumDisabledPlugins()
num_plugin = doc.getNumPlugins()
model = doc.getModel()
if model: 
    print("Model")
print("d_plugins", num_d_plugin)        
print("plugins", num_plugin)

layout_plugin = model.getPlugin("layout")
# Layout
layout = layout_plugin.getLayout(0) if (
    layout_plugin and layout_plugin.getNumLayouts() > 0) else None

# SBasePlugin, RenderLayoutPlugin
rPlugin = layout.getPlugin("render") if layout else None
# SBasePlugin, RenderListOfLayoutsPlugin
render_plugin = layout_plugin.getListOfLayouts(
    ).getPlugin("render") if layout_plugin else None

if (render_plugin and
    render_plugin.getNumGlobalRenderInformationObjects() > 0):

    for global_render_info in \
        render_plugin.getListOfGlobalRenderInformation():

        if global_render_info:

            print("GRI")

            for line_ending in global_render_info.getListOfLineEndings():

                bbox = line_ending.getBoundingBox()
                
                print("LE", line_ending.getId(), bbox.getX(), bbox.getY())




            