/* MIT License
 */

//== BEGINNING OF CODE ===============================================================

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "canvas.h"

namespace LibsbmlDraw {
    
    //--CLASS Canvas--
    Real Canvas::getWidth() const {
        return _w;
    }
    
    
    Real Canvas::getHeight() const {
        return _h;
    }
    
    void Canvas::setWidth(Real w) {
        if(w < 0.)
            SBNW_THROW(InvalidParameterException, "Width cannot be negative", "Canvas::setWidth");
        _w = w;
    }
    
    
    void Canvas::setHeight(Real h) {
        if(h < 0.)
            SBNW_THROW(InvalidParameterException, "Height cannot be negative", "Canvas::setWidth");
        _h = h;
    }

}
