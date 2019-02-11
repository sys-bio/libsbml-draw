/* MIT License
 */

//== FILEDOC =========================================================================

/** @file canvas.h
 * @brief Canvas for drawing diagram, dimensions
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SBNW_DRAW_MAGICK_H_
#define __SBNW_DRAW_MAGICK_H_

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "layout.h"  // this says, graphfab/sbml/layout.h which doesn't exist, is this the right one?

//-- C code --

#ifdef __cplusplus
extern "C" {
#endif

/**
 * @param[in] l Layout info
 * @param[in] filename The filename
 * @param[in] tf Pointer to @ref Affine2d describing the view transform
 */
void gf_MagickRenderToFile(gf_layoutInfo* l, const char* filename, void* tf);

#ifdef __cplusplus
}//extern "C"
#endif

//-- C++ code --
#ifdef __cplusplus

namespace LibsbmlDraw {

    
    
}

#endif

#endif
