# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 15:21:36 2019

@author: nrhaw
"""

import ctypes
    
# SBNW DLL
slib = ctypes.CDLL ('C:\\Tellurium-Winpython-3.6\\python-3.6.6.amd64\\Lib\\site-packages\\sbnw\\sbnw.dll')
# slib = ctypes.CDLL('C:\Users\nrhaw\Documents\Visual Studio 2017\Projects\sbnw\BUILD\graphfab\Release\sbnw.dll')

# Typedefs

# Enumerations
(GF_ROLE_SUBSTRATE,
 GF_ROLE_PRODUCT,
 GF_ROLE_SIDESUBSTRATE,
 GF_ROLE_SIDEPRODUCT,
 GF_ROLE_MODIFIER,
 GF_ROLE_ACTIVATOR,
 GF_ROLE_INHIBITOR) = map(ctypes.c_uint, range(7))

print("GF_ROLE_SUBSTRATE: ", GF_ROLE_SUBSTRATE)
print("GF_ROLE_SIDEPRODUCT: ", GF_ROLE_SIDEPRODUCT)
print("GF_ROLE_INHIBITOR: ", GF_ROLE_INHIBITOR)
print()

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
    _fields_ = [("s", point), 
                ("c1", point),
                ("c2", point),
                ("e", point)]


# Error Functions
# slib.gf_clearError.argtypes = [ctypes.c_void_p]
slib.gf_clearError.restype = None

# slib.gf_getLastError.argtypes = [ctypes.c_void_p] 
slib.gf_getLastError.restype = ctypes.c_char_p 

# slib.gf_haveError.argtypes = [ctypes.c_void_p]
slib.gf_haveError.restype = ctypes.c_uint64    

# IO Functions     
slib.gf_loadSBMLfile.argtypes = [ctypes.c_char_p]
slib.gf_loadSBMLfile.restype =  ctypes.c_uint64
slib.gf_writeSBML.argtypes = [ctypes.c_char_p, ctypes.c_uint64]
slib.gf_writeSBML.restype = ctypes.c_int
slib.gf_writeSBMLwithLayout.argtypes = [ctypes.c_char_p, ctypes.c_uint64, ctypes.c_uint64]
slib.gf_writeSBMLwithLayout.restype = ctypes.c_int
slib.gf_loadSBMLbuf.argtypes = [ctypes.c_char_p]
slib.gf_loadSBMLbuf.restype = ctypes.c_uint64

# Free Functions
slib.gf_freeLayoutInfo.argtypes = [ctypes.c_uint64]
slib.gf_freeLayoutInfo.restype = None
slib.gf_freeLayoutInfoHierarch.argtypes = [ctypes.c_uint64] 
slib.gf_freeLayoutInfoHierarch.restype = None
slib.gf_freeModelAndLayout.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_freeModelAndLayout.restype = None
slib.gf_free.argtypes = [ctypes.c_void_p]
slib.gf_free.restype = None
slib.gf_freeSBMLModel.argtypes = [ctypes.c_uint64]
slib.gf_freeSBMLModel.restype = None
slib.gf_strfree.argtypes = [ctypes.c_char_p]
slib.gf_strfree.restype = None

# Layout Functions
slib.gf_processLayout.argtypes = [ctypes.c_uint64]
slib.gf_processLayout.restype = ctypes.c_uint64
slib.gf_randomizeLayout.argtypes = [ctypes.c_uint64]
slib.gf_randomizeLayout.restype = None
slib.gf_randomizeLayout2.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_randomizeLayout2.restype = None
slib.gf_randomizeLayout_fromExtents.argtypes = [ctypes.c_uint64, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double] 
slib.gf_randomizeLayout_fromExtents.restype = None
slib.gf_doLayoutAlgorithm.argtypes = [fr_alg_options, ctypes.c_uint64]
slib.gf_doLayoutAlgorithm.restype = None
slib.gf_layoutInfo_newp.argtypes = [ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64]
slib.gf_layoutInfo_newp.restype = ctypes.c_uint64
slib.gf_doLayoutAlgorithm2.argtypes = [ctypes.POINTER(fr_alg_options), ctypes.c_uint64, ctypes.c_uint64]
slib.gf_doLayoutAlgorithm2.restype = None
slib.gf_getLayoutOptDefaults.argtypes = [ctypes.POINTER(fr_alg_options)]
slib.gf_getLayoutOptDefaults.restype = None
slib.gf_layout_setStiffness.argtypes = [ctypes.POINTER(fr_alg_options), ctypes.c_double]
slib.gf_layout_setStiffness.restype = None

# Library Info Functions
# slib.gf_getCurrentLibraryVersion.argtypes = [ctypes.c_void_p]
slib.gf_getCurrentLibraryVersion.restype = ctypes.c_char_p     

# Model Functions
# slib.gf_SBMLModel_newp.argtypes = [None]
slib.gf_SBMLModel_newp.restype = ctypes.c_uint64
slib.gf_setModelNamespace.argtypes = [ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64]
slib.gf_setModelNamespace.restype = None
slib.gf_getSBMLwithLayoutStr.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_getSBMLwithLayoutStr.restype = ctypes.c_char_p

# Compartment Functions
slib.gf_getDefaultCompartmentId.restype = ctypes.c_char_p
slib.gf_setDefaultCompartmentId.argtypes = [ctypes.c_char_p]
slib.gf_setDefaultCompartmentId.restype = None
slib.gf_node_setCompartment.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_releaseCompartment.argtypes = [ctypes.c_uint64]
slib.gf_releaseCompartment.restype = None
slib.gf_compartment_getID.argtypes = [ctypes.c_uint64]
slib.gf_compartment_getID.restype = ctypes.c_char_p
slib.gf_compartment_getMinCorner.argtypes = [ctypes.c_uint64]
slib.gf_compartment_getMinCorner.restype = ctypes.Structure
slib.gf_compartment_setMinCorner.argtypes = [ctypes.c_uint64, ctypes.Structure]
slib.gf_compartment_setMinCorner.restype = None
slib.gf_compartment_getMaxCorner.argtypes = [ctypes.c_uint64] 
slib.gf_compartment_getMaxCorner.restype = ctypes.Structure
slib.gf_compartment_setMaxCorner.argtypes = [ctypes.c_uint64, ctypes.Structure]
slib.gf_compartment_setMaxCorner.restype = None
slib.gf_compartment_getWidth.argtypes = [ctypes.c_uint64]
slib.gf_compartment_getWidth.restype = ctypes.c_double
slib.gf_compartment_getHeight.argtypes = [ctypes.c_uint64]
slib.gf_compartment_getHeight.restype = ctypes.c_double
slib.gf_compartment_getNumElt.argtypes = [ctypes.c_uint64]
slib.gf_compartment_getNumElt.restype = ctypes.c_uint64
slib.gf_compartment_addNode.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_compartment_addNode.restype = ctypes.c_int
slib.gf_compartment_removeNode.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_compartment_removeNode.restype = ctypes.c_int
slib.gf_compartment_containsNode.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_compartment_containsNode.restype = ctypes.c_int
slib.gf_compartment_containsReaction.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_compartment_containsReaction.restype = ctypes.c_int

# Network Functions
slib.gf_getNetworkp.argtypes = [ctypes.c_uint64]
slib.gf_getNetworkp.restype = ctypes.c_uint64
slib.gf_clearNetwork.argtypes = [ctypes.c_uint64]
slib.gf_clearNetwork.restype = None
slib.gf_releaseNetwork.argtypes = [ctypes.c_uint64]
slib.gf_releaseNetwork.restype = None
slib.gf_nw_getId.argtypes = [ctypes.c_uint64]
slib.gf_nw_getId.restype = ctypes.c_char_p 
slib.gf_nw_setId.argtypes = [ctypes.c_uint64, ctypes.c_char_p]
slib.gf_nw_setId.restype = None
slib.gf_nw_getNumNodes.argtypes = [ctypes.c_uint64]
slib.gf_nw_getNumNodes.restype = ctypes.c_uint64
slib.gf_nw_getNumUniqueNodes.argtypes = [ctypes.c_uint64]
slib.gf_nw_getNumUniqueNodes.restype = ctypes.c_uint64
slib.gf_nw_getNumRxns.argtypes = [ctypes.c_uint64]
slib.gf_nw_getNumRxns.restype = ctypes.c_uint64
slib.gf_nw_getNumComps.argtypes = [ctypes.c_uint64]
slib.gf_nw_getNumComps.restype = ctypes.c_uint64
slib.gf_nw_getNodep.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_nw_getNodep.restype = ctypes.c_uint64
slib.gf_nw_getUniqueNodep.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_nw_getUniqueNodep.restype = ctypes.c_uint64
slib.gf_nw_getNodepFromId.argtypes = [ctypes.c_uint64, ctypes.c_char_p]
slib.gf_nw_getNodepFromId.restype = ctypes.c_uint64
slib.gf_nw_getRxnp.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_nw_getRxnp.restype = ctypes.c_uint64
slib.gf_nw_removeRxn.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_nw_removeRxn.restype = None
slib.gf_nw_getCompartmentp.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_nw_getCompartmentp.restype = ctypes.c_uint64
slib.gf_nw_findCompartmentById.argtypes = [ctypes.c_uint64, ctypes.c_char_p]
slib.gf_nw_findCompartmentById.restype = ctypes.c_uint64
slib.gf_nw_rebuildCurves.argtypes = [ctypes.c_uint64]
slib.gf_nw_rebuildCurves.restype = None
slib.gf_nw_recenterJunctions.argtypes = [ctypes.c_uint64]
slib.gf_nw_recenterJunctions.restype = None
slib.gf_nw_newCompartmentp.argtypes = [ctypes.c_uint64, ctypes.c_char_p, ctypes.c_char_p]
slib.gf_nw_newCompartmentp.restype = ctypes.c_uint64
slib.gf_nw_newNodep.argtypes = [ctypes.c_uint64, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_uint64] 
slib.gf_nw_newNodep.restype = ctypes.c_uint64
slib.gf_nw_newAliasNodep.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_nw_newAliasNodep.restype = ctypes.c_uint64
slib.gf_nw_removeNode.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_nw_removeNode.restype = ctypes.c_uint64
slib.gf_nw_connectNode.argtypes = [ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64] 
slib.gf_nw_connectNode.restype = ctypes.c_int
slib.gf_nw_connectNodeRoleStr.argtypes = [ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_char_p] 
slib.gf_nw_connectNodeRoleStr.restype = ctypes.c_int
slib.gf_nw_isNodeConnected.argtypes = [ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64]
slib.gf_nw_isNodeConnected.restype = ctypes.c_int
slib.gf_nw_isLayoutSpecified.argtypes = [ctypes.c_uint64]
slib.gf_nw_isLayoutSpecified.restype = ctypes.c_int
slib.gf_nw_getNumAliasInstances.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_nw_getNumAliasInstances.restype = ctypes.c_uint64
slib.gf_nw_getAliasInstancep.argtypes = [ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64]
slib.gf_nw_getAliasInstancep.restype = ctypes.c_uint64

# _Node Functions
slib.gf_node_setCompartment.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_node_setCompartment.restype = None
slib.gf_releaseNode.argtypes = [ctypes.c_uint64]
slib.gf_releaseNode.restype = None
slib.gf_node_isLocked.argtypes = [ctypes.c_uint64]
slib.gf_node_isLocked.restype = ctypes.c_int
slib.gf_node_lock.argtypes = [ctypes.c_uint64]
slib.gf_node_lock.restype = None
slib.gf_node_unlock.argtypes = [ctypes.c_uint64]
slib.gf_node_unlock.restype = None
slib.gf_node_make_alias.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_node_make_alias.restype = ctypes.c_int
slib.gf_node_isAliased.argtypes = [ctypes.c_uint64]
slib.gf_node_isAliased.restype = ctypes.c_int
slib.gf_node_getCentroid.argtypes = [ctypes.c_uint64]
slib.gf_node_getCentroid.restype = ctypes.Structure
# slib.gf_node_getCentroidXY.argtypes = [ctypes.c_uint64, ctypes.c_double, ctypes.c_double]
slib.gf_node_setCentroid.argtypes = [ctypes.c_uint64, ctypes.Structure]
slib.gf_node_setCentroid.restype = None
slib.gf_node_getWidth.argtypes = [ctypes.c_uint64]
slib.gf_node_getWidth.restype = ctypes.c_double
slib.gf_node_setWidth.argtypes = [ctypes.c_uint64, ctypes.c_double]
slib.gf_node_setWidth.restype = None
slib.gf_node_getHeight.argtypes = [ctypes.c_uint64]
slib.gf_node_getHeight.restype = ctypes.c_double
slib.gf_node_setHeight.argtypes = [ctypes.c_uint64, ctypes.c_double]
slib.gf_node_setHeight.restype = None
slib.gf_node_getID.argtypes = [ctypes.c_uint64]
slib.gf_node_getID.restype = ctypes.c_char_p
slib.gf_node_setID.argtypes = [ctypes.c_uint64, ctypes.c_char_p]
slib.gf_node_setID.restype = None
slib.gf_node_getName.argtypes = [ctypes.c_uint64]
slib.gf_node_getName.restype = ctypes.c_char_p
slib.gf_node_setName.argtypes = [ctypes.c_uint64, ctypes.c_char_p]
slib.gf_node_setName.restype = None
slib.gf_node_getConnectedReactions.argtypes = [ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64] 
slib.gf_node_getConnectedReactions.restype = ctypes.c_int
slib.gf_node_getAttachedCurves.argtypes = [ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64, ctypes.c_uint64] 
slib.gf_node_getAttachedCurves.restype = ctypes.c_int
slib.gf_nw_nodeHasCompartment.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_nw_nodeHasCompartment.restype = ctypes.c_int
slib.gf_nw_nodeGetCompartment.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_nw_nodeGetCompartment.restype = ctypes.c_uint64
slib.gf_aliasNodebyDegree.argtypes = [ctypes.c_uint64, ctypes.c_int]
slib.gf_aliasNodebyDegree.restype = None

# Reaction Functions
slib.gf_releaseRxn.argtypes = [ctypes.c_uint64]
slib.gf_releaseRxn.restype = None
slib.gf_nw_newReactionp.argtypes = [ctypes.c_uint64, ctypes.c_char_p, ctypes.c_char_p]
slib.gf_nw_newReactionp.restype = ctypes.c_uint64
slib.gf_reaction_getID.argtypes = [ctypes.c_uint64]
slib.gf_reaction_getID.restype = ctypes.c_char_p
slib.gf_reaction_getCentroid.argtypes = [ctypes.c_uint64]
slib.gf_reaction_getCentroid.restype = ctypes.Structure
slib.gf_reaction_setCentroid.argtypes = [ctypes.c_uint64, ctypes.Structure]
slib.gf_reaction_setCentroid.restype = None
slib.gf_reaction_getNumSpec.argtypes = [ctypes.c_uint64]
slib.gf_reaction_getNumSpec.restype = ctypes.c_uint64
slib.gf_reaction_hasSpec.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_reaction_hasSpec.restype = ctypes.c_int   
slib.gf_reaction_getSpecRole.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_reaction_getSpecRole.restype = ctypes.Structure
slib.gf_reaction_specGeti.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_reaction_specGeti.restype = ctypes.c_uint64
slib.gf_reaction_getNumCurves.argtypes = [ctypes.c_uint64]
slib.gf_reaction_getNumCurves.restype = ctypes.c_uint64
slib.gf_reaction_getCurvep.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_reaction_getCurvep.restype = ctypes.c_uint64
slib.gf_reaction_recenter.argtypes = [ctypes.c_uint64]
slib.gf_reaction_recenter.restype = None
slib.gf_reaction_recalcCurveCPs.argtypes = [ctypes.c_uint64]
slib.gf_reaction_recalcCurveCPs.restype = None

# Role Functions
slib.gf_roleToStr.argtypes = [ctypes.c_uint]
slib.gf_roleToStr.restype = ctypes.c_char_p
slib.gf_strToRole.argtypes = [ctypes.c_char_p]
slib.gf_strToRole.restype = ctypes.c_uint

# Curve Functions
slib.gf_releaseCurve.argtypes = [ctypes.c_uint64]
slib.gf_releaseCurve.restype = None
slib.gf_curve_getRole.argtypes = [ctypes.c_uint64]
slib.gf_curve_getRole.restype = ctypes.c_int
slib.gf_getCurveCPs.argtypes = [ctypes.c_uint64]
slib.gf_getCurveCPs.restype = ctypes.Structure
slib.gf_curve_hasArrowhead.argtypes = [ctypes.c_uint64]
slib.gf_curve_hasArrowhead.restype = ctypes.c_int
slib.gf_curve_getArrowheadVerts.argtypes = [ctypes.c_uint64, ctypes.c_uint, ctypes.c_uint64] 
slib.gf_curve_getArrowheadVerts.restype = ctypes.c_int

# Window Fit Functions
slib.gf_fit_to_window.argtypes = [ctypes.c_uint64, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
slib.gf_fit_to_window.restype = None
slib.gf_moveNetworkToFirstQuad.argtypes = [ctypes.c_uint64, ctypes.c_double, ctypes.c_double]
slib.gf_moveNetworkToFirstQuad.restype = None

# Transform Functions
slib.gf_release_transform.argtypes = [ctypes.c_uint64]
slib.gf_release_transform.restype = None
slib.gf_tf_apply_to_point.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_tf_apply_to_point.restype = ctypes.Structure
slib.gf_tf_fitToWindow.argtypes = [ctypes.c_uint64, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double] 
slib.gf_tf_fitToWindow.restype = ctypes.c_uint64
slib.gf_tf_getScale.argtypes = [ctypes.c_uint64]
slib.gf_tf_getScale.restype = ctypes.Structure
slib.gf_tf_getScale.argtypes = [ctypes.c_uint64]
slib.gf_tf_getScale.restype = ctypes.Structure
slib.gf_tf_getDisplacement.argtypes = [ctypes.c_uint64]
slib.gf_tf_getDisplacement.restype = ctypes.Structure
slib.gf_tf_getPostDisplacement.argtypes = [ctypes.c_uint64]
slib.gf_tf_getPostDisplacement.restype = ctypes.Structure

# Canvas Functions
slib.gf_getCanvasp.argtypes = [ctypes.c_uint64]
slib.gf_getCanvasp.restype = ctypes.c_uint64
slib.gf_clearCanvas.argtypes = [ctypes.c_uint64]
slib.gf_clearCanvas.restype = None
slib.gf_releaseCanvas.argtypes = [ctypes.c_uint64]
slib.gf_releaseCanvas.restype = None
slib.gf_canvGetWidth.argtypes = [ctypes.c_uint64]
slib.gf_canvGetWidth.restype = ctypes.c_uint
slib.gf_canvGetHeight.argtypes = [ctypes.c_uint64]
slib.gf_canvGetHeight.restype = ctypes.c_uint
slib.gf_canvSetWidth.argtypes = [ctypes.c_uint64, ctypes.c_uint64]
slib.gf_canvSetWidth.restype = None
slib.gf_canvSetHeight.argtypes = [ctypes.c_uint64, ctypes.c_uint64]   
slib.gf_canvSetHeight.restype = None

# Cubic Bezier Functions
slib.gf_computeCubicBezierPoint.argtypes = [curveCP, ctypes.c_double]
slib.gf_computeCubicBezierPoint.restype = ctypes.Structure
slib.gf_computeCubicBezierLineIntersec.argtypes = [curveCP, point, point]
slib.gf_computeCubicBezierLineIntersec.restype = ctypes.c_uint64

# Arrowhead Functions
slib.gf_arrowheadStyleGetNumVerts.argtypes = [ctypes.c_int]
slib.gf_arrowheadStyleGetNumVerts.restype = ctypes.c_int
slib.gf_arrowheadStyleGetVert.argtypes = [ctypes.c_int, ctypes.c_int]
slib.gf_arrowheadStyleGetVert.restype = point
slib.gf_arrowheadStyleIsFilled.argtypes = [ctypes.c_int]
slib.gf_arrowheadStyleIsFilled.restype = ctypes.c_int
slib.gf_arrowheadNumStyles.restype = ctypes.c_uint64
slib.gf_arrowheadSetStyle.argtypes = [ctypes.c_uint, ctypes.c_int]
slib.gf_arrowheadSetStyle.restype = None
slib.gf_arrowheadGetStyle.argtypes = [ctypes.c_uint]
slib.gf_arrowheadGetStyle.restype = ctypes.c_int
   

# Render Functions
# -- gf_renderTikZ
# -- gf_renderTikZFile	


# Python Defs of SBNW functions

## Error Functions
def getLastError():
    return slib.gf_getLastError() 

def haveError(): 
    return slib.gf_haveError()

def clearError():
    return slib.gf_clearError()

# Free Functions
def free (pointer):
    return slib.gf_free(pointer)

def freeLayoutInfo(h_layout_info):
    return slib.gf_freeLayoutInfo(h_layout_info)

def freeLayoutInfoHierarchy(h_layout_info): 
    return slib.gf_freeLayoutInfoHierarch(h_layout_info)

def freeModelAndLayout(h_model, h_layout_info):
    return slib.gf_freeModelAndLayout(h_model, h_layout_info)

def strfree (h_str):
    return slib.gf_strfree(h_str)

def freeSBMLModel (h_sbml_model):
    return slib.gf_freeSBMLModel(h_sbml_model)

## IO Functions
def loadSBML (h_fileName):
   h_filename_string = h_fileName.encode('utf-8')
   return slib.gf_loadSBMLfile(h_filename_string)         

def loadSBMLbuf (h_buffer):
    return slib.gf_loadSBMLbuf(h_buffer)

def writeSBMLwithLayout (filename, h_layout, h_layout_info):
    return slib.gf_writeSBMLwithLayout(filename, h_layout, h_layout_info)

def writeSBML (filename, sbml_model):
    #filename_string = filename.encode('utf-8')
    return slib.gf_writeSBML(filename, sbml_model)

## Library Info Functions
def getCurrentLibraryVersion ():
    return slib.gf_getCurrentLibraryVersion()

## Model functions
def getSBMLwithLayoutStr (h_sbml_model, h_layout_info):
    return slib.gf_getSBMLwithLayoutStr(h_sbml_model, h_layout_info)

## Layout Functions
def processLayout (h_layout):
    return slib.gf_processLayout(h_layout)         

def randomizeLayout (h_layout_info):
    return slib.gf_randomizeLayout(h_layout_info)

def doLayoutAlgorithm (layout_options, h_layout_info):
    return slib.gf_doLayoutAlgorithm(layout_options, h_layout_info)

def layoutInfo_newp(level, version, width, height):
    return slib.gf_layoutInfo_newp(level, version, width, height)

def randomizeLayout2 (h_network, h_canvas):
    return slib.gf_randomizeLayout2(h_network, h_canvas)

def randomizeLayout_fromExtents (h_network, left, top, right, bottom):
    return slib.gf_randomizeLayout_fromExtents(h_network, left, top, right, bottom)
    
def doLayoutAlgorithm2 (fr_options, h_network, h_canvas):
    return slib.gf_doLayoutAlgorithm2(fr_options, h_network, h_canvas)

def getLayoutOptDefaults (fr_options):
    return slib.gf_getLayoutOptDefaults(fr_options)

def layout_setStiffness (fr_options, k):
    return slib.gf_layout_setStiffness(fr_options, k)

# Network Functions
def clearNetwork(h_network):
    return slib.gf_clearNetwork(h_network)

def getNetworkp(h_layout_info):
    return slib.gf_getNetworkp (h_layout_info)

def nw_connectNode (h_network, h_node, h_reaction, h_role):
    return slib.gf_nw_connectNode(h_network, h_node, h_reaction, h_role)

def nw_connectNodeRoleStr (h_network, h_node, h_reaction, h_role_str):
    return slib.gf_nw_connectNodeRoleStr(h_network, h_node, h_reaction, h_role_str)

def nw_findCompartmentById (h_network, h_id):
    return slib.gf_nw_findCompartmentById(h_network, h_id)

def nw_getCompartmentp (h_network, index):
    return slib.gf_nw_getCompartmentp(h_network, index)

def nw_getId(h_network):
    return slib.gf_nw_getId(h_network)

def nw_getNodep(h_network, id):
    return slib.gf_nw_getNodep(h_network, id)

def nw_getNodepFromId (h_network, h_id):
    return slib.gf_nw_getNodepFromId(h_network, h_id)

def nw_getNumAliasInstances (h_network, h_node):
    return slib.gf_nw_getNumAliasInstances(h_network, h_node)

def nw_getNumCompartments (h_network):
    return slib.gf_nw_getNumComps(h_network)

def nw_getNumNodes(h_network):
    return slib.gf_nw_getNumNodes(h_network)

def nw_getNumRxns (h_network):
    return slib.gf_nw_getNumRxns(h_network)

def nw_getNumUniqueNodes(h_network):
    return slib.gf_nw_getNumUniqueNodes(h_network)

def nw_getRxnp (h_network, index):
    return slib.gf_nw_getRxnp(h_network, index)

def nw_getUniqueNodep (h_network, index):
    return slib.gf_nw_getUniqueNodep(h_network, index)

def nw_isLayoutSpecified (h_network):
    return slib.gf_nw_isLayoutSpecified(h_network)

def nw_isNodeConnected (h_network, h_node, h_reaction):
    return slib.gf_nw_isNodeConnected()

def nw_newAliasNodep (h_network, h_source):
    return slib.gf_nw_newAliasNodep(h_network, h_source)

def nw_newCompartmentp (h_network, h_id, h_name):
    return slib.gf_nw_newCompartmentp(h_network, h_id, h_name)

def nw_newNodep (h_network, h_id, h_name, h_compartment):
    return slib.gf_nw_newNodep(h_network, h_id, h_name, h_compartment)

def nw_rebuildCurves (h_network):
    return slib.gf_nw_rebuildCurves(h_network)

def nw_recenterJunctions (h_network):
    return slib.gf_nw_recenterJunctions(h_network)

def nw_removeNode (h_network, h_node):
    return slib.gf_nw_removeNode(h_network, h_node)

def nw_removeRxn (h_network, h_reaction):
    return slib.gf_nw_removeRxn(h_network, h_reaction)

def nw_setId(h_network, h_id):
    return slib.gf_nw_setId(h_network, h_id)

def releaseNetwork(h_network):
    return slib.gf_releaseNetwork(h_network)

# Model Functions
def SBMLModel_newp ():
  return slib.gf_SBMLModel_newp()

def setModelNamespace(h_layout_info, level, version):
    return slib.gf_setModelNamespace(h_layout_info, level, version)

# Network Functions
def nw_getAliasInstancep (h_network, h_node, index):
    return slib.gf_nw_getAliasInstancep(h_network, h_node, index)
   
# _Node Functions
def nw_nodeHasCompartment (h_network, h_node):
    return slib.gf_nw_nodeHasCompartment(h_network, h_node)

def nw_nodeGetCompartment (h_network, h_node):
    return slib.gf_nw_nodeGetCompartment(h_network, h_node)

def node_setCompartment (h_node, h_compartment):
   return slib.gf_node_setCompartment(h_node, h_compartment)

def releaseNode (h_node):
    return slib.gf_releaseNode(h_node)

def node_isLocked (h_node):
    return slib.gf_node_isLocked(h_node)

def node_lock (h_node):
    return  slib.gf_node_lock(h_node)

def node_unlock (h_node):
    return slib.gf_node_unlock

def node_make_alias (h_node, h_network):
    return slib.gf_node_make_alias(h_node, h_network)

def node_isAliased (h_node):
    return slib.gf_node_isAliased(h_node)

def node_getCentroid (h_node):
    return slib.gf_node_getCentroid(h_node)

# don't think this one is in the c api code, though in the doc
#def node_getCentroidXY (h_node, h_x, h_y):
#    return slib.gf_node_getCentroidXY(h_node, h_x, h_y)

def node_setCentroid (h_node, point):
    return slib.gf_node_setCentroid(h_node, point)

def node_getWidth (h_node):
    return slib.gf_node_getWidth(h_node)

def node_setWidth (h_node, width):
    return slib.gf_node_setWidth(h_node, width)

def node_getHeight (h_node):
    return slib.gf_node_getHeight(h_node)

def node_setHeight (h_node, height):
    return slib.gf_node_setHeight(h_node, height)

def node_getID (h_node):
    return slib.gf_node_getID(h_node)

def node_setID (h_node, h_id):
    return slib.gf_node_setID(h_node, h_id)

def node_getName (h_node):
    return slib.gf_node_getName(h_node)
   
def node_setName (h_node, h_name):
    return slib.gf_node_setName(h_node, h_name)

def node_getConnectedReactions (h_node, h_network, h_num, h_rxns):
    return slib.gf_node_getConnectedReactions(h_node, h_network, h_num, h_rxns)

def node_getAttachedCurves (h_node, h_network, h_num, h_curves):
    return slib.gf_node_getAttachedCurves(h_node, h_network, h_num, h_curves)

# Role Functions   
def roleToStr (role):
    return slib.gf_roleToStr(role)

def strToRole (h_role):
    h_role_encoded = h_role.encode('utf-8')
    return slib.gf_strToRole(h_role_encoded)

# Reaction Functions   
def releaseRxn (h_reaction):
    return slib.gf_releaseRxn(h_reaction)

def nw_newReactionp (h_network, h_id, h_name):
    return slib.gf_nw_newReactionp(h_network, h_id, h_name)

def reaction_getID (h_reaction):
    return slib.gf_reaction_getID(h_reaction)

def reaction_getCentroid (h_reaction):
    return slib.gf_reaction_getCentroid(h_reaction)
    
def reaction_setCentroid (h_reaction, point):
    return slib.gf_reaction_setCentroid(h_reaction, point)

def reaction_getNumSpec (h_reaction):
    return slib.gf_reaction_getNumSpec(h_reaction)
   
def reaction_hasSpec (h_reaction, h_node):
    return slib.gf_reaction_hasSpec(h_reaction, h_node)

def reaction_getSpecRole (h_reaction, index):
    return slib.gf_reaction_getSpecRole(h_reaction, index)
   
def reaction_specGeti (h_reaction, index):
    return slib.gf_reaction_specGeti(h_reaction, index)

def reaction_getNumCurves (h_reaction):
    return slib.gf_reaction_getNumCurves(h_reaction) 

def reaction_getCurvep (h_reaction, index):
    return slib.gf_reaction_getCurvep(h_reaction, index)

def reaction_recenter (h_reaction):
    return slib.gf_reaction_recenter(h_reaction)

def reaction_recalcCurveCPs (h_reaction):
    return slib.gf_reaction_recalcCurveCPs(h_reaction)

# Curve Functions
def releaseCurve (h_curve):
    return slib.gf_releaseCurve()

def curve_getRole (h_curve):
    return slib.gf_curve_getRole(h_curve)
   
def getCurveCPs (h_curve):
    return slib.gf_getCurveCPs(h_curve)

def curve_hasArrowhead (h_curve):
    return slib.gf_curve_hasArrowhead(h_curve)

def curve_getArrowheadVerts (h_curve, h_n, h_point):
    return slib.gf_curve_getArrowheadVerts(h_curve, h_n, h_point)

# Compartment Functions    
def getDefaultCompartmentId():
    return slib.gf_getDefaultCompartmentId()

def setDefaultCompartmentId(h_id):
    return slib.gf_setDefaultCompartmentId(h_id)

def releaseCompartment (h_compartment):
    return slib.gf_releaseCompartment(h_compartment)    

def compartment_getID (h_compartment):
    return slib.gf_compartment_getID(h_compartment)

def compartment_getMinCorner (h_compartment):
    return slib.gf_compartment_getMinCorner(h_compartment)

def compartment_setMinCorner (h_compartment, point):
    return slib.gf_compartment_setMinCorner(h_compartment, point)

def compartment_getMaxCorner (h_compartment):
    return slib.gf_compartment_getMaxCorner(h_compartment)

def compartment_setMaxCorner (h_compartment, point):
    return slib.gf_compartment_setMaxCorner(h_compartment, point)

def compartment_getWidth (h_compartment):
    return slib.gf_compartment_getWidth(h_compartment)

def compartment_getHeight (h_compartment):
    return slib.gf_compartment_getHeight(h_compartment)

def compartment_getNumElt (h_compartment):
    return slib.gf_compartment_getNumElt(h_compartment)

def compartment_addNode (h_compartment, h_node):
    return slib.gf_compartment_addNode(h_compartment, h_node)

def compartment_removeNode (h_compartment, h_node):
    return slib.gf_compartment_removeNode(h_compartment, h_node)

def compartment_containsNode (h_compartment, h_node):
    return slib.gf_compartment_containsNode(h_compartment, h_node)

def compartment_containsReaction (h_compartment, h_reaction):
    return slib.gf_compartment_containsReaction(h_compartment, h_reaction)

# Window Fit Functions
def fit_to_window (h_layoutInfo, left, top, right, bottom):
    return slib.gf_fit_to_window(h_layoutInfo, left, top, right, bottom)

def tf_fitToWindow (h_layout_info, left, top, right, bottom):
    return slib.gf_tf_fitToWindow(h_layout_info, left, top, right, bottom)

def moveNetworkToFirstQuad (h_layout_info, x_disp, y_disp):
    return slib.gf_moveNetworkToFirstQuad(h_layout_info, x_disp, y_disp)

# Transform Functions
def tf_apply_to_point (h_transform, point):
    return slib.gf_tf_apply_to_point(h_transform, point)

def tf_getScale (h_transform):
    return slib.gf_tf_getScale(h_transform)

def tf_getDisplacement (h_transform):
    return slib.gf_tf_getDisplacement(h_transform)
   
def tf_getPostDisplacement (h_transform):
    return slib.gf_tf_getPostDisplacement(h_transform)

def release_transform (h_transform):
    return slib.gf_release_transform(h_transform)

# Canvas Functions
def getCanvasp (h_layout_info):
    return slib.gf_getCanvasp(h_layout_info)

def clearCanvas (canvas):
    return slib.gf_clearCanvas(canvas)

def releaseCanvas (canvas):
    return slib.gf_releaseCanvas(canvas)

def canvGetWidth (canvas):
    return slib.gf_canvGetWidth(canvas)

def canvGetHeight (canvas):
    return slib.gf_canvGetHeight(canvas)

def canvSetWidth (canvas, width):
    return slib.gf_canvSetWidth(canvas, width)

def canvSetHeight (canvas, height):
    return slib.gf_canvSetHeight(canvas, height)

def aliasNodebyDegree (h_layout_info, minDegree):
    return slib.gf_aliasNodebyDegree(h_layout_info, minDegree)

# Cubic Bezier Functions
def computeCubicBezierPoint (h_curveCP, t):
    return slib.gf_computeCubicBezierPoint(h_curveCP, t)

def computeCubicBezierLineIntersec (h_curveCP, h_line_start, h_line_end):
    return slib.gf_computeCubicBezierLineIntersec(h_curveCP, h_line_start, h_line_end)

# Arrowhead Functions   
def arrowheadStyleGetNumVerts (style):
    return slib.gf_arrowheadStyleGetNumVerts(style)
   
def arrowheadStyleGetVert (style, n):
    return slib.gf_arrowheadStyleGetVert(style, n)

def arrowheadStyleIsFilled (style):
    return slib.gf_arrowheadStyleIsFilled(style)

def arrowheadNumStyles ():
    return slib.gf_arrowheadNumStyles()

def arrowheadSetStyle (h_role, style):
    return slib.gf_arrowheadSetStyle(h_role, style)

def arrowheadGetStyle (h_role):
    return slib.gf_arrowheadGetStyle(h_role)


# Test bindings     
s = "C:\\tmp\\model.xml"
h_layout = loadSBML (s)     
h_layout_info = processLayout (h_layout)
randomizeLayout (h_layout_info)

layout_alg_options = fr_alg_options (20.0, 1, 0, 0, 500.0, 0.0, 1, 0, 0, 0.0)
doLayoutAlgorithm (layout_alg_options, h_layout_info)

output_fileName = "c:\\tmp\\model_with_layout.xml"
output_fileName_string = output_fileName.encode('utf-8')
writeSBMLwithLayout (output_fileName_string, h_layout, h_layout_info)

# Load Library - check features
print(f"current library version: {getCurrentLibraryVersion()}")

# Load Model - check features
print(f"\n--Load a Model--\n")
s = "C:\\tmp\\model.xml"
h_model = loadSBML (s)     
h_layout_info = processLayout (h_model)
randomizeLayout (h_layout_info)
print(f"h_layout: {h_layout}, {type(h_layout)}")
print(f"h_layout_info: {h_layout_info}, {type(h_layout_info)}")
lastError = getLastError()
print("Get last error: ", lastError, ", ", type(lastError))
haveAnError = haveError()
print("Have error: ", haveAnError, ", ", type(haveAnError))
defaultCompartmentId = getDefaultCompartmentId()
print("Default compartment id: ", defaultCompartmentId, ",", type(defaultCompartmentId))
h_network = getNetworkp(h_layout_info)
print("Network: ", h_network, ", ", type(h_network))
nw_id = nw_getId(h_network)
print("Network Id: ", nw_id, ", ", type(nw_id))
numNodes = nw_getNumNodes(h_network)
print("Number of Nodes = ", numNodes, ", ", type(numNodes))
numUniqueNodes = nw_getNumUniqueNodes(h_network)
print("Number of Unique Nodes = ", numUniqueNodes, ", ", type(numUniqueNodes))
numRxns = nw_getNumRxns(h_layout_info)
print ("Number of reactions = ", numRxns, ", " , type(numRxns))
numCompartments = nw_getNumCompartments(h_network)
print("Number of compartments = ", numCompartments, ", ", type(numCompartments))
h_node_A = nw_getNodep(h_network, 1)
print("_Node A: ", h_node_A, ", ", type(h_node_A))
h_node_unique_A = nw_getUniqueNodep(h_network, 1)
print("_Node A: ", h_node_unique_A, ", ", type(h_node_unique_A))
h_node_from_id = nw_getNodepFromId(h_network, "A".encode('utf-8'))
print("_Node A: ", h_node_from_id, ", ", type(h_node_from_id))
h_rxn_1 = nw_getRxnp(h_network, 1)
print("Reaction 1: ", h_rxn_1, ", ", type(h_rxn_1))
nw_removeRxn(h_network, h_rxn_1)
numRxnsAfterRemoval = nw_getNumRxns(h_layout_info)
print("Number of reactions after removal = ", numRxnsAfterRemoval, ", " , type(numRxnsAfterRemoval))
# Windows Error
#h_comp_0 = nw_getCompartmentp(h_network, 1)
#print("Compartment 0: ", h_comp_0, ", ", type(h_comp_0))
nw_rebuildCurves(h_network)
nw_recenterJunctions(h_network)
is_layout_specified = nw_isLayoutSpecified(h_network)
print("is layout specified? ", is_layout_specified, ", ", type(is_layout_specified))
#cmd below: node needs to have a centroid? else Window Error or the node ptr is null?
#centroid_point = node_getCentroid(h_node_A)
#print(f"centroid point: ", centroid_point, ", ", type(centroid_point))
# fcn below: is not in the dll?
#centroid_point = node_getCentroidXY(h_node_A, 1.0, 2.0)
#print(f"centroid point: ", centroid_point, ", ", type(centroid_point))

# Free Pointers
# free(h_model)
# free(h_layout_info)
# processLayout: Call gf_freeLayoutInfo to free the returned pointer. Do not call gf_free.

# ----------------------------------------
# Build Model - check features
# ----------------------------------------
print(f"\n--Build a Model--\n")
hb_model = SBMLModel_newp()
print("new model: ", hb_model, ", ", type(hb_model))
#the call below does not work: access violation
# hb_layout_info = processLayout (hb_model)
#print("layout info: ", hb_layout_info, ", ", type(hb_layout_info))
# layout: level, version, width, height
hb_layout_info = layoutInfo_newp(0, 1, 100, 100)
print("layout info: ", hb_layout_info, ", ", type(hb_layout_info))
# set namespace: layout_info, level, version
setModelNamespace(hb_layout_info, 0, 2)
numRxns = nw_getNumRxns(h_layout_info)
print ("Number of reactions = ", numRxns, ", " , type(numRxns))
defaultCompartmentId = getDefaultCompartmentId()
print("Default compartment id: ", defaultCompartmentId, ",", type(defaultCompartmentId))
setDefaultCompartmentId("compartment_default".encode('utf-8'))
defaultCompartmentId = getDefaultCompartmentId()
print("Default compartment id: ", defaultCompartmentId, ",", type(defaultCompartmentId))
hb_network = getNetworkp(hb_layout_info)
print("Network: ", h_network, ", ", type(hb_network))
nw_id = nw_getId(h_network)
print("Network Id: ", nw_id, ", ", type(nw_id))
nw_setId(h_network, "network_build".encode('utf-8'))
nw_id = nw_getId(h_network)
print("Network Id: ", nw_id, ", ", type(nw_id))
numNodes = nw_getNumNodes(hb_network)
print("Number of Nodes: ", numNodes, ", ", type(numNodes))
numUniqueNodes = nw_getNumUniqueNodes(hb_network)
print("Number of Unique Nodes: ", numUniqueNodes, ", ", type(numUniqueNodes))
numRxns = nw_getNumRxns(hb_layout_info)
print ("Number of reactions = ", numRxns, ", " , type(numRxns))
numCompartments = nw_getNumCompartments(hb_network)
print("Number of compartments = ", numCompartments, ", ", type(numCompartments))
# cmd below: WinError
#hb_comp_0 = nw_getCompartmentp(hb_network, 0)
#print("Compartment 0: ", hb_comp_0, ", ", type(hb_comp_0))
# cmd below: returns 0, what does that mean?
hb_comp_d = nw_findCompartmentById(hb_network, "compartment_default".encode('utf-8'))
print("Compartment default: ", hb_comp_d, ", ", type(hb_comp_d))
hb_comp_new = nw_newCompartmentp(hb_network, "ABC".encode('utf-8'), "ABC_Compartment".encode('utf-8'))
print("New compartment: ", hb_comp_new, ", ", type(hb_comp_new))
numCompsAfterAddOne = nw_getNumCompartments(hb_network)
print("Number of compartments after adding 1 = ", numCompsAfterAddOne, ", ", type(numCompsAfterAddOne))
hb_node_new = nw_newNodep(hb_network, "Z".encode('utf-8'), "new_node".encode('utf-8'), hb_comp_d)
print("New node:", hb_node_new, ", ", type(hb_node_new))
hb_alias_node = nw_newAliasNodep(h_network, hb_node_new)
print("Alias node: ", hb_alias_node, ", ", type(hb_alias_node))
num_aliases = nw_getNumAliasInstances(h_network, hb_node_new)
print("num alias instances: ", num_aliases, ", ", type(num_aliases))
node_removed = nw_removeNode(hb_network, hb_alias_node)
print("Removed node: ", node_removed, ", ", type(node_removed))
# hb_rxn = 
#role = 
#node_connected = nw_connectNode(hb_network, hb_node_new, hb_rxn, role)
# node_connected_rolestr = nw_connectNodeRoleStr(hb_network, hb_node_new, hb_rxn, "role_new".encode('utf-8'))
#is_connected = nw_isNodeConnected(h_network, hb_node_new, hb_rxn)
#print("is connected?: ", is_connected, ", ", type(is_connected))
is_layout_specified = nw_isLayoutSpecified(hb_network)
print("is layout specified? ", is_layout_specified, ", ", type(is_layout_specified))
hb_alias_instance_1 = nw_getAliasInstancep(hb_network, hb_node_new, 0)
print("alias instance 1: ", hb_alias_instance_1, ", ", type(hb_alias_instance_1))
# cmd below: I think this compartment can't be null? else OSError
node_setCompartment(hb_node_new, hb_comp_new)
releaseNode(hb_node_new)
is_node_locked = node_isLocked(hb_node_new)
print("is node locked? ", is_node_locked, ", ", type(is_node_locked))
node_lock(hb_node_new)
is_node_locked = node_isLocked(hb_node_new)
print("is node locked? ", is_node_locked, ", ", type(is_node_locked))
node_unlock(hb_node_new)
# result below: should be 0, but it is 1
is_node_locked = node_isLocked(hb_node_new)
print("is node locked? ", is_node_locked, ", ", type(is_node_locked))
hb_node_alias_node = node_make_alias(hb_node_new, hb_network)
print("node alias node: ", hb_node_alias_node, ", ", type(hb_node_alias_node))
is_node_aliased = node_isAliased(hb_node_new)
print(f"is node aliased: ", is_node_aliased, ", ", type(is_node_aliased))
# cmd below: node needs to have a centroid, else WinError
#centroid_point = node_getCentroid(hb_node_new)
#print(f"centroid point: ", centroid_point, ", ", type(centroid_point))
centroid_pt = point(1.0, 2.0)
print("centroid pt: ", centroid_pt.x, ", ", centroid_pt.y, ", ", type(centroid_pt))
node_setCentroid(hb_node_new, centroid_pt)
#centroid_point = node_getCentroid(hb_node_new)
#print(f"centroid point: ", centroid_point, ", ", type(centroid_point))
node_width = node_getWidth(hb_node_new)
print("node width: ", node_width, ", ", type(node_width))
node_height = node_getHeight(hb_node_new)
print("node height: ", node_height, ", ", type(node_height))
node_setWidth(hb_node_new, 40.2)
node_setHeight(hb_node_new, 20.2)
node_width = node_getWidth(hb_node_new)
print("node width: ", node_width, ", ", type(node_width))
node_height = node_getHeight(hb_node_new)
print("node height: ", node_height, ", ", type(node_height))
node_id = node_getID(hb_node_new)
print("node id: ", node_id, ", ", type(node_id))
node_setID(hb_node_new, "node_new_id".encode('utf-8'))
node_name = node_getName(hb_node_new)
print("node name: ", node_name, ", ", type(node_name))
node_setName(hb_node_new, "node_new_name".encode('utf-8'))
# cmd below, hb_num_rxns is the wrong type -> TypeError
#hb_num_rxns = None
#hb_rxns = None
#connected_rxns = node_getConnectedReactions(hb_node_new, hb_network, hb_num_rxns, hb_rxns)
#print("connected rxns: ", connected_rxns, ", ", type(connected_rxns))
#node_getAttacedCurves(hb_node_new, hb_network, hb_num_curves, hb_curves)
# do I expect node below to have a compartment?
node_has_compartment = nw_nodeHasCompartment(hb_network, hb_node_new)
print("node has compartment? ", node_has_compartment, ", ", type(node_has_compartment))
# cmd above says has no compartment,
# cmd below returns a pointer, leading to a compartment? 
hb_compartment = nw_nodeGetCompartment(hb_network, hb_node_new)
print("node compartment:", hb_compartment, ", ", type(hb_compartment))
hb_rxn_new = nw_newReactionp(hb_network, "rxn_new".encode('utf-8'), "rxn_first_step".encode('utf-8'))
print("new rxn: ", hb_rxn_new, ", ", type(hb_rxn_new))
hb_rxn_id = reaction_getID(hb_rxn_new)
print("rxn id: ", hb_rxn_id, ", ", type(hb_rxn_id))
#cmd below: OSError
#rxn_centroid_point = reaction_getCentroid(hb_rxn_new)
#print("rxn centroid: ", rxn_centroid_point, ", ", type(rxn_centroid_point))
centroid_point = point(10.0, 20.0)
reaction_setCentroid(hb_rxn_new, centroid_point)
# cmd below: OSError, access violation reading
#rxn_centroid_point = reaction_getCentroid(hb_rxn_new)
#print("rxn centroid: ", rxn_centroid_point, ", ", type(rxn_centroid_point))
releaseRxn(hb_rxn_new)
num_species = reaction_getNumSpec(hb_rxn_new)
print("rxn num species = ", num_species, ", ", type(num_species))
rxn_has_species = reaction_hasSpec(hb_rxn_new, hb_node_new)
print("rxn has this species?", rxn_has_species, ", ", type(rxn_has_species))
# cmd below: OSError, windows Error
# cmd below: OSError, windows Error
#species_role = reaction_getSpecRole(hb_rxn_new, 0)
#print("species role: ", species_role, ", ", type(species_role))
role_string = roleToStr(GF_ROLE_MODIFIER)
print("role to string: ", role_string, ", ", type(role_string))
species_role = strToRole("GF_ROLE_SUBSTRATE")
print("species role: ", species_role, ", ", type(species_role))
# cmd below: OSError windows error
#rxn_species_global_index = reaction_specGeti(hb_rxn_new, 0)
#print("rxn species global index: ", rxn_species_global_index, ", ", type(rxn_species_global_index))
rxn_num_curves = reaction_getNumCurves(hb_rxn_new)
print("rxn num curves = ", rxn_num_curves, ", ", type(rxn_num_curves))
# cmd below: OSError, Windows Error
#hb_rxn_curve = reaction_getCurvep(hb_rxn_new, 0)
#print("rxn curve 0: ", hb_rxn_curve, ", ", type(hb_rxn_curve))
reaction_recenter(hb_rxn_new)
reaction_recalcCurveCPs(hb_rxn_new)
#cmd below, don't yet a curve handle to release
#releaseCurve(hb_rxn_curve)
#cmd below, no curve yet
#curve_species_role = curve_getRole(hb_rxn_curve)
#print("curve species role: ", curve_species_role, ", ", type(curve_species_role))
# cmd below: no curve yet
#rxn_curve_CP = getCurveCPs(hb_rxn_curve)
#print("rxn curve control points: ", rxn_curve_CP, ", ", type(rxn_curve_CP))
#cmd below, no curve yet
#curve_has_arrowhead = curve_hasArrowhead(hb_rxn_curve)
#print("curve has arrowhead: ", curve_has_arrowhead, ", ", type(curve_has_arrowhead))
#num_verts = 
#arrowhead_vertices = 
#get_arrow_verts = curve_getArrowheadVerts(hb_rxn_curve, num_verts, arrowhead_vertices)
#print("get arrowhead vertices: ", get_arrow_verts, ", ", type(get_arrow_verts))
compartment_id = compartment_getID(hb_compartment)
print("compartment id: ", compartment_id, ", ", type(compartment_id))
upper_left_corner = point(0.0, 0.0)
lower_right_corner = point(100.0, 100.0)
#compartment_setMinCorner(hb_compartment, upper_left_corner)
#compartment_setMaxCorner(hb_compartment, lower_right_corner)
#min_corner_point = compartment_getMinCorner(hb_compartment)
#print("compartment min corner point: ", min_corner_point, ", ", type(min_corner_point))
#max_corner_point = compartment_getMaxCorner(hb_compartment)
#print("compartment max corner point: ", max_corner_point, ", ", type(max_corner_point))
#compartment_width = compartment_getWidth(hb_compartment)
#print("compartment width = ", compartment_width, ", ", type(compartment_width))
#compartment_height = compartment_getHeight(hb_compartment)
#print("compartment height = ", compartment_height, ", ", type(compartment_height))
#compartment_num_species = compartment_getNumElt(hb_compartment)
#print("compartment num species = ", compartment_num_species, ", ", type(compartment_num_species))
compartment_add_node = compartment_addNode(hb_compartment, hb_node_new)
print("compartment add node: ", compartment_add_node, ", ", type(compartment_add_node))
compartment_contains_node = compartment_containsNode(hb_compartment, hb_node_new)
print("compartment_contains_node: ", compartment_contains_node, ", ", type(compartment_contains_node))
compartment_remove_node = compartment_removeNode(hb_compartment, hb_node_new)
print("compartment remove node: ", compartment_remove_node, ", ", type(compartment_remove_node))
compartment_contains_reaction = compartment_containsReaction(hb_compartment, hb_rxn_new)
print("compartment contains reaction: ", compartment_contains_reaction, ", ", type(compartment_contains_reaction))
#cmd below: OSError
#releaseCompartment(hb_compartment)
hb_canvas = getCanvasp(hb_layout_info)
print("hb_canvas: ", hb_canvas, ", ", type(hb_canvas))
canvas_width = canvGetWidth(hb_canvas)
print("canvas width: ", canvas_width, ", ", type(canvas_width))
canvas_height = canvGetHeight(hb_canvas)
print("canvas height: ", canvas_height, ", ", type(canvas_height))
canvSetWidth(hb_canvas, 110)
canvSetHeight(hb_canvas, 110)
canvas_width = canvGetWidth(hb_canvas)
print("canvas width: ", canvas_width, ", ", type(canvas_width))
canvas_height = canvGetHeight(hb_canvas)
print("canvas height: ", canvas_height, ", ", type(canvas_height))
#cmd below: OSError, if canvas has been cleared or released
randomizeLayout2(hb_network, hb_canvas)

aliasNodebyDegree(hb_layout_info, 1)
randomizeLayout(hb_layout_info)
randomizeLayout_fromExtents(hb_network, 0.0, 0.0, 100.0, 100.0)

build_filename = "build_model.xml".encode('utf-8')
writeSBMLwithLayout(build_filename, hb_model, hb_layout_info)
writeSBML(build_filename, hb_model)
model_with_layout_string = getSBMLwithLayoutStr(hb_model, hb_layout_info)
print("model with layout string:\n", model_with_layout_string, ", ", type(model_with_layout_string))

start_point = point(0.0, 0.0)
control1_point = point(25.0, 25.0)
control2_point = point(50.0, 50.0)
end_point = point(100.0, 100.0)

curve_CP = curveCP(start_point, control1_point, control2_point, end_point)
print("curve CP: ", curve_CP, ", ", type(curve_CP))
print("curve CP.s x, y: ", curve_CP.s.x, ", ", curve_CP.s.y, ", ", type(curve_CP.s))
print("curve CP.c1 x, y: ", curve_CP.c1.x, ", ", curve_CP.c1.y, ", ", type(curve_CP.c1))
print("curve CP.c2 x, y: ", curve_CP.c2.x, ", ", curve_CP.c2.y, ", ", type(curve_CP.c2))
print("curve CP.e x, y: ", curve_CP.e.x, ", ", curve_CP.e.y, ", ", type(curve_CP.e))
#cmd below: OSError access violation
#bezier_point = computeCubicBezierPoint(curve_CP, 10.0)
#print("bezier_point: ", bezier_point, ", ", type(bezier_point))
bezier_line_intersec = computeCubicBezierLineIntersec(curve_CP, start_point, end_point)
print("bezier line intersection: ", bezier_line_intersec, ", ", type(bezier_line_intersec))
arrowhead_style = 6
arrowhead_num_verts = arrowheadStyleGetNumVerts(arrowhead_style)
print("arrowhead num verts: ", arrowhead_num_verts, ", ", type(arrowhead_num_verts))
arrowhead_vertex_num = 1
arrowhead_vertex = arrowheadStyleGetVert(arrowhead_style, arrowhead_vertex_num)
print("arrowhead_vertex:", arrowhead_vertex, ", ", type(arrowhead_vertex))
print("arrowhead vertex point x, y: ", arrowhead_vertex.x, ", ", arrowhead_vertex.y)
arrowhead_filled = arrowheadStyleIsFilled(arrowhead_style)
print("arrowhead filled: ", arrowhead_filled, ", ", type(arrowhead_filled))
arrowhead_num_styles = arrowheadNumStyles()
print("num arrowhead styles = ", arrowhead_num_styles, ", ", type(arrowhead_num_styles))

model_role = GF_ROLE_SUBSTRATE
arrowheadSetStyle(model_role, arrowhead_style)

arrowhead_substrate_style = arrowheadGetStyle(model_role) 
print("arrowhead substrate style: ", arrowhead_substrate_style, ", ", type(arrowhead_substrate_style))

doLayoutAlgorithm(layout_alg_options, hb_layout_info)
doLayoutAlgorithm2(layout_alg_options, hb_network, hb_canvas)
layout_alg_options_default = fr_alg_options()
getLayoutOptDefaults(layout_alg_options_default)
layout_alg_options_default_stiff = fr_alg_options()
layout_setStiffness(layout_alg_options_default_stiff, 1.0)

hb_model_buff = loadSBMLbuf(model_with_layout_string)
print("hb_model_buff: ", hb_model_buff, ", ", type(hb_model_buff))

clearCanvas(hb_canvas)
releaseCanvas(hb_canvas)

# free(hb_model)
# free(hb_layout_info)
# freeLayoutInfo(hb_layout_info)
# freeLayoutInfoHierarchy(hb_layout_info)
# freeModelAndLayout(hb_model, hb_layout_info)
# freeSBMLModel(hb_model)

#cmd below, kind of crashes the console
#test_string = "HelloWorld".encode('utf-8')
#strfree(test_string)

#class SBMLlayout:
    
    # maybe this should be a string type, now is <class 'bytes'>
#    SBNW_version = getCurrentLibraryVersion().decode('utf-8')
    
#    def __init__ (self, sbml_filename=None, layout_alg_options=fr_alg_options()):
        # note: the default values for the fr_alg_options are 0's
        # maybe need to change that?
#        self.sbml_filename = sbml_filename
#        self.layout_alg_options = layout_alg_options
#        h_network = getNetworkp(h_layout_info)

#        if sbml_filename:
#            self.h_model = loadSBML(sbml_filename)
#            self.h_layout_info = processLayout (h_model)                
#            self.h_network = getNetworkp(h_layout_info)
#        else:
#            print("No SBML filename given, creating a new model from scratch.")
#            self.h_model = SBMLModel_newp()
            # not sure if process layout does something default, our model is empty here
#            self.h_layout_info = processLayout (self.h_model)  
#            self.h_network = getNetworkp(self.h_layout_info)
            # add nodes
            # add reactions
            # add compartments

#    def arrowhead_get_style(self, role):
#        return slib.gf_arrowheadGetStyle(role) 
    
#    def arrowhead_set_style (self, role, style):
#        slib.gf_arrowheadSetStyle(role, style)

#    def do_layout_algorithm (self):
#        slib.gf_doLayoutAlgorithm(self.layout_alg_options, self.h_layout_info)

#    def fit_to_window (self, left, top, right, bottom):
#        slib.gf_fit_to_window(self.h_layout_info, left, top, right, bottom)

#    def get_number_of_nodes(self):
#        return slib.gf_nw_getNumNodes(self.h_network)        
        
#    def get_SBML_with_layout(self):
#        sbml_string = slib.gf_getSBMLwithLayoutStr(self.h_model, self.h_layout_info).decode('utf-8')
#        return sbml_string 
              
#    def randomize_layout (self):
#        slib.gf_randomizeLayout(self.h_layout_info)
        
#    def set_model_namespace(self, level, version):
#        slib.gf_setModelNamespace(self.h_layout_info, level, version)
        
#    def write_SBML_with_layout (self, output_filename):   
#        filename = output_filename.encode('utf-8')
#        result = slib.gf_writeSBMLwithLayout(filename, h_model, h_layout_info)
#        print("writeSBMLwithLayout result: ", result)
        # if result error, raise Exception?


#print()
# Create Layout
#fao = fr_alg_options()
#print("fao type: ", type(fao))
#print("fao k: ", fao.k)
#print("fao boundary: ", fao.boundary)
#print("fao mag: ", fao.mag)
#print("fao grav: ", fao.grav)

#print()
#sbml_filename = "C:\\tmp\\model.xml"
#layout_alg_options = fr_alg_options (20.0, 1, 0, 0, 500.0, 0.0, 1, 0, 0, 0.0)
#sbml_layout = SBMLlayout(sbml_filename)       
#print("sbnw version = ", sbml_layout.SBNW_version)
#print("sbml filename = ", sbml_layout.sbml_filename)

#sbml_layout.randomize_layout()
#sbml_layout.do_layout_algorithm()
#sbml_layout.fit_to_window(0,0,300,300)
# Write Model
#sbml_output_filename = "C:\\tmp\\model_with_layout_using_class3.xml"
#sbml_layout.write_SBML_with_layout(sbml_output_filename)
#sbml_string = sbml_layout.get_SBML_with_layout()
#print("sbml_string: ", type(sbml_string))
#print()
#print("gf_role_modifier: ", GF_ROLE_MODIFIER)
#ah_style = sbml_layout.arrowhead_get_style(GF_ROLE_MODIFIER)
#print("ah style MODIFIER: ", ah_style, ", ", type(ah_style))
#sbml_layout.arrowhead_set_style(GF_ROLE_MODIFIER, 7)
#ah_style = sbml_layout.arrowhead_get_style(GF_ROLE_MODIFIER)
#print("ah style MODIFIER: ", ah_style, ", ", type(ah_style))

#num_nodes = sbml_layout.get_number_of_nodes()
#print("num nodes: ", num_nodes)

#sl_build = SBMLlayout()
#print("sbml filename = ", sl_build.sbml_filename)





     