"""
Test the SBML_Layout API.
"""
import os

import pytest

import libsbml_draw.c_api.sbnw_c_api as sbnw
from libsbml_draw.model.sbml_layout import SBMLlayout

#import pkg_resources
#libsbmldraw_lib_file = pkg_resources.resource_string("libsbml-draw", "data/libsbml_draw.dll")
#DATA_PATH = pkg_resources.resource_filename("libsbml_draw", "data/")
#DLL_FILE = pkg_resources.resource_filename("libsbml_draw", "data/libsbml_draw.dll")
#DLL_STREAM = pkg_resources.resource_stream("libsbml_draw", "data/libsbml_draw.dll")
#OS_DLL_FILE = os.path.abspath(DLL_FILE)
#from pathlib import Path
#PATH_DLL_FILE = Path(DLL_FILE)

#print("data_path: ", DATA_PATH)
#print("dll file: ", DLL_FILE, "type: ", type(DLL_FILE))
#print("os path: " , OS_DLL_FILE)
#print("Path: ", PATH_DLL_FILE)
#print("dll stream: ", DLL_STREAM, "type: ", type(DLL_STREAM))
#TMP_DLL_FILE = "c:\\tmp\\libsbml_draw.dll"
#TMP_DLL_FILE = "c:users/nrhaw/documents/visual\ studio\ 2017/projects/project_libsbml_draw/project_libsbml_draw/libsbml-draw/src/python/libsbml_draw/data/libsbml_draw.dll"
#print("TMP_DLL_FILE: ", TMP_DLL_FILE)

#import ctypes

#assert os.path.isfile(TMP_DLL_FILE)

#slib = ctypes.CDLL(TMP_DLL_FILE)
#slib2 = ctypes.CDLL(DLL_FILE)
#slib.gf_getCurrentLibraryVersion.restype = ctypes.c_char_p
#print("slib: ", slib.gf_getCurrentLibraryVersion().decode('utf-8') )


TEST_ARROWHEAD_STYLE = 3
TEST_NUMBER_OF_NODES = 6
# This file does not have layout info
# It has: id=__main and name=__main 
# It has lists of: Compartments, Species, Parameters, Reactions
TEST_SBML_FILE_NO_LAYOUT = "C:\\tmp\\model.xml"
# This file has layout info
TEST_SBML_FILE_WITH_LAYOUT = "C:\\tmp\\model_with_layout.xml"
TEST_SBML_FILE_WITH_LAYOUT_OUTFILE = "C:\\tmp\\model_with_layout_write_again.xml"
TEST_SBML_FILE_WITH_LAYOUT_MODIFIER = "C:\\tmp\\modexmpl.xml"

@pytest.fixture
def layout_alg_options():
    # ten params
    return sbnw.fr_alg_options(
            20.0,        # k
            1,           # boundary
            0,           # mag
            0,           # grav
            500.0,       # baryx
            0.0,         # baryy
            1,           # autobary
            0,           # enable_comps
            0,           # prerandom
            0.0          # padding
            )    

@pytest.fixture
def sbml_without_layout(layout_alg_options):
   sl = SBMLlayout(TEST_SBML_FILE_NO_LAYOUT, layout_alg_options)
   return sl

@pytest.fixture
def sbml_with_layout(layout_alg_options):
    sl = SBMLlayout(TEST_SBML_FILE_WITH_LAYOUT, layout_alg_options)
    return sl

@pytest.fixture
def sbml_with_layout_modifier(layout_alg_options):
    sl = SBMLlayout(TEST_SBML_FILE_WITH_LAYOUT_MODIFIER, layout_alg_options)
    return sl


def test_describe_model(sbml_without_layout):
    result = sbml_without_layout.describeModel()
    # number of: compartments, nodes, reactions 
    assert result == (0, 6, 6)

def test_sbml_without_layout_num_nodes(sbml_without_layout):
    number_of_nodes = sbml_without_layout.getNumberOfNodes()
    print("\nnumber of nodes: ", number_of_nodes)
    assert number_of_nodes == TEST_NUMBER_OF_NODES            
    
