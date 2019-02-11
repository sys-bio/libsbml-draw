/* MIT License
 */

//== FILEDOC =========================================================================

/** @file min_max.h
 * @brief Min & max for reals
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SBNW_MIN_MAX_H_
#define __SBNW_MIN_MAX_H_

//== INCLUDES ========================================================================

#include "SagittariusCore.h"

//-- C++ code --
#ifdef __cplusplus

namespace LibsbmlDraw {

    inline Real min(const Real x, const Real y) {
        return x < y ? x : y;
    }

    inline Real max(const Real x, const Real y) {
        return x > y ? x : y;
    }
    
}

#endif

#endif
