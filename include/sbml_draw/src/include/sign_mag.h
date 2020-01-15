/* MIT License
 */

//== FILEDOC =========================================================================

/** @file sign_mag.h
 * @brief Sign & magnitude for reals
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SBNW_SIGN_MAG_H_
#define __SBNW_SIGN_MAG_H_

//== INCLUDES ========================================================================

#include "SagittariusCore.h"

//-- C++ code --
#ifdef __cplusplus

namespace LibsbmlDraw {

    inline Real sign(const Real x) {
        //the easy way: return x == 0 ? 0 : x / mag(x);
        if(x > 0.)
            return 1.;
        else if(x == 0.)
            return 0.;
        else
            return -1.;
    }
    
    inline Real mag(const Real x) {
        return (x < 0.) ? -x : x;
    }
    
}

#endif

#endif
