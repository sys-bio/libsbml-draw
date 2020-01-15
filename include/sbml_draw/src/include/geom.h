/* MIT License
 */

//== FILEDOC =========================================================================

/** @file transform.h
 * @brief 2d transform applied to canvas elements
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SBNW_MATH_GEOM_H_
#define __SBNW_MATH_GEOM_H_

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "point.h"
#include "box.h"
#include "sign_mag.h"

#include <math.h>

//-- C++ code --
#ifdef __cplusplus

namespace LibsbmlDraw {
    
    /// Degrees 2 radians
    inline Real deg2r(const Real deg) {
        const Real pi = 3.14159;
        return deg*pi/180.;
    }

    /// Return alpha*t^3 + beta*t^2 + gamma*t + delta
    inline Point computeCubic(const Point& alpha, const Point& beta, const Point& gamma, const Point& delta, Real t) {
      return alpha*t*t*t + beta*t*t + gamma*t + delta;
    }
    
    inline Point new2ndPos(const Point& first, const Point& second, const Real deg, const Real dist, const bool rel_dist) {
        Real h, o, a, x;
        Real hnew, onew, anew;
        
        o = second.y - first.y;
        a = second.x - first.x;
        h = sqrt(pow(a,2.) + pow(o,2.));
        
        if(rel_dist)
            hnew = h + h*dist;
        else
            hnew = h + dist;
        
        const Real ep = 1e-6;
        
        if(mag(a) > ep)
            x = atan(o/a);
        else
            x = sign(o)*3.14159/2.;
        
        onew = hnew * sin(x + deg2r(deg));
        anew = hnew * cos(x + deg2r(deg));
        
        if(second.x >= first.x)
            return Point(first.x + anew, first.y + onew);
        else
            return Point(first.x - anew, first.y - onew);
    }
    
    // bounding box-based
    Point calcCurveBackup(const Point& src, const Point& cent, const Box& ext, Real dist = 20);

    class Line2Desc {
    public:
      Line2Desc(const Point& start, const Point& end);

      Real getA() const { return A_; }

      Real getB() const { return B_; }

      Real getC() const { return C_; }

    protected:
      Real A_, B_, C_;

	  _GraphfabExport friend std::ostream& operator<<(std::ostream& o, const Line2Desc& c);
    };

    _GraphfabExport std::ostream& operator<<(std::ostream& o, const Line2Desc& c);

    class CubicBezier2Desc {
    public:
      CubicBezier2Desc(const Point& start, const Point& c1, const Point& c2, const Point& end);

      /// Computes a point on the parametric curve
      Point p(Real t) const;

      /// Returns the nth control point
      Point getCP(int n) const;

    protected:
      Point P0_, P1_, P2_, P3_;

	  _GraphfabExport friend std::ostream& operator<<(std::ostream& o, const CubicBezier2Desc& c);
    };

    _GraphfabExport std::ostream& operator<<(std::ostream& o, const CubicBezier2Desc& c);

    // http://www.particleincell.com/blog/2013/cubic-line-intersection/
    class CubicBezierIntersection {
    public:
      CubicBezierIntersection(const Line2Desc& l, const CubicBezier2Desc& c);

      const std::vector<Real>& getIntersectionPoints() const { return r_; }

    protected:
      std::vector<Real> r_;
    };

//     class LinearIntersectionResults {
//     public:
//       const Point& p() { return p_; }
//       bool exists() { return v_; }
//
//     protected:
//       Point p_;
//       bool v_;
//
//       friend class LinearIntersection;
//     };

    class LinearIntersection {
    public:
      LinearIntersection(const Point& pbegin, const Point& pend, const Point& qbegin, const Point& qend);

      const Point& p() { return p_; }
      bool exists() { return v_; }

    protected:
      Point p_;
      bool v_;
    };
    
}

#else                                                       // __cplusplus



#endif                                                      // __cplusplus

#endif
