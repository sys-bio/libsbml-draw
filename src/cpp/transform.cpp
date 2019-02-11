/* MIT License
 */

//== BEGINNING OF CODE ===============================================================

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "transform.h"

namespace LibsbmlDraw {
    
    // CLASS Affine2d:
    
    Affine2d Affine2d::inv() const {
        Affine2d t(
            (rc(1,1)*rc(2,2) - rc(1,2)*rc(2,1)), -(rc(0,1)*rc(2,2) - rc(0,2)*rc(2,1)),  (rc(0,1)*rc(1,2) - rc(0,2)*rc(1,1)),
           -(rc(1,0)*rc(2,2) - rc(1,2)*rc(2,0)),  (rc(0,0)*rc(2,2) - rc(0,2)*rc(2,0)), -(rc(0,0)*rc(1,2) - rc(0,2)*rc(1,0)),
            (rc(1,0)*rc(2,1) - rc(1,1)*rc(2,0)), -(rc(0,0)*rc(2,1) - rc(0,1)*rc(2,0)),  (rc(0,0)*rc(1,1) - rc(0,1)*rc(1,0))
        );
        
        return t/det();
    }
    
    Real Affine2d::det() const {
        return rc(0,0)*(rc(1,1)*rc(2,2)-rc(2,1)*rc(1,2)) -
               rc(0,1)*(rc(1,0)*rc(2,2)-rc(2,0)*rc(1,2)) +
               rc(0,2)*(rc(1,0)*rc(2,1)-rc(2,0)*rc(1,1));
    }
    
    // NOT TESTED!
//     Affine2d Affine2d::inv(const Affine2d& x) {
//         Affine2d t(x.cofactors());
//         
//         for(int i=0; i<3; ++i)
//             for(int j=0; j<3; ++j)
//                 t.set(i,j,x.rc(i,j)*t.rc(i,j));
//         
//         return t;
//     }
    
    Affine2d Affine2d::cofactors() const {
        Affine2d t;
        
        for(int i=0; i<3; ++i)
            for(int j=0; j<3; ++j)
                t.set(i,j,cofactor(i,j));
        
        return t;
    }
    
    Real Affine2d::cofactor(int i, int j) const {
        AT(0 <= i && i < 3, "col out of range");
        AT(0 <= j && j < 3, "row out of range");
        
        cutout c = getCutout(i,j);
        int sign = (i+j)%2 ? 1 : -1;
        
        return sign*c.det();
    }
    
    cutout Affine2d::getCutout(int r, int c) const {
        int i[2], j[2];
        
        int m=0,n=0;
        for(int k=0; k<3; ++k) {
            if(k != r) i[m++] = k;
            if(k != c) j[n++] = k;
        }
        
        return cutout(
            rc(i[0], j[0]), rc(i[0], j[1]),
            rc(i[1], j[0]), rc(i[1], j[1]));
    }
    
    Affine2d Affine2d::compose(const Affine2d& u, const Affine2d& v) {
        Affine2d a;
        for(int i=0; i<3; ++i)
            for(int j=0; j<3; ++j) {
                a.rcref(i,j) = 0.;
                for(int k=0; k<3; ++k)
                    a.rcref(i,j) += u.rc(i,k)*v.rc(k,j);
            }
        return a;
    }

    Affine2d Affine2d::FitToWindow(const Box& src, const Box& dst) {
//         std::cerr << "  Affine2d::FitToWindow: src " << src << " -> dst " << dst << "\n";
        Real factor = min(dst.width() / src.width(), dst.height() / src.height());
        // centering:
        Point offset((dst.width() - factor*src.width())/2., (dst.height() - factor*src.height())/2.);
        return fromPoints(Point(factor,0),
                          Point(0,factor),
                          dst.getMin() - factor*src.getMin() + offset);
    }
    
    Point Affine2d::operator*(const Point& x) const {
        return xformPoint(x, *this);
    }
    
    Box Affine2d::operator*(const Box& x) const {
        return xformBox(x, *this);
    }
    
    Affine2d Affine2d::operator*(const Real& k) const {
        return Affine2d(k*rc(0,0), k*rc(0,1), k*rc(0,2), 
                        k*rc(1,0), k*rc(1,1), k*rc(1,2), 
                        k*rc(2,0), k*rc(2,1), k*rc(2,2));
    }

    Point Affine2d::applyLinearOnly(const Point& p) const {
        return Point(
                     p.x*rc(0,0) + p.y*rc(0,1),
                     p.x*rc(1,0) + p.y*rc(1,1));
    }
    
    // GLOBALS:
    
    Point xformPoint(const Point& p, const Affine2d& t) {
        return Point(
                     p.x*t.rc(0,0) + p.y*t.rc(0,1) + t.rc(0,2),
                     p.x*t.rc(1,0) + p.y*t.rc(1,1) + t.rc(1,2));
    }
    
    Box xformBox(const Box& b, const Affine2d& t) {
        return Box(xformPoint(b.getMin(), t), xformPoint(b.getMax(), t));
    }
    
    Affine2d makeXlate(const Point& p) {
        Affine2d a;
        a.rcref(0,2) = p.x;
        a.rcref(1,2) = p.y;
        return a;
    }
    
    std::ostream& operator<<(std::ostream& o, const Affine2d& t) {
        o << t.rc(0,0) << ", " << t.rc(0,1) << ", " << t.rc(0,2) << "\n" << 
             t.rc(1,0) << ", " << t.rc(1,1) << ", " << t.rc(1,2) << "\n" <<
             t.rc(2,0) << ", " << t.rc(2,1) << ", " << t.rc(2,2) << "\n";
        return o;
    }

}
