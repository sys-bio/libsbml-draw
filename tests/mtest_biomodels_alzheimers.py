import site

site.addsitedir('../src/python')
import unittest, os, glob
import tellurium as te
from libsbml_draw.model.sbml_layout import SBMLlayout
import requests


class BioModelsProctor2005Tests(unittest.TestCase):

    def setUp(self) -> None:
        # Proctor2005 - Actions of chaperones and their role in ageing
        self.model_file_name = "BIOMD0000000091_url.xml"
        model_url = 'https://www.ebi.ac.uk/biomodels-main/download?mid=BIOMD0000000091'
        # get the model directly from url
        self.sbml = requests.get(model_url).content.decode('utf-8')
        self.fname = os.path.join(os.path.dirname(__file__), 'sbmlmodel.sbml')
        self.fname_pdf = os.path.join(os.path.dirname(__file__), 'network.pdf')
        with open(self.fname, 'w') as f:
            f.write(self.sbml)

    def tearDown(self) -> None:
        for i in [self.fname, self.fname_pdf]:
            if os.path.isfile(i):
                os.remove(i)

    def test_load_from_biomodels(self):
        sl = SBMLlayout(self.fname, applyRender=False)
        self.assertIsInstance(sl, SBMLlayout)

    def test_model_describe(self):
        sl = SBMLlayout(self.fname, applyRender=False)
        desc = sl._describeModel()
        expected = 16
        actual = desc['number_of_nodes']
        self.assertEqual(expected, actual)

    def test_draw_network_and_save_to_pdf(self):
        sl = SBMLlayout(self.fname, applyRender=False)
        sl.drawNetwork(self.fname_pdf)
        self.assertTrue(os.path.isfile(self.fname_pdf))


if __name__ == '__main__':
    unittest.main()
