import unittest
import site, os

from .add_to_path import add_to_path
add_to_path()

from libsbml_draw.layout import SBMLlayout
from libsbml_draw.network import Network, Compartment
from libsbml_draw.styles import _AttributeSet, Style
from tests.model_strings import teusink2000
from libsbml_draw.styles import black_and_white
from libsbml_draw import sbnw

ALG_OPTIONS = sbnw.FrAlgOptions(
    20.0,  # k
    1,  # boundary
    100,  # magnatism
    5.0,  # grav, has to be > 5 for effect
    500.0,  # baryx
    500.0,  # baryy
    1,  # autobary
    0,  # enable compartments
    1,  # pre-randomize
    20.0  # padding
)


class NetworkTests(unittest.TestCase):

    def setUp(self) -> None:
        self.sbml_fname = os.path.join(os.path.dirname(__file__), 'teusink2000.xml')
        self.sbml_with_layout = os.path.join(os.path.dirname(__file__), 'teusink2000WithLayoutFromPython.xml')
        self.sbml_model = sbnw.loadSBMLString(teusink2000)
        self.layout_info = sbnw.processLayout(self.sbml_model)

    def tearDown(self) -> None:
        pass

    def test_get_network_from_pointer(self):
        network = sbnw.getNetworkp(self.layout_info)
        self.assertIsInstance(network, int)

    def test_create_network_onj(self):
        network = sbnw.getNetworkp(self.layout_info)
        network = Network(network)
        self.assertIsInstance(network, Network)

    def test_network_compartments_len(self):
        network = sbnw.getNetworkp(self.layout_info)
        network = Network(network)
        self.assertEqual(2, len(network.compartments))

    def test_network_compartments_size(self):
        network = sbnw.getNetworkp(self.layout_info)
        network = Network(network)
        self.assertEqual(2, len(network.compartments))
        print(network.compartments)
        # self.assertIsInstance(network, Network)


class CompartmentTests(unittest.TestCase):

    def setUp(self) -> None:
        self.sbml_fname = os.path.join(os.path.dirname(__file__), 'teusink2000.xml')
        self.sbml_with_layout = os.path.join(os.path.dirname(__file__), 'teusink2000WithLayoutFromPython.xml')
        self.sbml_model = sbnw.loadSBMLString(teusink2000)
        self.layout_info = sbnw.processLayout(self.sbml_model)
        self.h_network = sbnw.getNetworkp(self.layout_info)
        self.network = Network(self.h_network)

    def test_compartment_isinstance(self):
        cytosol_comp = self.network.compartments['cytosol']
        self.assertIsInstance(cytosol_comp, Compartment)

    def test_compartment_after_do_algorithm(self):
        sbnw.randomizeLayout(self.layout_info)
        sbnw.doLayoutAlgorithm(ALG_OPTIONS, self.layout_info)

        cytosol_comp = self.network.compartments['cytosol']
        # print(cytosol_comp.min_corner.x)
        # print(cytosol_comp.min_corner.y)
        # print(cytosol_comp.width)
        # print(cytosol_comp.height)
        # print(cytosol_comp.max_corner.x)
        # print(cytosol_comp.max_corner.y)
        # print(cytosol_comp.center_x)
        # print(cytosol_comp.center_y)
        # print(cytosol_comp.lower_left_point)
        sbnw.writeSBMLwithLayout(self.sbml_with_layout, self.sbml_model, self.layout_info)
        self.assertTrue(cytosol_comp.min_corner.x > 0)
        self.assertTrue(cytosol_comp.min_corner.y > 0)

    def test_compartment_after_do_algorithm_twice(self):
        sbnw.randomizeLayout(self.layout_info)
        sbnw.doLayoutAlgorithm(ALG_OPTIONS, self.layout_info)
        sbnw.doLayoutAlgorithm(ALG_OPTIONS, self.layout_info)
        cytosol_comp = self.network.compartments['cytosol']
        self.assertTrue(cytosol_comp.min_corner.x > 0)
        self.assertTrue(cytosol_comp.min_corner.y > 0)

    def test_compartment_after_do_algorithm3(self):
        sbnw.randomizeLayout(self.layout_info)
        comp = sbnw.nw_getCompartmentp(self.h_network, 1)

        print('compartment_getWidth', sbnw.compartment_getWidth(comp))
        print('compartment_getHeight', sbnw.compartment_getHeight(comp))
        print('compartment_getMinCorner', sbnw.compartment_getMinCorner(comp))
        print('compartment_getMaxCorner', sbnw.compartment_getMaxCorner(comp))
        print('compartment_getID', sbnw.compartment_getID(comp))
        sbnw.writeSBMLwithLayout(self.sbml_with_layout, self.sbml_model, self.layout_info)























if __name__ == '__main__':
    unittest.main()


















