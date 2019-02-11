/* MIT License
 */

//== BEGINNING OF CODE ===============================================================

#include "SagittariusAssert.h"
#include <stdlib.h>
#include <stdio.h>

void sg_ast_fail(const char* message, const char* file, unsigned long line, const char* func) {
#ifdef SAGITTARIUS_PLATFORM_WIN
     fprintf(stderr, "assert fail %s\n", message);
#else
     __assert_fail (message, file, line, func);
#endif
    exit(1);
}