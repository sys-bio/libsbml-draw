"""Apply render information from SBML file, and add new render information to
the SBML file."""

from collections import namedtuple
import math

from matplotlib.colors import is_color_like
from matplotlib.font_manager import findSystemFonts
from pathlib import Path

import libsbml

PlotColor = namedtuple("PlotColor", ["is_valid_color", "color"])
FontProperty = namedtuple("FontProperty", ["is_valid_value", "value"])
GlyphProperty = namedtuple("GlyphProperty", ["type", "entity_id"])

FONT_STYLES = ["none", "normal", "italic"]


class Render:
    """Holds the render data and provides methods to apply that data to a
    network and to add a user's changes to the network to be added to the
    render data.
    """
    def __init__(self, sbml_doc, layout_number):

        # SBMLDocument, SBMLReader
        self.doc = sbml_doc
        # Model
        self.model = self.doc.getModel()
        # SBasePlugin, LayoutModelPlugin
        self.layout_plugin = self.model.getPlugin("layout")
        # Layout
        self.layout = self.layout_plugin.getLayout(layout_number) if (
            self.layout_plugin and self.layout_plugin.getNumLayouts() > 0
                                                                ) else None
        # SBasePlugin, RenderLayoutPlugin
        self.rPlugin = self.layout.getPlugin("render") if self.layout else None
        # SBasePlugin, RenderListOfLayoutsPlugin
        self.render_plugin = self.layout_plugin.getListOfLayouts(
                ).getPlugin("render") if self.layout_plugin else None
        self.font_properties = self._getFontProperties()
        self.color_definitions = {}
#        self.compartmentGlyphs = self.layout.getListOfCompartmentGlyphs()
#        self.reactionGlyphs = self.layout.getListOfReactionGlyphs()
#        self.speciesGlyphs = self.layout.getListOfSpeciesGlyphs()
#        self.textGlyphs = self.layout.getListOfTextGlyphs()
        self.speciesGlyphs = self._createSpeciesGlyphsDirectory()
        self.textGlyphs = self._createTextGlyphsDirectory()
        self.compartmentGlyphs = self._createCompartmentGlyphsDirectory()
        self.reactionGlyphs = self._createReactionGlyphsDirectory()
        self.glyphsDirectory = self._createGlyphsDirectory()

