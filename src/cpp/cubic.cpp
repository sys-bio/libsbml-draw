/* MIT License
 */

//== BEGINNING OF CODE ===============================================================

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "cubic.h"

namespace LibsbmlDraw {
    
    // CLASS CubicRoots:
    
    CubicRoots::CubicRoots(Real a2, Real a1, Real a0) {
      Complex p1 = a2*a2*a1*a1 +18.*a2*a1*a0 - 4.*a1*a1*a1 - 27.*a0*a0 - 4.*a2*a2*a2*a0;
      Complex p2 = 9.*a2*a1 - 27.*a0 - 2.*a2*a2*a2;

      Complex s = sqrtConventional(-3.*p1);

      Complex c1 = curtConventional((p2 + 3.*s)/2.);
      Complex c2 = curtConventional((p2 - 3.*s)/2.);

      Complex w = std::polar(1., 2.*pi/3.);

      Complex u1 = (-a2 + w*c1 + w*w*c2)/3.;
      Complex u2 = (-a2 + c1 + c2)/3.;
      Complex u3 = (-a2 + w*w*c1 + w*c2)/3.;

      x1_ = u1;
      x2_ = u2;
      x3_ = u3;
    }

    Complex CubicRoots::getRoot(int i) const {
      switch (i) {
        case 0:
          return x1_;
        case 1:
          return x2_;
        case 2:
          return x3_;
        default:
          SBNW_THROW(InvalidParameterException, "Index out of bounds", "CubicRoots::getRoot");
      }
    }

    bool CubicRoots::isRootReal(int i) const {
      Complex t = getRoot(i);
      Real r = std::real(t);
      const Real ep = 1e-3;
      return std::abs(std::abs(r) - std::abs(t)) < ep;
    }

    Real CubicRoots::getRealRoot(int i) const {
      if (!isRootReal(i))
        SBNW_THROW(RedundancyCheckFailureException, "Root is not real", "CubicRoots::getRealRoot");
      return std::real(getRoot(i));
    }

    Complex CubicRoots::sqrtConventional(Complex x) {
      return std::polar(std::pow(std::abs(x), 0.5), 0.5*std::arg(x));
    }

    Complex CubicRoots::curtConventional(Complex x) {
      Real r = std::pow(std::abs(x), 1/3.);
      Real a = std::arg(x);
      if (-pi < a && a < -pi/2)
        return std::polar(r, -(1./3.*a - 2./3.*pi));
      else if (a == -pi/2.)
        return std::polar(r, -(pi/2.));
      else if (-pi/2. < a && a < pi/2.)
        return std::polar(r, -(1/3.*a));
      else if (a ==  pi/2.)
        return std::polar(r, -(-pi/2.));
      else if (pi/2. < a && a <= pi)
        return std::polar(r, -(1./3.*a + 2./3.*pi));
      else
        // should not happen
        return std::polar(r, pi);
    }

    std::ostream& operator<<(std::ostream& o, const CubicRoots& c) {
      o << c.getRoot(0) << ", " << c.getRoot(1) << ", " << c.getRoot(2);
      return o;
    }

}
