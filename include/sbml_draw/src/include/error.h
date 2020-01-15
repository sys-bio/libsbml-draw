/* MIT License
 */

//== FILEDOC =========================================================================

/** @file error.h
 * @brief Error information
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SBNW_DIAG_ERROR_H_
#define __SBNW_DIAG_ERROR_H_

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "autolayoutSBML.h"


#ifdef __cplusplus
extern "C" {
#endif

/**
 * @brief Emit an error
 * @param[in] str The error message
 */
_GraphfabExport void gf_emitError(const char* str);

/**
 * @brief Emit a warning
 * @param[in] str The warning message
 */
_GraphfabExport void gf_emitWarn(const char* str);

/**
 * @brief Register an error listener
 * @param[in] listener The listener
 */
_GraphfabExport void gf_registerErrorListener(void (*)(const char* msg));

/** @brief Gets the last error
 *  @return The error message (owned by callee)
 *  \ingroup C_API
 */
_GraphfabExport char* gf_getLastError();

/** @brief Gets whether an error occurred
 *  @return True if an error has been set
 *  \ingroup C_API
 */
_GraphfabExport int gf_haveError();

/** @brief Clears the last error
 *  \ingroup C_API
 */
_GraphfabExport void gf_clearError();

/**
 * @brief Sets the last error
 * @param[in] msg The error message (is copied)
 *  \ingroup Internal
 */
_GraphfabExport void gf_setError(const char* msg);

#ifdef __cplusplus
}//extern "C"
#endif

#endif
