import unittest
import unittest
import site, os

from .add_to_path import add_to_path

add_to_path()

import ctypes
from libsbml_draw import SBMLlayout, sbnw
from tests.model_strings import compartment_model


class TestSBNWCAPIModelAsArg(unittest.TestCase):

    def setUp(self) -> None:
        self.sbml = compartment_model
        self.h_model = sbnw.loadSBMLString(self.sbml)
        self.h_layout_info = sbnw.processLayout(self.h_model)
        self.h_network = sbnw.getNetworkp(self.h_layout_info)
        self.h_canvas = sbnw.getCanvasp(self.h_layout_info)

    def test_test_load_sbnw(self):
        lib = sbnw.load_sbnw()
        self.assertIsInstance(lib, ctypes.CDLL)

    def test_test_getCurrentLibraryVersion(self):
        expected = '1.0.0'
        actual = sbnw.getCurrentLibraryVersion()
        self.assertEqual(expected, actual)

    def eval_type_via_class_name(self, type, obj):
        expected = type
        actual = obj.__class__.__name__
        self.assertEqual(expected, actual)

    def test_getCanvasp(self):
        actual = sbnw.getCanvasp(self.h_layout_info)
        self.eval_type_via_class_name('LP_Canvas', actual)

    def test_canvas_getWidth(self):
        expected = 1024
        actual = sbnw.canvas_getWidth(self.h_canvas)
        self.assertEqual(expected, actual)

    def test_canvas_getHeight(self):
        expected = 1024
        actual = sbnw.canvas_getHeight(self.h_canvas)
        self.assertEqual(expected, actual)

    def test_getSBMLwithLayoutStr(self):
        """
        What is this supposed to return? If this:
          <annotation>
          <layout:listOfLayouts xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:layout="http://projects.eml.org/bcb/sbml/level2">
            <layout:layout layout:id="Graphfab_Layout">
              <layout:dimensions layout:width="1024" layout:height="1024"/>
            </layout:layout>
          </layout:listOfLayouts>
        Then we have it and th eproblem lies with saving the render information. If not
        we still have a problem

        Returns:

        """
        actual=sbnw.getSBMLwithLayoutStr(self.h_model, self.h_layout_info, True)
        self.assertTrue(False)

    def test_loadSBMLString(self):
        actual = sbnw.loadSBMLString(self.sbml)
        print(actual)
        self.eval_type_via_class_name('int', actual)

    def test_writeSBML(self):
        # actual = sbnw.writeSBML(filename, self.h_sbml_model)
        self.assertTrue(False)

    def test_writeSBMLwithLayout(self):
        # actual = sbnw.writeSBMLwithLayout(filename, model, layout)
        self.assertTrue(False)

    def test_getLastError(self):
        expected = b''
        actual = sbnw.getLastError()
        self.assertEqual(expected, actual)

    def test_isLayoutSpecified(self):
        expected = False
        actual = sbnw.isLayoutSpecified(self.h_network)
        self.assertEqual(expected, actual)

    def test_processLayout(self):
        actual = sbnw.processLayout(self.h_model)
        self.eval_type_via_class_name('LP_LayoutInfo')

    def test_randomizeLayout(self):
        actual = sbnw.randomizeLayout(self.h_layout_info)
        self.assertTrue(False)

    def test_doLayoutAlgorithm(self):
        # actual = sbnw.doLayoutAlgorithm(layout_options, self.h_layout_info)
        self.assertTrue(False)

    def test_SBMLModel_newp(self):
        actual = sbnw.SBMLModel_newp()
        self.assertIsInstance(actual, int)

    def test_getNetworkp(self):
        actual = sbnw.getNetworkp(self.h_layout_info)
        self.assertIsInstance(actual, int)

    def test_nw_getNodep(self):
        actual = sbnw.nw_getNodep(self.h_network, 0)
        self.assertIsInstance(actual, int)

    # def test_nw_getNumCompartments(self):
    #     actual = sbnw.nw_getNumCompartments(self.h_network)
    #
    # def test_nw_getNumNodes(self):
    #     actual = sbnw.nw_getNumNodes(self.h_network)
    #
    # def test_nw_getNumRxns(self):
    #     actual = sbnw.nw_getNumRxns(self.h_network)
    #
    # def test_nw_getReactionp(self):
    #     actual = sbnw.nw_getReactionp(self.h_network, reaction_index)
    #
    # def test_nw_newAliasNodep(self):
    #     actual = sbnw.nw_newAliasNodep(self.h_network, h_node)
    #
    # def test_nw_getAliasInstancep(self):
    #     actual = sbnw.nw_getAliasInstancep(self.h_network, h_node, alias_index)
    #
    # def test_nw_getNumAliasInstances(self):
    #     actual = sbnw.nw_getNumAliasInstances(self.h_network, h_node)
    #
    # def test_nw_recenterJunctions(self):
    #     actual = sbnw.nw_recenterJunctions(self.h_network)
    #
    # def test_nw_rebuildCurves(self):
    #     actual = sbnw.nw_rebuildCurves(self.h_network)
    #
    # def test_node_getAttachedCurves(self):
    #     actual = sbnw.node_getAttachedCurves(h_node, self.h_network)
    #
    # def test_node_getCentroid(self):
    #     actual = sbnw.node_getCentroid(h_node)
    #
    # def test_node_setCentroid(self):
    #     actual = sbnw.node_setCentroid(h_node, point)
    #
    # def test_node_getHeight(self):
    #     actual = sbnw.node_getHeight(h_node)
    #
    # def test_node_setHeight(self):
    #     actual = sbnw.node_setHeight(h_node, height)
    #
    # def test_node_getWidth(self):
    #     actual = sbnw.node_getWidth(h_node)
    #
    # def test_node_setWidth(self):
    #     actual = sbnw.node_setWidth(h_node, width)
    #
    # def test_node_getName(self):
    #     actual = sbnw.node_getName(h_node)
    #
    # def test_node_getID(self):
    #     actual = sbnw.node_getID(h_node)
    #
    # def test_node_isLocked(self):
    #     actual = sbnw.node_isLocked(h_node)
    #
    # def test_node_lock(self):
    #     actual = sbnw.node_lock(h_node)
    #
    # def test_node_unlock(self):
    #     actual = sbnw.node_unlock(h_node)
    #
    # def test_node_make_alias(self):
    #     actual = sbnw.node_make_alias(h_node, self.h_network)
    #
    # def test_node_isAliased(self):
    #     actual = sbnw.node_isAliased(h_node)
    #
    # def test_reaction_getNumCurves(self):
    #     actual = sbnw.reaction_getNumCurves(h_reaction)
    #
    # def test_reaction_getNumSpec(self):
    #     actual = sbnw.reaction_getNumSpec(h_reaction)
    #
    # def test_reaction_getID(self):
    #     actual = sbnw.reaction_getID(h_reaction)
    #
    # def test_reaction_getCentroid(self):
    #     actual = sbnw.reaction_getCentroid(h_reaction)
    #
    # def test_reaction_getCurvep(self):
    #     actual = sbnw.reaction_getCurvep(h_reaction, curve_index)
    #
    # def test_getCurveCPs(self):
    #     actual = sbnw.getCurveCPs(h_curve)
    #
    # def test_curve_getRole(self):
    #     actual = sbnw.curve_getRole(h_curve)
    #
    # def test_fit_to_window(self):
    #     actual = sbnw.fit_to_window(self.h_layout_info, left, top, right, bottom)
    #
    # def test_arrowheadSetStyle(self):
    #     actual = sbnw.arrowheadSetStyle(h_role, style)
    #
    # def test_arrowheadGetStyle(self):
    #     actual = sbnw.arrowheadGetStyle(h_role)
    #
    # def test_arrowheadNumStyles(self):
    #     actual = sbnw.arrowheadNumStyles()
    #
    # def test_arrowheadStyleGetNumVerts(self):
    #     actual = sbnw.arrowheadStyleGetNumVerts(style)
    #
    # def test_arrowheadStyleGetVert(self):
    #     actual = sbnw.arrowheadStyleGetVert(style, vertex_number)
    #
    # def test_nw_getCompartmentp(self):
    #     actual = sbnw.nw_getCompartmentp(self.h_network, compartment_index)
    #
    # def test_compartment_getMinCorner(self):
    #     actual = sbnw.compartment_getMinCorner(h_compartment)
    #
    # def test_compartment_getMaxCorner(self):
    #     actual = sbnw.compartment_getMaxCorner(h_compartment)
    #
    # def test_compartment_getHeight(self):
    #     actual = sbnw.compartment_getHeight(h_compartment)
    #
    # def test_compartment_getWidth(self):
    #     actual = sbnw.compartment_getWidth(h_compartment)
    #
    # def test_compartment_getID(self):
    #     actual = sbnw.compartment_getID(h_compartment)
    #
    # def test_reaction_hasSpec(self):
    #     actual = sbnw.reaction_hasSpec(h_reaction, h_species)
    #
    # def test_reaction_recenter(self):
    #     actual = sbnw.reaction_recenter(h_reaction)
