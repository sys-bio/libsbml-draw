/* MIT License
 */

//== FILEDOC =========================================================================

/** @file autolayout.h
 * @brief SBML layout interface in C
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SBNW_AUTOLAYOUT_H_
#define __SBNW_AUTOLAYOUT_H_

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "autolayoutSBML.h"
#include "layout.h"
#include "fr.h"

#endif


/*! \mainpage libSBNW
 *
 * \section intro_sec Introduction
 *
 * libSBNW is an SBML-compliant layout generation program.
 *
 *
 * Example:
 *
 * \code
 *
 *     #include "autolayoutc_api.h"
 *
 *     //  ...
 *
 *     //  type to store layout info
 *     gf_layoutInfo* l;
 *
 *
 *     //  load the model
 *     gf_SBMLModel* mod = gf_loadSBMLbuf(buf);
 *
 *
 *     //  options for layout algo
 *     fr_options opt;
 *
 *
 *     //  read layout info from the model
 *     l = gf_processLayout(mod);
 *
 *
 *     //  randomize node positions
 *     gf_randomizeLayout(l);
 *
 *     // do layout algo
 *     opt.k = 20.;
 *     opt.boundary = 1;
 *     opt.mag = 0;
 *     opt.grav = 0.;
 *     opt.baryx = opt.baryy = 500.;
 *     opt.autobary = 1;
 *     gf_doLayoutAlgorithm(opt, l);
 *
 *     //  save layout information to new SBML file
 *     gf_writeSBMLwithLayout(outfile, mod, l);
 *
 *
 *     //  run destructors on the model
 *     gf_freeSBMLModel(mod);
 *
 *
 *     //  run destructors on the layout
 *     gf_freeLayoutInfo(l);
 *
 * \endcode
//
// \section error_handling_sec Error handling
//
// The library has several functions in the C API for error handling:
// @ref gf_haveError, @ref gf_getLastError, and @ref gf_clearError,
// Errors can be read by gf_getLastError. gf_haveError can be called
// to determine if there is an error or not.
//
 * \code
 *
 *       //  Clear any previous errors
 *       gf_clearError();
 *
 *       //  Load a model from disk
 *       gf_SBMLModel* mod = gf_loadSBMLfile("mymodel.xml");
 *
 *       //  Did an error occur?
 *       if ( gf_haveError() ) {
 *         //  Print the error message
 *         fprintf(stderr, "Error message: %s\n", gf_getLastError());
 *         //  Clear the error so that future calls to gf_haveError return false
 *         gf_clearError();
 *       }
 *
 * \endcode
//
// \section install_sec Installation
//
// Installation documentation is provided at https://github.com/sys-bio/sbnw.
//
// \section conventions_sec Conventions
//
// The library conforms to universial conventions for C such as return zero for success.


// \defgroup C_API External C API

// \defgroup C_Internal Internal C API (do not use)

//
//*/
//
