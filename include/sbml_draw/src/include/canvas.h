/* MIT License
 */

//== FILEDOC =========================================================================

/** @file canvas.h
 * @brief Canvas for drawing diagram, dimensions
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SBNW_LAYOUT_CANVAS_H_
#define __SBNW_LAYOUT_CANVAS_H_

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "autolayoutSBML.h"
#include "box.h"

//-- C++ code --
#ifdef __cplusplus

namespace LibsbmlDraw {

    /** @brief Drawing canvas
     */
    class Canvas {
        public:
            Canvas() : _w(0), _h(0) {}

            Canvas(Real width, Real height) : _w(width), _h(height) {}

            /// Get the canvas width
            Real getWidth() const;
            
            /// Get the canvas height
            Real getHeight() const;
            
            /// Get the canvas width
            void setWidth(Real w);
            
            /// Get the canvas height
            void setHeight(Real h);
            
            /// Get canvas as a box
            Box getBox() const { return Box(Point(0,0), Point(getWidth(),getHeight())); }
            
        protected:
            // member vars
            /// Width
            Real _w;
            
            /// Height
            Real _h;
    };
    
}

#endif

#endif