#        print("num compartment glyphs: ", len(self.compartmentGlyphs))
#        print("num species glyphs: ", len(self.speciesGlyphs))
#        print("num text glyphs: ", len(self.textGlyphs))


    def _createSpeciesGlyphsDirectory(self,):
        """
        Returns: dictionary, key=glyph_id, value=species_id
        """
        speciesDirectory = dict()

        for species in self.layout.getListOfSpeciesGlyphs():
            glyph_id = species.getId()
            species_id = species.getSpeciesId()
            speciesDirectory[glyph_id] = species_id
        
        return speciesDirectory
    
    def _createTextGlyphsDirectory(self,):
        """
        Returns: dictionary, key=glyph_id, value=species_id
        """
        textDirectory = dict()

        for text in self.layout.getListOfTextGlyphs():
            glyph_id = text.getId()
            species_id = self.speciesGlyphs[text.getGraphicalObjectId()]
            textDirectory[glyph_id] = species_id
        
        return textDirectory

    def _createCompartmentGlyphsDirectory(self,):
        """
        Returns: dictionary, key=glyph_id, value=species_id
        """
        compartmentDirectory = dict()

        for compartment in self.layout.getListOfCompartmentGlyphs():
            glyph_id = compartment.getId()
            compartment_id = compartment.getCompartmentId()
            compartmentDirectory[glyph_id] = compartment_id
        
        return compartmentDirectory

    def _createReactionGlyphsDirectory(self,):
        """
        Returns: dictionary, key=glyph_id, value=species_id
        """
        reactionDirectory = dict()

        for reaction in self.layout.getListOfReactionGlyphs():
            glyph_id = reaction.getId()
            reaction_id = reaction.getReactionId()
            reactionDirectory[glyph_id] = reaction_id
        
        return reactionDirectory


    def _createGlyphsDirectory(self,):
        """        
        """
        glyphsDirectory = dict()        

        for compartment in self.layout.getListOfCompartmentGlyphs():
            glyph_id = compartment.getId()
            compartment_id = compartment.getCompartmentId()
            glyphsDirectory[glyph_id] = GlyphProperty("compartment", compartment_id)
            print("compartment glyph: ", glyph_id)     
            print("compartment: ", compartment_id)
            
        for reaction in self.layout.getListOfReactionGlyphs(): 
            glyph_id = reaction.getId()
            reaction_id = reaction.getReactionId()
            glyphsDirectory[glyph_id] = GlyphProperty("reaction", reaction_id)
            print("reaction glyph: ", glyph_id)     
            print("reaction: ", reaction_id)
            
        for species in self.layout.getListOfSpeciesGlyphs():
            glyph_id = species.getId()
            species_id = species.getSpeciesId()
            glyphsDirectory[glyph_id] = GlyphProperty("species", species_id)
            print("species glyph: ", glyph_id)     
            print("species: ", species_id)
            
        for text in self.layout.getListOfTextGlyphs():
            glyph_id = text.getId()
            species_id = self.speciesGlyphs[text.getGraphicalObjectId()]
            glyphsDirectory[glyph_id] = GlyphProperty("text", species_id)
            print("text glyph: ", glyph_id)     
            print("text: ", species_id)    

        print("size glyphs dir:", len(glyphsDirectory))

        return glyphsDirectory
        

    def _getFontProperties(self,):
        """Finds the font families on the system, and provides valid values for
        font style, font family, and font size.

        Args: None

        Returns: dict
        """
        system_font_paths = findSystemFonts(fontpaths=None, fontext='ttf')
        system_font_names = [Path(fpath).stem for fpath in system_font_paths]

        font_properties = {
            "style": [1, 2],
            "family": system_font_names + ["serif", "sans-serif", "cursive",
                                           "fantasy", "monospace"],
            "size": ["xx-small", "x-small", "small", "medium", "large",
                     "x-large", "xx-large"]
        }

        return font_properties

    def _describeRenderInfo(self,):
        """Prints type info for libsbml layout and render variables.
        """
        print("layout_plugin: ", type(self.layout_plugin))
        print("layout: ", type(self.layout))
        print("rPlugin: ", type(self.rPlugin))
        print("render_plugin: ", type(self.render_plugin))
        print("num layouts: ", self.layout_plugin.getNumLayouts())

    def _collectColorDefinitions(self, global_render_info):
        """Gets the global render color definitions.

        Args:
            global_render_info(libsbml.Render):

        Returns: dict, keys = color id, values = color value
        """
        color_definitions = {}
        for color_defn in global_render_info.getListOfColorDefinitions():
            color_definitions[color_defn.getId()
                              ] = color_defn.createValueString()
        return color_definitions

    def _set_plot_color_and_validity(self, color):
        """Determines if the plot color is valid.

        Args:
            color(str): id of color

        Returns: named tuple PlotColor with fields is_valid_color and color
        """
        if is_color_like(color) and color != "none":
            plot_color = PlotColor(True, color)
        elif color in self.color_definitions and is_color_like(
                self.color_definitions[color]):
            plot_color = PlotColor(True, self.color_definitions[color])
        else:
            plot_color = PlotColor(False, color)

        return plot_color

    def _updateNodesBasedOnSpeciesGlyph(self, render_style, network, idList):
        """Sets node values based on the SPECIESGLYPH settings.

        Args:
            render_style(libsbml.Style): contains style info
            network (libsbml_draw.model.Network): the model's network
            idList(list): list of ids to update

        Returns: None
        """
        
        element = render_style.getGroup().getElement(0)

