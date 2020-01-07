/* MIT License
 */

//== FILEDOC =========================================================================

/** @file fr.h
 * @brief Fruchterman-Reingold algorithm
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SBNW_LAYOUT_FR_H_
#define __SBNW_LAYOUT_FR_H_

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "canvas.h"
#include "network.h"
#include "layout.h"

//-- C code --

#ifdef __cplusplus
extern "C" {
#endif

  /**
 *  @author JKM
 *  @brief Options passed to the Fruchterman-Reingold algorithm
 *  @details This structure holds the settings used by the Fruchterman-Reingold algorithm.
 *  @note: boundary (can use fit_to_window instead), mag (seems to have no effect), 
 *  enable_comps (assists with compartments, but causes layouts to overlap), and 
 *  prerandomize (can use randomizeLayout instead) have been removed.
 *  \ingroup C_API
 */
typedef struct __fr_options {
    /// Stiffness - distance between points
    Real k;
    /// Strength of gravity (must be greater than 5 to have an effect)
    Real grav;
    /// Center of gravitational force
    Real baryx, baryy;
    /// Should the barycenter be set automatically from layout info?  Uses dimensions of the canvas.
    int autobary;
    /// Padding on compartments
    Real padding;
} fr_options;

/**
 *  @author JKM
 *  @brief Run the autolayout (Fruchterman-Reingold) algorithm on a given layout structure
 *  @note @ref l should be a layout info object obtained from a call to @ref gf_processLayout.
 *  @param[in] opt The options controlling the layout algorithm
 *  @param[in/out] l The layout info
 *  \ingroup C_API
 */
_GraphfabExport void gf_doLayoutAlgorithm(fr_options opt, gf_layoutInfo* l);

/** @brief Run the autolayout (Fruchterman-Reingold) algorithm on a a network and optional canvas
 *  @details Can be used when full layout struct is not available
 *  @param[in] opt The options controlling the layout algorithm
 *  @param[in/out] n The network
 *  @param[in] c The canvas (may be NULL)
 *  \ingroup C_API
 */
_GraphfabExport void gf_doLayoutAlgorithm2(fr_options opt, gf_network* n, gf_canvas* c);

/** @brief Generate default values for the layout options
 *  @param[out] l The layout info in which to store the options
 *  \ingroup C_API
 */
_GraphfabExport void gf_getLayoutOptDefaults(fr_options* opt);

/** @brief Set the stiffness for the FR algorithm
 *  @param[out] opt The layout info in which to store the stiffness
 *  @param[in] k The stiffness
 *  \ingroup C_API
 */
_GraphfabExport void gf_layout_setStiffness(fr_options* opt, double k);

#ifdef __cplusplus
}//extern "C"
#endif

//-- C++ code --
#ifdef __cplusplus

// #include <string>

#include <iostream>

namespace LibsbmlDraw {

    /// Software Practice & Experience '91
    void FruchtermanReingold(fr_options opt, Network& net, Canvas* can, gf_layoutInfo* l);
    
}

#endif

#endif
