"""Apply render information from SBML file, and add new render information to 
the SBML file."""

from collections import namedtuple
from matplotlib.colors import is_color_like
from matplotlib.font_manager import findSystemFonts
from pathlib import Path

import libsbml

PlotColor = namedtuple("PlotColor", ["is_valid_color", "color"])
FontProperty = namedtuple("FontProperty", ["is_valid_value", "value"])

FONT_STYLES = ["italic", "normal"]


class Render:
    
    def __init__(self, sbml_filename, layout_number):
        
        self.doc = libsbml.readSBMLFromFile(sbml_filename)
        self.model = self.doc.getModel()
        self.layout_plugin = self.model.getPlugin("layout")
        self.layout = self.layout_plugin.getLayout(layout_number) if self.layout_plugin and self.layout_plugin.getNumLayouts() > 0 else None
        self.rPlugin = self.layout.getPlugin("render") if self.layout else None 
        self.render_plugin = self.layout_plugin.getListOfLayouts().getPlugin("render") if self.layout_plugin else None       
        self.font_properties = self._setFontProperties()

    def _setFontProperties(self,):
        system_font_paths = findSystemFonts(fontpaths=None, fontext='ttf')
        system_font_names = [Path(fpath).stem for fpath in system_font_paths]

        font_properties = {
            "style": [0, 1],        
            "family": system_font_names + ["serif", "sans-serif", "cursive", "fantasy", "monospace"],
            "size": ["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"]
        }                
        
        return font_properties
    
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
        return color_definitions

    def _set_plot_color_and_validity(self, color, color_definitions):

        if is_color_like(color):        
            plot_color = PlotColor(True, color)
        elif color in color_definitions and is_color_like(color_definitions[color]):
            plot_color = PlotColor(True, color_definitions[color])
        else:
            plot_color = PlotColor(False, color)

        return plot_color

    def _updateNodesBasedOnSpeciesGlyph(self, global_style, color_definitions, network):
    
        node_fill_color = self._set_plot_color_and_validity(
                global_style.getGroup().getFillColor(), color_definitions)     
        node_edge_color = self._set_plot_color_and_validity(
                global_style.getGroup().getStroke(), color_definitions)
        
        for node in network.nodes.values():

            if node_fill_color.is_valid_color:    
                node.fill_color = node_fill_color.color
                print("set node fill color: ", node.fill_color)      
            else:
                pass
                # log this, and stick with default value

            if node_edge_color.is_valid_color:    
                node.edge_color = node_edge_color.color 
                print("set node edge color: ", node.edge_color)             
            else:
                pass
                # log this, and stick with default value

    def _set_font_property(self, font_property, property_value):

        if font_property == "style":
            if property_value in self.font_properties[font_property]:              
                font_property = FontProperty(True, FONT_STYLES[property_value])
            else:
                font_property = FontProperty(False, property_value)
 
        elif font_property == "family":
            if property_value.lower() in self.font_properties[font_property]:
                font_property = FontProperty(True, property_value)
            else:
                font_property = FontProperty(False, property_value)
            
        elif font_property == "size":
            if str(round(property_value)).isdigit() or str(property_value).lower() in self.font_properties[font_property]:
                font_property = FontProperty(True, property_value)
                print("font size is valid")
            else:
                font_property = FontProperty(False, property_value)
        else:
            font_property = FontProperty(False, property_value)

        return font_property
                                           
    def _updateNodesBasedOnTextGlyph(self, global_style, color_definitions, network):
    
        node_font_color = self._set_plot_color_and_validity(
                global_style.getGroup().getStroke(), color_definitions)
        
        node_font_size = self._set_font_property("size", global_style.getGroup().getFontSize().getAbsoluteValue())
        print("node_font_size: ", node_font_size) 
        node_font_family = self._set_font_property("family", global_style.getGroup().getFontFamily())
        print("node_font_family: ", node_font_family)
        node_font_style = self._set_font_property("style", global_style.getGroup().getFontStyle())
        print("node_font_style: ", node_font_style)
        
        print("setting valid node text values")        
        for node in network.nodes.values():

            if node_font_color.is_valid_color:    
                node.font_color = node_font_color.color

            if node_font_style.is_valid_value:
                node.font_style = node_font_style.value

            if node_font_size.is_valid_value:
                node.font_size = node_font_size.value

            if node_font_family.is_valid_value:
                node.font_family = node_font_family.value

    def _updateNodesBasedOnReactionGlyph(self, global_style, color_definitions, network):

        reaction_edge_color = self._set_plot_color_and_validity(
                global_style.getGroup().getStroke(), color_definitions)     

        reaction_edge_width = global_style.getGroup().getStrokeWidth()
        
        for reaction in network.edges.values():

            if reaction_edge_color.is_valid_color:    
                reaction.edge_color = reaction_edge_color.color 
                reaction.fill_color = reaction_edge_color.color
                print("set reaction edge color: ", reaction.edge_color)             
            else:
                pass
                # log this, and stick with default value

            #if reaction_edge_width > 0?, need to check this
            reaction.curve_width = reaction_edge_width
        
    def applyGlobalRenderInformation(self, network):

        if self.render_plugin:

            print("num global info: ", self.render_plugin.getNumGlobalRenderInformationObjects())

            if self.render_plugin.getNumGlobalRenderInformationObjects() > 0:

                for global_render_info in self.render_plugin.getListOfGlobalRenderInformation():
                    # Process each global render information object
                    if global_render_info:
                        # collect the color definitions
                        print("num color definitions: ", global_render_info.getNumColorDefinitions())
                        color_definitions = self._collectColorDefinitions(global_render_info)
                        # process Styles 	                  
                        # x = global_render_info.getListOfStyles()
                        # print("list of GS: ", type(x), ", ", len(x))
                        for global_style in global_render_info.getListOfStyles(): 
                            if global_style.isInTypeList("SPECIESGLYPH"):
                                self._updateNodesBasedOnSpeciesGlyph(global_style, color_definitions, network)
                            elif global_style.isInTypeList("TEXTGLYPH"):
                                self._updateNodesBasedOnTextGlyph(global_style, color_definitions, network)
                            elif global_style.isInTypeList("REACTIONGLYPH"):
                                self._updateNodesBasedOnReactionGlyph(global_style, color_definitions, network)
                            else:
                                pass
                            
                        print("color definitions: ", len(color_definitions))
        
    def applyLocalRenderInformation(self, network):

        if self.rPlugin:
            
            print("num local info: ", self.rPlugin.getNumLocalRenderInformationObjects())

            for local_render_info in self.rPlugin.getListOfLocalRenderInformation():

                if local_render_info:
                    
                    for local_style in local_render_info.getListOfStyles():
                        ids = local_style.getIdList()
                        print("local style ids: ", ids)
                        #network.nodes.keys()
                        #network.edges.keys()                        

        #print("local render, rPlugin type: ", type(self.rPlugin))    

        
    def addRenderInformation(self, network): 
        # Global
        # get global object, else create global object
        if self.render_plugin.getNumGlobalRenderInformationObjects() > 0:
            # get Global Object of Interest
            print("global render IO's")







        
        
        
        
                