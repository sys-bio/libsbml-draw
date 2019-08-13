"""Apply render information from SBML file, and add new render information to
the SBML file."""

from collections import namedtuple
import math

from matplotlib.colors import is_color_like
from matplotlib.font_manager import findSystemFonts
import numpy as np
from pathlib import Path
import matplotlib.path as mplp

import pkg_resources
import xml.etree.ElementTree as ET

import libsbml

PlotColor = namedtuple("PlotColor", ["is_valid_color", "color"])
FontProperty = namedtuple("FontProperty", ["is_valid_value", "value"])
GlyphProperty = namedtuple("GlyphProperty", ["type", "entity_id"])
BoxDimensions = namedtuple("BoxDimensions",
                           ["x_offset", "y_offset", "width", "height"])
EllipseData = namedtuple("EllipseData",
                         ["x", "y", "rx", "ry", "stroke_width"])

LINE_ENDINGS_STYLE_SHEET = "render-stylesheet_global.xml"

FONT_STYLES = ["none", "normal", "italic"]

ROLES = ["substrate", "product", "sidesubstrate", "sideproduct",
         "modifier", "activator", "inhibitor"]

# The values in these "types" vars are sorted by specificity:
# most specific to least specific

COMPARTMENT_TYPES = ["COMPARTMENTGLYPH", "ANY"]

SPECIES_TYPES = ["SPECIESGLYPH", "ANY"]

TEXT_TYPES = ["TEXTGLYPH", "ANY"]

