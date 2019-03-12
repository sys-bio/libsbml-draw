"""
Sets up the python bindings to the c api.
"""
import ctypes

import pkg_resources
from pathlib import Path
#libsbmldraw_lib_file = pkg_resources.resource_string("libsbml-draw", "data/libsbml_draw.dll")
#DATA_PATH = pkg_resources.resource_filename("libsbml_draw", "data/")
DLL_FILE = Path(pkg_resources.resource_filename("libsbml_draw", "data/libsbml_draw.dll"))
print("DLL FILE: ", type(DLL_FILE), str(DLL_FILE))
slib = ctypes.CDLL(str(DLL_FILE))

#
#if sys.platform.startswith('win32'):
#    rrInstallFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'bin'))
#    sharedLib = os.path.join(rrInstallFolder, 'roadrunner_c_api.dll')
#    rrLib=CDLL(sharedLib)
#else:
#    rrInstallFolder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'lib'))
#    if os.path.isfile(os.path.join(rrInstallFolder, 'libroadrunner_c_api.so')):
#        sharedLib = os.path.join(rrInstallFolder, 'libroadrunner_c_api.so')
#    elif os.path.isfile(os.path.join(rrInstallFolder, 'libroadrunner_c_api.dylib')):
#        sharedLib = os.path.join(rrInstallFolder, 'libroadrunner_c_api.dylib')
#    else:
#        raise Exception("could not locate RoadRunner shared library")
#    rrLib = cdll.LoadLibrary(sharedLib)

#print("data_path: ", DATA_PATH)
#print("dll file: ", DLL_FILE)

# SBNW DLL
#slib = ctypes.CDLL("libsbml_draw.dll")
#slib = ctypes.CDLL(libsbmldraw_lib_file)
#slib = ctypes.CDLL(r"C:\Users\nrhaw\Documents\Tellurium\libsbml_draw.dll")
#slib = ctypes.CDLL(r"C:\Users\nrhaw\Documents\Tellurium\sbnw.dll")
# slib = ctypes.CDLL ('C:\\Tellurium-Winpython-3.6\\python-3.6.6.amd64\\Lib\\site-packages\\sbnw\\sbnw.dll')
# slib = ctypes.CDLL('C:\Users\nrhaw\Documents\Visual Studio 2017\Projects\sbnw\BUILD\graphfab\Release\sbnw.dll')

# Enumerations
(GF_ROLE_SUBSTRATE,
 GF_ROLE_PRODUCT,
 GF_ROLE_SIDESUBSTRATE,
 GF_ROLE_SIDEPRODUCT,
 GF_ROLE_MODIFIER,
 GF_ROLE_ACTIVATOR,
 GF_ROLE_INHIBITOR) = map(ctypes.c_uint, range(7))

# Classes
class fr_alg_options(ctypes.Structure):
     _fields_ = [("k", ctypes.c_double),
                ("boundary", ctypes.c_int),
                ("mag", ctypes.c_int),
                ("grav", ctypes.c_double),
                ("baryx", ctypes.c_double),
                ("baryy", ctypes.c_double),
                ("autobary", ctypes.c_int),
                ("enable_comps", ctypes.c_int),
                ("prerandom", ctypes.c_int),
                ("padding", ctypes.c_double)]

class point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]

class curveCP(ctypes.Structure):
    _fields_ = [("start", point), 
                ("control_point_1", point),
                ("control_point_2", point),
                ("end", point)]


# Library Info Functions
slib.gf_getCurrentLibraryVersion.restype = ctypes.c_char_p  

# Library Info Functions
def getCurrentLibraryVersion ():
    return slib.gf_getCurrentLibraryVersion().decode('utf-8')

# IO Functions     
slib.gf_getSBMLwithLayoutStr.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_getSBMLwithLayoutStr.restype = ctypes.c_char_p
slib.gf_loadSBMLfile.argtypes = [ctypes.c_char_p]
slib.gf_loadSBMLfile.restype =  ctypes.c_uint64
slib.gf_writeSBML.argtypes = [ctypes.c_char_p, ctypes.c_uint64]
slib.gf_writeSBML.restype = ctypes.c_int
slib.gf_writeSBMLwithLayout.argtypes = [ctypes.c_char_p, ctypes.c_uint64, ctypes.c_uint64]
slib.gf_writeSBMLwithLayout.restype = ctypes.c_int

