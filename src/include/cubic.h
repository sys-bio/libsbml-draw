/* MIT License
 */

//== FILEDOC =========================================================================

/**
 * @author JKM
 * @file transform.h
 * @date 12/18/2014
 * @copyright BSD 3-clause (details in source)
 * @brief Roots of cubic equations
 * @details See https://hal.archives-ouvertes.fr/file/index/docid/627327/filename/SFCEC.pdf
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SBNW_CUBIC_H_
#define __SBNW_CUBIC_H_

//== INCLUDES ========================================================================

#include "SagittariusCore.h"

//-- C++ code --
# ifdef __cplusplus

# include <iostream>

namespace LibsbmlDraw {
    
	class _GraphfabExport CubicRoots {
        public:
            /// Solve the cubic polynomial x^3 + a2*x^2 + a1*x + a0 = 0
            CubicRoots(Real a2, Real a1, Real a0);

            Complex getRoot(int i) const;

            bool isRootReal(int i) const;

            Real getRealRoot(int i) const;

            /// Square root according to ZWH convention
            static Complex sqrtConventional(Complex x);

            /// Cubic root according to ZWH convention
            static Complex curtConventional(Complex x);

        protected:
          Complex x1_, x2_, x3_;
    };

    _GraphfabExport std::ostream& operator<<(std::ostream& o, const CubicRoots& c);
    
}

# endif

#endif
