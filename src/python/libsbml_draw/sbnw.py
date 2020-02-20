"""
Sets up the python bindings to the c api.
"""
import ctypes
import os
import platform
from ctypes import POINTER


def load_sbnw():
    directory = os.path.dirname(__file__)
    if platform.system() == "Windows":
        lib = os.path.join(directory, 'libsbml_draw.dll')
    elif platform.system() == "Linux":
        lib = os.path.join(directory, 'libsbml_draw.so')
    else:
        lib = os.path.join(directory, 'libsbml_draw.dylib')
    if not os.path.isfile(lib):
        raise FileNotFoundError('Did not find the libsbml-draw c api "{}"'.format(lib))
    lib = os.path.join(os.path.dirname(__file__), lib)
    return ctypes.CDLL(lib)


slib = load_sbnw()

# Enumerations
ROLES = (GF_ROLE_SUBSTRATE,
         GF_ROLE_PRODUCT,
         GF_ROLE_SIDESUBSTRATE,
         GF_ROLE_SIDEPRODUCT,
         GF_ROLE_MODIFIER,
         GF_ROLE_ACTIVATOR,
         GF_ROLE_INHIBITOR) = tuple(map(ctypes.c_uint, range(7)))


# Classes
class FrAlgOptions(ctypes.Structure):
    _fields_ = [("k", ctypes.c_double),
                ("gravity", ctypes.c_double),
                ("baryx", ctypes.c_double),
                ("baryy", ctypes.c_double),
                ("autobary", ctypes.c_int),
                ("padding", ctypes.c_double)]


class Point(ctypes.Structure):
    _fields_ = [("x", ctypes.c_double),
                ("y", ctypes.c_double)]


class CurveCP(ctypes.Structure):
    _fields_ = [("start", Point),
                ("control_point_1", Point),
                ("control_point_2", Point),
                ("end", Point)]


class GFCurve(ctypes.Structure):
    _fields_ = [("c", ctypes.c_void_p)]


class LayoutInfo(ctypes.Structure):
    _fields_ = [
        ("net", ctypes.c_void_p),
        ("canv", ctypes.c_void_p),
        ("cont", ctypes.c_char_p),
        ("level", ctypes.c_int),
        ("version", ctypes.c_int)
    ]


class Canvas(ctypes.Structure):
    _fields_ = [("canv", ctypes.c_void_p)]


class SBMLModel(ctypes.Structure):
    _fields_ = [("pdoc", ctypes.c_void_p)]


# Library Info Functions
slib.gf_getCurrentLibraryVersion.restype = ctypes.c_char_p


# Library Info Functions
def getCurrentLibraryVersion():
    return slib.gf_getCurrentLibraryVersion().decode('utf-8')


# Canvas Functions
slib.gf_getCanvasp.argtypes = [POINTER(LayoutInfo)]
slib.gf_getCanvasp.restype = POINTER(Canvas)

slib.gf_canvGetWidth.argtypes = [POINTER(Canvas)]
slib.gf_canvGetWidth.restype = ctypes.c_int
slib.gf_canvGetHeight.argtypes = [POINTER(Canvas)]
slib.gf_canvGetHeight.restype = ctypes.c_int


def getCanvasp(h_layout_info):
    return slib.gf_getCanvasp(h_layout_info)


def canvas_getWidth(h_canvas):
    return slib.gf_canvGetWidth(h_canvas)


def canvas_getHeight(h_canvas):
    return slib.gf_canvGetHeight(h_canvas)


# alternative to FitToWindow, returns void
slib.gf_layout_alignToOrigin.argtypes = [POINTER(LayoutInfo), ctypes.c_double,
                                         ctypes.c_double]
slib.gf_layout_alignToOrigin.restype = None


def layout_alignToOrigin(h_layoutInfo, pad_x, pad_y):
    return slib.gf_layout_alignToOrigin(h_layoutInfo, pad_x, pad_y)


