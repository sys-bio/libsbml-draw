/* MIT License
 */

//== FILEDOC =========================================================================

/** @file sbml.h
 * @brief SBML interface
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SBNW_SBML_H_
#define __SBNW_SBML_H_

//== INCLUDES ========================================================================

#include "SagittariusCore.h"

#ifdef __cplusplus
extern "C" {
#endif

/** @brief C wrapper for SBMLDocument
 */
typedef struct __gf_SBMLLayout {
    void* pdoc; /// Pointer to SBMLDocument cast to void
} gf_SBMLModel;

/** @brief Destructor for @ref gf_SBMLModel
 *  @param[in] lo The SBML model; all memory used by the model is freed
 *  \ingroup C_API
 */
_GraphfabExport void gf_freeSBMLModel(gf_SBMLModel* lo);

/** @brief Load SBML from memory buffer. Struct contains a pointer to the document.
 *  @param[in] buf The buffer containing the SBML file
 *  @param[out] r The SBML model; the model that contains the SBML info from the buffer
 *  \ingroup C_API
 */
_GraphfabExport gf_SBMLModel* gf_loadSBMLbuf(const char* buf);

/** @brief Load SBML from memory buffer. Struct contains a pointer to the document.
 *  @param[in] buf The buffer containing the SBML file
 *  @param[out] r The SBML model; the model that contains the SBML info from the buffer
 *  \ingroup C_API
 */
_GraphfabExport gf_SBMLModel* gf_loadSBMLfile(const char* file);

#ifdef __cplusplus
}//extern "C"
#endif

#endif