# IO Functions
def getSBMLwithLayoutStr (h_sbml_model, h_layout_info):
    return slib.gf_getSBMLwithLayoutStr(h_sbml_model, h_layout_info).decode('utf-8')

def loadSBML (h_fileName):
   h_filename_string = h_fileName.encode('utf-8')
   return slib.gf_loadSBMLfile(h_filename_string)      

def writeSBMLwithLayout (filename, h_layout, h_layout_info):
    return slib.gf_writeSBMLwithLayout(filename, h_layout, h_layout_info)

def writeSBML (filename, sbml_model):
    #filename_string = filename.encode('utf-8')
    return slib.gf_writeSBML(filename, sbml_model)

# Layout Functions
slib.gf_nw_isLayoutSpecified.argtypes = [ctypes.c_uint64]
slib.gf_nw_isLayoutSpecified.restype = ctypes.c_uint64
slib.gf_processLayout.argtypes = [ctypes.c_uint64]
slib.gf_processLayout.restype = ctypes.c_uint64
slib.gf_randomizeLayout.argtypes = [ctypes.c_uint64]
slib.gf_randomizeLayout.restype = None
slib.gf_doLayoutAlgorithm.argtypes = [fr_alg_options, ctypes.c_uint64]
slib.gf_doLayoutAlgorithm.restype = None

# Layout Functions
def isLayoutSpecified(h_network):
    return slib.gf_nw_isLayoutSpecified(h_network)

def processLayout (h_layout):
    return slib.gf_processLayout(h_layout)         

def randomizeLayout (h_layout_info):
    return slib.gf_randomizeLayout(h_layout_info)

def doLayoutAlgorithm (layout_options, h_layout_info):
    return slib.gf_doLayoutAlgorithm(layout_options, h_layout_info)

# Model Functions
slib.gf_SBMLModel_newp.restype = ctypes.c_uint64
slib.gf_setModelNamespace.argtypes = [ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64]
slib.gf_setModelNamespace.restype = None

# Model Functions
def SBMLModel_newp ():
  return slib.gf_SBMLModel_newp()

def setModelNamespace(h_layout_info, level, version):
    return slib.gf_setModelNamespace(h_layout_info, level, version)

# Network Functions
slib.gf_getNetworkp.argtypes = [ctypes.c_uint64]
slib.gf_getNetworkp.restype = ctypes.c_uint64
slib.gf_nw_getNodep.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_nw_getNodep.restype = ctypes.c_uint64
slib.gf_nw_getNodepFromId.argtypes = [ctypes.c_uint64, ctypes.c_char_p]
slib.gf_nw_getNodepFromId.restype = ctypes.c_uint64

slib.gf_nw_getNumComps.argtypes = [ctypes.c_uint64]
slib.gf_nw_getNumComps.restype = ctypes.c_uint64
slib.gf_nw_getNumNodes.argtypes = [ctypes.c_uint64]
slib.gf_nw_getNumNodes.restype = ctypes.c_uint64
slib.gf_nw_getNumRxns.argtypes = [ctypes.c_uint64]
slib.gf_nw_getNumRxns.restype = ctypes.c_uint64

slib.gf_nw_getRxnp.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_nw_getRxnp.restype = ctypes.c_uint64

# Network Functions
def getNetworkp(h_layout_info):
    return slib.gf_getNetworkp (h_layout_info)    

def nw_getNodep(h_network, node_index):
    return slib.gf_nw_getNodep(h_network, node_index)

def nw_getNodepFromId (h_network, h_id):
    return slib.gf_nw_getNodepFromId(h_network, h_id)

def nw_getNumCompartments (h_network):
    return slib.gf_nw_getNumComps(h_network)

