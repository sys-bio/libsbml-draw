/* MIT License
 */

//== FILEDOC =========================================================================

/** @file string_helpers.h
 * @brief C string utilities
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SBNW_UTIL_STRING_H_
#define __SBNW_UTIL_STRING_H_

//== INCLUDES ========================================================================

#include "SagittariusCore.h"

//-- C methods --

#ifdef __cplusplus
extern "C" {
#endif

// allocates memory & copies src into it - user must deallocate
/** @internal
 */
_GraphfabExport char* gf_strclone(const char* src);

/** @brief Free a C string (char*)
 *  @param[in] str The string to free
 *  \ingroup C_API
 */
_GraphfabExport void gf_strfree(char* str);
    
#ifdef __cplusplus
}//extern "C"
#endif

#endif