#        print("element data ", type(element), element.isRectangle(), element.isRenderCurve(), element.getStroke())
        
        node_fill_color = self._set_plot_color_and_validity(
                render_style.getGroup().getFillColor())
        node_edge_color = self._set_plot_color_and_validity(
                render_style.getGroup().getStroke())

        node_edge_width = render_style.getGroup().getStrokeWidth()
        
        nodes_to_update = {k: network.nodes[k]
                           for k in network.nodes.keys() & idList}

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

            node.edge_width = node_edge_width

    def _set_font_property(self, font_property, property_value):
        """Determines if the font property of is valid.  Font properties which
        can be validated are 'style', 'family', and 'size'.

        Args:
            font_property(str): 'style', 'family', or 'size'
            property_value(str or int): value for the font_property

        Returns: named tuple with fields is_valid_value and value
        """
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
            # property_value is a float
            if (not math.isnan(property_value) and
                (str(round(property_value)).isdigit() or
                 str(property_value).lower() in self.font_properties[
                    font_property])):
                font_property = FontProperty(True, property_value)
            else:
                font_property = FontProperty(False, property_value)
        else:
            font_property = FontProperty(False, property_value)

        return font_property

    def _updateNodesBasedOnTextGlyph(
            self,
            render_style,
            network,
            idList):
        """Sets node values based on the TEXTGLYPH settings.

        Args:
            render_style(libsbml.Style): contains style info
            network (libsbml_draw.model.Network): the model's network
            idList(list): list of ids to update

        Returns: None
        """
        node_font_color = self._set_plot_color_and_validity(
                render_style.getGroup().getStroke())

        node_font_size = self._set_font_property(
                "size",
                render_style.getGroup().getFontSize().getAbsoluteValue())

        node_font_family = self._set_font_property(
                "family",
                render_style.getGroup().getFontFamily())

        node_font_style = self._set_font_property(
                "style",
                render_style.getGroup().getFontStyle())

        nodes_to_update = {k: network.nodes[k]
                           for k in network.nodes.keys() & idList}

        for node in nodes_to_update.values():

            if node_font_color.is_valid_color:
                node.font_color = node_font_color.color

            if node_font_style.is_valid_value:
                node.font_style = node_font_style.value

            if node_font_size.is_valid_value:
                node.font_size = node_font_size.value

            if node_font_family.is_valid_value:
                node.font_family = node_font_family.value

    def _updateReactionsBasedOnReactionGlyph(
            self,
            render_style,
            network,
            idList):

        """Sets reaction values based on the REACTIONGLYPH settings.

        Args:
            render_style(libsbml.Style): contains style info
            network (libsbml_draw.model.Network): the model's network
            idList(list): list of ids to update

        Returns: None
        """
        reaction_edge_color = self._set_plot_color_and_validity(
                render_style.getGroup().getStroke())

        reaction_edge_width = render_style.getGroup().getStrokeWidth()

        reactions_to_update = {k: network.reactions[k]
                               for k in network.reactions.keys() & idList}

        for reaction in reactions_to_update.values():

            if reaction_edge_color.is_valid_color:
                reaction.edge_color = reaction_edge_color.color
                reaction.fill_color = reaction_edge_color.color
            else:
                pass
                # stick with default value

            reaction.curve_width = reaction_edge_width

    def _updateCompartmentsBasedOnCompartmentGlyph(
            self,
            render_style,
            network,
            idList):

        """Sets compartment values based on the COMPARTMENTGLYPH settings.

        Args:
            render_style(libsbml.Style): contains style info
            network (libsbml_draw.model.Network): the model's network
            idList(list): list of ids to update

        Returns: None
        """
        print("UPDATING COMPARTMENTS")
        
        
        
        compartment_edge_color = self._set_plot_color_and_validity(
                render_style.getGroup().getStroke())

        compartment_fill_color = self._set_plot_color_and_validity(
                render_style.getGroup().getFillColor())

        compartment_line_width = render_style.getGroup().getStrokeWidth()

        compartments_to_update = {k: network.compartments[k] for k in
                                  network.compartments.keys() & idList}

## the compartment render data is inside the "rectangle" element, which can't
## be reached due to a bug in libsbml, as confirmed by Frank.        

        rectangle = render_style.getGroup().getElement(0)

        print("rectangle data ", type(rectangle), rectangle.isRectangle())
#        print("stroke: ", rectangle.getStroke())
#        print("stroke width:", rectangle.getStrokeWidth())
#        print("fill color: ", rectangle.getFillColor())