REACTION_TYPES = ["REACTIONGLYPH", "ANY"]


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
        self.linear_gradients = {}
        self.line_endings = {}
        self.libsbml_line_endings = []
        self.speciesGlyphs = self._createSpeciesGlyphsDirectory()
        self.speciesToGlyphs = self._createSpeciesDirectory()
        self.textToGlyphs = self._createSpeciesTextDirectory()
        self.textGlyphs = self._createTextGlyphsDirectory()
        self.compartmentGlyphs = self._createCompartmentGlyphsDirectory()
        self.compartmentsToGlyphs = self._createCompartmentsDirectory()
        self.reactionGlyphs = self._createReactionGlyphsDirectory()
        self.reactionToGlyphs = self._createReactionsDirectory()
        self.glyphsDirectory = self._createGlyphsDirectory()
        self.findSpeciesReferenceGlyphId = self._createSpeciesReferenceGlyphDirectory()  # noqa

    def _createSpeciesReferenceGlyphDirectory(self,):
        """Create a directory to find the glyph id of a curve, which is a
        "species_reference_glyph_id", based on ("reaction_id", "curve role",
        "species_id").

        Args: None

        Returns: dictionary, keys = ("reaction_id", "curve role",
        "species_id"), values = "species_reference_glyph_id"
        """
        srgDirectory = dict()

        for reaction in self.layout.getListOfReactionGlyphs():
            for srg in reaction.getListOfSpeciesReferenceGlyphs():
                if srg.isSetSpeciesReferenceId():
                    species_id = srg.getSpeciesReferenceId()
                elif srg.isSetSpeciesGlyphId():
                    species_glyph_id = srg.getSpeciesGlyphId()
                    if species_glyph_id in self.speciesGlyphs:
                        species_id = self.speciesGlyphs[species_glyph_id]
                else:
                    species_id = ""
                    raise RuntimeWarning(
                            "Can't create proper species reference glyph key.",
                            "species id = ", species_id)
                srgDirectory[(reaction.getReactionId(), srg.getRoleString(),
                              species_id)] = srg.getId()

        return srgDirectory

    def _createSpeciesDirectory(self,):
        """Create a directory to find the glyph id of a species, based on the
        species_id.

        Args: None

        Returns: dictionary, keys = "species id", values = "species glyph id"
        """
        speciesDirectory = dict()

        for species in self.layout.getListOfSpeciesGlyphs():
            glyph_id = species.getId()
            species_id = species.getSpeciesId()
            speciesDirectory[species_id] = glyph_id

        return speciesDirectory

    def _createSpeciesTextDirectory(self,):
        """Create a directory to find the glyph id of species text, based on
        the species_id.

        Args: None

        Returns: dictionary, keys = "species id",
            values = "species text glyph id"
        """
        speciesTextDirectory = dict()

        for text in self.layout.getListOfTextGlyphs():
            glyph_id = text.getId()
            species_id = self.speciesGlyphs[text.getGraphicalObjectId()]
            speciesTextDirectory[species_id] = glyph_id

        return speciesTextDirectory

    def _createReactionsDirectory(self,):
        """Create a directory to find the glyph id of a reaction, based on the
        reaction_id.

        Args: None

        Returns: dictionary, keys = "reaction id", values = "reaction glyph id"
        """
        reactionsDirectory = dict()

        for reaction in self.layout.getListOfReactionGlyphs():
            glyph_id = reaction.getId()
            reaction_id = self.reactionGlyphs[reaction.getId()]
            reactionsDirectory[reaction_id] = glyph_id

        return reactionsDirectory

    def _createCompartmentsDirectory(self,):
        """Create a directory to find the glyph id of a compartment, based on
        the compartment_id.

        Args: None

        Returns: dictionary, keys = "compartment id",
            values = "compartment glyph id"
        """
        compartmentsDirectory = dict()

        for compartment in self.layout.getListOfCompartmentGlyphs():
            glyph_id = compartment.getId()
            compartment_id = self.compartmentGlyphs[compartment.getId()]
            compartmentsDirectory[compartment_id] = glyph_id

        return compartmentsDirectory

    def _createSpeciesGlyphsDirectory(self,):
        """Create a directory to find the species id based on the species glyph
        id.

        Args: None

        Returns: dictionary, key=species_glyph_id, value=species_id
        """
        speciesGlyphsDirectory = dict()

        for species in self.layout.getListOfSpeciesGlyphs():
            glyph_id = species.getId()
            species_id = species.getSpeciesId()
            speciesGlyphsDirectory[glyph_id] = species_id

        return speciesGlyphsDirectory

    def _createTextGlyphsDirectory(self,):
        """Create a directory to find the species id based on the species text
        glyph id.

        Args: None

        Returns: dictionary, key=species_text_glyph_id, value=species_id
        """
        textDirectory = dict()

        for text in self.layout.getListOfTextGlyphs():
            glyph_id = text.getId()
            species_id = self.speciesGlyphs[text.getGraphicalObjectId()]
            textDirectory[glyph_id] = species_id

        return textDirectory

    def _createCompartmentGlyphsDirectory(self,):
        """Create a directory to find the compartment id based on the
        compartment glyph id.

        Args: None

        Returns: dictionary, key=compartment_glyph_id, value=compartment_id
        """
        compartmentDirectory = dict()

        for compartment in self.layout.getListOfCompartmentGlyphs():
            glyph_id = compartment.getId()
            compartment_id = compartment.getCompartmentId()
            compartmentDirectory[glyph_id] = compartment_id

        return compartmentDirectory

    def _createReactionGlyphsDirectory(self,):
        """Create a directory to find the reaction id based on the reaction
        glyph id.

        Args: None

        Returns: dictionary, key=reaction_glyph_id, value=reaction_id
        """
        reactionDirectory = dict()

        for reaction in self.layout.getListOfReactionGlyphs():
            glyph_id = reaction.getId()
            reaction_id = reaction.getReactionId()
            reactionDirectory[glyph_id] = reaction_id

        return reactionDirectory

    def _createGlyphsDirectory(self,):
        """Create a directory to find the type ("compartment", "reaction",
        "species", or "text") and id based on a glyph id.

        Args: None

        Returns: dictionary, key=glyph_id, value=libsbml_draw.GlyphProperty
        """
        glyphsDirectory = dict()

        for compartment in self.layout.getListOfCompartmentGlyphs():
            glyph_id = compartment.getId()
            compartment_id = compartment.getCompartmentId()
            glyphsDirectory[glyph_id] = GlyphProperty(
                    "compartment",
                    compartment_id)

        for reaction in self.layout.getListOfReactionGlyphs():
            glyph_id = reaction.getId()
            reaction_id = reaction.getReactionId()
            glyphsDirectory[glyph_id] = GlyphProperty("reaction", reaction_id)

        for species in self.layout.getListOfSpeciesGlyphs():
            glyph_id = species.getId()
            species_id = species.getSpeciesId()
            glyphsDirectory[glyph_id] = GlyphProperty("species", species_id)

        for text in self.layout.getListOfTextGlyphs():
            glyph_id = text.getId()
            species_id = self.speciesGlyphs[text.getGraphicalObjectId()]
            glyphsDirectory[glyph_id] = GlyphProperty("text", species_id)

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
                     "x-large", "xx-large"],
            "weight": ["normal", "bold"]
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

    def _collectColorDefinitions(self, render_info):
        """Gets the render color definitions.

        Args:
            render_info(libsbml.Render):

        Returns: dict, keys = color id, values = color value
        """
        color_definitions = {}
        for color_defn in render_info.getListOfColorDefinitions():
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

        elif font_property == "textanchor":
            if property_value == "middle":
                font_property = FontProperty(True, "center")
            elif property_value == "start":
                font_property = FontProperty(True, "left")
            elif property_value == "end":
                font_property = FontProperty(True, "right")
            elif property_value in ("center", "right", "left"):
                font_property = FontProperty(True, property_value)
            else:
                font_property = FontProperty(False, property_value)

        elif font_property == "vtextanchor":
            # flip top, bottom, and baseline since (0,0) is lower-left corner
            # for matplotlib in draw_network.py
            if property_value == "middle":
                font_property = FontProperty(True, "center")
            elif property_value == "top":
                font_property = FontProperty(True, "bottom")
            elif property_value == "bottom":
                font_property = FontProperty(True, "top")
            elif property_value == "baseline":
                font_property = FontProperty(True, "top")
            elif property_value in ("center", "top", "bottom", "baseline",
                                    "center_baseline"):
                font_property = FontProperty(True, property_value)
            else:
                font_property = FontProperty(False, property_value)

        elif font_property == "weight":
            if property_value in self.font_properties[font_property]:
                font_property = FontProperty(True, FONT_STYLES[property_value])
            else:
                font_property = FontProperty(False, property_value)

        else:
            font_property = FontProperty(False, property_value)

        return font_property

    def _collectLinearGradients(self, render_info):
        """Gets the render linear gradient definitions.

        Args:
            render_info(libsbml.Render):

        Returns: dict, keys = linear gradient id,
            values = tuple of (spread_method, list of stop colors)
        """
        linear_gradients = {}

        for linear_gradient in render_info.getListOfGradientDefinitions():

            spread_method = linear_gradient.getSpreadMethodString()

            stop_colors = list()

            for gradient_stop in linear_gradient.getListOfGradientStops():

                gradient_stop_color = self._set_plot_color_and_validity(
                    gradient_stop.getStopColor())

                if gradient_stop_color.is_valid_color:
                    stop_colors.append(gradient_stop_color)

            linear_gradients[linear_gradient.getId()] = (
                    spread_method,
                    stop_colors)

        return linear_gradients

    def _collectLineEndings(self, render_info):
        """Gets the render line ending definitions.

        Args:
            render_info(libsbml.Render):

        Returns: dict, keys = line ending id,
            values = np.array of [x,y] points
        """
        line_endings = {}
        libsbml_line_endings = []

        for line_ending in render_info.getListOfLineEndings():

            libsbml_line_endings.append(line_ending)

            line_ending_id = line_ending.getId()

            bounding_box = line_ending.getBoundingBox()

            box_dimensions = BoxDimensions(
                    bounding_box.getX(),
                    bounding_box.getY(),
                    bounding_box.getWidth(),
                    bounding_box.getHeight())

            enable_rotational_mapping = line_ending.getEnableRotationalMapping()  # noqa

            line_ending_points = []

            element = line_ending.getGroup().getElement(0)

            if element.getElementName() == "polygon":

                for curve in element.getListOfElements():

                    x = self._getAbsoluteValue(curve.getX(),
                                               box_dimensions.width)

                    y = self._getAbsoluteValue(curve.getY(),
                                               box_dimensions.height)

                    line_ending_points.append([x, y])

                line_endings[line_ending_id] = (
                        "polygon",
                        np.array(line_ending_points),
                        box_dimensions,
                        enable_rotational_mapping)

            elif element.getElementName() == "ellipse":

                x = self._getAbsoluteValue(element.getCX(),
                                           box_dimensions.width)

                y = self._getAbsoluteValue(element.getCY(),
                                           box_dimensions.height)

                rx = self._getAbsoluteValue(element.getRX(),
                                            box_dimensions.width)

                ry = self._getAbsoluteValue(element.getRY(),
                                            box_dimensions.height)

                stroke_width = element.getStrokeWidth()

                ellipseData = EllipseData(x, y, rx, ry, stroke_width)

                line_endings[line_ending_id] = (
                        "ellipse",
                        ellipseData,
                        box_dimensions,
                        enable_rotational_mapping)

        return (line_endings, libsbml_line_endings)

    def _getAbsoluteValue(self, element_value, box_dimension):
        """A value can be absolute or relative (%).  This function returns the
        absolute value whether the input is absolute or relative.  In the case
        that the value is relative, the absolute value is computed.

        Args:
            element_value(libsbml.RelAbsVector): an element value, for example,
                the x value for a curve element. x can be absolute or relative.
            box_dimension(one of the dimensions of libsbml_draw.BoxDimensions):
                for example, width or height.
        Returns:
        """
        if (not element_value.isSetAbsoluteValue() and
                not element_value.isSetRelativeValue()):

            abs_value = 0

        elif element_value.isSetRelativeValue():

            abs_value = element_value.getRelativeValue()*box_dimension/100

        elif element_value.isSetAbsoluteValue():

            abs_value = element_value.getAbsoluteValue()

        return abs_value

    def _applyGlobalRenderInformation(self, network):
        """Applies global style render information as specified in the
        roleList (eg. product) or typeList (eg. SPECIESGLYPH).

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

                    bg_color = self._set_plot_color_and_validity(
                       global_render_info.getBackgroundColor())

                    if bg_color.is_valid_color:
                        network.bg_color = bg_color.color

                    self.linear_gradients = self._collectLinearGradients(
                            global_render_info)

                    line_endings_tuple = self._collectLineEndings(
                            global_render_info)

                    self.line_endings = line_endings_tuple[0]
                    self.libsbml_line_endings = line_endings_tuple[1]

                    network.line_endings = self.line_endings
                    network.libsbml_line_endings = self.libsbml_line_endings

                    global_styles = global_render_info.getListOfStyles()

                    compartments_type = dict()
                    nodes_type = dict()
                    node_text_type = dict()
                    reaction_type = dict()
                    role_type = dict()

                    for global_style in global_styles:

                        # collect types which apply to compartments
                        for glyph_type in COMPARTMENT_TYPES:
                            if global_style.isInTypeList(glyph_type):
                                compartments_type[glyph_type] = global_style
                            else:
                                pass
                        # collect types which apply to nodes
                        for glyph_type in SPECIES_TYPES:
                            if global_style.isInTypeList(glyph_type):
                                nodes_type[glyph_type] = global_style
                            else:
                                pass
                        # collect types which apply to node text
                        for glyph_type in TEXT_TYPES:
                            if global_style.isInTypeList(glyph_type):
                                node_text_type[glyph_type] = global_style
                            else:
                                pass
                        # collect types which apply to reactions
                        for glyph_type in REACTION_TYPES:
                            if global_style.isInTypeList(glyph_type):
                                reaction_type[glyph_type] = global_style
                            else:
                                pass
                        # collect roles
                        for role in ROLES:
                            if global_style.isInRoleList(role):
                                role_type[role] = global_style
                            else:
                                pass

                    # update compartments
                    for glyph_type in COMPARTMENT_TYPES:
                        if glyph_type in compartments_type:
                            for compartment in network.compartments.values():
                                self._updateCompartment(
                                        compartment,
                                        compartments_type[glyph_type])
                            break
                        else:
                            pass

                    # update nodes
                    for glyph_type in SPECIES_TYPES:
                        if glyph_type in nodes_type:
                            print("GLOBAL: ", glyph_type)
                            for node in network.nodes.values():
                                print("updating node: ", node.id)
                                self._updateNode(
                                        node,
                                        nodes_type[glyph_type])
                            break
                        else:
                            pass

                    # update node text
                    for glyph_type in TEXT_TYPES:
                        if glyph_type in node_text_type:
                            for node in network.nodes.values():
                                self._updateNodeText(
                                        node,
                                        node_text_type[glyph_type])
                            break
                        else:
                            pass

                    # update reaction curves
                    for reaction in network.reactions.values():
                        for curve in reaction.curves:
                            if curve.role_name.lower() in role_type:
                                self._updateCurve(
                                        curve,
                                        role_type[curve.role_name.lower()])
                            else:
                                for glyph_type in REACTION_TYPES:
                                    if glyph_type in reaction_type:
                                        self._updateCurve(
                                                curve,
                                                reaction_type[curve.role_name.lower()])  # noqa
                                        break
                                    else:
                                        pass

    def _updateCurve(self, curve, render_style):
        """Update the curve attributes by applying the render style found in
        the input SBML file.

        Args:
            curve (libsbml_draw.network.Curve): the curve to update
            render_style (libsbml.LocalStyle or libsbml.GlobalStyle): the style
                to apply to the curve.

        Returns: None
        """
        curve_edge_color = self._set_plot_color_and_validity(
                render_style.getGroup().getStroke())

        curve_edge_width = render_style.getGroup().getStrokeWidth()

        if curve_edge_color.is_valid_color:
            curve.edge_color = curve_edge_color.color
            curve.fill_color = curve_edge_color.color
        else:
            pass

        if curve_edge_width > 0:
            curve.curve_width = curve_edge_width

        curve.endHead = render_style.getGroup().getEndHead()

    def _applyLocalRenderInformation(self, network):
        """Sets values in the model's species (nodes), reactions, and
        compartments by finding the most specific local style that applies.
        Styles can be applied based on an id (of a glyph), role (of a curve),
        or type of glyph (SPECIES, TEXT, REACTION, and COMPARTMENT).

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

                    bg_color = self._set_plot_color_and_validity(
                       local_render_info.getBackgroundColor())

                    if bg_color.is_valid_color:
                        network.bg_color = bg_color.color

                    self.linear_gradients = self._collectLinearGradients(
                            local_render_info)

                    line_endings_tuple = self._collectLineEndings(
                            local_render_info)

                    self.line_endings = line_endings_tuple[0]
                    self.libsbml_line_endings = line_endings_tuple[1]

                    network.line_endings = self.line_endings
                    network.libsbml_line_endings = self.libsbml_line_endings

                local_styles = local_render_info.getListOfStyles()

                # Nodes - assign a style
                for node in network.nodes.values():

                    nodes_type = dict()
                    node_assigned = False
                    glyph_id = self.speciesToGlyphs[node.id]

                    for local_style in local_styles:
                        idList = local_style.getIdList()
                        if idList.size():
                            if local_style.isInIdList(glyph_id):
                                self._updateNode(node, local_style)
                                node_assigned = True
                                break
                        # has type list and no id list
                        elif local_style.getTypeList().size():
                            for node_type in SPECIES_TYPES:
                                if (local_style.isInTypeList(node_type) and
                                        node_type not in nodes_type):
                                    # want the first one found
                                    nodes_type[node_type] = local_style
                        else:
                            pass

                    if not node_assigned:
                        for node_type in SPECIES_TYPES:
                            if node_type in nodes_type:
                                self._updateNode(node, nodes_type[node_type])
                                break

                # Nodes text - assign a style
                for node in network.nodes.values():

                    node_text_type = dict()
                    node_assigned = False
                    glyph_id = self.textToGlyphs[node.id]

                    for local_style in local_styles:
                        idList = local_style.getIdList()
                        if idList.size():
                            if local_style.isInIdList(glyph_id):
                                self._updateNodeText(node, local_style)
                                node_assigned = True
                                break
                        # has type list and no id list
                        elif local_style.getTypeList().size():
                            for node_type in TEXT_TYPES:
                                if (local_style.isInTypeList(node_type) and
                                        node_type not in node_text_type):
                                    # want the first one found
                                    node_text_type[node_type] = local_style
                        else:
                            pass

                    if not node_assigned:
                        for node_type in TEXT_TYPES:
                            if node_type in node_text_type:
                                self._updateNodeText(node,
                                                     nodes_type[node_type])
                                break

                # Compartments - assign a style
                for compartment in network.compartments.values():

                    compartments_type = dict()
                    compartment_assigned = False
                    glyph_id = self.compartmentsToGlyphs[compartment.id]

                    for local_style in local_styles:
                        idList = local_style.getIdList()
                        if idList.size():
                            if local_style.isInIdList(glyph_id):
                                self._updateCompartment(
                                        compartment, local_style)
                                compartment_assigned = True
                                break
                        # has type list and no id list
                        elif local_style.getTypeList().size():
                            for compartment_type in COMPARTMENT_TYPES:
                                if (local_style.isInTypeList(compartment_type)
                                        and compartment_type
                                        not in compartments_type):
                                    # want the first one found
                                    compartments_type[
                                            compartment_type] = local_style
                        else:
                            pass

                    if not compartment_assigned:
                        for compartment_type in COMPARTMENT_TYPES:
                            if compartment_type in compartments_type:
                                self._updateCompartment(
                                        compartment,
                                        compartments_type[compartment_type])
                                break

                # Reactions - assign a style to each curve
                for reaction in network.reactions.values():

                    reactions_type = dict()
                    roles_type = dict()
                    rxn_id_style = None
                    rxn_glyph_id = self.reactionToGlyphs[reaction.id]

                    for curve in reaction.curves:

                        id_key = (reaction.id,
                                  curve.role_name.lower(),
                                  curve.species)

                        if id_key in self.findSpeciesReferenceGlyphId:
                            curve_id = self.findSpeciesReferenceGlyphId[id_key]
                        else:
                            curve_id = None

                        curve_assigned = False

                        for local_style in local_styles:

                            # has idList
                            if local_style.getIdList().size():
                                if local_style.isInIdList(curve_id):
                                    self._updateCurve(curve, local_style)
                                    curve_assigned = True
                                    break
                                elif (local_style.isInIdList(rxn_glyph_id) and
                                        not rxn_id_style):
                                    rxn_id_style = local_style

                            # has roleList
                            elif local_style.getRoleList().size():
                                if (local_style.isInRoleList(
                                        curve.role_name.lower()) and
                                        curve.role_name.lower()
                                        not in roles_type):
                                    # want first one found
                                    roles_type[
                                        curve.role_name.lower()] = local_style

                            # has typeList
                            elif local_style.getTypeList().size():
                                for reaction_type in REACTION_TYPES:
                                    if (local_style.isInTypeList(reaction_type)
                                            and reaction_type
                                            not in reactions_type):
                                        reactions_type[
                                                reaction_type] = local_style

                        if not curve_assigned:
                            # assign based on role
                            if curve.role_name.lower() in roles_type:
                                self._updateCurve(
                                        curve,
                                        roles_type[curve.role_name.lower()])
                            # assign based on rxn id
                            elif rxn_id_style:
                                self._updateCurve(
                                        curve,
                                        rxn_id_style)
                            # assign based on type
                            else:
                                for reaction_type in REACTION_TYPES:
                                    if reaction_type in reactions_type:
                                        self._updateCurve(curve, local_style)
                                        break
                        else:
                            pass

    def _computeRectangleRounding(self, element, nw_element):
        """Computes a value to use in matplotlib for rounding of rectangle
        corners.

        Args:
            element (libsbml.Rectangle): rectangle data from the SBML file
            nw_element (libsbml_draw.network.Node or
                libsbml_draw.network.Compartment): graphical element in the
                network to which the SBML data will be applied.

        Returns: float
        """
        rx = element.getRX()
        ry = element.getRY()

        if rx.isSetAbsoluteValue():
            node_rx = rx.getAbsoluteValue()
        elif rx.isSetRelativeValue():
            node_rx = rx.getRelativeValue()*nw_element.width/100
        else:
            node_rx = 0

        if ry.isSetAbsoluteValue():
            node_ry = ry.getAbsoluteValue()
        elif ry.isSetRelativeValue():
            node_ry = ry.getRelativeValue()*nw_element.height/100
        else:
            node_ry = 0

        rectangle_rounding = (max(node_rx, node_ry) /
                              max(nw_element.width, nw_element.height))

        return rectangle_rounding

    def _updateNode(self, node, render_style):
        """Update the node attributes by applying the render style found in
        the input SBML file.

        Args:
            node (libsbml_draw.network.Node): the node to update
            render_style (libsbml.LocalStyle or libsbml.GlobalStyle): the style
                to apply.

        Returns: None
        """
        render_group = render_style.getGroup()
        node_element = render_group.getElement(0)

        if node_element.isSetFillColor():
            fill_color = node_element.getFillColor()
        else:
            fill_color = render_group.getFillColor()

        node_fill_color = self._set_plot_color_and_validity(
                fill_color)

        if node_element.isSetStroke():
            edge_color = node_element.getStroke()
        else:
            edge_color = render_group.getStroke()

        node_edge_color = self._set_plot_color_and_validity(
                edge_color)

        if node_element.isSetStrokeWidth():
            node_edge_width = node_element.getStrokeWidth()
        else:
            node_edge_width = render_group.getStrokeWidth()

        if node_fill_color.is_valid_color:
            node.fill_color = node_fill_color.color
        else:
            pass

        if node_edge_color.is_valid_color:
                node.edge_color = node_edge_color.color
        else:
            pass

        node.edge_width = node_edge_width

        node_shape = node_element.getElementName()
        self._setShapeData(node_element, node, node_shape)

    def _setShapeData(self, libsbml_element, nw_element, nw_element_shape):
        """Collects the data needed to draw the shape of a node or a
        compartment, and stores it on the node or compartment representation.

        Args:
            libsbml_elemnet (libsbml.Element): a libsbml Rectangle, Polygon,
                or Ellipse
            nw_element (libsbml_draw.model.network.Node or
                libsbml_draw.model.network.Compartment: set the shape data on
                    this element
            nw_element_shape (str): "rectangle", "polygon" or "ellipse"

        Returns: None
        """
        if nw_element_shape == "rectangle":

            nw_element.shape = "round_box"

            nw_element.rectangle_rounding = self._computeRectangleRounding(
                    libsbml_element, nw_element)

        elif nw_element_shape == "polygon":

            nw_element.shape = nw_element_shape

            nw_element.polygon = libsbml_element

            points = []
            codes = []
            types = []

            curve_count = 0

            for curve in libsbml_element.getListOfElements():

                curve_count += 1

                types.append(type(curve))

                if curve.getTypeCode() == libsbml.SBML_RENDER_CUBICBEZIER:

                    if curve_count == 1:
                        raise ValueError(
                                "First Element must be RenderPoint",
                                " not RenderCubicBezier")
                    else:
                        pass

                    codes.append(mplp.Path.CURVE4)
                    codes.append(mplp.Path.CURVE4)
                    codes.append(mplp.Path.CURVE4)

                    points.append([
                            self._getAbsoluteValue(curve.getBasePoint1_x(),
                                                   nw_element.width),
                            self._getAbsoluteValue(curve.getBasePoint1_y(),
                                                   nw_element.height)])
                    points.append([
                            self._getAbsoluteValue(curve.getBasePoint2_x(),
                                                   nw_element.width),
                            self._getAbsoluteValue(curve.getBasePoint2_y(),
                                                   nw_element.height)])
                    points.append([
                            self._getAbsoluteValue(curve.getX(),
                                                   nw_element.width),
                            self._getAbsoluteValue(curve.getY(),
                                                   nw_element.height)])

                elif curve.getTypeCode() == libsbml.SBML_RENDER_POINT:

                    if curve_count == 1:
                        codes.append(mplp.Path.MOVETO)
                    else:
                        codes.append(mplp.Path.LINETO)

                    points.append([
                            self._getAbsoluteValue(curve.getX(),
                                                   nw_element.width),
                            self._getAbsoluteValue(curve.getY(),
                                                   nw_element.height)])

                else:
                    pass

            nw_element.polygon_points = points
            nw_element.polygon_codes = codes

        elif nw_element_shape == "ellipse":
            nw_element.shape = nw_element_shape

        else:
            pass

    def _updateNodeText(self, node, render_style):
        """Update the node text attributes by applying the render style found
        in the input SBML file.

        Args:
            node (libsbml_draw.network.Node): the node to update
            render_style (libsbml.LocalStyle or libsbml.GlobalStyle): the style
                to apply.

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

        node_horizontal_alignment = self._set_font_property(
                "textanchor",
                render_style.getGroup().getTextAnchorAsString())

        node_vertical_alignment = self._set_font_property(
                "vtextanchor",
                render_style.getGroup().getVTextAnchorAsString())

        node_weight = self._set_font_property(
                "weight",
                render_style.getGroup().getFontWeight())

        if node_font_color.is_valid_color:
            node.font_color = node_font_color.color

        if node_font_style.is_valid_value:
            node.font_style = node_font_style.value

        if node_font_size.is_valid_value:
            node.font_size = node_font_size.value

        if node_font_family.is_valid_value:
            node.font_family = node_font_family.value

        if node_horizontal_alignment.is_valid_value:
            node.text_anchor = node_horizontal_alignment.value

        if node_vertical_alignment.is_valid_value:
            node.vtext_anchor = node_vertical_alignment.value

        if node_weight.is_valid_value:
            node.weight = node_weight.value

    def _updateCompartment(self, compartment, render_style):
        """Update the compartment attributes by applying the render style found
        in the input SBML file.

        Args:
            compartment (libsbml_draw.network.Compartment): the compartment to
                update
            render_style (libsbml.LocalStyle or libsbml.GlobalStyle): the style
                to apply.

        Returns: None
        """
        compartment_element = render_style.getGroup().getElement(0)

        compartment_edge_color = self._set_plot_color_and_validity(
                compartment_element.getStroke())

        compartment_fill_color = self._set_plot_color_and_validity(
                compartment_element.getFillColor())

        compartment_line_width = compartment_element.getStrokeWidth()  # noqa

        if compartment_edge_color.is_valid_color:
            compartment.edge_color = compartment_edge_color.color
        else:
            pass

        if compartment_fill_color.is_valid_color:
            compartment.fill_color = compartment_fill_color.color
        else:
            pass

        if compartment_line_width > 0:
            compartment.line_width = compartment_line_width

        compartment_shape = compartment_element.getElementName()
        self._setShapeData(compartment_element, compartment, compartment_shape)

    def _getSBMLRenderTextAnchor(self, text_anchor, alignment_direction):
        """Returns the text anchor value needed for libsbml_draw.draw_network
        and matplotlib.

        Args:
            text_anchor (str): the value for the text anchor, eg. "top"
            alignment_direction (str): "horizontal" or "vertical"

        Returns:
        """
        if alignment_direction == "horizontal":
            if text_anchor == "center":
                return "middle"
            elif text_anchor == "left":
                return "start"
            elif text_anchor == "right":
                return "end"
            else:
                return "middle"
        elif alignment_direction == "vertical":
            # the plotting in draw_network has (0,0) in lower-left corner
            # so flip here
            if text_anchor == "center":
                return "middle"
            elif text_anchor == "top":
                return "bottom"
            elif text_anchor == "bottom":
                return "top"
            elif text_anchor == "baseline":
                return "top"
            else:
                return "middle"
        else:
            raise ValueError("Invalid value for alignment_direction: ",
                             alignment_direction)

    def _getLineEndingsFromStyleSheet(self,):
        """Experimental function to get line endings from an SBML file.  Makes
        use of Python's ElementTree.

        Args: None

        Returns: dictionary, keys=line endings id, values=string of XML line
            ending block
        """
        line_endings = {}

        stylesheet_file_name = "LineEnding_styles.xml"
        stylesheet_file = Path(pkg_resources.resource_filename("libsbml_draw",
                               "model/data/" + stylesheet_file_name))

        tree = ET.parse(stylesheet_file)

        nns_le = "lineEnding"

        root = tree.getroot()

        for le in root.findall(nns_le):
            line_endings[le.attrib["id"]] = ET.tostring(le, encoding="unicode")

        return line_endings

    def _addLocalStylesRenderInformation(self, local_render_info, network):
        """Add a LocalStyle for each compartment, node, node text, and reaction
        curve.

        Args:
            local_render_info(libsbml.Render): SBML local render info
            network (libsbml_draw.model.Network): the model's network

        Returns: None
        """
        local_render_info.setId("localRenderInfo")
        local_render_info.setName("Render Information")

        if network.libsbml_line_endings:

            for line_ending in network.libsbml_line_endings:

                result = local_render_info.addLineEnding(line_ending)

                if result != libsbml.LIBSBML_OPERATION_SUCCESS:
                    raise RuntimeWarning("libsbml could not add line ending",
                                         result)
        else:
            # read line endings from style sheet?
            pass

        for node in network.nodes.values():
            # LocalStyle, RenderGroup

            # node body
            style = local_render_info.createStyle("")
            style.getGroup().setFillColor(node.fill_color)
            style.getGroup().setStroke(node.edge_color)
            style.getGroup().setStrokeWidth(node.edge_width)
            style.addId(self.speciesToGlyphs[node.id])

            if node.shape == "rectangle" or node.shape == "round_box":
                rectangle = style.getGroup().createRectangle()
                rectangle.setX(libsbml.RelAbsVector("000%"))
                rectangle.setY(libsbml.RelAbsVector("000%"))
                rectangle.setWidth(libsbml.RelAbsVector("100%"))
                rectangle.setHeight(libsbml.RelAbsVector("100%"))
                rectangle.setFill(node.fill_color)
                rectangle.setStroke(node.edge_color)
                rectangle.setStrokeWidth(node.edge_width)
#                rectangle.setRX(node.rectangle_rounding)
#                rectangle.setRY(node.rectangle_rounding)
            elif node.shape == "ellipse":
                ellipse = style.getGroup().createEllipse()
                ellipse.setCX(libsbml.RelAbsVector("000%"))
                ellipse.setCY(libsbml.RelAbsVector("000%"))
                ellipse.setRX(libsbml.RelAbsVector("100%"))
                ellipse.setRY(libsbml.RelAbsVector("100%"))
                ellipse.setFill(node.fill_color)
                ellipse.setStroke(node.edge_color)
                ellipse.setStrokeWidth(node.edge_width)

            elif node.shape == "polygon":
                node.polygon.setFill(node.fill_color)
                node.polygon.setStroke(node.edge_color)
                node.polygon.setStrokeWidth(node.edge_width)
                result = style.getGroup().addElement(node.polygon)
                if result != libsbml.LIBSBML_OPERATION_SUCCESS:
                    raise RuntimeWarning(
                        "Could not add polygon to local style for node: ",
                        node.id)
            else:
                raise ValueError("invalid node shape: ", node.shape)

            # node text
            style = local_render_info.createStyle("")
            style.getGroup().setFontFamily(node.font_family)
            style.getGroup().setFontSize(libsbml.RelAbsVector(node.font_size))
            style.getGroup().setFontWeight(node.font_weight)
            style.getGroup().setTextAnchor(
                    self._getSBMLRenderTextAnchor(
                            node.text_anchor, "horizontal"))
            style.getGroup().setVTextAnchor(
                    self._getSBMLRenderTextAnchor(
                            node.vtext_anchor, "vertical"))
            if node.font_style == "italic":
                style.getGroup().setFontStyle(libsbml.FONT_STYLE_ITALIC)
            else:  # "normal"
                style.getGroup().setFontStyle(libsbml.FONT_STYLE_NORMAL)
            style.getGroup().setStroke(node.font_color)
            style.addId(self.textToGlyphs[node.id])

        # curves
        for reaction in network.reactions.values():
            rxn_glyph_id = self.reactionToGlyphs[reaction.id]
            for curve in reaction.curves:
                curve_key = (reaction.id,
                             curve.role_name.lower(),
                             curve.species)
                if curve_key in self.findSpeciesReferenceGlyphId:
                    curve_glyph_id = self.findSpeciesReferenceGlyphId[
                        curve_key]
                else:
                    curve_glyph_id = None

                style = local_render_info.createStyle("")
                style.getGroup().setStroke(curve.edge_color)
                style.getGroup().setFillColor(curve.fill_color)
                style.getGroup().setStrokeWidth(curve.curve_width)

                if curve.endHead:
                    style.getGroup().setEndHead(curve.endHead)
                else:
                    style.getGroup().setEndHead(curve.role_name.lower())

                if curve_glyph_id:
                    style.addId(curve_glyph_id)
                else:
                    style.addId(rxn_glyph_id)

        # compartments
        for compartment in network.compartments.values():
            style = local_render_info.createStyle("")
            style.getGroup().setStroke(compartment.edge_color)
            style.getGroup().setFillColor(compartment.fill_color)
            style.getGroup().setStrokeWidth(compartment.line_width)
            style.addId(self.compartmentsToGlyphs[compartment.id])

            if (compartment.shape == "rectangle" or
                    compartment.shape == "round_box"):
                rectangle = style.getGroup().createRectangle()
                rectangle.setX(libsbml.RelAbsVector("000%"))
                rectangle.setY(libsbml.RelAbsVector("000%"))
                rectangle.setWidth(libsbml.RelAbsVector("100%"))
                rectangle.setHeight(libsbml.RelAbsVector("100%"))
                rectangle.setFill(compartment.fill_color)
                rectangle.setStroke(compartment.edge_color)
                rectangle.setStrokeWidth(compartment.line_width)
#                rectangle.setRX(compartment.rectangle_rounding)
#                rectangle.setRY(compartment.rectangle_rounding)

        # create product style
#        style = local_render_info.createStyle("")
#        style.addRole("product")
#        style.getGroup().setEndHead("product")

    def addRenderInformation(self, network):
        """Add render information to the model as Local Style render
        information.  If local render information already exists, remove it,
        and add new entries for the compartments (if any), nodes, node text,
        and reaction curves.

        Args:
            network (libsbml_draw.model.Network): the model's network

        Returns: None
        """
        # add local styles
        if (self.rPlugin is not None and
                self.rPlugin.getNumLocalRenderInformationObjects() > 0):

            # remove any existing local render information
            for local_index in range(
                    self.rPlugin.getNumLocalRenderInformationObjects()):
                local_render_info = \
                    self.rPlugin.removeLocalRenderInformation(local_index)

            # add local_styles to represent the render info
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

            print("Adding local styles render info")

            self._addLocalStylesRenderInformation(local_render_info, network)

    def _readLineEndingsStyleSheet(self, network):
        """Read in a default line endings style sheet, and assign it to the
        model's network.

        Args:
            network (libsbml_draw.network.Network): the model's network

        Return: None
        """
        LINE_ENDINGS_FILE = Path(pkg_resources.resource_filename(
                                 "libsbml_draw",
                                 "model/data/" + LINE_ENDINGS_STYLE_SHEET))

        doc = libsbml.readSBMLFromFile(str(LINE_ENDINGS_FILE))
        model = doc.getModel()
        layout_plugin = model.getPlugin("layout")
        # layout = layout_plugin.getLayout(0) if (
        #    layout_plugin and layout_plugin.getNumLayouts() > 0) else None
        # SBasePlugin, RenderLayoutPlugin
        # rPlugin = layout.getPlugin("render") if layout else None
        # SBasePlugin, RenderListOfLayoutsPlugin
        render_plugin = layout_plugin.getListOfLayouts(
            ).getPlugin("render") if layout_plugin else None

        if (render_plugin and
                render_plugin.getNumGlobalRenderInformationObjects() > 0):

            for global_render_info in \
                    render_plugin.getListOfGlobalRenderInformation():

                if global_render_info:

                    line_endings_tuple = self._collectLineEndings(
                            global_render_info)

                    network.stylesheet_line_endings = line_endings_tuple[0]

                    network.stylesheet_libsbml_line_endings = line_endings_tuple[1]  # noqa

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
        self._readLineEndingsStyleSheet(network)
