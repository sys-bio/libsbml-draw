import os
import site

site.addsitedir(os.path.dirname(__file__))
import unittest

from add_to_path import add_to_path

add_to_path()
from libsbml_draw.layout import SBMLlayout
from libsbml_draw.render import Render
from libsbml_draw.utils import biomodels_download
import tesbml as libsbml

class TestRender(unittest.TestCase):
    model_id = 'BIOMD0000000604'

    def setUp(self) -> None:
        self.sbml = biomodels_download(self.model_id)
        self.doc = libsbml.readSBMLFromString(self.sbml)
        # self.doc.setLevelAndVersion(3, 2)
        print(self.doc.getLevel(), self.doc.getVersion())
        # print(libsbml.writeSBMLToString(self.doc))

    def test(self):
        # print(self.doc)
        # r = Render(self.doc, 0)
        # print(r)
        print(libsbml.LIBSBML_OPERATION_SUCCESS)







if __name__ == '__main__':
    unittest.TestCase()


