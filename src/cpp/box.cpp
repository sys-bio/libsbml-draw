/* MIT License
 */

//== BEGINNING OF CODE ===============================================================

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "box.h"
#include "sign_mag.h"
#include "allen.h"

namespace LibsbmlDraw {
    
    std::ostream& operator<< (std::ostream& o, const Box& b) {
        b.dump(o);
		return o;
    }
    
    // intersection of a ray emating from the origin (in direction v) & a horizontal line
    Point intersectRayHLine(const Point& v, const Real c) {
        AT(mag(v.y) > 1e-6, "No intersection");
        Real s = c / v.y;
        return Point(s*v.x, c);
    }
    
    // intersection of a ray emating from the origin (in direction v) & a vertical line
    Point intersectRayVLine(const Point& v, const Real c) {
        AT(mag(v.x) > 1e-6, "No intersection");
        Real s = c / v.x;
        return Point(c, s*v.y);
    }
    
    // intersection of line segment origin->v & horizontal line y = c
    std::pair<bool, Point> intersectVecHLineBounded(const Point& v, const Real c, const Real min, const Real max) {
        if(pointInInterval(c, Interval(0, v.y))) {
            Point p = intersectRayHLine(v,c);
            // check that it fits in the bounds of the box
            if(min <= p.x && p.x <= max)
                return std::make_pair(true, p);
            return std::make_pair(false, Point(0,0));
        } else
            return std::make_pair(false, Point(0,0));
    }
    
    // intersection of line segment origin->v & vertical line x = c
    std::pair<bool, Point> intersectVecVLineBounded(const Point& v, const Real c, const Real min, const Real max) {
        if(pointInInterval(c, Interval(0, v.x))) {
            Point p = intersectRayVLine(v,c);
            // check that it fits in the bounds of the box
            if(min <= p.y && p.y <= max)
                return std::make_pair(true, p);
            return std::make_pair(false, Point(0,0));
        } else
            return std::make_pair(false, Point(0,0));
    }
    
    std::pair<bool, Point> intersectBoxLine(const Box& b_, const Point& u, const Point& v_) {
        // make relative to a:
        Box b(b_.getMin()-u, b_.getMax()-u);
        Real bx1 = b.getMin().x, bx2 = b.getMax().x, by1 = b.getMin().y, by2 = b.getMax().y;
        Point v(v_-u);
        std::pair<bool, Point> r;
        // try top edge
        r = intersectVecHLineBounded(v, by1, bx1, bx2);
        if(r.first)
            return r;
        // try bottom edge
        r = intersectVecHLineBounded(v, by2, bx1, bx2);
        if(r.first)
            return r;
        // try left edge
        r = intersectVecVLineBounded(v, bx1, by1, by2);
        if(r.first)
            return r;
        // try right edge
        r = intersectVecVLineBounded(v, bx2, by1, by2);
        if(r.first)
            return r;
        
        AN(0, "Should not happen");
        return r;
    }

}
