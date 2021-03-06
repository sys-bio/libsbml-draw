/* MIT License
 */

//== BEGINNING OF CODE ===============================================================

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "fr.h"
#include "canvas.h"
#include "rand_unif.h"
#include "min_max.h"
#include "dist.h"
#include "transform.h"

//#if SBNW_USE_MAGICK
//#include "magick.h"
//#endif

#include <sstream>

//#include <math.h>

#define e 2.71828182845905

//#include <fenv.h>

static bool dumpForces_ = false;

void gf_getLayoutOptDefaults(fr_options* opt) {
    opt->k = 50.;
    opt->grav = 0.;
    opt->baryx = opt->baryy = 500.;
    opt->autobary = 1;
    opt->padding = 15;
}

void gf_layout_setStiffness(fr_options* opt, double k) {
    opt->k = k;
}

void gf_doLayoutAlgorithm(fr_options opt, gf_layoutInfo* l) {
    using namespace LibsbmlDraw;
    
    Network* net = (Network*)l->net;
    AN(net, "No network");
    Canvas* can = (Canvas*)l->canv;
    AN(can, "No canvas");
    
	FruchtermanReingold(opt, *net, can, l);
}

void gf_doLayoutAlgorithm2(fr_options opt, gf_network* n, gf_canvas* c) {
    using namespace LibsbmlDraw;
    
    AN(n, "No network");
    Network* net = (Network*)n->n;
    AN(net, "No network");
    
    Canvas* can = NULL;
    if(c) {
        can = (Canvas*)c->canv;
        AN(can, "No canvas");
    }
    
    FruchtermanReingold(opt, *net, can, NULL);
}

namespace LibsbmlDraw {
    
    bool eltTypesInteract(const NetworkEltType a, const NetworkEltType b, fr_options* opt) {
//         if (a == b && b == NET_ELT_TYPE_SPEC)
//           return false;
        if(typeMatchEither(a,b,NET_ELT_TYPE_COMP))
            return false;
        if(typeMatchEither(a,b,NET_ELT_TYPE_RXN) && typeMatchEither(a,b,NET_ELT_TYPE_COMP))
            //reactions & comps don't interact
            return false;
        return true;
    }
    
    Real calc_fr(const Real k, const Real d) {
        return k*k/d;
    }
    
    Real calc_fa(const Real k, const Real d) {
        return d*d/k;
    }
    
    // compute the internal force between a compartment & its node
    void do_internalForce(NetworkElement* u, Compartment& c, Real k) {
        c.doInternalForce(u, k*k, 10.);
    }
    
    // compute the repulsion force between two elements & apply it
    void do_repulForce(NetworkElement& u, NetworkElement& v, Real k, uint64 num) {
//         if(typeMatchEither(u.getType(),v.getType(),NET_ELT_TYPE_RXN))
          // reaction centroids to not repel
//           return;
//         if(typeMatchEither(u.getType(),v.getType(),NET_ELT_TYPE_RXN) && typeMatchEither(u.getType(),v.getType(),NET_ELT_TYPE_SPEC))
          // species and reaction centroids to not repel
//           return;

        Point delta(u.centroidDisplacementFrom(v).normed());
        Point f(0,0);
        
        // needs to be large because force is no longer calculated on the
        // basis of centroids
        Real ep = 1e-6;
        
        Real d = max(u.centroidDisplacementFrom(v).mag(), 0.1);
        
        if(u.centroidDisplacementFrom(v).mag2() < ep) {
            // repel nodes very close together with a large force of unspecified magnitude
            Real extreme = 100.*sqrt((Real)num);
            f = Point(rand_range(-extreme, extreme), rand_range(-extreme, extreme));
            
        } else {
            Real adjk = (k*log((Real)u.degree()+v.degree()+2) + (max(v.getWidth(), v.getHeight()) + max(u.getWidth(), u.getHeight()))/4);
//             std::cerr << "max(v.getWidth(), v.getHeight()) = " << max(v.getWidth(), v.getHeight()) << ", max(u.getWidth(), u.getHeight()) = " << max(u.getWidth(), u.getHeight()) << "\n";
            f = Point(delta * calc_fr(adjk, d));

            // compartment repulsion
            if(u.getType() == NET_ELT_TYPE_COMP && v.getType() == NET_ELT_TYPE_COMP) {
                f = 0.01*f;
                if(d > 25.)
                    f = Point(0,0);
            }
        }
        
        if (dumpForces_)
          std::cout << "Repulsion force between " << eltTypeToStr(u.getType()) << " and " << eltTypeToStr(v.getType()) << ": " << f.mag()/d << "\n";
        
        u.addDelta(f);
        
        v.addDelta(-f);
    }
    
