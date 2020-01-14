import site

site.addsitedir('../src/python')
import unittest
from pathlib import Path
import os
import pkg_resources
from libsbml_draw.model.sbml_layout import SBMLlayout
from .model_strings import model_xml

class TestAttributes(unittest.TestCase):

    def setUp(self) -> None:
        self.sl = SBMLlayout(model_xml, applyRender=True)

    def testNodeFontSize(self):
        # default font size
        assert self.sl.getNodeFontSize("S0") == 10
        self.sl.setNodeFontSize("S0", 24)
        # self.sl.drawNetwork()
        self.assertEqual(24, self.sl.getNodeFontSize("S0"))

    def testRegenerateLayout(self):
        """
        Could implement __eq__ etc. to recognize the location of vertices
        but might be overkill. Otherwise, I don't know how to test this.
        Returns:

        """
        pass

    def test_aliasNode(self):
        """
        Model doesn't has aliasNodes, as far as I can tell. Not sure.
        Returns:

        """
        print(self.sl.aliasNode("S0"))
        assert True is False

    def test_getArrowheadNumStyles(self):
        expected = 8
        actual = self.sl.getArrowheadNumStyles()
        self.assertEqual(expected, actual)

    def test_getArrowheadNumVerts(self):
        """
        Actual value for int argument of 1 2 and 3
        all returns 4. But there are 6 arrows in the
        diagram so I'm not sure what this is doing.
        Returns:

        """
        actual = self.sl.getArrowheadNumVerts(3)
        expected = 4
        self.sl.drawNetwork()
        print(actual)

    def test_getNumberOfRoles(self):
        expected = 7
        actual = self.sl.getNumberOfRoles()
        self.assertEqual(expected, actual)

    def test_getArrowheadStyle(self):
        expected = 1
        actual = self.sl.getArrowheadStyle(1)  # must be between 1 and 7
        self.assertEqual(expected, actual)

    def test_setArrowheadStyle(self):
        """
        Changing the arrow head style does not do anything
        Returns:

        """
        expected = 1
        self.sl.setArrowheadStyle(role=1, style=3)
        self.sl.regenerateLayout()
        self.sl.drawNetwork()
        # flag to mark this test as broken, since its not clear what the true answer should be
        assert True == False
        # self.assertEqual(expected, actual)

    def test_getArrowheadScale(self):
        expected = 15
        actual = self.sl.getArrowheadScale(1)
        self.assertEqual(expected, actual)

    def test_setArrowheadScale(self):
        expected = 50
        self.sl.setArrowheadScale(role=1, arrowhead_scale=expected)
        actual = self.sl.getArrowheadScale(1)
        # self.sl.drawNetwork()
        self.assertEqual(expected, actual)

    def test_getArrowheadVert(self):
        obj = self.sl.getArrowheadVert(style=1, vertex_number=2)
        expected = (-1.0, 0.0)
        actual = (obj.x, obj.y)
        self.assertEqual(expected, actual)

    def test_setArrowheadVert(self):
        """
        No setter exists
        Returns:

        """
        pass

    def test_getBoundarySpeciesIds(self):
        expected = ['S7']
        actual = self.sl.getBoundarySpeciesIds()
        self.assertEqual(expected, actual)

    def test_getCompartmentIds(self):
        expected = 'default_compartment'
        actual = self.sl.getCompartmentIds()
        self.assertEqual(expected, actual)

    def test_getCompartmentEdgeColor(self):
        """
        Test relies on getCompartmentIds which doesn't work
        Returns:

        """
        # print(self.sl.getCompartmentIds())
        print(self.sl.getCompartmentEdgeColor('default_compartment'))

    def test_getCompartmentFillColor(self):
        print(self.sl.getCompartmentFillColor('default_compartment'))

    def test_getCompartmentLineWidth(self):
        print(self.sl.getCompartmentLineWidth('default_compartment'))

    def test_getFloatingSpeciesIds(self):
        expected = ['S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6']  # S7 is a boundary condition id
        actual = self.sl.getFloatingSpeciesIds()
        self.assertEqual(expected, actual)

    def test_getNodeIds(self):
        expected = ['S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7']
        actual = self.sl.getNodeIds()
        self.assertEqual(expected, actual)

    def test_getIsNodeAliased(self):
        # aliasing means using clones of nodes for a species.
        self.sl.aliasNode('S4')  # replaces S4 with S4_0, S4_1 etc.
        self.assertTrue(self.sl.getIsNodeAliased('S4_1'))

    def test_getIsNodeLocked(self):
        """
        This test doesn't test much since I
        Returns:

        """
        self.sl.lockNode('S2')
        self.assertTrue(self.sl.getIsNodeLocked('S2'))

    def test_getLayoutAlgorithmOptions(self):
        dct = {}
        alg_options = self.sl.getLayoutAlgorithmOptions()
        dct['autobary'] = alg_options.autobary
        dct['baryx'] = alg_options.baryx
        dct['baryy'] = alg_options.baryy
        dct['gravity'] = alg_options.gravity
        dct['k'] = alg_options.k
        dct['padding'] = alg_options.padding
        expected = {'autobary': 1, 'baryx': 500.0, 'baryy': 500.0, 'gravity': 0.0, 'k': 20.0, 'padding': 20.0}
        actual = dct
        self.assertEqual(expected, actual)

    def test_getNetworkBackgroundColor(self):
        expected = '#ffffff'
        actual = self.sl.getNetworkBackgroundColor()
        self.assertEqual(expected, actual)

    def test_setNetworkBackgroundColor(self):
        expected = 'blue'
        self.sl.setNetworkBackgroundColor(expected)
        # self.sl.drawNetwork() // this was manually checked, and works
        actual = self.sl.getNetworkBackgroundColor()
        self.assertEqual(expected, actual)

    def test_getNodeCentroid(self):
        expectd = (30.464084888166553, 281.84839361341085)
        actual = self.sl.getNodeCentroid('S1')
        self.assertEqual(expectd, actual)

    def test_getNodeColor(self):
        expected = '#c9e0fb'
        actual = self.sl.getNodeColor('S1')
        self.assertEqual(expected, actual)

    def test_setNodeColor(self):
        expected = 'green'
        self.sl.setNodeColor('S1', expected)
        actual = self.sl.getNodeColor('S1')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeEdgeColor(self):
        expected = '#0000ff'
        actual = self.sl.getNodeEdgeColor('S1')
        self.assertEqual(expected, actual)

    def test_setNodeEdgeColor(self):
        expected = 'green'
        self.sl.setNodeEdgeColor('S1', expected)
        actual = self.sl.getNodeEdgeColor('S1')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeEdgeWidth(self):
        expected = 1
        actual = self.sl.getNodeEdgeWidth('S1')
        self.assertEqual(expected, actual)

    def test_setNodeEdgeWidth(self):
        expected = 4
        self.sl.setNodeEdgeWidth('S1', expected)
        actual = self.sl.getNodeEdgeWidth('S1')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeFillColor(self):
        expected = '#c9e0fb'
        actual = self.sl.getNodeFillColor('S1')
        self.assertEqual(expected, actual)

    def test_setNodeFillColor(self):
        expected = '#ff0000ff'
        self.sl.setNodeFillColor('S1', expected)
        actual = self.sl.getNodeFillColor('S1')
        self.sl.drawNetwork()  # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeFontColor(self):
        expected = '#000000'
        actual = self.sl.getNodeFontColor('S1')
        self.assertEqual(expected, actual)

    def test_setNodeFillColor(self):
        expected = '#ff0000ff'
        self.sl.setNodeFontColor('S1', expected)
        actual = self.sl.getNodeFontColor('S1')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeFontFamily(self):
        expected = 'Arial'
        actual = self.sl.getNodeFontFamily('S1')
        self.assertEqual(expected, actual)

    def test_setNodeFontFamily(self):
        expected = 'Times New Roman'
        self.sl.setNodeFontFamily('S1', expected)
        actual = self.sl.getNodeFontFamily('S1')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeFontName(self):
        expected = 'Arial'
        actual = self.sl.getNodeFontName('S1')
        self.assertEqual(expected, actual)

    def test_setNodeFontName(self):
        expected = 'Times New Roman'
        self.sl.setNodeFontName('S1', expected)
        actual = self.sl.getNodeFontName('S1')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeFontSize(self):
        expected = 10
        actual = self.sl.getNodeFontSize('S1')
        self.assertEqual(expected, actual)

    def test_setNodeFontSize(self):
        expected = 14
        self.sl.setNodeFontSize('S1', expected)
        actual = self.sl.getNodeFontSize('S1')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeFontStyle(self):
        expected = 'normal'
        actual = self.sl.getNodeFontStyle('S1')
        self.assertEqual(expected, actual)

    def test_setNodeFontSize(self):
        """
        No support for setting the node font size
        Returns:

        """
        pass
        # expected = 'large'
        # self.sl.setNodeStyle('S1', expected)
        # actual = self.sl.getNodeStyle('S1')
        # self.sl.drawNetwork() # manually checked and is working correctly
        # self.assertEqual(expected, actual)

    def test_getNodeFontWeight(self):
        expected = 'normal'
        actual = self.sl.getNodeFontWeight('S1')
        self.assertEqual(expected, actual)

    def test_setNodeFontWeight(self):
        expected = 'bold'
        self.sl.setNodeFontWeight('S1', expected)
        actual = self.sl.getNodeFontWeight('S1')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeHeight(self):
        expected = 20.0
        actual = self.sl.getNodeHeight('S1')
        self.assertEqual(expected, actual)

    def test_setNodeHeight(self):
        """
        No support for setting the node height
        Returns:

        """
        pass
        # expected = 50.0
        # self.sl.setNode('S1', expected)
        # actual = self.sl.getNodeHeight('S1')
        # self.sl.drawNetwork() # manually checked and is working correctly
        # self.assertEqual(expected, actual)

    def test_getNodeKeywordIds(self):
        """
        unsure of functionality to test
        Returns:

        """
        expected = 20.0
        actual = self.sl.getNodeKeywordIds('S1')
        self.assertTrue(False)  # to flag this test

    def test_getNodeLowerLeftPoint(self):
        expected = [10.464084888166553, 271.84839361341085]
        actual = self.sl.getNodeLowerLeftPoint('S1')
        self.assertEqual(expected, actual)

    def test_getNodeName(self):
        expected = 'S1'
        actual = self.sl.getNodeName('S1')
        self.assertEqual(expected, actual)

    def test_getNodeTextAnchor(self):
        expected = 'center'
        actual = self.sl.getNodeTextAnchor('S1')
        self.assertEqual(expected, actual)

    def test_setNodeTextAnchor(self):
        """
        The roles of left and right have been reversed.
        Returns:

        """
        expected = 'right'
        self.sl.setNodeTextAnchor('S1', 'left')
        actual = self.sl.getNodeTextAnchor('S1')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getVNodeTextAnchor(self):
        expected = 'center'
        actual = self.sl.getNodeVTextAnchor('S1')
        self.assertEqual(expected, actual)

    def test_setVNodeTextAnchor(self):
        expected = 'bottom'  # roles are again reversed
        self.sl.setNodeVTextAnchor('S1', 'top')
        actual = self.sl.getNodeVTextAnchor('S1')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeWidth(self):
        expected = 40.0
        actual = self.sl.getNodeWidth('S1')
        self.assertEqual(expected, actual)

    def test_getNumberOfCompartments(self):
        expected = 1
        actual = self.sl.getNumberOfCompartments()
        self.assertEqual(expected, actual)

    def test_getNumberOfNodes(self):
        expected = 8
        actual = self.sl.getNumberOfNodes()
        self.assertEqual(expected, actual)

    def test_getNumberOfReactions(self):
        expected = 20
        actual = self.sl.getNumberOfReactions()
        self.assertEqual(expected, actual)

    def test_getNumberOfRoles(self):
        expected = 7
        actual = self.sl.getNumberOfRoles()
        self.assertEqual(expected, actual)

    def test_getReactionIds(self):
        expected = ['_J0', '_J1', '_J2', '_J3', '_J4', '_J5', '_J6', '_J7', '_J8', '_J9', '_J10', '_J11', '_J12',
                    '_J13', '_J14', '_J15', '_J16', '_J17', '_J18', '_J19']
        actual = self.sl.getReactionIds()
        self.assertEqual(expected, actual)

    def test_getReactionBezierPoints(self):
        points = self.sl.getReactionBezierPoints('_J0')
        expected_start = (30.292040531605835, 261.3818950449853)
        expected_end = (8.42004407743616, 177.23493978456554)
        start = points[0].start
        end = points[0].end
        self.assertEqual(expected_start, start)
        self.assertEqual(expected_end, end)


    def test_getReactionCentroid(self):
        actual = (8.42004407743616, 177.23493978456554)
        expected = self.sl.getReactionCentroid('_J0')
        self.assertEqual(expected, actual)

    def test_getReactionCurveWidth(self):
        expected = ('S1', 'SUBSTRATE', 3)
        curve = self.sl.getReactionCurveWidth('_J0')
        actual = curve[0]
        self.assertEqual(expected, actual)

    def test_getReactionEdgeColor(self):
        expected = '#0000ff'
        reaction = self.sl.getReactionEdgeColor('_J0')
        actual = reaction[0][2]
        self.assertEqual(expected, actual)

    def test_setReactionEdgeColor(self):
        expected = '#c9e0fbff'
        self.sl.setReactionEdgeColor('_J0', expected)
        reaction = self.sl.getReactionEdgeColor('_J0')
        actual = reaction[0][2]
        self.assertEqual(expected, actual)

    def test_getReactionFillColor(self):
        expected = '#0000ff'
        reaction = self.sl.getReactionFillColor('_J0')
        actual = reaction[0][2]
        self.assertEqual(expected, actual)

    def test_setReactionFillColor(self):
        expected = '#c9e0fbff'
        self.sl.setReactionFillColor('_J0', expected)
        reaction = self.sl.getReactionFillColor('_J0')
        actual = reaction[0][2]
        self.assertEqual(expected, actual)

    def test_getSBMLString(self):
        print(self.sl.getSBMLString())