# IO Functions
slib.gf_getSBMLwithLayoutStr.argtypes = [ctypes.c_uint64, POINTER(LayoutInfo), ctypes.c_int]
slib.gf_getSBMLwithLayoutStr.restype = ctypes.c_char_p
slib.gf_loadSBMLfile.argtypes = [ctypes.c_char_p]
slib.gf_loadSBMLfile.restype = ctypes.c_uint64

slib.gf_loadSBMLbuf.argtypes = [ctypes.c_char_p]
slib.gf_loadSBMLbuf.restype = ctypes.c_uint64


def getSBMLwithLayoutStr(h_sbml_model, h_layout_info,
                         useLastTransformedCoordinates):
    return slib.gf_getSBMLwithLayoutStr(
        h_sbml_model, h_layout_info,
        useLastTransformedCoordinates).decode('utf-8')


def loadSBMLFile(h_fileName):
    h_filename_string = h_fileName.encode('utf-8')
    return slib.gf_loadSBMLfile(h_filename_string)


def loadSBMLString(h_stringName):
    h_stringname_string = h_stringName.encode('utf-8')
    return slib.gf_loadSBMLbuf(h_stringname_string)


slib.gf_writeSBML.argtypes = [ctypes.c_char_p, POINTER(SBMLModel)]
slib.gf_writeSBML.restype = None


def writeSBML(filename, h_sbml_model):
    """
    Original signature:

        int gf_writeSBML(const char* filename, gf_SBMLModel* m) {

    Returns:

    """

    return slib.gf_writeSBML(filename, h_sbml_model)


slib.gf_writeSBMLwithLayout.argtypes = [ctypes.c_char_p, ctypes.c_uint64, POINTER(LayoutInfo)]
slib.gf_writeSBMLwithLayout.restypes = None


def writeSBMLwithLayout(filename, model, layout):
    """
    original signture:
            const char* filename, gf_SBMLModel* m, gf_layoutInfo* l
    Args:
        model:
        layout:

    Returns:

    """
    return slib.gf_writeSBMLwithLayout(filename, model, layout)


# error stuff
slib.gf_getLastError.restype = ctypes.c_char_p


def getLastError():
    return slib.gf_getLastError()


# Layout Functions
slib.gf_nw_isLayoutSpecified.argtypes = [ctypes.c_uint64]
slib.gf_nw_isLayoutSpecified.restype = ctypes.c_uint64
slib.gf_processLayout.argtypes = [ctypes.c_uint64]
slib.gf_processLayout.restype = POINTER(LayoutInfo)
slib.gf_randomizeLayout.argtypes = [POINTER(LayoutInfo)]
slib.gf_randomizeLayout.restype = None
slib.gf_doLayoutAlgorithm.argtypes = [FrAlgOptions, POINTER(LayoutInfo)]
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
slib.gf_setModelNamespace.argtypes = [POINTER(LayoutInfo), ctypes.c_uint64,
                                      ctypes.c_uint64]
slib.gf_setModelNamespace.restype = None


# Model Functions
def SBMLModel_newp():
    return slib.gf_SBMLModel_newp()


def setModelNamespace(h_layout_info, level, version):
    return slib.gf_setModelNamespace(h_layout_info, level, version)


# Network Functions
slib.gf_getNetworkp.argtypes = [POINTER(LayoutInfo)]
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

slib.gf_nw_newAliasNodep.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_nw_newAliasNodep.restype = ctypes.c_uint64
slib.gf_nw_getAliasInstancep.argtypes = [ctypes.c_uint64, ctypes.c_uint64,
                                         ctypes.c_uint64]
slib.gf_nw_getAliasInstancep.restype = ctypes.c_uint64
slib.gf_nw_getNumAliasInstances.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_nw_getNumAliasInstances.restype = ctypes.c_int

slib.gf_nw_rebuildCurves.argtypes = [ctypes.c_uint64]
slib.gf_nw_recenterJunctions.argtypes = [ctypes.c_uint64]


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


