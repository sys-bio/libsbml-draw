/* MIT License
 */

//== FILEDOC =========================================================================

/** @file min_max.h
 * @brief Min & max for reals
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SBNW_MATH_ROUND_H_
#define __SBNW_MATH_ROUND_H_

//== INCLUDES ========================================================================

#include "SagittariusCore.h"

//-- C++ code --
#ifdef __cplusplus

namespace LibsbmlDraw {

    inline int64 sround(const Real x) {
        return x + 0.5;
    }
    
}

#endif

#endif
