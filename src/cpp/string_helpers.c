/* MIT License
 */

//== BEGINNING OF CODE ===============================================================

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "string_helpers.h"

#include <stdlib.h>
#include <string.h>

char* gf_strclone(const char* src) {
    if(!src) {
        AN(0, "gf_strclone passed null arg");
        return NULL;
    } else {
        size_t size = strlen(src)+1;
        char* dst = malloc(size*sizeof(char));
        
        memcpy(dst, src, size); // copies null char
        
        return dst;
    }
}

void gf_strfree(char* str) {
    free(str);
}