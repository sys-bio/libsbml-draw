import unittest

from libsbml_draw.sbml_layout import SBMLlayout
from libsbml_draw.styles import _AttributeSet, Style
from tests.model_strings import compartment_model


# todo enable config of all node/edge attributes with a single command
# todo make seed for algorithm depend on time
# todo check with larger models.
# todo


class ValidatedDictTests(unittest.TestCase):
    class Items(_AttributeSet):
        chair = 'brown'
        length = 14

    def setUp(self) -> None:
        self.items = ValidatedDictTests.Items()

    def test_access_by_dot_notation(self):
        self.assertEqual(self.items.chair, 'brown')

    def test_instantiation_of_ValidatedDict(self):
        expected = 'brown'
        actual = list(self.items.values())[0]
        self.assertEqual(expected, actual)

    def test_error_when_adding_new_key(self):
        with self.assertRaises(TypeError):
            self.items['x'] = 'y'

    def test_getitem(self):
        items = self.Items()
        expected = 'brown'
        actual = getattr(items, 'chair')
        self.assertEqual(expected, actual)

    def test_setitem(self):
        items = self.Items()
        expected = 'green'
        setattr(items, 'chair', 'green')
        actual = getattr(items, 'chair')
        self.assertEqual(expected, actual)

    def test_change_variable_directly_from_attribute(self):
        items = self.Items()
        items.chair = 'green'
        actual = getattr(items, 'chair')
        expected = 'green'
        self.assertEqual(expected, actual)

    def test_items_method(self):
        items = self.Items()
        items.chair = 'red'
        expected = None
        for k, v in items.items():
            if k == 'chair':
                expected = v
        self.assertEqual(expected, 'red')



class SettingsTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_style_instantiation(self):
        self.assertIsInstance(Style(), Style)

    def test_you_can_change_a_value(self):
        s = Style()
        s.node.edgecolor = 'red'
        self.assertEqual('red', s.node.edgecolor)

    def test_dict_attr_has_updated(self):
        s = Style()
        s.node.edgecolor = 'red'
        # self.assertEqual('red', s.node.edgecolor)
        expected = 'red'
        actual = s.node.edgecolor
        self.assertEqual(expected, actual)

    def test_edgecolor_via_a_style(self):
        s = Style()
        s.edge.color = 'green'
        s = SBMLlayout(compartment_model, style=s)
        actual = [s.getReactionEdgeColor(i) for i in s.getReactionIds()]
        colours = []
        for i in actual:
            for j in i:
                colours.append(j[2])
        expected = '#008000ff'
        actual = list(set(colours))[0]
        self.assertEqual(expected, actual)



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

    def test2(self):
        pass
        # s = SBMLlayout(compartment_model)

        # print(s.getCompartmentEdgeColor('vol1'))
        # print(s.getCompartmentFillColor('vol1'))
        # print(s.getCompartmentLineWidth('vol1'))


if __name__ == '__main__':
    unittest.main()