def test_sbml_without_layout_sbnw_version(sbml_without_layout):
    sbnw_version = sbml_without_layout.SBNW_version
    print("sbnw_version: ", sbnw_version)
    assert sbnw_version == "1.3.27"

def test_sbml_without_layout_input_file(sbml_without_layout):
    sbml_filename_returned = sbml_without_layout.sbml_filename
    print("sbml input file: ", sbml_filename_returned)
    assert sbml_filename_returned == TEST_SBML_FILE_NO_LAYOUT

def test_sbml_without_layout_write_file(sbml_without_layout):
    sbml_without_layout.randomizeLayout()
    sbml_without_layout.doLayoutAlgorithm()
    # Write Model file
    result = sbml_without_layout.writeSBMLWithLayout(TEST_SBML_FILE_WITH_LAYOUT)
    assert result == 0
    assert os.path.isfile(TEST_SBML_FILE_WITH_LAYOUT)
    assert os.stat(TEST_SBML_FILE_WITH_LAYOUT).st_size != 0

def test_sbml_without_layout_arrowhead_style(sbml_without_layout):
    role = sbnw.GF_ROLE_MODIFIER
    print("gf_role_modifier: ", role)
    # style at this point is: 
    ah_style = sbml_without_layout.arrowheadGetStyle(role)
    print("ah style MODIFIER: ", ah_style, ", ", type(ah_style))
    sbml_without_layout.arrowheadSetStyle(role, TEST_ARROWHEAD_STYLE)
    ah_style = sbml_without_layout.arrowheadGetStyle(role)
    print("ah style MODIFIER: ", ah_style, ", ", type(ah_style))
    assert ah_style == TEST_ARROWHEAD_STYLE

def test_sbml_without_layout_string_version(sbml_without_layout):
    # Get String version of the model
    sbml_without_layout.fitToWindow(0,0,300,300)
    # level, version
    sbml_without_layout.setModelNamespace(0, 1)    
    sbml_string = sbml_without_layout.getSBMLWithLayout()
    print("sbml_string: ", type(sbml_string))
    assert "layout" in sbml_string
    #print(sbml_string)
    # what do we see in this string?
    # list of: Compartments, Species, Reactions, Layouts
    # layout: 1024 x 1024
    # 40 x 20 boxes for species

def test_node_information(sbml_with_layout):
    # uses node id
    centroid = sbml_with_layout.nodeGetCentroid("X0")
    # uses node index
    width = sbml_with_layout.nodeGetWidth(0)
    height = sbml_with_layout.nodeGetHeight(0)    
    print("node centroid, x,y: ", centroid.x, ", ", centroid.y)
    print("node width: ", width)
    print("node height: ", height)
    assert centroid.x == 671.0 and centroid.y == -212.0
    assert width == 40
    assert height == 20

#def test_reaction_information(sbml_with_layout):
#    reaction_index = 0
#    reaction_p 
#    centroid = sbml_with_layout.reactionGetCentroid(reaction_index)
#    print("reaction 0 centroid, x,y:", centroid.x, ", ", centroid.y)
#    numSpecies =  
#    numCurves = 
    
# need to free pointers?

def test_sbml_with_layout(sbml_with_layout):
    # Write the file
    result = sbml_with_layout.writeSBMLWithLayout(TEST_SBML_FILE_WITH_LAYOUT_OUTFILE)
    # In PowerShell we see that the diff is 0 between the two written files
    assert result == 0
    assert os.path.isfile(TEST_SBML_FILE_WITH_LAYOUT_OUTFILE)
    assert os.stat(TEST_SBML_FILE_WITH_LAYOUT).st_size != 0    

def test_sbml_with_layout_string_version(sbml_with_layout):  
    sbml_string = sbml_with_layout.getSBMLWithLayout()
    print("sbml_string: ", type(sbml_string))
    assert "layout" in sbml_string
    assert '<layout:position layout:x="651" layout:y="-221"/>' in sbml_string
    #print(sbml_string)

def test_draw_network(sbml_with_layout_modifier):
    sbml_with_layout_modifier.createNetwork()
    print("drawing network")
    sbml_with_layout_modifier.drawNetwork()


    