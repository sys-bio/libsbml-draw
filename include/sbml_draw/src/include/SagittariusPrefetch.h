/* MIT License
 */

//== BEGINNING OF CODE ===============================================================

#ifndef __SAGITTARIUS_ASSERT_H_
#define __SAGITTARIUS_ASSERT_H_

//== INCLUDES ========================================================================

#include "SagittariusCommon.h"

#if SAGITTARIUS_COMPILER == SAGITTARIUS_COMPILER_GNUC
    #define SPREFETCH(x)    __builtin_prefetch(x) //two additional arguments: rw and locality, see http://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html
#endif


#endif
