/* MIT License
 */

//== FILEDOC =========================================================================

/** @file SagittariusCommon.h
 * @brief Common required definitions
  * @details This provides definitions and limit info for basic types
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SAGITTARIUS_COMMON_H_
#define __SAGITTARIUS_COMMON_H_

//== INCLUDES ========================================================================

#include "SagittariusPlatform.h"
#include "config.h"

#ifdef __cplusplus
    #include <string>
    #include <vector>
    #include <list>
    #include <complex>
#endif

// Standard macros
// http://stackoverflow.com/questions/3419332/c-preprocessor-stringify-the-result-of-a-macro
#define QUOTE(ARG) #ARG
#define EXPAND_AND_QUOTE(ARG) QUOTE(ARG)
// http://www.altdevblogaday.com/2011/07/12/abusing-the-c-preprocessor/
#define JOIN(x, y) x##y

#ifdef __cplusplus
namespace LibsbmlDraw
{
#endif

    //C99 compatibility
    #ifndef __cplusplus
        #if __STDC_VERSION__ < 199901L
        // Gave up
        //#   error "C99 Support is REQUIRED"
        #endif
    #endif
    
    //maximum unsigned char...
    #if SAGITTARIUS_PLATFORM == SAGITTARIUS_PLATFORM_LINUX
    #   if SAGITTARIUS_ARCH == SAGITTARIUS_ARCH_64
    #       define PLATFORM_UCHAR_MAX 256
    #   elif SAGITTARIUS_ARCH == SAGITTARIUS_ARCH_32
    #       define PLATFORM_UCHAR_MAX 256
    #   endif
    #elif SAGITTARIUS_PLATFORM == SAGITTARIUS_PLATFORM_WIN
    #   if SAGITTARIUS_ARCH == SAGITTARIUS_ARCH_64
    #       define PLATFORM_UCHAR_MAX 256
    #   elif SAGITTARIUS_ARCH == SAGITTARIUS_ARCH_32
    #       define PLATFORM_UCHAR_MAX 256
    #   endif
    #elif SAGITTARIUS_PLATFORM == SAGITTARIUS_PLATFORM_APPLE
    #   if SAGITTARIUS_ARCH == SAGITTARIUS_ARCH_64
    #       define PLATFORM_UCHAR_MAX 256
    #   elif SAGITTARIUS_ARCH == SAGITTARIUS_ARCH_32
    #       define PLATFORM_UCHAR_MAX 256
    #   endif
    #endif
    
    /// See typedef below
    #define SAGITTARIUS_REAL double
    #define GF_PYREALFMT "d"
        
    /// Determines verbosity of diagnostic messages
    #define SAGITTARIUS_DEBUG_LEVEL SBNW_DEBUG_LEVEL
    
    //C++ typedefs
    
    #ifdef __cplusplus
        
        /// Default floating point type
        typedef SAGITTARIUS_REAL Real;

        typedef std::complex<Real> Complex;

        extern const Real pi;
        
        #if SAGITTARIUS_USE_WIDE_STRINGS
            /// Default string type (leading underscore means internal)
            typedef std::wstring _String;
        #else
            typedef std::string _String;
        #endif
        
        /// The real deal (cf. @ref _String);
        typedef _String String;
        /// If you need to be more specific about your charset...
        typedef _String ASCIIString;
        
        /// Not used?
        typedef unsigned long index_t;
        
    #endif//End of C++ typedefs
    
#ifdef __cplusplus
} //namespace Graphfab
#endif


//C typedefs
/// Make @ref Real visible to C. Consider letting @ref Real lie in top namespace.
// FIXME: this will cause problems
typedef SAGITTARIUS_REAL Real;


#endif