def nw_newAliasNodep(h_network, h_node):
    return slib.gf_nw_newAliasNodep(h_network, h_node)


def nw_getAliasInstancep(h_network, h_node, alias_index):
    return slib.gf_nw_getAliasInstancep(h_network, h_node, alias_index)


def nw_getNumAliasInstances(h_network, h_node):
    return slib.gf_nw_getNumAliasInstances(h_network, h_node)


def nw_recenterJunctions(h_network):
    return slib.gf_nw_recenterJunctions(h_network)


def nw_rebuildCurves(h_network):
    return slib.gf_nw_rebuildCurves(h_network)


# _Node Information
slib.gf_node_getCentroid.argtypes = [ctypes.c_uint64]
slib.gf_node_getCentroid.restype = Point
slib.gf_node_setCentroid.argtypes = [ctypes.c_uint64, Point]

slib.gf_node_getHeight.argtypes = [ctypes.c_uint64]
slib.gf_node_getHeight.restype = ctypes.c_double
slib.gf_node_setHeight.argtypes = [ctypes.c_uint64, ctypes.c_double]

slib.gf_node_getWidth.argtypes = [ctypes.c_uint64]
slib.gf_node_getWidth.restype = ctypes.c_double
slib.gf_node_setWidth.argtypes = [ctypes.c_uint64, ctypes.c_double]

slib.gf_node_getName.argtypes = [ctypes.c_uint64]
slib.gf_node_getName.restype = ctypes.c_char_p
slib.gf_node_getID.argtypes = [ctypes.c_uint64]
slib.gf_node_getID.restype = ctypes.c_char_p

slib.gf_node_isLocked.argtypes = [ctypes.c_uint64]
slib.gf_node_isLocked.restype = ctypes.c_int
slib.gf_node_lock.argtypes = [ctypes.c_uint64]
slib.gf_node_unlock.argtypes = [ctypes.c_uint64]

slib.gf_node_make_alias.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_node_make_alias.restype = ctypes.c_int
slib.gf_node_isAliased.argtypes = [ctypes.c_uint64]
slib.gf_node_isAliased.restype = ctypes.c_int

slib.gf_node_getAttachedCurves.argtypes = [ctypes.c_uint64, ctypes.c_uint64,
                                           POINTER(ctypes.c_uint),
                                           POINTER(POINTER(GFCurve))]
slib.gf_node_getAttachedCurves.restype = ctypes.c_int


def node_getAttachedCurves(h_node, h_network):
    num_curves = ctypes.c_uint(0)

    h_curves = POINTER(GFCurve)()

    slib.gf_node_getAttachedCurves(h_node, h_network, ctypes.byref(num_curves),
                                   ctypes.byref(h_curves))

    return [h_curves[k] for k in range(num_curves.value)]


def node_getCentroid(h_node):
    return slib.gf_node_getCentroid(h_node)


def node_setCentroid(h_node, point):
    return slib.gf_node_setCentroid(h_node, point)


def node_getHeight(h_node):
    return slib.gf_node_getHeight(h_node)


def node_setHeight(h_node, height):
    return slib.gf_node_setHeight(h_node, height)


def node_getWidth(h_node):
    return slib.gf_node_getWidth(h_node)


def node_setWidth(h_node, width):
    return slib.gf_node_setWidth(h_node, width)


def node_getName(h_node):
    return slib.gf_node_getName(h_node).decode('utf-8')


def node_getID(h_node):
    return slib.gf_node_getID(h_node).decode('utf-8')


def node_isLocked(h_node):
    return slib.gf_node_isLocked(h_node)


def node_lock(h_node):
    return slib.gf_node_lock(h_node)


def node_unlock(h_node):
    return slib.gf_node_unlock(h_node)


def node_make_alias(h_node, h_network):
    return slib.gf_node_make_alias(h_node, h_network)


def node_isAliased(h_node):
    return slib.gf_node_isAliased(h_node)


