/* MIT License 
*/

//== FILEDOC =========================================================================

/** @file allen.h
 * @brief Intervals
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SBNW_ALLEN_H_
#define __SBNW_ALLEN_H_

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "min_max.h"

//-- C++ code --
#ifdef __cplusplus

namespace LibsbmlDraw {
    
    class Interval {
        public:
            /// Reorder endpoints if necessary
            Interval(const Real a, const Real b) {
                if(a <= b) {
                    _a = a;
                    _b = b;
                } else {
                    _a = b;
                    _b = a;
                }
            }
            
            /// Number-one reason why ignoring qualifiers is not okay
            Real a() const { return _a; }
            
            /// Returns reference
            Real& a() { return _a; }
            
            Real b() const { return _b; }
            
            Real& b() { return _b; }
        private:
            /// Endpoints, _a < _b
            Real _a, _b;
    };

    /// Get the distance between two intervals [u,v] and [x,y]; zero if they intersect.
    inline Real allenDist(const Real u, const Real v, const Real x, const Real y) {
        if(!(v < x || y < u))
            //intersect
            return 0.;
        Real a = x-v, b=u-y; //one will be negative
        return max(a,b);
    }

    /// allenDist returns absolute val of this; difficult to explain; used in @ref NetworkElement::forceVec
    inline Real allenOrdered(const Real u, const Real v, const Real x, const Real y) {
        // think of it like the result of b-a, where b and a are intervals
        if(!(v < x || y < u))
            //intersect
            return 0.;
        if(v < x)
            return x-v; //positive
        else
            return y-u; //negative
    }
    
    /// Is the point in the interval?
    inline bool pointInInterval(const Real p, const Interval& i) {
        return (i.a() <= p && p <= i.b()) ? true : false;
    }
    
}

#endif

#endif
