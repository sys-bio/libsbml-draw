/* MIT License
 */

//== BEGINNING OF CODE ===============================================================

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "layout.h"
#include "error.h"
#include "string.h"

#include "sbml/SBMLTypes.h"
#include "sbml/packages/layout/common/LayoutExtensionTypes.h"

#include <exception>

static std::string lastError_;

void gf_emitError(const char* str) {
    lastError_ = str;
    fprintf(stderr, "%s",  str);
}

void gf_emitWarn(const char* str) {
    fprintf(stderr, "%s", str);
}

char* gf_getLastError() {
  if (lastError_.size())
    return gf_strclone(lastError_.c_str());
  else
    return gf_strclone("");
}

int gf_haveError() {
  return lastError_.size();
}

void gf_clearError() {
  lastError_ = "";
}

void gf_setError(const char* msg) {
  lastError_ = msg;
}