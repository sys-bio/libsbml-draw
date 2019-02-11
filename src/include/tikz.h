/* MIT License
 */

//== FILEDOC =========================================================================

/**
 * @author JKM
 * @file tikz.h
 * @date 01/13/2015
 * @copyright BSD 3-clause (details in source)
 * @brief Render TikZ plots
  */

//== BEGINNING OF CODE ===============================================================

#ifndef __SBNW_DRAW_TIKZ_H_
#define __SBNW_DRAW_TIKZ_H_

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "box.h"
#include "canvas.h"
#include "network.h"
#include "layout.h"

#ifdef __cplusplus
extern "C" {
#endif

/** @brief Render the model as a TikZ image
 *  @param[in] l The model/layout infor
 *  \ingroup C_API
 */
_GraphfabExport const char* gf_renderTikZ(gf_layoutInfo* l);

/** @brief Render the model as a TikZ image
 *  @param[in] l The model/layout infor
 *  \ingroup C_API
 */
_GraphfabExport int gf_renderTikZFile(gf_layoutInfo* l, const char* filename);

#ifdef __cplusplus
}//extern "C"
#endif

//-- C++ code --
# ifdef __cplusplus

# include <iostream>

namespace LibsbmlDraw {
    
	class _GraphfabExport TikZRenderer {
    public:
      TikZRenderer(Box extents, Real widthcm, Real heightcm);

      std::string str(Network* net, Canvas* can);

      std::string process(Point p) const;

      std::string formatNodeText(const std::string& text) const;

    protected:
      Box extents_;
      Real widthcm_, heightcm_;
  };

    _GraphfabExport std::ostream& operator<<(std::ostream& o, const TikZRenderer& r);
    
}

# endif

#endif
