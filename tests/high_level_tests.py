import unittest
import os, glob

from tests.model_strings import compartment_model, schmierer2008, kholodenko2000
from libsbml_draw.model.sbml_layout import SBMLlayout
from libsbml_draw.model.sbml_layout import _ValidatedDict, _ValidatedDict, _Font


# todo enable config of all node/edge attributes with a single command
# todo make seed for algorithm depend on time
# todo check with larger models.
# todo


class ValidatedDictTests(unittest.TestCase):
    class Items(_ValidatedDict):
        chair = 'brown'
        length = 14

    def setUp(self) -> None:
        self.items = ValidatedDictTests.Items()

    def test_instantiation_of_ValidatedDict(self):
        expected = 'brown'
        actual = list(self.items.values())[0]
        self.assertEqual(expected, actual)

    def test_error_when_adding_new_key(self):
        with self.assertRaises(TypeError):
            self.items['America'] = 'big'

    def test_access_by_dot_notation(self):
        self.assertEqual(self.items.chair, 'brown')



class HighLevelTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test(self):
        s = SBMLlayout(compartment_model)
        s.drawNetwork(show=True)

        s.setNodeFontSize('Node1', 30)
        s.drawNetwork(show=True)

        s.regenerateLayout()
        s.drawNetwork(show=True)


        # print(s.getCompartmentEdgeColor('vol1'))
        # print(s.getCompartmentFillColor('vol1'))
        # print(s.getCompartmentLineWidth('vol1'))







if __name__ == '__main__':
    unittest.main()

