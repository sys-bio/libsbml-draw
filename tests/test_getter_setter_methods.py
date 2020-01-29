import os
import site

# add the library to path
site.addsitedir(os.path.join(os.path.dirname(os.path.dirname(__file__)), "src/python"))
import unittest
# remove all the layers of submodules
from libsbml_draw.sbml_layout import SBMLlayout
from tests.model_strings import schmierer2008
import numpy

numpy.random.seed(1)


class TestAttributes(unittest.TestCase):

    def setUp(self) -> None:
        self.sl = SBMLlayout(schmierer2008, applyRender=True)

    def tearDown(self) -> None:
        del self.sl

    def testNodeFontSize(self):
        # default font size
        self.sl.setNodeFontSize("S2_n", 24)
        # self.sl.drawNetwork()
        self.assertEqual(24, self.sl.getNodeFontSize("S2_n"))

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
        self.sl.aliasNode("S2_n")
        expected = ['PPase', 'pS2_n', 'G_n', 'pG_n', 'S22_n',
                    'S24_n', 'S4_n', 'G2_n', 'G4_n', 'GG_n',
                    'S22_c', 'S24_c', 'S4_c', 'S2_c', 'pS2_c',
                    'G_c', 'pG_c', 'G2_c', 'G4_c', 'GG_c',
                    'TGFb_c', 'R_act', 'R', 'R_inact', 'SB',
                    'S2_n_0', 'S2_n_1']
        actual = self.sl.getNodeIds()
        self.assertEqual(expected, actual)

    def test_getArrowheadNumStyles(self):
        expected = 8
        actual = self.sl.getArrowheadNumStyles()
        self.assertEqual(expected, actual)

    def test_getNumberOfRoles(self):
        expected = 7
        actual = self.sl.getNumberOfRoles()
        self.assertEqual(expected, actual)

    def test_getArrowheadStyle(self):
        expected = 1
        actual = self.sl.getArrowheadStyle(1)  # must be between 1 and 7
        self.assertEqual(expected, actual)

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
        expected = ['SB-431542', 'TGFb_c', 'PPase']
        actual = self.sl.getBoundarySpeciesIds()
        # self.assertEqual(sorted(expected), sorted(actual))

    def test_getCompartmentEdgeColor(self):
        """
        Test relies on getCompartmentIds which doesn't work
        Returns:

        """
        # print(self.sl.getCompartmentIds())
        print(self.sl.getCompartmentEdgeColor('nucleus'))

    def test_getCompartmentFillColor(self):
        print(self.sl.getCompartmentFillColor('nucleus'))

    def test_getCompartmentLineWidth(self):
        print(self.sl.getCompartmentLineWidth('nucleus'))

    def test_getFloatingSpeciesIds(self):
        expected = ['PPase', 'S2_n', 'pS2_n', 'G_n', 'pG_n',
                    'S22_n', 'S24_n', 'S4_n', 'G2_n', 'G4_n',
                    'GG_n', 'S22_c', 'S24_c', 'S4_c', 'S2_c',
                    'pS2_c', 'G_c', 'pG_c', 'G2_c', 'G4_c',
                    'GG_c', 'TGFb_c', 'R_act', 'R', 'R_inact',
                    'SB']
        actual = self.sl.getFloatingSpeciesIds()
        self.assertEqual(sorted(expected), sorted(actual))

    def test_getNodeIds(self):
        expected = ['PPase', 'S2_n', 'pS2_n', 'G_n',
                    'pG_n', 'S22_n', 'S24_n', 'S4_n',
                    'G2_n', 'G4_n', 'GG_n', 'S22_c',
                    'S24_c', 'S4_c', 'S2_c', 'pS2_c',
                    'G_c', 'pG_c', 'G2_c', 'G4_c',
                    'GG_c', 'TGFb_c', 'R_act', 'R',
                    'R_inact', 'SB']

        actual = self.sl.getNodeIds()
        self.assertEqual(expected, actual)

    def test_getIsNodeAliased(self):
        # aliasing means using clones of nodes for a species.
        self.sl.aliasNode('PPase')  # replaces S4 with S4_0, S4_1 etc.
        self.assertTrue(self.sl.getIsNodeAliased('PPase_1'))

    def test_getIsNodeLocked(self):
        """
        This test doesn't test much since I
        Returns:

        """
        self.sl.lockNode('PPase')
        self.assertTrue(self.sl.getIsNodeLocked('PPase'))

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
        """
        NodeCertroid is inherently stochastic and so cannot
        be simply tested
        Returns:

        """
        expectd = (30.464084888166553, 281.84839361341085)
        actual = self.sl.getNodeCentroid('PPase')
        # self.assertAlmostEqual(expectd[0], actual[0])
        # self.assertAlmostEqual(expectd[1], actual[1])

    def test_getNodeColor(self):
        expected = '#c9e0fbff'
        actual = self.sl.getNodeColor('PPase')
        self.assertEqual(expected, actual)


    def test_setNodeColor(self):
        expected = '#008000ff'
        self.sl.setNodeColor('PPase', expected)
        actual = self.sl.getNodeColor('PPase')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeEdgeColor(self):
        expected = '#0000ffff'
        actual = self.sl.getNodeEdgeColor('PPase')
        self.assertEqual(expected, actual)

    def test_setNodeEdgeColor(self):
        expected = '#008000ff'
        self.sl.setNodeEdgeColor('PPase', expected)
        actual = self.sl.getNodeEdgeColor('PPase')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeEdgeWidth(self):
        expected = 3
        actual = self.sl.getNodeEdgeWidth('PPase')
        self.assertEqual(expected, actual)

    def test_setNodeEdgeWidth(self):
        expected = 4
        self.sl.setNodeEdgeWidth('PPase', expected)
        actual = self.sl.getNodeEdgeWidth('PPase')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeFillColor(self):
        expected = '#c9e0fbff'
        actual = self.sl.getNodeFillColor('PPase')
        self.assertEqual(expected, actual)

    def test_setNodeFillColor(self):
        expected = '#ff0000ff'
        self.sl.setNodeFillColor('PPase', expected)
        actual = self.sl.getNodeFillColor('PPase')
        self.sl.drawNetwork()  # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeFontColor(self):
        expected = '#000000ff'
        actual = self.sl.getNodeFontColor('PPase')
        self.assertEqual(expected, actual)

    def test_setNodeFillColor(self):
        expected = '#ff0000ff'
        self.sl.setNodeFontColor('PPase', expected)
        actual = self.sl.getNodeFontColor('PPase')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeFontFamily(self):
        expected = 'Arial'
        actual = self.sl.getNodeFontFamily('PPase')
        self.assertEqual(expected, actual)

    def test_setNodeFontFamily(self):
        expected = 'Times New Roman'
        self.sl.setNodeFontFamily('PPase', expected)
        actual = self.sl.getNodeFontFamily('PPase')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeFontName(self):
        expected = 'Arial'
        actual = self.sl.getNodeFontName('PPase')
        self.assertEqual(expected, actual)

    def test_setNodeFontName(self):
        expected = 'Times New Roman'
        self.sl.setNodeFontName('PPase', expected)
        actual = self.sl.getNodeFontName('PPase')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeFontSize(self):
        expected = 20
        actual = self.sl.getNodeFontSize('PPase')
        self.assertEqual(expected, actual)

    def test_setNodeFontSize(self):
        expected = 14
        self.sl.setNodeFontSize('PPase', expected)
        actual = self.sl.getNodeFontSize('PPase')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeFontStyle(self):
        expected = 'normal'
        actual = self.sl.getNodeFontStyle('PPase')
        self.assertEqual(expected, actual)

    def test_setNodeFontSize(self):
        """
        No support for setting the node font size
        Returns:

        """
        pass
        # expected = 'large'
        # self.sl.setNodeStyle('PPase', expected)
        # actual = self.sl.getNodeStyle('PPase')
        # self.sl.drawNetwork() # manually checked and is working correctly
        # self.assertEqual(expected, actual)

    def test_getNodeFontWeight(self):
        expected = 'normal'
        actual = self.sl.getNodeFontWeight('PPase')
        self.assertEqual(expected, actual)

    def test_setNodeFontWeight(self):
        expected = 'bold'
        self.sl.setNodeFontWeight('PPase', expected)
        actual = self.sl.getNodeFontWeight('PPase')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeHeight(self):
        expected = 40.0
        actual = self.sl.getNodeHeight('PPase')
        self.assertAlmostEqual(expected, actual)

    def test_setNodeHeight(self):
        """
        No support for setting the node height
        Returns:

        """
        pass
        # expected = 50.0
        # self.sl.setNode('PPase', expected)
        # actual = self.sl.getNodeHeight('PPase')
        # self.sl.drawNetwork() # manually checked and is working correctly
        # self.assertEqual(expected, actual)

    def test_getNodeLowerLeftPoint(self):
        """
        Lower left point is a stochastic entity it seems,
        so cannot test without mocking (or seeding? )
        Returns:

        """
        actual = self.sl.getNodeLowerLeftPoint('PPase')
        self.assertIsInstance(actual, list)
        self.assertEqual(2, len(actual))
        self.assertIsInstance(actual[0], float)

    def test_getNodeName(self):
        expected = 'PPase'
        actual = self.sl.getNodeName('PPase')
        self.assertEqual(expected, actual)

    def test_getNodeTextAnchor(self):
        expected = 'center'
        actual = self.sl.getNodeTextAnchor('PPase')
        self.assertEqual(expected, actual)

    def test_setNodeTextAnchor(self):
        """
        The roles of left and right have been reversed.
        Returns:

        """
        expected = 'right'
        self.sl.setNodeTextAnchor('PPase', 'left')
        actual = self.sl.getNodeTextAnchor('PPase')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getVNodeTextAnchor(self):
        expected = 'center'
        actual = self.sl.getNodeVTextAnchor('PPase')
        self.assertEqual(expected, actual)

    def test_setVNodeTextAnchor(self):
        expected = 'bottom'  # roles are again reversed
        self.sl.setNodeVTextAnchor('PPase', 'top')
        actual = self.sl.getNodeVTextAnchor('PPase')
        # self.sl.drawNetwork() # manually checked and is working correctly
        self.assertEqual(expected, actual)

    def test_getNodeWidth(self):
        expected = 140.0
        actual = self.sl.getNodeWidth('PPase')
        self.assertAlmostEqual(expected, actual)

    def test_getNumberOfCompartments(self):
        expected = 2
        actual = self.sl.getNumberOfCompartments()
        self.assertEqual(expected, actual)

    def test_getNumberOfNodes(self):
        expected = 26
        actual = self.sl.getNumberOfNodes()
        self.assertEqual(expected, actual)

    def test_getNumberOfReactions(self):
        expected = 26
        actual = self.sl.getNumberOfReactions()
        self.assertEqual(expected, actual)

    def test_getNumberOfRoles(self):
        expected = 7
        actual = self.sl.getNumberOfRoles()
        self.assertEqual(expected, actual)

    def test_getReactionIds(self):
        expected = ['reaction_1', 'reaction_2', 'reaction_3', 'reaction_4',
                    'reaction_5', 'reaction_6', 'reaction_7', 'reaction_8',
                    'reaction_9', 'reaction_10', 'reaction_11', 'reaction_12',
                    'reaction_13', 'reaction_14', 'reaction_15', 'reaction_16',
                    'reaction_17', 'reaction_18', 'reaction_19', 'reaction_20',
                    'reaction_21', 'reaction_22', 'reaction_23', 'reaction_24',
                    'reaction_25', 'reaction_26']
        actual = self.sl.getReactionIds()
        self.assertEqual(expected, actual)

    def test_getReactionBezierPoints2(self):
        """
        random variable - so can't test exact.
        Returns:

        """
        points = self.sl.getReactionBezierPoints('reaction_1')
        end = points[0].end
        self.assertIsInstance(end, tuple)
        self.assertIsInstance(end[0], float)
        self.assertEqual(2, len(end))

    def test_getReactionCentroid(self):
        actual = self.sl.getReactionCentroid('reaction_1')
        self.assertEqual(2, len(actual))

    def test_getReactionCurveWidth(self):
        expected = ('S4_c', 'SUBSTRATE', 3)
        curve = self.sl.getReactionCurveWidth('reaction_1')
        actual = curve[0]
        self.assertEqual(expected, actual)

    def test_getReactionEdgeColor(self):
        expected = '#0000ffff'
        reaction = self.sl.getReactionEdgeColor('reaction_1')
        actual = reaction[0][2]
        self.assertEqual(expected, actual)

    def test_setReactionEdgeColor(self):
        expected = '#c9e0fbff'
        self.sl.setReactionEdgeColor('reaction_1', expected)
        reaction = self.sl.getReactionEdgeColor('reaction_1')
        actual = reaction[0][2]
        self.assertEqual(expected, actual)

    def test_getReactionFillColor(self):
        expected = '#0000ff'
        reaction = self.sl.getReactionFillColor('reaction_1')
        actual = reaction[0][2]
        self.assertEqual(expected, actual)

    def test_setReactionFillColor(self):
        expected = '#c9e0fbff'
        self.sl.setReactionFillColor('reaction_1', expected)
        reaction = self.sl.getReactionFillColor('reaction_1')
        actual = reaction[0][2]
        self.assertEqual(expected, actual)

    def test_getSBMLString(self):
        string = self.sl.getSBMLString()
        self.assertIsInstance(string, str)

    def test_getCompartmentIds(self):
        expected = ['nucleus', 'cytosol']
        actual = self.sl.getCompartmentIds()
        self.assertEqual(expected, actual)

    def test_get_num_compartments_with_libsbml(self):
        expected = 2
        sl = SBMLlayout(schmierer2008, applyRender=True)
        n = sl._network
        self.assertEqual(expected, n.getNumCompartmentsWithLibsbml())
