/* MIT License
 */

//== BEGINNING OF CODE ===============================================================

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "magick.h"
#include "network.h"
#include "layoutall.h"
#include "transform.h"

#include <wand/MagickWand.h>

#include <iostream>

using namespace LibsbmlDraw;

//create image of a specified size
void gf_MagickSizeImage(MagickWand *wand, gf_layoutInfo* l) {
    //pixel wand
    PixelWand* pixie = NewPixelWand();
    
    PixelSetColor(pixie, "white");
    PixelSetAlpha(pixie, 1);
    
    //get canvas
    Canvas* can = (Canvas*)l->canv;
    if(can)
        MagickNewImage(wand, can->getWidth(), can->getHeight(), pixie);
    else
        MagickNewImage(wand, 1024, 1024, pixie);
    
    //release wands
    pixie = DestroyPixelWand(pixie);
}

//draw the compartments
void gf_MagickDrawComps(MagickWand *wand, gf_layoutInfo* l, Affine2d* tf) {
    Network* net = (Network*)l->net;
    AN(net, "No network");
    
    //create our wands
    PixelWand* pixie = NewPixelWand();
    PixelSetColor(pixie, "gold");
    DrawingWand* dw = NewDrawingWand();
    DrawSetFillColor(dw, pixie);
    PixelSetColor(pixie, "black");
    DrawSetStrokeColor(dw, pixie);
    DrawSetStrokeWidth(dw, 2.0);
    
    for(Network::ConstCompIt i=net->CompsBegin(); i!=net->CompsEnd(); ++i) {
        LibsbmlDraw::Compartment* c = *i;
        // coordiates of bounding box
        LibsbmlDraw::Point ul = xformPoint(c->getExtents().getMin(), *tf), lr = xformPoint(c->getExtents().getMax(), *tf);
        
        DrawRoundRectangle(dw, ul.x, ul.y, lr.x, lr.y, 25., 25.);
        MagickDrawImage(wand, dw);
    }
    
    //release wands
    dw = DestroyDrawingWand(dw);
    pixie = DestroyPixelWand(pixie);
}

//draw the nodes
void gf_MagickDrawNodes(MagickWand *wand, gf_layoutInfo* l, Affine2d* tf) {
    Network* net = (Network*)l->net;
    AN(net, "No network");
    
    //create our wands
    PixelWand* pixie = NewPixelWand();
    PixelSetColor(pixie, "purple");
    DrawingWand* dw = NewDrawingWand();
    DrawSetFillColor(dw, pixie);
    
    for(Network::ConstNodeIt i=net->NodesBegin(); i!=net->NodesEnd(); ++i) {
        Node* n = *i;
        // coordiates of bounding box
        LibsbmlDraw::Point ul = xformPoint(n->getUpperLeftCorner(), *tf), lr = xformPoint(n->getLowerRightCorner(), *tf);
        
        //set the color
        if(n->isAlias())
            PixelSetColor(pixie, "pink");
        else
            PixelSetColor(pixie, "purple");
        DrawSetFillColor(dw, pixie);
        
        DrawRoundRectangle(dw, ul.x, ul.y, lr.x, lr.y, 10., 10.);
        MagickDrawImage(wand, dw);
    }
    
    //release wands
    dw = DestroyDrawingWand(dw);
    pixie = DestroyPixelWand(pixie);
}

//draw a curve
void gf_MagickDrawRxnCurve(MagickWand *wand, RxnBezier* c, bool straight, Affine2d* tf) {
    //create our wands
    PixelWand* pixie = NewPixelWand();
    PixelSetColor(pixie, "black");
    DrawingWand* dw = NewDrawingWand();
    DrawSetStrokeColor(dw, pixie);
    DrawSetStrokeWidth(dw, 2.0);
    PixelSetColor(pixie, "none");
    DrawSetFillColor(dw, pixie);
    
    if(straight) {
        LibsbmlDraw::Point start(xformPoint(*c->as, *tf)), stop(xformPoint(*c->ae, *tf));
        DrawLine(dw, start.x, start.y, stop.x, stop.y);
    } else {
        LibsbmlDraw::Point s (xformPoint(c->s, *tf)),  e (xformPoint(c->e, *tf)),
                        c1(xformPoint(c->c1, *tf)), c2(xformPoint(c->c2, *tf));
        const PointInfo p[8] = {
            {s.x, s.y}, {c1.x,c1.y}, {c2.x,c2.y}, {e.x,e.y}};
        DrawBezier(dw, 4, p);
    }
    MagickDrawImage(wand, dw);
    
    //release wands
    dw = DestroyDrawingWand(dw);
    pixie = DestroyPixelWand(pixie);
}

//draw the reactions
void gf_MagickDrawRxns(MagickWand *wand, gf_layoutInfo* l, Affine2d* tf) {
    Network* net = (Network*)l->net;
    AN(net, "No network");
    
    for(Network::ConstRxnIt i=net->RxnsBegin(); i!=net->RxnsEnd(); ++i) {
        LibsbmlDraw::Reaction* rxn = *i;
        AN(rxn->getCurves().size());
        for(LibsbmlDraw::Reaction::ConstCurveIt c=rxn->getCurves().begin(); c!=rxn->getCurves().end(); ++c) {
            AN(*c);
            gf_MagickDrawRxnCurve(wand, *c, false, tf);
        }
    }
}

void gf_MagickRenderToFile(gf_layoutInfo* l, const char* filename, void* tf_) {
    MagickWand *wand;
    //global MagickWand library startup
    MagickWandGenesis();
    //create our wand
    wand = NewMagickWand();
    AN(wand, "Failed to create Magick Wand");
    
    Affine2d I;
    Affine2d* tf = NULL;
    if(tf_)
        tf = (Affine2d*)tf_;
    else
        tf = &I;
    
    //create the canvas
    gf_MagickSizeImage(wand, l);
    //enable alpha
    MagickSetImageAlphaChannel(wand, ActivateAlphaChannel);
    
    // draw the compartments
    gf_MagickDrawComps(wand, l, tf);
    
    //draw the reactions
    gf_MagickDrawRxns(wand, l, tf);
    
    //draw the nodes
    gf_MagickDrawNodes(wand, l, tf);
    
    //write the image
    MagickWriteImage(wand, filename);
    
    std::cout << "Wrote image to" << filename << "\n";
    
    //release wands
    wand = DestroyMagickWand(wand);
    //global MagickWand library shutdown
    MagickWandTerminus();
}