/* MIT License
 */

//== FILEDOC =========================================================================

/**
 * @author JKM
 * @file arrowhead.cpp
 * @date 02/05/2015
 * @copyright BSD 3-clause (details in source)
 * @brief Arrowhead primitive
  */

//== BEGINNING OF CODE ===============================================================

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "arrowhead.h"

//-- C++ code --
#ifdef __cplusplus

#include <string>

#include <iostream>

static unsigned long n_semicirc_segments = 16;

namespace LibsbmlDraw {

  unsigned long ArrowheadStyles::count() {
    return 8;
  }

  unsigned long ArrowheadStyles::getNumVerts(ArrowheadStyle style) {
    switch (style) {
      case 0:
        return 0;
      case 1:
      case 2:
        return 4;
      case 3:
      case 4:
        return 4;
      case 5:
        return 2;
      case 6:
        return 4;
      case 7:
        return n_semicirc_segments;
      default:
        SBNW_THROW(InvalidParameterException, "Unknown style", "ArrowheadStyles::getNumVerts");
    }
  }

  bool ArrowheadStyles::isFilled(ArrowheadStyle style) {
    switch (style) {
      case 0:
        return false;
      case 1:
        return false;
      case 2:
        return true;
      case 3:
        return false;
      case 4:
        return true;
      case 5:
        return false;
      case 6:
        return false;
      case 7:
        return false;
      default:
        SBNW_THROW(InvalidParameterException, "Unknown style", "ArrowheadStyles::isFilled");
    }
  }

  Point ArrowheadStyles::getVert(ArrowheadStyle style, int n) {
    switch (style) {
      case 0:
        SBNW_THROW(InvalidParameterException, "No verts", "ArrowheadStyles::getVert");
      case 1:
      case 2:
        // wide arrow
        switch (n) {
          case 0:
            return Point(0, 1);
          case 1:
            return Point(1, 0);
          case 2:
            return Point(-1, 0);
          case 3:
            return Point(0, 1);
          default:
            SBNW_THROW(InvalidParameterException, "Index out of range", "ArrowheadStyles::getVert");
        }
      case 3:
      case 4:
        // narrow arrow
        switch (n) {
          case 0:
            return Point(0, 1);
          case 1:
            return Point(0.5, 0);
          case 2:
            return Point(-0.5, 0);
          case 3:
            return Point(0, 1);
          default:
            SBNW_THROW(InvalidParameterException, "Index out of range", "ArrowheadStyles::getVert");
        }
      case 5:
        // crossbar
        switch (n) {
          case 0:
            return Point(-1, 0);
          case 1:
            return Point(1, 0);
          default:
            SBNW_THROW(InvalidParameterException, "Index out of range", "ArrowheadStyles::getVert");
        }
      case 6:
        // open box
        switch (n) {
          case 0:
            return Point(-1, 0.5);
          case 1:
            return Point(-1, 0);
          case 2:
            return Point(1, 0);
          case 3:
            return Point(1, 0.5);
          default:
            SBNW_THROW(InvalidParameterException, "Index out of range", "ArrowheadStyles::getVert");
        }
      case 7:
        // semicircle
        {
          Real t = (Real)n/(Real)n_semicirc_segments;
          return Point(cos(t*pi), -sin(t*pi)+1.);
        }
      default:
        SBNW_THROW(InvalidParameterException, "Unknown style", "ArrowheadStyles::getVert");
    }
  }

  unsigned long SubstrateArrowhead::getNumVerts() const {
    return ArrowheadStyles::getNumVerts(ArrowheadStyleLookup(this));
  }

  Point SubstrateArrowhead::getVert(unsigned long n) const {
    return ArrowheadStyles::getVert(ArrowheadStyleLookup(this), n);
  }

  unsigned long ProductArrowhead::getNumVerts() const {
    return ArrowheadStyles::getNumVerts(ArrowheadStyleLookup(this));
  }

  Point ProductArrowhead::getVert(unsigned long n) const {
    return ArrowheadStyles::getVert(ArrowheadStyleLookup(this), n);
  }

  unsigned long ActivatorArrowhead::getNumVerts() const {
    return ArrowheadStyles::getNumVerts(ArrowheadStyleLookup(this));
  }

  Point ActivatorArrowhead::getVert(unsigned long n) const {
    return ArrowheadStyles::getVert(ArrowheadStyleLookup(this), n);
  }

  unsigned long InhibitorArrowhead::getNumVerts() const {
    return ArrowheadStyles::getNumVerts(ArrowheadStyleLookup(this));
  }

  Point InhibitorArrowhead::getVert(unsigned long n) const {
    return ArrowheadStyles::getVert(ArrowheadStyleLookup(this), n);
  }

  unsigned long ModifierArrowhead::getNumVerts() const {
    return ArrowheadStyles::getNumVerts(ArrowheadStyleLookup(this));
  }

  Point ModifierArrowhead::getVert(unsigned long n) const {
    return ArrowheadStyles::getVert(ArrowheadStyleLookup(this), n);
  }

  ArrowheadStyle sub_arrow_style_ = 0;
  ArrowheadStyle prod_arrow_style_ = 1;
  ArrowheadStyle act_arrow_style_ = 4;
  ArrowheadStyle inh_arrow_style_ = 5;
  ArrowheadStyle mod_arrow_style_ = 7;

}

#endif
