/* MIT License
 */

//== BEGINNING OF CODE ===============================================================

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "tikz.h"
#include "string_helpers.h"

#include <sstream>

const char* gf_renderTikZ(gf_layoutInfo* l) {
  using namespace LibsbmlDraw;

  try {
    Network* net = (Network*)l->net;
    if (!net)
      SBNW_THROW(InternalCheckFailureException, "No network set", "gf_renderTikZ");
    Canvas* can = (Canvas*)l->canv;
    if (!can)
      SBNW_THROW(InternalCheckFailureException, "No canvas set", "gf_renderTikZ");

    LibsbmlDraw::Real cmscale = 50.;
    TikZRenderer renderer(can->getBox(), can->getWidth()/cmscale, can->getHeight()/cmscale);
    return gf_strclone(renderer.str(net, can).c_str());
  } catch (const Exception& e) {
    gf_setError( e.getReport().c_str() );
    return NULL;
  }
}

int gf_renderTikZFile(gf_layoutInfo* l, const char* filename) {
  try {
//   fprintf(stderr, "Saving to TikZ file %s\n", filename);
    FILE* f = fopen(filename, "w");
    if (!f)
      SBNW_THROW(LibsbmlDraw::InternalCheckFailureException, "Could not open file " + ( filename ? std::string(filename) : std::string("") ), "gf_renderTikZFile");

    const char* buf = gf_renderTikZ(l);
    if (!buf)
      SBNW_THROW(LibsbmlDraw::InternalCheckFailureException, "Could not create buffer", "gf_renderTikZFile");

    fprintf(f, "%s", buf);

    fclose(f);

    return 0;

  } catch (const LibsbmlDraw::Exception& e) {
    gf_setError( e.getReport().c_str() );
    return 1;
  }
}

namespace LibsbmlDraw {

  std::string replaceSubstr(const std::string& input, const std::string& src, const std::string& dst) {
    // http://stackoverflow.com/questions/4643512/replace-substring-with-another-substring-c
    std::string result(input);
    std::size_t index = 0;
    while (true) {
      index = result.find(src, index);
      if (index == std::string::npos) break;

      result.replace(index, src.size(), dst);
      index += dst.size();
    }
    return result;
  }

  TikZRenderer::TikZRenderer(Box extents, Real widthcm, Real heightcm)
    : extents_(extents), widthcm_(widthcm), heightcm_(heightcm) {}

  std::string TikZRenderer::process(Point p) const {
    p.y = extents_.height() - p.y;
    return (0.01*p).rep();
  }

  std::string TikZRenderer::formatNodeText(const std::string& text) const {
    return replaceSubstr(text, "_", "\\_");
  }

  std::string TikZRenderer::str(Network* net, Canvas* can) {
    std::stringstream ss;
    ss << "\\begin{tikzpicture}\n";

    ss << "\\definecolor{jdorange}{rgb}{0.8, 0.5, 0.5}\n";

    ss << "\\definecolor{jdzero}{rgb}{1.0, 0.5, 0.5}\n";

    ss << "\n";

//     ss <<
//       "\\begin{axis}[\n"
//       "xmin=" << extents_.getMin().x << ", xmax=" << extents_.getMax().x << ",\n"
//       "ymin=" << extents_.getMin().y << ", ymax=" << extents_.getMax().y << ",\n"
//       "axis on top,\n"
//       "width=" << widthcm_ << "cm,\n"
//       "height=" <<  heightcm_ <<  "cm  \n"
//       "]\n";

    for (Network::RxnIt i=net->RxnsBegin(); i!=net->RxnsEnd(); ++i) {
      Reaction* r = *i;
      //  rebuilds curves
      r->getNumCurves();
      for (Reaction::CurveIt ci=r->CurvesBegin(); ci!=r->CurvesEnd(); ++ci) {
         RxnBezier* c = *ci;
         ss << "\\draw " <<
           process(c->s)  << " .. controls " <<
           process(c->c1)  << " and " <<
           process(c->c2) << " .. " <<
           process(c->e) <<
           ";\n";
      }
    }

    ss << "\n\n";

    for(Network::NodeIt i=net->NodesBegin(); i!=net->NodesEnd(); ++i) {
      Node* n = *i;
      Box b = n->getExtents();
//       ss <<
//        "\\draw " <<
//         process(b.getFirstQuadCorner())  << " -- " <<
//         process(b.getSecondQuadCorner()) << " -- " <<
//         process(b.getThirdQuadCorner())  << " -- " <<
//         process(b.getFourthQuadCorner()) << " -- " <<
//         process(b.getFirstQuadCorner())  << ";\n";

      ss <<
        "\\node[rounded corners=2pt, draw=jdorange, left color=jdzero,  right color=white] at " << process(n->getCentroid()) << "[\n" <<
        "  scale=0.45,\n" <<
        "  text=black,\n" <<
        "  rotate=0.0\n" <<
        "]{" << formatNodeText(n->getId()) << "};\n";
    }

    ss << "\n";

//     ss << "\\end{axis}\n";
    ss << "\\end{tikzpicture}\n";

    return ss.str();
  }

  std::ostream& operator<<(std::ostream& o, const TikZRenderer& r) {
    return o;
  }

}
