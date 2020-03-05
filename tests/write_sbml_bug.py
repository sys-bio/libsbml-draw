import unittest
import os
import site

site.addsitedir(os.path.dirname(__file__))
site.addsitedir(r'D:\libsbml-draw\src\python')
import unittest

from libsbml_draw import sbnw

from add_to_path import add_to_path

add_to_path()
from libsbml_draw import SBMLlayout, sbnw, Style

from model_strings import schmierer2008


class TestWriteFile(unittest.TestCase):

    def setUp(self) -> None:
        self.image_fname = os.path.join(os.path.dirname(__file__), 'teusink2000network.png')
        # self.sbml_fname = r'D:\ReproduciblePaper\BIOMD64\JWSOnline_Teusink.xml'
        self.sbml_fname = r'D:\sbnw\test\teusink2000.xml'
        self.sbml_with_layout = r'D:\sbnw\test\teusink2000WithLayoutFromPython.xml'
        self.sbml_with_layout2 = r'D:\sbnw\test\teusink2000WithLayoutFromPythonSecond.xml'

    def test_with_libsbml_draw(self):
        from collections import OrderedDict
        opt = OrderedDict(
            k=20.0,  # k
            boundary=1,  # boundary
            magnatism=100,  # magnatism
            grav=5,  # grav, has to be > 5 for effect
            baryx=500.0,  # baryx
            baryy=500.0,  # baryy
            autobary=1,  # autobary
            enable_comps=0,  # enable compartments // breaks the algorithm
            prerandomize=1,  # pre-randomize
            padding=20.0  # padding
        )
        s = Style()

        # edge attributes
        s.edge.edgecolor = 'grey'
        s.edge.fillcolor = 'grey'
        # s.edge.width = 15

        # font attributes
        s.font.color = 'black'
        # s.font.size = 35
        s.font.weight = 'bold'

        # node attributes
        s.node.edgecolor = '#b36b00'
        s.node.fillcolor = '#ffcc80'
        s.node.edgewidth = 5

        # compartment attributes
        s.compartment.edgecolor = 'black'
        s.compartment.fillcolor = '#ffebcc'
        # s.compartment.linewidth = 20

        # arrow attributes
        s.arrow.scale = 50

        sl = SBMLlayout(self.sbml_fname, autoComputeLayout=True, style=s,
                        layout_alg_options=opt)
        # sl.drawNetwork(self.image_fname, show=False, scaling_factor=1.0)
        # sl.writeSBML(self.sbml_with_layout)

    def test_with_libsbml_draw2(self):
        sl = SBMLlayout(self.sbml_with_layout, autoComputeLayout=True)
        # sl.drawNetwork(self.image_fname, show=False, scaling_factor=1.0)
        sl.writeSBML(self.sbml_with_layout2)

    def test_with_sbnw_c_api(self):
        sbml_model = sbnw.loadSBMLFile(self.sbml_fname)
        layout_info = sbnw.processLayout(sbml_model)
        sbnw.randomizeLayout(layout_info)
        network = sbnw.getNetworkp(layout_info)

        _layout_alg_options = sbnw.FrAlgOptions(
            20.0,  # k
            1,      #boundary
            100,  # magnatism
            5.0,  # grav, has to be > 5 for effect
            500.0,  # baryx
            500.0,  # baryy
            1,  # autobary
            0,  #enable compartments
            1,  #pre-randomize
            20.0  # padding
        )

        comp = sbnw.nw_getCompartmentp(network, 0)
        comp_height_before = sbnw.compartment_getHeight(comp)
        print('comp_height_before', comp_height_before)
        sbnw.doLayoutAlgorithm(_layout_alg_options, layout_info)
        comp_height_after = sbnw.compartment_getHeight(comp)
        print('comp_height_after', comp_height_after)

        # print(sbnw.getSBMLwithLayoutStr(sbml_model, layout_info))
        print(sbnw.writeSBMLwithLayout(self.sbml_with_layout, sbml_model, layout_info))

        #remember to free memory

    def test_with_sbnw_c_api2(self):
        sbml_model = sbnw.loadSBMLFile(self.sbml_fname)
        layout_info = sbnw.processLayout(sbml_model)
        sbnw.randomizeLayout(layout_info)
        network = sbnw.getNetworkp(layout_info)

        _layout_alg_options = sbnw.FrAlgOptions(
            20.0,  # k
            1,      #boundary
            100,  # magnatism
            0.0,  # grav, has to be > 5 for effect
            500.0,  # baryx
            500.0,  # baryy
            1,  # autobary
            0,  #enable compartments
            1,  #pre-randomize
            20.0  # padding
        )

        # comp = sbnw.nw_getCompartmentp(network, 0)
        # comp_height_before = sbnw.compartment_getHeight(comp)
        # print('comp_height_before', comp_height_before)
        # sbnw.doLayoutAlgorithm(_layout_alg_options, layout_info)
        # comp_height_after = sbnw.compartment_getHeight(comp)
        # print('comp_height_after', comp_height_after)
        #
        # # print(sbnw.getSBMLwithLayoutStr(sbml_model, layout_info))
        # print(sbnw.writeSBMLwithLayout(self.sbml_with_layout, sbml_model, layout_info))

        #remember to free memory

if __name__ == '__main__':
    unittest.main()
