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

    def _collectColorDefinitions(self, global_render_info):
        # -- collect color definitions
        color_definitions = {}
        for color_defn in global_render_info.getListOfColorDefinitions():
            color_definitions[color_defn.getId()] = color_defn.createValueString()    
    
    def applyGlobalRenderInformation(self, network):

        if self.render_plugin:

            print("num global info: ", self.render_plugin.getNumGlobalRenderInformationObjects())

            if self.render_plugin.getNumGlobalRenderInformationObjects() > 0:

                for global_render_info in self.render_plugin.getListOfGlobalRenderInformation():
                    # Process each global render information object
                    if(global_render_info):
                        # collect the color definitions
                        print("num color definitions: ", global_render_info.getNumColorDefinitions())
                        color_definitions = self._collectColorDefinitions(global_render_info)
                        # process Styles 	                  
                        for global_style in global_render_info.getListOfGlobalStyles(): 

                            #   SPECIESGLYPHS
                            #   TEXTGLYPHS
                            #   REACTIONGLYPHS
                            
                            # apply to nodes                                
                            if global_style.isInTypeList("SPECIESGLYPH"):
                           
                                if global_style.getGroup().isSetFillColor():
                                    node_color = global_style.getGroup().getFillColor()
                                    for node in network.nodes.values():
                                        node.fill_color = node_color
                                        print("set node color: ", node.fill_color)                            
                        
            print("color definitions: ", len(color_definitions))
        
    def applyLocalRenderInformation(self, network):
        if self.rPlugin:
            print("num local info: ", self.rPlugin.getNumLocalRenderInformationObjects())
        print("local render, network type: ", type(network))
        
        
        
        
        
        