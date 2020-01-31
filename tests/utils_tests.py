import site
import unittest
import os

from .add_to_path import add_to_path
add_to_path()
from libsbml_draw.utils import biomodels_download


class TestDownloader(unittest.TestCase):
    fname = os.path.join(os.path.dirname(__file__), 'network.sbml')

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        if os.path.isfile(self.fname):
            os.remove(self.fname)

    def test(self):
        biom = 'BIOMD0000000086'
        sbml = biomodels_download(biom, self.fname)
        self.assertTrue(sbml.startswith('<?xml'))

    def test(self):
        biom = 'BIOMD0000000096'
        biomodels_download(biom, self.fname)
        self.assertTrue(os.path.isfile(self.fname))



if __name__ == '__main__':
    unittest.main()
