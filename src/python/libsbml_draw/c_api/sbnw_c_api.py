"""
Sets up the python bindings to the c api.
"""
import ctypes
from pathlib import Path
import pkg_resources
import platform

if platform.system() == "Windows":
    DLL_FILE = Path(pkg_resources.resource_filename(
            "libsbml_draw", "c_api/data/sbnw.dll"))
    slib = ctypes.CDLL(str(DLL_FILE))
elif platform.system() == "Linux":
    SO_FILE = Path(pkg_resources.resource_filename(
            "libsbml_draw", "c_api/data/libsbml_draw.so"))
    slib = ctypes.CDLL(str(SO_FILE))
else:
    DYLIB_FILE = Path(pkg_resources.resource_filename(
            "libsbml_draw", "c_api/data/libsbml_draw.dylib"))
    slib = ctypes.CDLL(str(DYLIB_FILE))

# Enumerations
ROLES = (GF_ROLE_SUBSTRATE,
    GF_ROLE_PRODUCT,
    GF_ROLE_SIDESUBSTRATE,
    GF_ROLE_SIDEPRODUCT,
    GF_ROLE_MODIFIER,
    GF_ROLE_ACTIVATOR,
    GF_ROLE_INHIBITOR) = tuple(map(ctypes.c_uint, range(7)))


# Classes
# The default values for the fr_alg_options are 0's
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
def getCurrentLibraryVersion():
    return slib.gf_getCurrentLibraryVersion().decode('utf-8')


# IO Functions
slib.gf_getSBMLwithLayoutStr.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_getSBMLwithLayoutStr.restype = ctypes.c_char_p
slib.gf_loadSBMLfile.argtypes = [ctypes.c_char_p]
slib.gf_loadSBMLfile.restype = ctypes.c_uint64

slib.gf_loadSBMLbuf.argtypes = [ctypes.c_char_p]
slib.gf_loadSBMLbuf.restype = ctypes.c_uint64

slib.gf_writeSBML.argtypes = [ctypes.c_char_p, ctypes.c_uint64]
slib.gf_writeSBML.restype = ctypes.c_int
slib.gf_writeSBMLwithLayout.argtypes = [ctypes.c_char_p, ctypes.c_uint64,
                                        ctypes.c_uint64]
slib.gf_writeSBMLwithLayout.restype = ctypes.c_int


# IO Functions
def getSBMLwithLayoutStr(h_sbml_model, h_layout_info):
    return slib.gf_getSBMLwithLayoutStr(
            h_sbml_model, h_layout_info).decode('utf-8')


def loadSBMLFile(h_fileName):
    h_filename_string = h_fileName.encode('utf-8')
    return slib.gf_loadSBMLfile(h_filename_string)


def loadSBMLString(h_stringName):
    h_stringname_string = h_stringName.encode('utf-8')
    return slib.gf_loadSBMLbuf(h_stringname_string)


def writeSBMLwithLayout(filename, h_layout, h_layout_info):
    return slib.gf_writeSBMLwithLayout(filename, h_layout, h_layout_info)


def writeSBML(filename, sbml_model):
    filename_string = filename.encode('utf-8')
    return slib.gf_writeSBML(filename_string, sbml_model)


slib.gf_getLastError.restype = ctypes.c_char_p


def getLastError():
    return slib.gf_getLastError()


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


def processLayout(h_model):
    return slib.gf_processLayout(h_model)


def randomizeLayout(h_layout_info):
    return slib.gf_randomizeLayout(h_layout_info)


def doLayoutAlgorithm(layout_options, h_layout_info):
    return slib.gf_doLayoutAlgorithm(layout_options, h_layout_info)


# Model Functions
slib.gf_SBMLModel_newp.restype = ctypes.c_uint64
slib.gf_setModelNamespace.argtypes = [ctypes.c_uint64, ctypes.c_uint64,
                                      ctypes.c_uint64]
slib.gf_setModelNamespace.restype = None


# Model Functions
def SBMLModel_newp():
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
    return slib.gf_getNetworkp(h_layout_info)


def nw_getNodep(h_network, node_index):
    return slib.gf_nw_getNodep(h_network, node_index)


def nw_getNodepFromId(h_network, h_id):
    return slib.gf_nw_getNodepFromId(h_network, h_id)


def nw_getNumCompartments(h_network):
    return slib.gf_nw_getNumComps(h_network)


def nw_getNumNodes(h_network):
    return slib.gf_nw_getNumNodes(h_network)


def nw_getNumRxns(h_network):
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


def node_getCentroid(h_node):
    return slib.gf_node_getCentroid(h_node)


def node_getHeight(h_node):
    return slib.gf_node_getHeight(h_node)


def node_getWidth(h_node):
    return slib.gf_node_getWidth(h_node)


def node_getName(h_node):
    return slib.gf_node_getName(h_node).decode('utf-8')


def node_getID(h_node):
    return slib.gf_node_getID(h_node).decode('utf-8')


# Reaction Information
slib.gf_reaction_getNumCurves.argtypes = [ctypes.c_uint64]
slib.gf_reaction_getNumCurves.restype = ctypes.c_uint64
slib.gf_reaction_getNumSpec.argtypes = [ctypes.c_uint64]
slib.gf_reaction_getNumSpec.restype = ctypes.c_uint64
slib.gf_reaction_getID.argtypes = [ctypes.c_uint64]
slib.gf_reaction_getID.restype = ctypes.c_char_p
slib.gf_reaction_getCentroid.argtypes = [ctypes.c_uint64]
slib.gf_reaction_getCentroid.restype = point


def reaction_getNumCurves(h_reaction):
    return slib.gf_reaction_getNumCurves(h_reaction)


def reaction_getNumSpec(h_reaction):
    return slib.gf_reaction_getNumSpec(h_reaction)


