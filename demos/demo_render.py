#import libsbml

from libsbml_draw.model.sbml_layout import SBMLlayout
#from libsbml_draw.model.render import Render


#model_file = "C:\\tmp\\copasi.xml"
model_file = "C:\\tmp\\largerpathway.xml"

#doc = libsbml.readSBMLFromFile(model_file)
#model = doc.getModel()
#layout_plugin = model.getPlugin("layout")

#if layout_plugin:
#    print("num layouts: ", layout_plugin.getNumLayouts())


sl = SBMLlayout(model_file)

sl._describeModel()

sl.drawNetwork()
#r = Render(model_file, sl.layout_number)
#r._describeRenderInfo()

#print("render: ", type(r))
#print("num layouts: ", r.layout_plugin.getNumLayouts())

#sl._applyRenderInformation(None)



