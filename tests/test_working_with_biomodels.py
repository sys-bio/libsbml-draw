import os
import site

site.addsitedir(os.path.dirname(__file__))
import unittest

from add_to_path import add_to_path

add_to_path()
from libsbml_draw import SBMLlayout, sbnw
import requests
import codecs


# matplotlib.use('TkAgg')


class TestWorksWithBioModels(unittest.TestCase):
    base_url = "https://www.ebi.ac.uk/biomodels-main/download?mid"
    model_id = 'BIOMD0000000091'
    sbml_fname = os.path.join(os.path.dirname(__file__), 'sbmlmodel.xml')
    sbml_layout_fname = os.path.join(os.path.dirname(__file__), 'sbmlmodel_with_layout.xml')
    image_fname = os.path.join(os.path.dirname(__file__), 'network.png')
    expected_number_of_compartments = 0
    expected_number_of_nodes = 16
    expected_number_of_reactions = 23
    tear_down = True

    def get_model_from_url(self):
        self.model_file_name = f"{self.model_id}_url.xml"
        model_url = f'{self.base_url}={self.model_id}'
        # get the model directly from url
        sbml = requests.get(model_url).content.decode('utf-8')
        with codecs.open(self.sbml_fname, 'w', 'utf-8') as f:
            f.write(sbml)
        return sbml

    def tearDown(self) -> None:
        if self.tear_down:
            for i in [self.sbml_fname, self.image_fname, self.sbml_layout_fname]:
                if os.path.isfile(i):
                    os.remove(i)

    def setUp(self) -> None:
        self.sbml = self.get_model_from_url()
        self.sl = SBMLlayout(self.sbml_fname, applyRender=False)

    def test_setup(self):
        self.get_model_from_url()
        self.assertTrue(os.path.isfile(self.sbml_fname))

    def test_load_from_biomodels(self):
        self.assertIsInstance(self.sl, SBMLlayout)

    def do_describe(self):
        desc = self.sl.describeModel()
        return desc

    def test_number_of_nodes(self):
        described = self.do_describe()
        self.assertEqual(self.expected_number_of_nodes, described['number_of_nodes'])

    def test_number_of_compartments(self):
        described = self.do_describe()
        self.assertEqual(self.expected_number_of_compartments, described['number_of_compartments'])

    def test_number_of_reactions(self):
        described = self.do_describe()
        self.assertEqual(self.expected_number_of_reactions, described['number_of_reactions'])

    def test_draw_network_and_save_to_pdf(self):
        self.sl.drawNetwork(self.image_fname, show=False, scaling_factor=1.0)
        self.assertTrue(os.path.isfile(self.image_fname))

    def test_save_sbml_to_file(self):
        self.sl.drawNetwork(self.image_fname, show=False, scaling_factor=1.0)
        self.sl.writeSBMLFile(self.sbml_layout_fname)
        self.assertTrue(os.path.isfile(self.sbml_layout_fname))

class TestBioMD0000000011(TestWorksWithBioModels):
    model_id = 'BIOMD0000000011'
    expected_number_of_compartments = 1
    expected_number_of_nodes = 22
    expected_number_of_reactions = 30


class TestBioMD0000000001(TestWorksWithBioModels):
    model_id = 'BIOMD0000000001'
    expected_number_of_compartments = 1
    expected_number_of_nodes = 12
    expected_number_of_reactions = 17


class TestBioMD0000000002(TestWorksWithBioModels):
    model_id = 'BIOMD0000000002'
    expected_number_of_compartments = 1
    expected_number_of_nodes = 13
    expected_number_of_reactions = 17



if __name__ == '__main__':
    unittest.main()