# Reaction Information
slib.gf_reaction_getNumCurves.argtypes = [ctypes.c_uint64]
slib.gf_reaction_getNumCurves.restype = ctypes.c_uint64
slib.gf_reaction_getNumSpec.argtypes = [ctypes.c_uint64]
slib.gf_reaction_getNumSpec.restype = ctypes.c_uint64
slib.gf_reaction_getID.argtypes = [ctypes.c_uint64]
slib.gf_reaction_getID.restype = ctypes.c_char_p
slib.gf_reaction_getCentroid.argtypes = [ctypes.c_uint64]
slib.gf_reaction_getCentroid.restype = Point


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
slib.gf_reaction_getCurvep.restype = POINTER(GFCurve)

slib.gf_getCurveCPs.argtypes = [POINTER(GFCurve)]
slib.gf_getCurveCPs.restype = CurveCP

slib.gf_curve_getRole.argtypes = [POINTER(GFCurve)]
slib.gf_curve_getRole.restype = ctypes.c_uint


def reaction_getCurvep(h_reaction, curve_index):
    return slib.gf_reaction_getCurvep(h_reaction, curve_index)


def getCurveCPs(h_curve):
    return slib.gf_getCurveCPs(h_curve)


def curve_getRole(h_curve):
    return slib.gf_curve_getRole(h_curve)


# Model Sizing Functions
slib.gf_fit_to_window.argtypes = [POINTER(LayoutInfo), ctypes.c_double,
                                  ctypes.c_double, ctypes.c_double,
                                  ctypes.c_double]


# Model Sizing Functions
def fit_to_window(h_layout_info, left, top, right, bottom):
    return slib.gf_fit_to_window(h_layout_info, left, top, right, bottom)


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
slib.gf_arrowheadStyleGetVert.restype = Point


def arrowheadStyleGetNumVerts(style):
    return slib.gf_arrowheadStyleGetNumVerts(style)


def arrowheadStyleGetVert(style, vertex_number):
    return slib.gf_arrowheadStyleGetVert(style, vertex_number)


# Compartment Functions

slib.gf_nw_getCompartmentp.argtypes = [ctypes.c_uint64]
slib.gf_nw_getCompartmentp.restype = ctypes.c_uint64
slib.gf_compartment_getMinCorner.argtypes = [ctypes.c_uint64]
slib.gf_compartment_getMinCorner.restype = Point
slib.gf_compartment_getMaxCorner.argtypes = [ctypes.c_uint64]
slib.gf_compartment_getMaxCorner.restype = Point
slib.gf_compartment_getHeight.argtypes = [ctypes.c_uint64]
slib.gf_compartment_getHeight.restype = ctypes.c_double
slib.gf_compartment_getWidth.argtypes = [ctypes.c_uint64]
slib.gf_compartment_getWidth.restype = ctypes.c_double
slib.gf_compartment_getID.argtypes = [ctypes.c_uint64]
slib.gf_compartment_getID.restype = ctypes.c_char_p


def nw_getCompartmentp(h_network, compartment_index):
    return slib.gf_nw_getCompartmentp(h_network, compartment_index)


def compartment_getMinCorner(h_compartment):
    return slib.gf_compartment_getMinCorner(h_compartment)


def compartment_getMaxCorner(h_compartment):
    return slib.gf_compartment_getMaxCorner(h_compartment)


def compartment_getHeight(h_compartment):
    return slib.gf_compartment_getHeight(h_compartment)


def compartment_getWidth(h_compartment):
    return slib.gf_compartment_getWidth(h_compartment)


def compartment_getID(h_compartment):
    return slib.gf_compartment_getID(h_compartment).decode("utf-8")


slib.gf_reaction_hasSpec.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_reaction_hasSpec.restype = ctypes.c_int


def reaction_hasSpec(h_reaction, h_species):
    return not not slib.gf_reaction_hasSpec(h_reaction, h_species)


slib.gf_reaction_recenter.argtypes = [ctypes.c_uint64]


def reaction_recenter(h_reaction):
    return not not slib.gf_reaction_recenter(h_reaction)
