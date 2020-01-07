/* MIT License
 */

//== FILEDOC =========================================================================

/** @file sig.h
 * @brief Sigmoid function
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SBNW_MATH_SIG_H_
#define __SBNW_MATH_SIG_H_

//== INCLUDES ========================================================================

#include "SagittariusCore.h"

//-- C++ code --
#ifdef __cplusplus

namespace LibsbmlDraw {

    inline Real sig(const Real t) {
        return 1./(1. + exp(-t));
    }
    
}

#endif

#endif