def nw_getNumNodes(h_network):
    return slib.gf_nw_getNumNodes(h_network)

def nw_getNumRxns (h_network):
    return slib.gf_nw_getNumRxns(h_network)

def nw_getReactionp(h_network, reaction_index):
    return slib.gf_nw_getRxnp(h_network, reaction_index)

# Node Information
slib.gf_node_getCentroid.argtypes = [ctypes.c_uint64]
slib.gf_node_getCentroid.restype = point
slib.gf_node_getHeight.argtypes = [ctypes.c_uint64]
slib.gf_node_getHeight.restype = ctypes.c_double
slib.gf_node_getWidth.argtypes = [ctypes.c_uint64]
slib.gf_node_getWidth.restype = ctypes.c_double
slib.gf_node_getName.argtypes = [ctypes.c_uint64]
slib.gf_node_getName.restype = ctypes.c_char_p
slib.gf_node_getID.argtypes = [ctypes.c_uint64]
slib.gf_node_getID.restype = ctypes.c_char_p

def node_getCentroid (h_node):
    return slib.gf_node_getCentroid(h_node)

def node_getHeight (h_node):
    return slib.gf_node_getHeight(h_node)

def node_getWidth (h_node):
    return slib.gf_node_getWidth(h_node)

def node_getName (h_node):
    return slib.gf_node_getName(h_node).decode('utf-8')

def node_getID (h_node):
    return slib.gf_node_getID(h_node).decode('utf-8')

# Reaction Information
slib.gf_reaction_getNumCurves.argtypes = [ctypes.c_uint64]
slib.gf_reaction_getNumCurves.restype = ctypes.c_uint64
slib.gf_reaction_getNumSpec.argtypes = [ctypes.c_uint64]
slib.gf_reaction_getNumSpec.restype = ctypes.c_uint64
slib.gf_reaction_getID.argtypes = [ctypes.c_uint64]
slib.gf_reaction_getID.restype = ctypes.c_char_p

def reaction_getNumCurves (h_reaction):
    return slib.gf_reaction_getNumCurves(h_reaction)

def reaction_getNumSpec (h_reaction):
    return slib.gf_reaction_getNumSpec(h_reaction)

def reaction_getID (h_reaction):
    return slib.gf_reaction_getID(h_reaction).decode('utf-8')

# Curve Information
slib.gf_reaction_getCurvep.argtypes = [ctypes.c_uint64, ctypes.c_uint64] 
slib.gf_reaction_getCurvep.restype = ctypes.c_uint64
slib.gf_getCurveCPs.argtypes = [ctypes.c_uint64] 
slib.gf_getCurveCPs.restype = curveCP
slib.gf_curve_getRole.argtypes = [ctypes.c_uint64]
slib.gf_curve_getRole.restype = ctypes.c_uint

def reaction_getCurvep (h_reaction, curve_index):
    return slib.gf_reaction_getCurvep(h_reaction, curve_index)

def getCurveCPs(h_curve):
    return slib.gf_getCurveCPs(h_curve)

def curve_getRole(h_curve):
    return slib.gf_curve_getRole(h_curve)
    
# Model Sizing Functions
slib.gf_fit_to_window.argtypes = [ctypes.c_uint64, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
slib.gf_fit_to_window.restype = None

# Model Sizing Functions
def fit_to_window (h_layoutInfo, left, top, right, bottom):
    return slib.gf_fit_to_window(h_layoutInfo, left, top, right, bottom)

# Styling Functions
slib.gf_arrowheadSetStyle.argtypes = [ctypes.c_uint, ctypes.c_int]
slib.gf_arrowheadSetStyle.restype = None
slib.gf_arrowheadGetStyle.argtypes = [ctypes.c_uint]
slib.gf_arrowheadGetStyle.restype = ctypes.c_int    

# Styling Functions
def arrowheadSetStyle (h_role, style):
    return slib.gf_arrowheadSetStyle(h_role, style)

def arrowheadGetStyle (h_role):
    return slib.gf_arrowheadGetStyle(h_role)




