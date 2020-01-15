/* MIT License
 */

//== FILEDOC =========================================================================

/** @file BaseWORDS.h
 * @brief Bit-size typedefs
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SAGITTARIUS_BASEWORDS_H_
#define __SAGITTARIUS_BASEWORDS_H_

//== INCLUDES ========================================================================

#include "SagittariusCommon.h"

#include <stdint.h>

//==DEFINES/TYPES===================================//

//Sorry, but we can't put these typedefs in the Sagittarius
//namespace. There are extern "C" functions defined in C++
//headers that need to use these types, hence they must be
//available in the default namespace
/*#ifdef __cplusplus
namespace Sagittarius
{
#endif*/
    
    //These int sizes must be verified for each platform, but once that is done,
    //just plug in the appropriate types and go.
    
    //INTs:
    
    typedef int8_t      int8;
    typedef uint8_t     uint8;
    
    typedef int16_t     int16;
    typedef uint16_t    uint16;
    
    #define SG_UINT16_MAX 65535
    
    //typedef long            int32; //8 bytes for x86_64
    //typedef unsigned long   uint32; //8 bytes for x86_64
    
    typedef int32_t     int32;
    typedef uint32_t    uint32;
    
    typedef int64_t     int64; //also long long
    typedef uint64_t    uint64;
    
    //FLOATING POINT TYPES:
    
    typedef float       fp32;
    typedef double      fp64;
    
    //CHARACTERS:
    
    typedef char char8;
    typedef unsigned char uchar8;
    
    #define INT64_LOW_MASK  0x00000000FFFFFFFF
    #define INT64_HIGH_MASK 0xFFFFFFFF00000000
    
    //pointers
    #if SAGITTARIUS_ARCH == SAGITTARIUS_ARCH_64
        #define SG_POINTER_UINT uint64
    #elif SAGITTARIUS_ARCH == SAGITTARIUS_ARCH_64
        #define SG_POINTER_UINT uint32
    #endif
    
    //misc
    //booleans
    #define true 1 //don't rely on if(b == true), use if(b) instead
    #define false 0
    #ifndef __cplusplus
        #define sg_casbool sg_cas32
        typedef int32 bool;
    #endif
    
/*#ifdef __cplusplus
}
#endif*/

#endif
