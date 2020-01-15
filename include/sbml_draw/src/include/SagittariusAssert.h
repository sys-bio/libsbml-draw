/* MIT License
 */

//== BEGINNING OF CODE ===============================================================

#ifndef __SAGITTARIUS_ASSERT_H_
#define __SAGITTARIUS_ASSERT_H_

//== INCLUDES ========================================================================

#include "SagittariusCommon.h"
#include <assert.h>

#ifndef PYTHON_SCREWED_IT_UP
    #define REALASSERT(x) assert(x);
#else
    #if SAGITTARIUS_PLATFORM == SAGITTARIUS_PLATFORM_LINUX
        #define REALASSERT(x) ((x) ? (void)0 : sg_ast_fail(QUOTE(x), __FILE__, __LINE__, __PRETTY_FUNCTION__))
    #elif SAGITTARIUS_PLATFORM == SAGITTARIUS_PLATFORM_WIN
        #define REALASSERT(x) ((x) ? (void)0 : sg_ast_fail(QUOTE(x), __FILE__, __LINE__, __FUNCTION__))
    #elif SAGITTARIUS_PLATFORM == SAGITTARIUS_PLATFORM_APPLE
        #define REALASSERT(x) ((x) ? (void)0 : sg_ast_fail(QUOTE(x), __FILE__, __LINE__, __PRETTY_FUNCTION__))
    #endif
#endif

    //We have many styles to choose from...
    #define SAGITTARIUS_ASSERT1( x ) REALASSERT( x )
    #define SAGITTARIUS_ASSERT2( x, msg ) REALASSERT( (x) && msg ) //thank you gcc
    #define SAGITTARIUS_IASSERT1( x ) REALASSERT( !(x) )
    #define SAGITTARIUS_IASSERT2( x, msg ) REALASSERT( !(x) && msg )
    #define EXPAND(x) x //Workaround for MSVC bug
    #define GET_ASTM(A1, A2, A3, A4, ...) A4
    
    #define SAGITTARIUS_ASSERT ( ... ) EXPAND (GET_ASTM(__VA_ARGS__, ***error*** "Too many arguments to assert; file: "__FILE__:__LINE__,\
        SAGITTARIUS_ASSERT2, SAGITTARIUS_ASSERT1)( __VA_ARGS__ ))
    
    //Shorthand:
    #define AST( ... ) SAGITTARIUS_ASSERT( __VA_ARGS__ )
    //Assert true
    #define AT( ... ) SAGITTARIUS_ASSERT( __VA_ARGS__ )
    //Assert not zero:
    /** @details @ref AN and @ref AZ were inspired by an ACM letter
     * whose author escapes me right now. It's a beautifully concise
     * way to write assertions that are self-explanatory. AN means
     * "assert not zero" and AZ means "assert zero". An optional second
     * argument provides an error report that the user will see. Very useful.
     */
    #define AN( ... ) SAGITTARIUS_ASSERT( __VA_ARGS__ )
    //Assert ^ZERO^:
    #define AZ( ... ) EXPAND(GET_ASTM(__VA_ARGS__, ***error*** "Too many arguments to assert; file: "__FILE__:__LINE__,\
        SAGITTARIUS_IASSERT2, SAGITTARIUS_IASSERT1)( __VA_ARGS__ ))

#ifdef __cplusplus
extern "C" {
#endif

_GraphfabExport void sg_ast_fail(const char* message, const char* file, unsigned long line, const char* func);
        
#ifdef __cplusplus
}//extern "C"
#endif

#endif
