/* MIT License
 */

//== FILEDOC =========================================================================

/** @file sign_mag.h
 * @brief Sign & magnitude for reals
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SBNW_RAND_UNIF_H_
#define __SBNW_RAND_UNIF_H_

//== INCLUDES ========================================================================

#include "SagittariusCore.h"

#include <stdlib.h>

//-- C++ code --
#ifdef __cplusplus

namespace LibsbmlDraw {

    inline Real rand_range(const Real l, const Real u) {
        AT(u >= l, "Bounds reversed");
        return l + (Real)rand()*(u-l)/RAND_MAX;
    }
    
}

#endif

#endif
