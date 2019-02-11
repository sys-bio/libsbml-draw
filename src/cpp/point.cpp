/* MIT License
 */

//== BEGINNING OF CODE ===============================================================

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "point.h"

namespace LibsbmlDraw {
    
    /*Point makePoint(const Real x, const Real y) {
        return Point(x,y);
    }*/

    Point Point::polar(Real mag, Real theta) {
      return Point(mag*cos(theta), mag*sin(theta));
    }
    
    Point operator- (const Point& p, const Point& q) {
        return Point(p.x-q.x, p.y-q.y);
    }
    
    Point operator+ (const Point& p, const Point& q) {
        return Point(p.x+q.x, p.y+q.y);
    }
    
    Point operator* (const Point& p, const Real s) {
        return Point(p.x*s, p.y*s);
    }
    
    Point operator* (const Real s, const Point& p) {
        return Point(p.x*s, p.y*s);
    }
    
    Point operator/ (const Point& p, const Real s) {
        return (1/s)*p;
    }

    std::string Point::rep() const {
      std::stringstream ss;
      ss << "(" << x << "," << y << ")";
      return ss.str();
    }
    
    std::ostream& operator<< (std::ostream& o, const Point& p) {
        o << "(" << p.x << ", " << p.y << ")";
		return o;
    }

}
