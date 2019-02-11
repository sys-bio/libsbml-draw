/* MIT License
 */

//== FILEDOC =========================================================================

/** @file dist.h
 * @brief Euclidean distance
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SBNW_MATH_DIST_H_
#define __SBNW_MATH_DIST_H_

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "point.h"

//-- C++ code --
#ifdef __cplusplus

namespace LibsbmlDraw {
    
    /// 2d Euclidean distance
    inline Real euclidean2d(const Point& x, const Point& y) {
        Point d = x - y;
        return sqrt(d.x*d.x + d.y*d.y);
    }
    
}

#endif

#endif