def reaction_getID(h_reaction):
    return slib.gf_reaction_getID(h_reaction).decode('utf-8')


def reaction_getCentroid(h_reaction):
    return slib.gf_reaction_getCentroid(h_reaction)


# Curve Information
slib.gf_reaction_getCurvep.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_reaction_getCurvep.restype = ctypes.c_uint64
slib.gf_getCurveCPs.argtypes = [ctypes.c_uint64]
slib.gf_getCurveCPs.restype = curveCP
slib.gf_curve_getRole.argtypes = [ctypes.c_uint64]
slib.gf_curve_getRole.restype = ctypes.c_uint


def reaction_getCurvep(h_reaction, curve_index):
    return slib.gf_reaction_getCurvep(h_reaction, curve_index)


def getCurveCPs(h_curve):
    return slib.gf_getCurveCPs(h_curve)


def curve_getRole(h_curve):
    return slib.gf_curve_getRole(h_curve)


# Model Sizing Functions
slib.gf_fit_to_window.argtypes = [ctypes.c_uint64, ctypes.c_double,
                                  ctypes.c_double, ctypes.c_double,
                                  ctypes.c_double]


# Model Sizing Functions
def fit_to_window(h_layoutInfo, left, top, right, bottom):
    return slib.gf_fit_to_window(h_layoutInfo, left, top, right, bottom)


# Styling Functions
slib.gf_arrowheadSetStyle.argtypes = [ctypes.c_uint, ctypes.c_int]
slib.gf_arrowheadSetStyle.restype = None
slib.gf_arrowheadGetStyle.argtypes = [ctypes.c_uint]
slib.gf_arrowheadGetStyle.restype = ctypes.c_int
slib.gf_arrowheadNumStyles.restype = ctypes.c_ulong


# Styling Functions
def arrowheadSetStyle(h_role, style):
    return slib.gf_arrowheadSetStyle(h_role, style)


def arrowheadGetStyle(h_role):
    return slib.gf_arrowheadGetStyle(h_role)


def arrowheadNumStyles():
    return slib.gf_arrowheadNumStyles()


# Arrowhead Functions
slib.gf_arrowheadStyleGetNumVerts.argtypes = [ctypes.c_uint]
slib.gf_arrowheadStyleGetNumVerts.restype = ctypes.c_uint
slib.gf_arrowheadStyleGetVert.argtypes = [ctypes.c_uint, ctypes.c_uint]
slib.gf_arrowheadStyleGetVert.restype = point


def arrowheadStyleGetNumVerts(style):
    return slib.gf_arrowheadStyleGetNumVerts(style)


def arrowheadStyleGetVert(style, vertex_number):
    return slib.gf_arrowheadStyleGetVert(style, vertex_number)


slib.readSBMLFromFile.argtypes = [ctypes.c_char_p]
slib.readSBMLFromFile.restype = ctypes.c_uint64
slib.readSBMLFromString.argtypes = [ctypes.c_char_p]
slib.readSBMLFromString.restype = ctypes.c_uint64


# Compartment Functions

slib.gf_compartment_getMinCorner.argtypes = [ctypes.c_uint64]
slib.gf_compartment_getMinCorner.restype = point
slib.gf_compartment_getMaxCorner.argtypes = [ctypes.c_uint64]
slib.gf_compartment_getMaxCorner.restype = point
slib.gf_compartment_getHeight.argtypes = [ctypes.c_uint64]
slib.gf_compartment_getHeight.restype = ctypes.c_double
slib.gf_compartment_getWidth.argtypes = [ctypes.c_uint64]
slib.gf_compartment_getWidth.restype = ctypes.c_double
slib.gf_compartment_getID.argtypes = [ctypes.c_uint64]
slib.gf_compartment_getID.restype = ctypes.c_char_p


def compartment_getMinCorner(h_compartment):
    return slib.gf_compartment_getMinCorner(h_compartment)

       
def compartment_getMaxCorner(h_compartment):
    return slib.gf_compartment_getMaxCorner(h_compartment)
    

def compartment_getHeight(h_compartment):
    return slib.gf_compartment_getHeight(h_compartment)

     
def compartment_getWidth(h_compartment): 
    return slib.gf_compartment_getWidth(h_compartment)


def compartment_getID(h_compartment):
    return slib.gf_compartment_getID(h_compartment)


# libsbml Functions

def readSBMLFromFile(sbml_file):
    return slib.readSBMLFromFile(sbml_file.encode('utf-8'))


def readSBMLFromString(sbml_file):
    return slib.readSBMLFromString(sbml_file.encode('utf-8'))


slib.writeSBMLToFile.argtypes = [ctypes.c_uint64, ctypes.c_char_p]
slib.writeSBMLToString.argtypes = [ctypes.c_uint64]
slib.writeSBMLToString.restype = ctypes.c_char_p


def writeSBMLToFile(doc, out_file_name):
    return slib.writeSBMLToFile(doc, out_file_name.encode('utf-8'))
    

def writeSBMLToString(doc):
    return slib.writeSBMLToString(doc).decode('utf-8')


# slib.RelAbsVector.argtypes = [ctypes.c_float]
# slib.RelAbsVector.restype = ctypes.c_uint64


# def RelAbsVector(font_size):
#    return slib.RelAbsVector(font_size)


# slib.RenderExtension.getXmlnsL2.restype = ctypes.c_char_p
# slib.RenderExtension.getXmlnsL3V1V1.restype = ctypes.c_char_p


# def RenderExtension_getXmlnsL2():
#    return slib.RenderExtension.getXmlnsL2()

# def RenderExtension_getXmlnsL3V1V1():
#    return slib.RenderExtension.getXmlnsL3V1V()
