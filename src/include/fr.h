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
 *  \ingroup C_API
 */
typedef struct __fr_options {
    /// Stiffness
    Real k;
    /**
     * @brief Constrain network elements to boundary (i.e. the drawing canvas?
     * @note It should never be necessary to use this option, as @ref gf_tf_fitToWindow or
     * @ref gf_fit_to_window can be used to achieve the same effect but with more robustness.
     */
    int boundary;
    /**
     * @brief Use magnetism?
     * @details When "magnetism" is enabled, forces can bridge reactions
     * (i.e. nodes can exert attractive forces on each other if connected by a reaction).
     */
    int mag;
    /// Strength of gravity (must be greater than 5 to have an effect)
    Real grav;
    /// Center of gravitational force
    Real baryx, baryy;
    /// Should the barycenter be set automatically from layout info?
    int autobary;
    /// Enable compartment-compartment and compartment-node interaction?
    int enable_comps;
    /// Randomize node positions before doing layout algo (library code DOES NOT call srand for reproducibility reasons)
    int prerandomize;
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