    // apply the attraction force
    void do_attForce(NetworkElement& u, NetworkElement& v, Real k) {
        Point delta(u.centroidDisplacementFrom(v).normed());
        //std::cout << "delta: " << delta << "\n";

//         std::cerr << "attr bet " << eltTypeToStr(u.getType()) << " & " << eltTypeToStr(v.getType()) << "\n";

        Real ep = 1.e-6;
        
        Real d = u.centroidDisplacementFrom(v).mag();
        
        if(d > ep) {
            //Real invd = 1./d;
            
            //Real adjk = k*log((Real)u.degree()+v.degree()+2);
            Real adjk = (k*log((Real)u.degree()+v.degree()+2) + (max(v.getWidth(), v.getHeight()) + max(u.getWidth(), u.getHeight()))/4);
            u.addDelta(-delta * calc_fa(u.getType() == NET_ELT_TYPE_RXN ? k : adjk, d));
            if (dumpForces_)
              std::cerr << "attr force bet "<< eltTypeToStr(u.getType()) << " & " << eltTypeToStr(v.getType()) << ": " << (delta * calc_fa(u.getType() == NET_ELT_TYPE_RXN ? k : adjk, d)).mag()/d << "\n";

            v.addDelta( delta * calc_fa(v.getType() == NET_ELT_TYPE_RXN ? k : adjk, d));
        }
    }

    // apply "gravitational" force
    void do_gravity(NetworkElement& u, Point bary, Real strength, Real k) {
      Point delta = u.getCentroid() - bary;

      if (delta.mag() < 1e-2)
        return;

      Real adjk = strength / k;
      u.addDelta( -delta * adjk );
    }
    
    // single interation
    void FRSingle(fr_options& opt, Network& net, Box bound, Real T, Real k, uint64 num) {
        net.resetActivity();
        
        net.updateExtents();
        
        // repulsive forces
        for(uint64 i=0; i<net.getNElts(); ++i) {
            //NetworkElement* u = *i;
            NetworkElement* u = net.getElt(i);;
            
            // is the network element a container?
            LibsbmlDraw::Compartment* comp=NULL;
            if(u->getType() == NET_ELT_TYPE_COMP)
                comp = dynamic_cast<Compartment*>(u); //get the associated compartment
            
            for(uint64 j=i+1; j<net.getNElts(); ++j) {
                //NetworkElement* v = *j;
                NetworkElement* v = net.getElt(j);
                AT(u != v, "Cannot apply to self");
                if(!eltTypesInteract(u->getType(), v->getType(), &opt))
                    continue; // elements do not interact
                
                do_repulForce(*u, *v, k, num);
            }
        }
        
        // attractive forces
        for(Network::RxnIt i=net.RxnsBegin(); i!=net.RxnsEnd(); ++i) {
            Reaction* u = *i;
            for(Reaction::NodeIt j=u->NodesBegin(); j!=u->NodesEnd(); ++j) {
                Node* v = j->first;
                do_attForce(*u, *v, k);
            }
        }

        if (opt.grav >= 5.) {
          for(uint64 i=0; i<net.getNElts(); ++i) {
            NetworkElement* u = net.getElt(i);;
            if (u->getType() == NET_ELT_TYPE_SPEC) {
              do_gravity(*u, Point(opt.baryx, opt.baryy), opt.grav, k);
            }
          }
        }
        
        net.capDeltas(T);
        
        //net.updatePositions(0.000025*T);
//         net.updatePositions(0.0001*T);
        net.updatePositions(T);

    }
    
    void FruchtermanReingold(fr_options opt, Network& net, Canvas* can, gf_layoutInfo* l) {
        //AT(feenableexcept(FE_DIVBYZERO) != -1);
        Box bound;
        
        uint64 num = net.getTotalNumPts();
        uint64 m = 100.*log((Real)num+2);
        
//         std::cerr << "m = " << m << "\n";
        
        Real k = opt.k;
        
        // initial temperature
        Real Ti = 1000.*log((Real)num+2);
        // Current temp
        Real T;
        
        // time
        Real t = 0.;
        // delta time
        Real dt = 1./m;
        
        Real alpha = log(Ti/0.25);
        
        Real ep = 1.e-6;
        
        dumpForces_ = false;

        for(uint64 z=0; z<m; ++z) {
            T = Ti*pow(e, -alpha*t);
            t += dt;
//             std::cerr << "T = " << T << "\n";

            // dump forces for last iteration
//             if (z == m-1)
//               dumpForces_ = true;
            
            FRSingle(opt, net, bound, T, k, num);
            
//             std::cout << "Network:\n";
//             net.dump(std::cout, 0);
            
//             std::cout << "Network forces:\n";
//             net.dumpEltForces(std::cout, 0);
            
//             std::cout << "Network mean: " << net.pmean() << "\n";
//             std::cout << "Network variance: " << net.pvariance() << "\n";
            
            /*#if SBNW_USE_MAGICK && 0
            if(!(z % 10)) {
                net.rebuildCurves();
                std::stringstream ss;
                ss << "/tmp/tmpfs/pic" << z/10 << ".png";
                Real w,h;
                if(can) {
                    w = can->getWidth();
                    h = can->getHeight();
                } else {
                    w = h = 1024.;
                }
                Affine2d view(Affine2d::makeXlate(-net.center())*
                    Affine2d::makeScale(0.5, 0.5)*Affine2d::makeXlate(Point(w*3/2,h*3/2)));
                AN(l, "Need layout to write images");
                gf_MagickRenderToFile(l, ss.str().c_str(), &view);
            }
            #endif  */
        }
        
        net.resizeCompsEnclose(opt.padding);
        
        net.rebuildCurves();
    }

}
