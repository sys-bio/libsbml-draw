import unittest
import site, os

from .add_to_path import add_to_path
add_to_path()

from libsbml_draw.sbml_layout import SBMLlayout
from libsbml_draw.styles import _AttributeSet, Style
from tests.model_strings import compartment_model


# todo enable config of all node/edge attributes with a single command
# todo make seed for algorithm depend on time
# todo check with larger models.
# todo


# class AttributeSetTests(unittest.TestCase):
#     class Items(_AttributeSet):
#         chair = 'brown'
#         length = 14
#
#     def setUp(self) -> None:
#         self.items = AttributeSetTests.Items()
#
#     def test_access_by_dot_notation(self):
#         self.assertEqual(self.items.chair, 'brown')
#
#     def test_instantiation_of_ValidatedDict(self):
#         expected = 'brown'
#         actual = list(self.items.values())[0]
#         self.assertEqual(expected, actual)
#
#     def test_error_when_adding_new_key(self):
#         with self.assertRaises(TypeError):
#             self.items['x'] = 'y'
#
#     def test_getitem(self):
#         items = self.Items()
#         expected = 'brown'
#         actual = getattr(items, 'chair')
#         self.assertEqual(expected, actual)
#
#     def test_setitem(self):
#         items = self.Items()
#         expected = 'green'
#         setattr(items, 'chair', 'green')
#         actual = getattr(items, 'chair')
#         self.assertEqual(expected, actual)
#
#     def test_change_variable_directly_from_attribute(self):
#         items = self.Items()
#         items.chair = 'green'
#         actual = getattr(items, 'chair')
#         expected = 'green'
#         self.assertEqual(expected, actual)
#
#     def test_items_method(self):
#         items = self.Items()
#         items.chair = 'red'
#         expected = None
#         for k, v in items.items():
#             if k == 'chair':
#                 expected = v
#         self.assertEqual(expected, 'red')
#
#
#
# class StyleTests(unittest.TestCase):
#
#     def setUp(self) -> None:
#         self.style = Style()
#
#     def test_style_instantiation(self):
#         self.assertIsInstance(self.style, Style)
#
#     def test_you_can_change_a_value(self):
#         self.style.node.edgecolor = 'red'
#         self.assertEqual('red', self.style.node.edgecolor)
#
#     def test_dict_attr_has_updated(self):
#         self.style .node.edgecolor = 'red'
#         expected = 'red'
#         actual = self.style .node.edgecolor
#         self.assertEqual(expected, actual)
#
#     def test_edgecolor_via_a_style(self):
#         self.style.edge.color = 'orange'
#         sl = SBMLlayout(compartment_model, style=self.style)
#         actual = [sl.getReactionEdgeColor(i) for i in sl.getReactionIds()]
#         colours = []
#         for i in actual:
#             for j in i:
#                 colours.append(j[2])
#         expected = '#ffa500ff'
#         actual = list(set(colours))[0]
#         self.assertEqual(expected, actual)
#
#     def testx(self):
#         self.style.node.color = 'black'
#         sl = SBMLlayout(compartment_model, style=self.style)
#         print(sl.getNodeColor('Node0'))
#         sl.drawNetwork('network2.png', show=False)
#         # expected = '#c9e0fb'
#         # actual = self.sl.getNodeColor('PPase')
#         # self.assertEqual(expected, actual)
#
#     def tearDown(self) -> None:
#         del self.style
#
# if __name__ == '__main__':
#     unittest.main()
