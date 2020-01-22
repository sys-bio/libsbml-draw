import os
import site

# add the library to path
site.addsitedir(os.path.join(os.path.dirname(os.path.dirname(__file__)), "src/python"))
# print(p)
import unittest
from tests.model_strings import model_xml
from libsbml_draw.model.sbml_layout import SBMLlayout
# from libsbml_draw.draw.patch import Patch

import libsbml

document = libsbml.readSBMLFromString(model_xml)
if document.getNumErrors() > 0:
    print("Encountered the following SBML errors:" + "\n")
    document.printErrors()

model = document.getModel()

print(model.getNumCompartments())

x = model.getCompartment(0)

print(x.getId())




# class TestLibSBMLPatch(unittest.TestCase):
#
#     def setUp(self) -> None:
#         pass
#
#     def tearDown(self) -> None:
#         pass
#
#     def test(self):
#         SBMLlayout(model_xml)
#
#     def test_read_sbml(self):
#         patch = Patch(model_xml)
#         expected = 0
#         actual = patch._doc.getNumErrors()
#         self.assertEqual(expected, actual)
#
#     # def test_get_compartments(self):
#     #     expected = ["default_compartment"]
#     #     patch = Patch(minimal_sbml)
#     #     actual = patch.get_compartments()
#     #
#     # def test_get_floating_species(self):
#     #     patch = Patch(model_xml)
#     #     print(patch.get_floating_species())
#     #
#     # def test_compartments_with_bs4(self):
#     #     expected = ['default_compartment']
#     #     patch = Patch(model_xml)
#     #     actual = patch.get_compartments_with_bs4()
#     #     self.assertEqual(expected, actual)
#     #
#     # def test_boundary_species_with_bs4(self):
#     #     patch = Patch(model_xml)
#     #     actual = patch.boundary_species_ids
#     #     expected = ['S7']
#     #     self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