#        print("compartment_fill_color: ", compartment_fill_color.color,
#              compartment_fill_color.is_valid_color)
#        print("compartment_edge_color: ", compartment_edge_color.color,
#              compartment_edge_color.is_valid_color)

        for compartment in compartments_to_update.values():

            if compartment_edge_color.is_valid_color:
                compartment.edge_color = compartment_edge_color.color
            else:
                pass
                # stick with default value

            if compartment_fill_color.is_valid_color:
                compartment.fill_color = compartment_fill_color.color
            else:
                pass
                # stick with default value

            if compartment_line_width > 0:
                compartment.line_width = compartment_line_width

    def _applyGlobalRenderInformation(self, network):
        """Applies global style render information as specified in the
        SPECIESGLYPH, TEXTGLYPH, REACTIONGLYPH, and COMPARTMENTGLYPH.

        Args:
            network (libsbml_draw.model.Network): the model's network

        Returns: None
        """
        if (self.render_plugin and
                self.render_plugin.getNumGlobalRenderInformationObjects() > 0):

            for global_render_info in \
                    self.render_plugin.getListOfGlobalRenderInformation():

                if global_render_info:

                    self.color_definitions = self._collectColorDefinitions(
                            global_render_info)

                    for global_style in global_render_info.getListOfStyles():
                        
                        if global_style.isInTypeList("SPECIESGLYPH"):
                            self._updateNodesBasedOnSpeciesGlyph(
                                    global_style,
                                    network,
                                    network.nodes.keys())
                        elif global_style.isInTypeList("TEXTGLYPH"):
                            self._updateNodesBasedOnTextGlyph(
                                    global_style,
                                    network,
                                    network.nodes.keys())
                        elif global_style.isInTypeList("REACTIONGLYPH"):
                            self._updateReactionsBasedOnReactionGlyph(
                                    global_style,
                                    network,
                                    network.reactions.keys())
                        elif global_style.isInTypeList("COMPARTMENTGLYPH"):
                            self._updateCompartmentsBasedOnCompartmentGlyph(
                                    global_style,
                                    network,
                                    network.compartments.keys())
                        else:
                            pass

    def _getLocalIdList(self, local_style, network_id_set):
        """Gets a list of ids from the network (nodes, reactions, or
        compartments), which are found in the LocalStyle's id list.

        Args:
            local_style(libsbml.LocalStyle):

        Returns: list
        """
        idList = set()

        for this_id in network_id_set:
            if local_style.getIdList().has_key(this_id):  # noqa
                idList.add(this_id)

        return idList

    def _applyLocalRenderInformationOrig(self, network):
        """Sets values in the model's nodes and reactions as specified by
        the idList for each local style.

        Args:
            network (libsbml_draw.model.Network): the model's network

        Returns: None
        """
        if self.layout:
            reaction_glyphs = self.layout.getListOfReactionGlyphs()
            for reaction_glyph in reaction_glyphs:
                print("rg: ", reaction_glyph.getElementName(), 
                      reaction_glyph.getId(), reaction_glyph.getReactionId())

            
        #    for index in range(self.layout.getNumCompartmentGlyphs()):
        #        compartment_glyph = self.layout.getCompartmentGlyph(index)
        #        print("cg id: ", compartment_glyph.getId())
        #        print("compartment id: ", compartment_glyph.getCompartmentId(
        # ))

        if self.rPlugin:

            for local_render_info in \
                    self.rPlugin.getListOfLocalRenderInformation():

                if local_render_info:
                    
                    self.color_definitions = self._collectColorDefinitions(
                            local_render_info)

                    for local_style in local_render_info.getListOfStyles():

                        nodes_id_list = self._getLocalIdList(
                                local_style, network.nodes.keys())

                        if len(nodes_id_list) > 0:

                            if local_style.isInTypeList("SPECIESGLYPH"):
                                self._updateNodesBasedOnSpeciesGlyph(
                                    local_style, network, nodes_id_list)
                            elif local_style.isInTypeList("TEXTGLYPH"):
                                self._updateNodesBasedOnTextGlyph(
                                    local_style, network, nodes_id_list)
                            else:
                                pass

                        reactions_id_list = self._getLocalIdList(
                                local_style, network.reactions.keys())

                        if len(reactions_id_list) > 0:

                            if local_style.isInTypeList("REACTIONGLYPH"):
                                self._updateReactionsBasedOnReactionGlyph(
                                    local_style, network, reactions_id_list)
                            else:
                                pass

                        compartments_id_list = \
                            self._getCompartmentIdsFromCGlyphs(local_style,
                                                               network)

                        if len(compartments_id_list) > 0:

                            if local_style.isInTypeList("COMPARTMENTGLYPH"):
                                self._updateCompartmentsBasedOnCompartmentGlyph(  # noqa  
                                    local_style, network, compartments_id_list)

    def _getCompartmentIdsInIdList(self, idList):
        """ """
        compartmentIds = list()

        for glyph in self.compartmentGlyphs:

            if idList.has_key(glyph):
                compartmentIds.append(self.compartmentGlyphs[glyph])

        return compartmentIds

    def _getSpeciesIdsInIdList(self, idList):
        """ """
        speciesIds = list()

        for glyph in self.speciesGlyphs:

            if idList.has_key(glyph):
                speciesIds.append(self.speciesGlyphs[glyph])

        return speciesIds

    def _getSpeciesIdsForTextInIdList(self, idList):
        """ """
        speciesIdsForText = list()

        for glyph in self.textGlyphs:

            if idList.has_key(glyph):
                speciesIdsForText.append(self.textGlyphs[glyph])

        return speciesIdsForText

    def _getReactionIdsInIdList(self, idList):
        """ """
        reactionIds = list()

        for glyph in self.reactionGlyphs:

            if idList.has_key(glyph):
                reactionIds.append(self.reactionGlyphs[glyph])

        return reactionIds

        

    def _applyLocalRenderInformation(self, network):
        """Sets values in the model's nodes and reactions as specified by
        the idList for each local style.

        Args:
            network (libsbml_draw.model.Network): the model's network

        Returns: None
        """

        if self.rPlugin:

            for local_render_info in \
                    self.rPlugin.getListOfLocalRenderInformation():

                if local_render_info:
                    
                    self.color_definitions = self._collectColorDefinitions(
                            local_render_info)

                    for local_style in local_render_info.getListOfStyles():

                        idList = local_style.getIdList()
                        roleList = local_style.getRoleList()
                        typeList = local_style.getTypeList()
                        
                        if idList.size():
                            # get the id's of the elements to update
                            compartmentIds = self._getCompartmentIdsInIdList(idList)                            
                            speciesIds = self._getSpeciesIdsInIdList(idList)
                            reactionIds = self._getReactionIdsInIdList(idList)
                            textIds = self._getSpeciesIdsForTextInIdList(idList)
                            print()
                            print("num compartment ids: ", len(compartmentIds))
                            print("num species ids: ", len(speciesIds))
                            print("num reaction ids: ", len(reactionIds))
                            print("num text ids: ", len(textIds))
                            print()
                            
                            if len(compartmentIds) > 0:
                                self._updateCompartmentsBasedOnCompartmentGlyph(  # noqa  
                                    local_style, network, compartmentIds)

                            if len(speciesIds) > 0:
                                self._updateNodesBasedOnSpeciesGlyph(
                                    local_style, network, speciesIds)

                            if len(textIds) > 0:
                                self._updateNodesBasedOnTextGlyph(
                                    local_style, network, textIds)
                                
                        elif roleList.size():
                            pass                            
                        elif typeList.size():
                            pass
                        else:
                            pass

    def _getCompartmentIdsFromCGlyphs(self, local_style, network):
        """
        """
        all_compartment_ids = list()

        for cglyph_index in range(self.layout.getNumCompartmentGlyphs()):
            cglyph = self.layout.getCompartmentGlyph(cglyph_index)
            if local_style.getIdList().has_key(cglyph.getId()):  # noqa
                all_compartment_ids.append(cglyph.getCompartmentId())

        network_compartment_ids = list()

        for compartment_id in all_compartment_ids:
            if compartment_id in network.compartments:
                network_compartment_ids.append(compartment_id)

        return network_compartment_ids

    def _addLocalStylesRenderInformation(self, local_render_info, network):
        """Add a LocalStyle of type SPECIESGLYPH and TEXTGLYPH for each node,
        and of type REACTIONGLYPH for each reaction.

        Args:
            local_render_info(libsbml.Render): SBML local render info
            network (libsbml_draw.model.Network): the model's network

        Returns: None
        """
        local_render_info.setId("localRenderInfo")
        local_render_info.setName("Fill_Color Render Information")

        for node in network.nodes.values():
            style = local_render_info.createStyle("")
            # LocalStyle, RenderGroup
            style.getGroup().setFillColor(node.fill_color)
            style.getGroup().setStroke(node.edge_color)
            style.getGroup().setStrokeWidth(node.edge_width)
            style.addId(node.id)
            style.addType("SPECIESGLYPH")
            rectangle = style.getGroup().createRectangle()
            rectangle.setX(libsbml.RelAbsVector("000%"))
            rectangle.setY(libsbml.RelAbsVector("000%"))
            rectangle.setWidth(libsbml.RelAbsVector("100%"))
            rectangle.setHeight(libsbml.RelAbsVector("100%"))
            rectangle.setFill(node.fill_color)
            rectangle.setStroke(node.edge_color)
            rectangle.setStrokeWidth(node.edge_width)

            style = local_render_info.createStyle("")
            style.getGroup().setFontFamily(node.font_family)
            style.getGroup().setFontSize(libsbml.RelAbsVector(node.font_size))
            style.getGroup().setTextAnchor("middle")
            style.getGroup().setVTextAnchor("middle")
            if node.font_style == "italic":
                style.getGroup().setFontStyle(2)
            else:  # "normal"
                style.getGroup().setFontStyle(1)
            style.getGroup().setStroke(node.font_color)
            style.addId(node.id)
            style.addType("TEXTGLYPH")

        for reaction in network.reactions.values():
            style = local_render_info.createStyle("")
            style.getGroup().setStroke(reaction.edge_color)
            style.getGroup().setFillColor(reaction.fill_color)
            style.getGroup().setStrokeWidth(reaction.curve_width)
            style.addId(reaction.id)
            style.addType("REACTIONGLYPH")

        for compartment in network.compartments.values():
            style = local_render_info.createStyle("")
            style.getGroup().setStroke(compartment.edge_color)
            style.getGroup().setFillColor(compartment.fill_color)
            style.getGroup().setStrokeWidth(compartment.line_width)
            style.addId(compartment.id)
            style.addType("COMPARTMENTGLYPH")

    def addRenderInformation(self, network):
        """Add render information to the model as Local Style render
        information.  If local render information already exists, remove it,
        and add new entries for the nodes and reactions.

        Args:
            network (libsbml_draw.model.Network): the model's network

        Returns: None
        """
        # add local elements for each node and reaction
        if (self.rPlugin is not None and
                self.rPlugin.getNumLocalRenderInformationObjects() > 0):
            for local_index in range(
                    self.rPlugin.getNumLocalRenderInformationObjects()):
                local_render_info = \
                    self.rPlugin.removeLocalRenderInformation(local_index)
            local_render_info = self.rPlugin.createLocalRenderInformation()
            self._addLocalStylesRenderInformation(local_render_info, network)
        else:
            uri = libsbml.RenderExtension_getXmlnsL2() if self.doc.getLevel(
                    ) == 2 else libsbml.RenderExtension_getXmlnsL3V1V1()

            # enable render package
            self.doc.enablePackage(uri, "render", True)
            self.doc.setPackageRequired("render", False)

            rPlugin = self.layout.getPlugin("render")

            local_render_info = rPlugin.createLocalRenderInformation()

            self._addLocalStylesRenderInformation(local_render_info, network)

    def applyRenderInformation(self, network):
        """Applies global style render information as specified in the
        SPECIESGLYPH, TEXTGLYPH, and REACTIONGLYPH, and local render
        information based on id's of nodes, reactions, and compartments.

        Args:
            network (libsbml_draw.model.Network): the model's network

        Returns: None
        """
        self._applyGlobalRenderInformation(network)
        self._applyLocalRenderInformation(network)

        