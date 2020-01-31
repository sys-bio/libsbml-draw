import unittest
import site
import os
site.addsitedir(os.path.dirname(__file__))

import tellurium as te

from add_to_path import add_to_path
add_to_path()
from libsbml_draw.sbml_layout import SBMLlayout


# matplotlib.use('TkAgg')


class AntimonyModelTests(unittest.TestCase):

    def setUp(self) -> None:
        self.r = te.loada('''
        // Created by libAntimony v2.9.4
        model *untitled()
        
          // _Compartments and Species:
          species Node0, Node3, Node5, Node6, Node7, Node8888888, Node9, Node10, Node11;
          species Node12, Node13, Node14;
        
          // Reactions:
          J0: Node8888888 + Node5 => Node9; 1;
          J1: Node11 + Node9 => Node14; 1;
          J2: Node0 + Node13 => Node7 + Node12; 1;
          J3: Node0 => Node13; 1;
          J4: Node8888888 + Node14 => Node6; 1;
          J5: Node12 + Node5 => Node13 + Node0; 1;
          J6: Node0 + Node3 => Node8888888; 1;
          J7: Node10 => Node8888888; 1;
        
          // Species initializations:
          Node0 = 0;
          Node3 = 0;
          Node5 = 0;
          Node6 = 0;
          Node7 = 0;
          Node8888888 = 0;
          Node9 = 0;
          Node10 = 0;
          Node11 = 0;
          Node12 = 0;
          Node13 = 0;
          Node14 = 0;
        end
        ''')
        self.sl = SBMLlayout(self.r.getSBML())
        self.fname = os.path.join(os.path.dirname(__file__), 'network.png')

    def test_sbml_layout(self):
        self.assertIsInstance(self.sl, SBMLlayout)

    def test_describe_model_layout_number(self):
        description = self.sl.describeModel()
        expected = 0
        actual = description['layout_number']
        self.assertEqual(expected, actual)

    def test_describe_model_layout_layout_is_specified(self):
        description = self.sl.describeModel()
        expected = False
        actual = description['layout_is_specified']
        self.assertEqual(expected, actual)

    def test_describe_model_layout_auto_compute_layout(self):
        description = self.sl.describeModel()
        expected = False
        actual = description['auto_compute_layout']
        self.assertEqual(expected, actual)

    def test_describe_model_layout_number_of_compartments(self):
        description = self.sl.describeModel()
        expected = 0
        actual = description['number_of_compartments']
        self.assertEqual(expected, actual)

    def test_describe_model_layout_number_of_nodes(self):
        description = self.sl.describeModel()
        expected = 12
        actual = description['number_of_nodes']
        self.assertEqual(expected, actual)

    def test_describe_model_layout_number_of_reactions(self):
        description = self.sl.describeModel()
        expected = 8
        actual = description['number_of_reactions']
        self.assertEqual(expected, actual)

    def test_draw_network(self):
        fig = self.sl.drawNetwork()
        fig.savefig(self.fname, bbox_inches='tight', dpi=300)
        self.assertTrue(os.path.isfile(self.fname))

    def test_load_from_string(self):
        slsl = SBMLlayout(self.r.getSBML())
        slsl.loadSBMLString(self.r.getSBML())
        self.assertIsInstance(slsl, SBMLlayout)

    def test_draw_network_from_model_loaded_from_string(self):
        slsl = SBMLlayout(self.r.getSBML())
        slsl.loadSBMLString(self.r.getSBML())
        fig = slsl.drawNetwork()
        fig.savefig(self.fname, bbox_inches='tight', dpi=300)
        self.assertTrue(os.path.isfile(self.fname))

    def tearDown(self) -> None:
        if os.path.isfile(self.fname):
            os.remove(self.fname)

if __name__ == '__main__':
    unittest.main()
