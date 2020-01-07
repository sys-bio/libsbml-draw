import site
site.addsitedir('../src/python')
import unittest

import tellurium as te
from libsbml_draw.model.sbml_layout import SBMLlayout


class AntimonyModelTests(unittest.TestCase):

    def setUp(self) -> None:
        self.r = te.loada('''
        // Created by libAntimony v2.9.4
        model *untitled()
        
          // Compartments and Species:
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

    def test_sbml_layout(self):
        self.assertIsInstance(self.sl, SBMLlayout)

    def test_describe_model(self):
        print(self.sl._describeModel())
    #
    # sl.drawNetwork()
    #
    # assert sl.getNumberOfNodes() == 12
    # assert sl.getNumberOfReactions() == 8
    #
    # slsl = SBMLlayout()
    #
    # slsl.loadSBMLString(r.getSBML())
    #
    # slsl._describeModel()
    #
    # slsl.drawNetwork()
    #
    #
    # assert slsl.getNumberOfNodes() == 12
    # assert slsl.getNumberOfReactions() == 8

if __name__ == '__main__':
    unittest.main()

