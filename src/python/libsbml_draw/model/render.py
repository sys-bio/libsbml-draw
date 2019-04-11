"""Apply render information from SBML file, and add new render information to 
the SBML file."""

from collections import namedtuple
from matplotlib.colors import is_color_like
from matplotlib.font_manager import findSystemFonts
from pathlib import Path

import libsbml

PlotColor = namedtuple("PlotColor", ["is_valid_color", "color"])
FontProperty = namedtuple("FontProperty", ["is_valid_value", "value"])

FONT_STYLES = ["none", "normal", "italic"]


class Render:
    
    def __init__(self, sbml_filename, layout_number):
        
        # SBMLDocument, SBMLReader
        self.doc = libsbml.readSBMLFromFile(sbml_filename)
        # Model
        self.model = self.doc.getModel()
        # SBasePlugin, LayoutModelPlugin
        self.layout_plugin = self.model.getPlugin("layout")
        # Layout
        self.layout = self.layout_plugin.getLayout(layout_number) if self.layout_plugin and self.layout_plugin.getNumLayouts() > 0 else None
        # SBasePlugin, RenderLayoutPlugin
        self.rPlugin = self.layout.getPlugin("render") if self.layout else None 
        # SBasePlugin, RenderListOfLayoutsPlugin
        self.render_plugin = self.layout_plugin.getListOfLayouts().getPlugin("render") if self.layout_plugin else None       
        self.font_properties = self._setFontProperties()

    def _setFontProperties(self,):
        system_font_paths = findSystemFonts(fontpaths=None, fontext='ttf')
        system_font_names = [Path(fpath).stem for fpath in system_font_paths]

        font_properties = {
            "style": [1, 2],        
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

    def _updateNodesBasedOnSpeciesGlyph(self, global_style, color_definitions, network, idList):
    
        node_fill_color = self._set_plot_color_and_validity(
                global_style.getGroup().getFillColor(), color_definitions)     
        node_edge_color = self._set_plot_color_and_validity(
                global_style.getGroup().getStroke(), color_definitions)

        nodes_to_update = {k: network.nodes[k] for k in network.nodes.keys() & idList}
        
        for node in nodes_to_update.values():

            if node_fill_color.is_valid_color:    
                node.fill_color = node_fill_color.color
            else:
                pass
                # stick with default value

            if node_edge_color.is_valid_color:    
                node.edge_color = node_edge_color.color 
            else:
                pass
                # stick with default value

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
            else:
                font_property = FontProperty(False, property_value)
        else:
            font_property = FontProperty(False, property_value)

        return font_property
                                           
    def _updateNodesBasedOnTextGlyph(self, global_style, color_definitions, network, idList):
    
        node_font_color = self._set_plot_color_and_validity(
                global_style.getGroup().getStroke(), color_definitions)
        
        node_font_size = self._set_font_property("size", global_style.getGroup().getFontSize().getAbsoluteValue())
        
        node_font_family = self._set_font_property("family", global_style.getGroup().getFontFamily())

        node_font_style = self._set_font_property("style", global_style.getGroup().getFontStyle())

        nodes_to_update = {k: network.nodes[k] for k in network.nodes.keys() & idList}
        
        for node in nodes_to_update.values():

            if node_font_color.is_valid_color:    
                node.font_color = node_font_color.color

            if node_font_style.is_valid_value:
                node.font_style = node_font_style.value

            if node_font_size.is_valid_value:
                node.font_size = node_font_size.value

            if node_font_family.is_valid_value:
                node.font_family = node_font_family.value

    def _updateNodesBasedOnReactionGlyph(self, global_style, color_definitions, network, idList):

        reaction_edge_color = self._set_plot_color_and_validity(
                global_style.getGroup().getStroke(), color_definitions)     

        reaction_edge_width = global_style.getGroup().getStrokeWidth()

        reactions_to_update = {k: network.edges[k] for k in network.edges.keys() & idList}
        
        for reaction in reactions_to_update.values():

            if reaction_edge_color.is_valid_color:    
                reaction.edge_color = reaction_edge_color.color 
                reaction.fill_color = reaction_edge_color.color
            else:
                pass
                # stick with default value

            reaction.curve_width = reaction_edge_width
        
    def applyGlobalRenderInformation(self, network):

        if self.render_plugin:

            if self.render_plugin.getNumGlobalRenderInformationObjects() > 0:

                for global_render_info in self.render_plugin.getListOfGlobalRenderInformation():
                    
                    if global_render_info:
                        
                        color_definitions = self._collectColorDefinitions(global_render_info)

                        for global_style in global_render_info.getListOfStyles(): 
                            if global_style.isInTypeList("SPECIESGLYPH"):
                                self._updateNodesBasedOnSpeciesGlyph(global_style, color_definitions, network, network.nodes.keys())
                            elif global_style.isInTypeList("TEXTGLYPH"):
                                self._updateNodesBasedOnTextGlyph(global_style, color_definitions, network, network.nodes.keys())
                            elif global_style.isInTypeList("REACTIONGLYPH"):
                                self._updateNodesBasedOnReactionGlyph(global_style, color_definitions, network, network.edges.keys())
                            else:
                                pass

    def _getLocalIdList(self, local_style, full_id_set):

        idList = set()

        for this_id in full_id_set:
        
            if local_style.getIdList().has_key(this_id):
                idList.add(this_id)
                        
        return idList
                                                     
    def applyLocalRenderInformation(self, network):

        if self.rPlugin:
            
            print("num local info: ", self.rPlugin.getNumLocalRenderInformationObjects())

            for local_render_info in self.rPlugin.getListOfLocalRenderInformation():

                if local_render_info:
                    
                    for local_style in local_render_info.getListOfStyles():

                        if local_style.getTypeList().has_key("SPECIESGLYPH"):
                            idList = self._getLocalIdList(local_style, network.nodes.keys())
                            self._updateNodesBasedOnSpeciesGlyph(local_style, {}, network, idList) 
                        elif local_style.getTypeList().has_key("TEXTGLYPH"):
                            idList = self._getLocalIdList(local_style, network.nodes.keys())
                            self._updateNodesBasedOnTextGlyph(local_style, {}, network, idList) 
                        elif local_style.getTypeList().has_key("REACTIONGLYPH"):
                            idList = self._getLocalIdList(local_style, network.edges.keys())
                            self._updateNodesBasedOnReactionGlyph(local_style, {}, network, idList) 
                        else:
                            pass                        

    def _addLocalStylesRenderInformation(self, local_render_info, network):
        
        local_render_info.setId("localRenderInfo")
        local_render_info.setName("Fill_Color Render Information")

        print("adding local render info for nodes")
 
        for node in network.nodes.values():            
            style = local_render_info.createStyle("nodeStyle")
            # LocalStyle, RenderGroup
            style.getGroup().setFillColor(node.fill_color)
            style.getGroup().setStroke(node.edge_color)
            style.addId(node.id)
            style.addType("SPECIESGLYPH")

            style = local_render_info.createStyle("nodeStyle")
            style.getGroup().setFontFamily(node.font_family)
            style.getGroup().setFontSize(libsbml.RelAbsVector(node.font_size))
            if node.font_style == "italic":
                style.getGroup().setFontStyle(2)
            else:
                style.getGroup().setFontStyle(1)
            print("font style: ", style.getGroup().getFontStyle())
            style.getGroup().setStroke(node.font_color)
            style.addId(node.id)
            style.addType("TEXTGLYPH")

        print("adding local render info for reactions")

        for reaction in network.edges.values():
            style = local_render_info.createStyle("reactionStyle")
            style.getGroup().setStroke(reaction.edge_color)
            style.getGroup().setFillColor(reaction.fill_color)
            style.getGroup().setStrokeWidth(reaction.curve_width)
            style.addId(reaction.id)
            style.addType("REACTIONGLYPH")
    
    def addRenderInformation(self, network):
        # add local elements for each node and reaction
        if (self.rPlugin is not None and self.rPlugin.getNumLocalRenderInformationObjects() > 0):
            print("num local render info objects: ", self.rPlugin.getNumLocalRenderInformationObjects())
            print("removing local render information objects")
            for local_index in range(self.rPlugin.getNumLocalRenderInformationObjects()): 
                local_render_info = self.rPlugin.removeLocalRenderInformation(local_index)            
            #print("num local render info objects: ", self.rPlugin.getNumLocalRenderInformationObjects())
            local_render_info = self.rPlugin.createLocalRenderInformation()
            print("num local render info objects: ", self.rPlugin.getNumLocalRenderInformationObjects())
            print("adding local render styles")
            self._addLocalStylesRenderInformation(local_render_info, network)
        else:
            uri = libsbml.RenderExtension.getXmlnsL2() if self.doc.getLevel(
                    ) == 2 else libsbml.RenderExtension.getXmlnsL3V1V1()

            # enable render package
            self.doc.enablePackage(uri, "render", True)
            self.doc.setPackageRequired("render", False)

            rPlugin = self.layout.getPlugin("render")

            local_render_info = rPlugin.createLocalRenderInformation()

            self._addLocalStylesRenderInformation(local_render_info, network)            


        
        
        
        
                