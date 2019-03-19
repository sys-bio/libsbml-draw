"""Apply render information from SBML file, and add new render information to 
the SBML file."""

import libsbml


class Render:
    
    def __init__(self, sbml_filename, layout_number):
        
        self.doc = libsbml.readSBMLFromFile(sbml_filename)
        self.model = self.doc.getModel()
        self.layout_plugin = self.model.getPlugin("layout")
        self.layout = self.layout_plugin.getLayout(layout_number) if self.layout_plugin.getNumLayouts() > 0 else None
        self.rPlugin = self.layout.getPlugin("render") if self.layout else None 
        self.render_plugin = self.layout_plugin.getListOfLayouts().getPlugin("render") if self.layout_plugin else None       
    
    def _describeRenderInfo(self,):
        print("layout_plugin: ", type(self.layout_plugin))
        print("layout: ", type(self.layout))         
        print("rPlugin: ", type(self.rPlugin))
        print("render_plugin: ", type(self.render_plugin))
        print("num layouts: ", self.layout_plugin.getNumLayouts())
    
    def applyGlobalRenderInformation(self, network):
        if self.render_plugin:
            print("num global info: ", self.render_plugin.getNumGlobalRenderInformationObjects())
        print("network type: ", type(network))
        
    def applyLocalRenderInformation(self, network):
        if self.rPlugin:
            print("num local info: ", self.rPlugin.getNumLocalRenderInformationObjects())
