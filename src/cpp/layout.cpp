/* MIT License
 */

//== BEGINNING OF CODE ===============================================================

//== INCLUDES ========================================================================

#include "SagittariusCore.h"
#include "layout.h"
#include "error.h"
#include "network.h"
#include "canvas.h"
#include "box.h"
#include "point.h"
#include "round.h"
#include "geom.h"
#include "transform.h"
#include "string_helpers.h"

#include "sbml/SBMLTypes.h"
#include "sbml/packages/layout/common/LayoutExtensionTypes.h"

#include <exception>
#include <typeinfo>

#include <stdlib.h> // free SBML strings

using namespace LibsbmlDraw;

void gf_freeLayoutInfo(gf_layoutInfo* l) {
    AN(l, "gf_freeLayoutInfo: unexpected null ptr");

    if(l->cont)
        free(l->cont);
    free(l);
}

void gf_freeLayoutInfoHierarch(gf_layoutInfo* l) {
    AN(l, "gf_freeLayoutInfo: unexpected null ptr");

    Network* net = (Network*)l->net;
    net->hierarchRelease();
    delete net;
    Canvas *canv = (Canvas*)l->canv;
    if(canv)
        delete canv;
    if(l->cont)
        free(l->cont);
    free(l);
}

void gf_freeModelAndLayout(gf_SBMLModel* mod, gf_layoutInfo* l) {
    if(mod) {
        SBMLDocument* doc = (SBMLDocument*)mod->pdoc;
        delete doc;
        free(mod);
    }

    if(l) {
        Network* net = (Network*)l->net;
        delete net;
        Canvas *canv = (Canvas*)l->canv;
        if(canv)
            delete canv;
        if(l->cont)
            free(l->cont);
        free(l);
    }
}

void gf_initLayoutInfo(gf_layoutInfo* l) {
    l->cont = NULL;
}

RxnRoleType gf_specRole2RxnRoleType(gf_specRole role) {
    switch(role) {
        case GF_ROLE_SUBSTRATE: return RXN_ROLE_SUBSTRATE;
        case GF_ROLE_PRODUCT: return RXN_ROLE_PRODUCT;
        case GF_ROLE_SIDESUBSTRATE: return RXN_ROLE_SIDESUBSTRATE;
        case GF_ROLE_SIDEPRODUCT: return RXN_ROLE_SIDEPRODUCT;
        case GF_ROLE_MODIFIER: return RXN_ROLE_MODIFIER;
        case GF_ROLE_ACTIVATOR: return RXN_ROLE_ACTIVATOR;
        case GF_ROLE_INHIBITOR: return RXN_ROLE_INHIBITOR;
        default:
            gf_emitError("Unknown role type");
            return RXN_ROLE_SUBSTRATE;
    }
}

gf_SBMLModel gf_SBMLModel_new() {
    gf_SBMLModel r;
    r.pdoc = NULL;
    return r;
}

gf_SBMLModel* gf_SBMLModel_newp() {
    gf_SBMLModel* r = (gf_SBMLModel*)malloc(sizeof(gf_SBMLModel));
    *r = gf_SBMLModel_new();
    return r;
}

gf_layoutInfo gf_layoutInfo_new(uint64_t level, uint64_t version, uint64_t width, uint64_t height) {
    gf_layoutInfo l;
    l.level = level;
    l.version = version;
    l.net = (void*)(new Network());
    l.canv = (void*)(new Canvas(width, height));
    l.cont = NULL;
    return l;
}

gf_layoutInfo* gf_layoutInfo_newp(uint64_t level, uint64_t version, uint64_t width, uint64_t height) {
    gf_layoutInfo* l = (gf_layoutInfo*)malloc(sizeof(gf_layoutInfo));
    *l = gf_layoutInfo_new(level, version, width, height);
    return l;
}

gf_layoutInfo* gf_processLayout(gf_SBMLModel* lo) {
    gf_layoutInfo* l;
    SBMLDocument* doc = (SBMLDocument*)lo->pdoc;

    // enable the layout package if it is not already
    if (!doc->isPkgEnabled("layout")) {
        if (doc->getLevel() == 2) {
            doc->enablePackage(LayoutExtension::getXmlnsL2(), "layout",  true);
        } else if (doc->getLevel() == 3) {
            doc->enablePackage(LayoutExtension::getXmlnsL3V1V1(), "layout",  true);
        }
    }

    // ensure layout package is enabled
    AT(doc->isPkgEnabled("layout"), "Layout package not enabled");

    // get the model
    Model* mod = doc->getModel();
    AN(mod, "Failed to load model");

    // layout plugin ptr
    SBasePlugin* layoutBase = mod->getPlugin("layout");
    AN(layoutBase, "No plugin named \"layout\"");

    // cast to derived
    LayoutModelPlugin* layoutPlugin=NULL;
    try {
        layoutPlugin = dynamic_cast<LayoutModelPlugin*>(layoutBase);
    } catch(std::bad_cast e) {
        gf_emitError("Unable to get layout information");
        AN(0);
    }

    //determine if there is layout information present
    int have_layout;
    #if SAGITTARIUS_DEBUG_LEVEL >= 2
//     printf("Number of layouts: %d\n", layoutPlugin->getNumLayouts());
    #endif
    if(layoutPlugin->getNumLayouts() == 0)
        have_layout = 0;
    else
        have_layout = 1;
    if(layoutPlugin->getNumLayouts() > 1)
        gf_emitWarn("Warning: multiple layouts. Using first");
    const Layout* layout = layoutPlugin->getLayout(0);

    //construct the network
    Network* net=NULL;
    if(have_layout)
        net = networkFromLayout(*layout, *mod);
    else
        net = networkFromModel(*mod);
    AN(net, "Failed to construct network");

    //get the canvas
    Canvas* canv;
    if(have_layout) {
        canv = new Canvas();
        //get dimensions from SBML layout
        const Dimensions* dims = layout->getDimensions();
        canv->setWidth(dims->getWidth());
        canv->setHeight(dims->getHeight());
//         std::cerr << "Canvas width = " << canv->getWidth() << ", height = " << canv->getHeight() << "\n";
    } else {
        canv = new Canvas();
        //get dimensions from SBML layout
        canv->setWidth(1024);
        canv->setHeight(1024);
    }
    #if SAGITTARIUS_DEBUG_LEVEL >= 3
        //print
        net->dump(std::cout,0);
    #endif

    l = (gf_layoutInfo*)malloc(sizeof(gf_layoutInfo));
    gf_initLayoutInfo(l);
    l->level = doc->getLevel();
    l->version = doc->getVersion();
    l->net = net;
    l->canv = canv;
    return l;
}

void gf_getNodeCentroid(gf_layoutInfo* l, const char* id, CPoint* p) {
    Network* net = (Network*)l->net;
    AN(net, "No network");

    LibsbmlDraw::Point pp(0,0);
    Node* n = net->findNodeById(id);
    if(!n) {
        gf_emitError("gf_getNodeCentroid: unable to find a node with the given id");
        return;
    }
    pp = n->getCentroid(NetworkElement::COORD_SYSTEM_GLOBAL);

    p->x = pp.x;
    p->y = pp.y;
}

int gf_lockNode(gf_layoutInfo* l, const char* id) {
    Network* net = (Network*)l->net;
    AN(net, "No network");

    Node* n = net->findNodeById(id);
    if(!n)
        return 1;
    n->lock();
    return 0;
}

int gf_unlockNode(gf_layoutInfo* l, const char* id) {
    Network* net = (Network*)l->net;
    AN(net, "No network");

    Node* n = net->findNodeById(id);
    if(!n)
        return 1;
    n->unlock();
    return 0;
}

int gf_aliasNode(gf_layoutInfo* l, const char* id) {
    Network* net = (Network*)l->net;
    AN(net, "No network");

    Node* n = net->findNodeById(id);
    if(!n)
        return 1;
    n->setAlias(true);
    for(Network::RxnIt i=net->RxnsBegin(); i!=net->RxnsEnd(); ++i) {
        LibsbmlDraw::Reaction* r = *i;
        if(r->hasSpecies(n)) {
            Node* w = new Node(*n);
            w->setGlyph(w->getGlyph() + "_" + r->getId());
            w->setCentroid(new2ndPos(r->getCentroid(), w->getCentroid(), 0., -25., false));
            net->addNode(w);
            r->substituteSpecies(n, w);
        }
    }
    return 0;
}

void gf_aliasNodebyDegree(gf_layoutInfo* l, int minDegree) {
    Network* net = (Network*)l->net;
    AN(net, "No network");

    int a, b, nodecount1, nodecount2, size = net->getTotalNumNodes(), i = 0, aliasCount = 0;
    char aliasCountString[33];
    sprintf(aliasCountString, "%d", aliasCount);
    std::vector<Node *> foundNodes;
    std::vector<LibsbmlDraw::Reaction *> Rxns;

    //Iterator does not work because nodes are added to the list, had to use while loop instead
    //for(Network::NodeIt i = net->NodesBegin(); i < net->NodesEnd(); ++i) {
    while(i < size) {
        LibsbmlDraw::Node* n = net->getNodeAtIndex(i);

        //If the node is the required minimum degree or greater and is not an alias
        if(n->degree() >= minDegree && !n->isCentroidSet() && !n->isAlias()) {

            for(Network::RxnIt c=net->RxnsBegin(); c!=net->RxnsEnd(); ++c) {
                LibsbmlDraw::Reaction* r = *c;

                if(r->hasSpecies(n)) {
                    if(n->degree() > 1) {

                        //Create a temp copy of all reactions
                        for(Network::RxnIt d=net->RxnsBegin(); d!=net->RxnsEnd(); ++d) {
                            LibsbmlDraw::Reaction* react = *d;
                            Rxns.push_back(react);
                        }

                        foundNodes.push_back(n);

                        //Find all nodes that are in the subgraph with node n
                        a = 0;
                        while(a < foundNodes.size()) {
                            b = 0;
                            while(b < Rxns.size()) {
                                if(Rxns[b]->hasSpecies(foundNodes[a])) {
                                    for(LibsbmlDraw::Reaction::NodeIt j=Rxns[b]->NodesBegin(); j!=Rxns[b]->NodesEnd(); ++j) {
                                        LibsbmlDraw::Node* node = j->first;
                                        for(int m = 0; m < foundNodes.size(); ++m) {
                                            if(node == foundNodes[m]) break;
                                            else if(m == foundNodes.size() - 1) foundNodes.push_back(node);
                                        }
                                    }
                                    Rxns.erase(Rxns.begin() + b);
                                }
                                else {
                                    b++;
                                }
                            }
                            a++;
                        }

                        nodecount1 = foundNodes.size();

                        //Create the alias node
                        Node* w = new Node(*n);
                        w->setGlyph(w->getGlyph() + "_" + r->getId() + "_alias_" + aliasCountString);
                        w->set_degree(1);
                        w->setCentroid(new2ndPos(r->getCentroid(), w->getCentroid(), 0., -25., false));
                        w->setAlias(true);
                        //Substitute the alias into the current reaction, but don't add to the network
                        r->substituteSpecies(n, w);
                        n->set_degree(n->degree() - 1);

                        Rxns.clear();
                        foundNodes.clear();

                        //Create a temp copy of all reactions
                        for(Network::RxnIt d=net->RxnsBegin(); d!=net->RxnsEnd(); ++d) {
                            LibsbmlDraw::Reaction* react = *d;
                            Rxns.push_back(react);
                        }

                        foundNodes.push_back(w);

                        //Find all nodes that are in the subgraph with the alias node
                        a = 0;
                        while(a < foundNodes.size()) {
                            b = 0;
                            while(b < Rxns.size()) {
                                if(Rxns[b]->hasSpecies(foundNodes[a])) {
                                    for(LibsbmlDraw::Reaction::NodeIt j=Rxns[b]->NodesBegin(); j!=Rxns[b]->NodesEnd(); ++j) {
                                        LibsbmlDraw::Node* node = j->first;
                                        for(int m = 0; m < foundNodes.size(); ++m) {
                                            if(node == foundNodes[m]) break;
                                            else if(m == foundNodes.size() - 1) foundNodes.push_back(node);
                                        }
                                    }
                                    Rxns.erase(Rxns.begin() + b);
                                }
                                else {
                                    b++;
                                }
                            }
                            a++;
                        }

                        nodecount2 = foundNodes.size();


                        if(nodecount1 > nodecount2) {

                            //If we lost a node(s), reset the connection to the original

                            r->substituteSpecies(w, n);
                            n->set_degree(n->degree() + 1);
                            delete(w);

                        } else {
                            //The node counts are equal. The alias can be kept
                            net->addNode(w);
                            aliasCount++;
                            sprintf(aliasCountString, "%d", aliasCount);
                        }
                    }

                }
            }
        }
        i++;
    }
    //printf("Aliases created: %d\n", aliasCount);
}



SBMLDocument* populateSBMLdoc(gf_SBMLModel* m, gf_layoutInfo* l, NetworkElement::COORD_SYSTEM coord = NetworkElement::COORD_SYSTEM_LOCAL) {
//     SBMLDocument* doc = (SBMLDocument*)m->pdoc;
    SBMLNamespaces sbmlns(l ? (l->level ? l->level : 3) : 3, l ? (l->version ? l->version : 1) : 1, "layout", 1);
    SBMLDocument* doc = new SBMLDocument(&sbmlns);
    AN(doc, "No SBML document");
    AT(doc->isPkgEnabled("layout"), "Layout package not enabled");
    #if SAGITTARIUS_DEBUG_LEVEL >= 2
//     std::cout << "doc->isPkgEnabled(\"layout\") = " << doc->isPkgEnabled("layout") << std::endl;
    #endif

    // get the model
//     Model* mod = doc->getModel();
//     AN(mod, "Failed to load model");

    bool create_default_compartment = false;

    Model* model = doc->createModel();
    doc->setPkgRequired("layout", false); // libSBML will refuse to open the file if required=true
    doc->setModel(model);

    // layout plugin
    LayoutPkgNamespaces layoutns(l ? (l->level ? l->level : 3) : 3, l ? (l->version ? l->version : 1) : 1, 1);
//     if (doc->getLevel() == 2)
//       doc->enablePackage(LayoutExtension::getXmlnsL2(),"layout", true);
//     else if (doc->getLevel() == 3)
//       doc->enablePackage(LayoutExtension::getXmlnsL3V1V1(),"layout", true);
    SBasePlugin* layoutBase = model->getPlugin("layout");
    AN(layoutBase, "No plugin named \"layout\"");

    // cast to derived
    LayoutModelPlugin* layoutPlugin=NULL;
    try {
        layoutPlugin = dynamic_cast<LayoutModelPlugin*>(layoutBase);
    } catch(std::bad_cast) {
        gf_emitError("Unable to get layout information");
        AN(0);
    }

    // clear all previous annotations
    while(layoutPlugin->getNumLayouts())
        layoutPlugin->removeLayout(0);
    // clear non-standard annotations
//     if(mod->getAnnotation())
//         mod->getAnnotation()->removeChildren();

    // add one layout element
    Layout* lay(layoutPlugin->createLayout());

    Canvas* can = NULL;
    if(l)
        can = (Canvas*)l->canv;
    Dimensions dims;
    if(can) {
        dims.setWidth(can->getWidth());
        dims.setHeight(can->getHeight());
    } else {
        dims.setWidth(1024.);
        dims.setHeight(1024.);
    }
    lay->setDimensions(&dims);

    // set id
    lay->setId("Graphfab_Layout");

    // get the network model
    Network* net = NULL;
    if(l) {
        net = (Network*)l->net;
        AT(net->doByteCheck(), "Network has wrong type");
    }

    std::map<std::string, int> species_map;

    if(net) {
        // If the network has an id, it becomes the id of the SBML model
        if(net->isSetId())
            model->setId(net->getId());

        // rebuild the curves as we will need them shortly
        net->rebuildCurves();

        // add compartments
        for(Network::ConstCompIt i=net->CompsBegin(); i!=net->CompsEnd(); ++i) {
            const LibsbmlDraw::Compartment* c = *i;

            // create glyph
            CompartmentGlyph* cg = new CompartmentGlyph();

            // id
            if(c->getGlyph() != "")
                cg->setId(c->getGlyph());
            else
                cg->setId(c->getId() + "_Glyph");

            // set model reference
            cg->setCompartmentId(c->getId());

            // do bounding box
            BoundingBox bb;
            bb.setX(sround(c->getMinX(coord)));
            bb.setY(sround(c->getMinY(coord)));
            bb.setWidth(sround(c->getWidth(coord)));
            bb.setHeight(sround(c->getHeight(coord)));
            // apply bb to glyph
            cg->setBoundingBox(&bb);

            lay->addCompartmentGlyph(cg);

            delete cg;

            // add compartment
            ::Compartment* compartment = model->createCompartment();
            compartment->setId(c->getId());
            compartment->setSize(1.);
            compartment->setConstant(false);
        }

        // add species
        uint64 calias=0;
        for(Network::NodeIt i=net->NodesBegin(); i!=net->NodesEnd(); ++i) {
            Node* n = *i;
            AN(n, "Empty node");

            SpeciesGlyph* sg = new SpeciesGlyph();

            // id
            if(n->getGlyph() == "") {
                // empty glyph: populate it
                if(!n->isAlias())
                    n->setGlyph(n->getId() + "_Glyph");
                else {
                    std::stringstream ss;
                    ss << n->getId() << "_Alias" << ++calias << "_Glyph";
                    n->setGlyph(ss.rdbuf()->str()); //TODO: try replacing with ss.str()
                }
            }
            sg->setId(n->getGlyph());

            // set model reference
            sg->setSpeciesId(n->getId());

            // do bounding box
            BoundingBox bb;
            bb.setX(sround(n->getMinX(coord)));
            bb.setY(sround(n->getMinY(coord)));
            bb.setWidth(sround(n->getWidth(coord)));
            bb.setHeight(sround(n->getHeight(coord)));
            // apply bb to glyph
            sg->setBoundingBox(&bb);

            lay->addSpeciesGlyph(sg);

            delete sg;

            // add species if it doesn't already exist
            if (!species_map.count(n->getId())) {
                ::Species* species = model->createSpecies();
                species->setId(n->getId());
                LibsbmlDraw::Compartment* com = net->findContainingCompartment(n);
                if(com)
                    species->setCompartment(com->getId());
                else {
                    species->setCompartment("graphfab_default_compartment");
                    create_default_compartment = true;
                }
                species->setInitialConcentration(0.);
                species->setBoundaryCondition(0.);
                species->setHasOnlySubstanceUnits(false);
                species->setConstant(false);

                species_map[n->getId()] = 1;
            }
        }

        if (create_default_compartment) {
            for(Network::ConstCompIt i=net->CompsBegin(); i!=net->CompsEnd(); ++i) {
                const LibsbmlDraw::Compartment* c = *i;
                if (c->getId() == "graphfab_default_compartment")
                    // already exists
                    goto skip_default_comp;
            }
            ::Compartment* compartment = model->createCompartment();
            compartment->setId("graphfab_default_compartment");
            compartment->setSize(1.);
            compartment->setConstant(false);
            int sbo_result = compartment->setSBOTerm(410);
//             int sbo_result = compartment->setSBOTerm("0000410");
            switch (sbo_result) {
              case LIBSBML_INVALID_ATTRIBUTE_VALUE:
                std::cerr << "SBO term invalid\n";
                break;
              case LIBSBML_UNEXPECTED_ATTRIBUTE:
                std::cerr << "SBO term unexpected\n";
                break;
              case LIBSBML_OPERATION_SUCCESS:
//                 std::cerr << "SBO term success";
                break;
              default:
//                 std::cerr << "SBO term default " << sbo_result << "\n";
//                 std::cerr << "LIBSBML_UNEXPECTED_ATTRIBUTE " << LIBSBML_UNEXPECTED_ATTRIBUTE << "\n";
                break;
            }
        }
        skip_default_comp:;

            // add species' text glyphs
        for(Network::NodeIt i=net->NodesBegin(); i!=net->NodesEnd(); ++i) {
            Node* n = *i;
            AN(n, "Empty node");

            TextGlyph* tg = new TextGlyph();

            //// id
            tg->setId("t" + n->getGlyph());

            // link to species glyph
            tg->setGraphicalObjectId(n->getGlyph());

            // set text to be displayed
            if(n->getName() != "")
                tg->setText(n->getName());

            // if no name use id
            else
                tg->setText(n->getId());

            // do bounding box
            BoundingBox bb;
            bb.setX(sround(n->getMinX(coord)));
            bb.setY(sround(n->getMinY(coord)));
            bb.setWidth(sround(n->getWidth(coord)));
            bb.setHeight(sround(n->getHeight(coord)));
            // apply bb to glyph
            tg->setBoundingBox(&bb);

            lay->addTextGlyph(tg);

            delete tg;
        }

        // add reactions
        for(Network::ConstRxnIt i=net->RxnsBegin(); i!=net->RxnsEnd(); ++i) {
            const LibsbmlDraw::Reaction* r = *i;
            AN(r, "Empty reaction");

            ReactionGlyph* rg = new ReactionGlyph();

            // id
            rg->setId(r->getId() + "_Glyph");

            // model reference
            rg->setReactionId(r->getId());

            // do species
            uint64 sref=0;
            LibsbmlDraw::Reaction::ConstNodeIt in=r->NodesBegin();
            LibsbmlDraw::Reaction::ConstCurveIt ic=r->CurvesBegin();
            for(;in != r->NodesEnd() && ic != r->CurvesEnd(); ++in, ++ic) {
                const Node* n = in->first;
                AN(n, "Empty species reference");
                const RxnBezier* c = *ic;
                AN(n, "Empty curve reference");

                SpeciesReferenceGlyph* srg = rg->createSpeciesReferenceGlyph();

                // set id
                {
                    std::stringstream ss;
                    ss << r->getId() << "_SpeciesRef" << ++sref;
                    srg->setId(ss.rdbuf()->str());
                }

                // set reference & glyph
                srg->setSpeciesReferenceId(n->getId());
                srg->setSpeciesGlyphId(n->getGlyph());

                // set role
                switch(in->second) {
                    case RXN_ROLE_SUBSTRATE:
                        srg->setRole("substrate");
                        break;
                    case RXN_ROLE_PRODUCT:
                        srg->setRole("product");
                        break;
                    case RXN_ROLE_SIDESUBSTRATE:
                        srg->setRole("sidesubstrate");
                        break;
                    case RXN_ROLE_SIDEPRODUCT:
                        srg->setRole("sideproduct");
                        break;
                    case RXN_ROLE_MODIFIER:
                        srg->setRole("modifier");
                        break;
                    case RXN_ROLE_ACTIVATOR:
                        srg->setRole("activator");
                        break;
                    case RXN_ROLE_INHIBITOR:
                        srg->setRole("inhibitor");
                        break;
                    default:
                        AN(0, "Unrecognized role");
                }

                // setup the SBML curve
                ::Curve curv;
                // cubic Bezier
                CubicBezier* cb = curv.createCubicBezier();

                ::Point p;

                if (coord == NetworkElement::COORD_SYSTEM_LOCAL) {
                // end-points
                p.setX(c->s.x);
                p.setY(c->s.y);
                cb->setStart(&p);
                p.setX(c->e.x);
                p.setY(c->e.y);
                cb->setEnd(&p);

                // control points
                p.setX(c->c1.x);
                p.setY(c->c1.y);
                cb->setBasePoint1(&p);
                p.setX(c->c2.x);
                p.setY(c->c2.y);
                cb->setBasePoint2(&p);
                } else {
                  // end-points
                  p.setX(c->getTransformedS().x);
                  p.setY(c->getTransformedS().y);
                  cb->setStart(&p);
                  p.setX(c->getTransformedE().x);
                  p.setY(c->getTransformedE().y);
                  cb->setEnd(&p);

                  // control points
                  p.setX(c->getTransformedC1().x);
                  p.setY(c->getTransformedC1().y);
                  cb->setBasePoint1(&p);
                  p.setX(c->getTransformedC2().x);
                  p.setY(c->getTransformedC2().y);
                  cb->setBasePoint2(&p);
                }

                // set curve
                srg->setCurve(&curv);
            }

            lay->addReactionGlyph(rg);

            delete rg;

            ::Reaction* reaction = model->createReaction();
            reaction->setId(r->getId());
            reaction->setReversible(false);
            reaction->setFast(false);
            ::KineticLaw* kine = reaction->createKineticLaw();
            kine->setFormula("1");
            for(LibsbmlDraw::Reaction::ConstNodeIt inode = r->NodesBegin();inode != r->NodesEnd(); ++inode) {
                switch(inode->second) {
                    case RXN_ROLE_SUBSTRATE: {
                        ::SpeciesReference* sref = reaction->createReactant();
                        sref->setSpecies((inode->first)->getId());
                        sref->setConstant(false);
                        sref->setStoichiometry(1.);
                        break;}
                    case RXN_ROLE_PRODUCT: {
                        ::SpeciesReference* sref = reaction->createProduct();
                        sref->setSpecies((inode->first)->getId());
                        sref->setConstant(false);
                        sref->setStoichiometry(1.);
                        break;}
                    case RXN_ROLE_SIDESUBSTRATE:{
                        ::SpeciesReference* sref = reaction->createReactant();
                        sref->setSpecies((inode->first)->getId());
                        sref->setConstant(false);
                        sref->setStoichiometry(1.);
                        break;}
                    case RXN_ROLE_SIDEPRODUCT:{
                        ::SpeciesReference* sref = reaction->createProduct();
                        sref->setSpecies((inode->first)->getId());
                        sref->setConstant(false);
                        sref->setStoichiometry(1.);
                        break;}
                    case RXN_ROLE_MODIFIER:{
                        ::ModifierSpeciesReference* sref = reaction->createModifier();
                        sref->setSpecies((inode->first)->getId());
                        break;}
                    case RXN_ROLE_ACTIVATOR:{
                        ::ModifierSpeciesReference* sref = reaction->createModifier();
                        sref->setSpecies((inode->first)->getId());
                        break;}
                    case RXN_ROLE_INHIBITOR:{
                        ::ModifierSpeciesReference* sref = reaction->createModifier();
                        sref->setSpecies((inode->first)->getId());
                        break;}
                    default:
                        AN(0, "Unrecognized role");
                }
            }
        }
    }

    return doc;
}

// DEPRECATED
gf_layoutInfo* gf_loadSBMLIntoLayoutEngine(const char* buf, gf_SBMLModel* r) {
	r=(gf_SBMLModel*)malloc(sizeof(gf_SBMLModel));
    SBMLReader reader;
    SBMLDocument* document = reader.readSBMLFromString(buf);

    AN(document, "Failed to parse SBML"); //not libSBML's documented way of failing, but just in case...

    if(document->getNumErrors()) {
        fprintf(stderr, "Failed to parse SBML\n");
        return NULL;
    }

    r->pdoc = document;

	gf_layoutInfo* l;
    SBMLDocument* doc = (SBMLDocument*)r->pdoc;
    AT(doc->isPkgEnabled("layout"), "Layout package not enabled");

    // get the model
    Model* mod = doc->getModel();
    AN(mod, "Failed to load model");

    // layout plugin ptr
    SBasePlugin* layoutBase = mod->getPlugin("layout");
    AN(layoutBase, "No plugin named \"layout\"");

    // cast to derived
    LayoutModelPlugin* layoutPlugin=NULL;
    try {
        layoutPlugin = dynamic_cast<LayoutModelPlugin*>(layoutBase);
    } catch(std::bad_cast e) {
        gf_emitError("Unable to get layout information");
        AN(0);
    }

    //determine if there is layout information present
    int have_layout;
    #if SAGITTARIUS_DEBUG_LEVEL >= 2
    printf("Number of layouts: %d\n", layoutPlugin->getNumLayouts());
    #endif
    if(layoutPlugin->getNumLayouts() == 0)
        have_layout = 0;
    else
        have_layout = 1;
    if(layoutPlugin->getNumLayouts() > 1)
        gf_emitWarn("Warning: multiple layouts. Using first");
    const Layout* layout = layoutPlugin->getLayout(0);

    //construct the network
    Network* net=NULL;
    if(have_layout)
        net = networkFromLayout(*layout, *mod);
    else
        net = networkFromModel(*mod);
    AN(net, "Failed to construct network");

    //get the canvas
    Canvas* canv;
    if(have_layout) {
        canv = new Canvas();
        //get dimensions from SBML layout
        const Dimensions* dims = layout->getDimensions();
        canv->setWidth(dims->getWidth());
        canv->setHeight(dims->getHeight());
        #if SAGITTARIUS_DEBUG_LEVEL >= 2
        std::cout << "Canvas width = " << canv->getWidth() << ", height = " << canv->getHeight() << "\n";
        #endif
    } else {
        canv = new Canvas();
        //get dimensions from SBML layout
        canv->setWidth(1024);
        canv->setHeight(1024);
    }
    #if SAGITTARIUS_DEBUG_LEVEL >= 3
    //print
    net->dump(std::cout,0);
    #endif

    l = (gf_layoutInfo*)malloc(sizeof(gf_layoutInfo));
    gf_initLayoutInfo(l);

    l->net = net;

    l->canv = canv;

    return l;
}

void gf_setModelNamespace(gf_layoutInfo* l, unsigned long level, unsigned long version) {
  l->level = level;
  l->version = version;
}

const char* gf_getDefaultCompartmentId() {
  return getDefaultCompartmentId().c_str();
}

void gf_setDefaultCompartmentId(const char* id) {
  setDefaultCompartmentId(id);
}

void gf_layout_fit_to_window(gf_layoutInfo* l, double left, double top, double right, double bottom) {
    Network* net = (Network*)l->net;
    AN(net, "No network");
    net->fitToWindow(Box(left, top, right, bottom));
}

void gf_layout_alignToOrigin(gf_layoutInfo* l, double pad_x, double pad_y) {
    Network* net = (Network*)l->net;
    AN(net, "No network");

    LibsbmlDraw::Box bbox = net->getBoundingBox();
    LibsbmlDraw::Box window(pad_x, pad_y, bbox.width()+pad_x, bbox.height()+pad_y);
    LibsbmlDraw::Affine2d tf = LibsbmlDraw::Affine2d::FitToWindow(bbox,
                                                   window);
    net->setTransform(tf);
    net->setInverseTransform(tf.inv());
}

gf_network gf_getNetwork(gf_layoutInfo* l) {
    gf_network n;
    n.n = l->net;
    AN(n.n, "No network");
    return n;
}

gf_network* gf_getNetworkp(gf_layoutInfo* l) {
    gf_network* n = (gf_network*)malloc(sizeof(gf_network));
    n->n = l->net;
    AN(n->n, "No network");
    return n;
}

void gf_clearNetwork(gf_network* n) {
    n->n = NULL;
}

void gf_releaseNetwork(gf_network* n) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");

    delete net;
}

char* gf_nw_getId(gf_network* n) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");

    return gf_strclone(net->getId().c_str());
}

void gf_nw_setId(gf_network* n, const char* id) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");

    net->setId(id);
}

uint64_t gf_nw_getNumNodes(const gf_network* n) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");

    return net->getTotalNumNodes();
}

uint64_t gf_nw_getNumUniqueNodes(const gf_network* n) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");

    return net->getNumUniqueNodes();
}

uint64_t gf_nw_getNumRxns(const gf_network* n) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");

    return net->getTotalNumRxns();
}

uint64_t gf_nw_getNumComps(const gf_network* n) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");

    return net->getTotalNumComps();
}

gf_node gf_nw_getNode(gf_network* n, uint64_t i) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");
    gf_node node;
    node.n = net->getNodeAt(i);
    return node;
}

gf_node gf_nw_getUniqueNode(gf_network* n, uint64_t i) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");
    gf_node node;
    node.n = net->getUniqueNodeAt(i);
    return node;
}

gf_node* gf_nw_getNodep(gf_network* n, uint64_t i) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");
    gf_node* node = (gf_node*)malloc(sizeof(gf_node));
    node->n = net->getNodeAt(i);
    return node;
}

gf_node* gf_nw_getUniqueNodep(gf_network* n, uint64_t i) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");
    gf_node* node = (gf_node*)malloc(sizeof(gf_node));
    node->n = net->getUniqueNodeAt(i);
    return node;
}

gf_node *gf_nw_getNodepFromId(gf_network *nw, const char* id) {
  int k;
  if(nw == NULL) {
    gf_emitError("gf_nw_getNodeFromId: Unable to get layout information");
    return NULL;
  }

  for(k = 0; k< gf_nw_getNumNodes(nw); ++k) {
    if( !strcmp(gf_node_getID(gf_nw_getNodep(nw, k)) , id) ) {
      return gf_nw_getNodep(nw, k);
    }
  }

  gf_emitError("gf_nw_getNodeFromId: Cannot find node with given id");
  return NULL;
}

gf_reaction gf_nw_getRxn(gf_network* n, uint64_t i) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");
    gf_reaction r;
    r.r = net->getRxnAt(i);
    // optional
    LibsbmlDraw::Reaction* rxn = (LibsbmlDraw::Reaction*)r.r;
    AT(rxn->doByteCheck(), "Type verification failed");

    return r;
}

gf_reaction* gf_nw_getRxnp(gf_network* n, uint64_t i) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");
    gf_reaction* r = (gf_reaction*)malloc(sizeof(gf_reaction));
    r->r = net->getRxnAt(i);
    // optional
    LibsbmlDraw::Reaction* rxn = (LibsbmlDraw::Reaction*)r->r;
    AT(rxn->doByteCheck(), "Type verification failed");

    return r;
}

void gf_nw_removeRxn(gf_network* nw, gf_reaction* r) {
    Network* net = CastToNetwork(nw->n);
    LibsbmlDraw::Reaction* rx = CastToReaction(r->r);
    AN(net, "No network");
    AN(rx, "No reaction");

    net->removeReaction(rx);
}

gf_compartment gf_nw_getCompartment(gf_network* n, uint64_t i) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");
    gf_compartment c;
    c.c = net->getCompAt(i);
    return c;
}

gf_compartment* gf_nw_getCompartmentp(gf_network* n, uint64_t i) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");
    gf_compartment* c = (gf_compartment*)malloc(sizeof(gf_compartment));
    c->c = net->getCompAt(i);
    return c;
}

gf_compartment* gf_nw_findCompartmentById(gf_network* n, const char* id) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");
    LibsbmlDraw::Compartment* comp = net->findCompById(id);
    if (!comp) {
        gf_emitError("gf_nw_findCompartmentById: no such compartment in network\n");
        return NULL;
    }
    gf_compartment* c = (gf_compartment*)malloc(sizeof(gf_compartment));
    c->c = comp;
    return c;
}

void gf_nw_rebuildCurves(gf_network* n) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");
    net->rebuildCurves();
}

void gf_nw_recenterJunctions(gf_network* n) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");
    net->recenterJunctions();
}

gf_compartment gf_nw_newCompartment(gf_network* nw, const char* id, const char* name) {
    Network* net = CastToNetwork(nw->n);
    gf_compartment cd;
    cd.c = NULL;
    AN(net, "No network");

    std::cout << "gf_nw_newCompartment started\n";
    LibsbmlDraw::Compartment* c = new LibsbmlDraw::Compartment();

    std::cout << "gf_nw_newCompartment setting id\n";
    c->setName(name);
    if(id) {
        if(!net->findCompById(id))
            c->setId(id);
        else {
            #if SAGITTARIUS_DEBUG_LEVEL >= 1
            fprintf(stderr, "A node with the specified id already exists\n");
            #endif
            return cd;
        }
    } else
        c->setId(net->getUniqueId());

    net->addCompartment(c);

    cd.c = c;
    return cd;
}

gf_compartment* gf_nw_newCompartmentp(gf_network* nw, const char* id, const char* name) {
    gf_compartment* comp = (gf_compartment*)malloc(sizeof(gf_compartment));
    *comp = gf_nw_newCompartment(nw, id, name);
    return comp;
}

gf_node gf_nw_newNode(gf_network* nw, const char* id, const char* name, gf_compartment* compartment) {
    Network* net = CastToNetwork(nw->n);
    gf_node nd;
    nd.n = NULL;
    AN(net, "No network");

//     std::cout << "gf_nw_newNode started\n";
    Node* n = new Node();

//     std::cout << "gf_nw_newNode setting id\n";
    n->setName(name);
    if(id) {
        if(!net->findNodeById(id))
            n->setId(id);
        else {
            #if SAGITTARIUS_DEBUG_LEVEL >= 1
            fprintf(stderr, "A node with the specified id already exists\n");
            #endif
            // used to be an error; do it anyway because id's are now shared across alias nodes
            n->setId(id);
        }
    } else
        n->setId(net->getUniqueId());
    n->numUses() = 1;
    n->setAlias(false);

    if(compartment) {
        LibsbmlDraw::Compartment* c = (LibsbmlDraw::Compartment*)compartment->c;
        c->addElt(n);
        n->_comp = c;
    }

    // set index
    n->set_i(net->getUniqueIndex());

    net->addNode(n);

//     std::cout << "gf_nw_newNode: node = " << n << ", index " << n->get_i() << "\n";

    nd.n = n;
    return nd;
}

gf_node gf_nw_aliasOf(gf_network* nw, gf_node* srcnode) {
    Network* net = CastToNetwork(nw->n);
    Node* src = CastToNode(srcnode->n);
    gf_node nd;
    nd.n = NULL;
    AN(net, "No network");

//     std::cout << "gf_nw_newNode started\n";
    Node* n = new Node();

//     std::cout << "gf_nw_newNode setting id\n";
    n->setName(src->getName());
    n->setId(src->getId());
    n->setGlyph(net->getUniqueGlyphId(*src));
    n->numUses() = 1;
    n->setAlias(true);
    src->setAlias(true);

    // TODO: reuse compartment

    // set index
    n->set_i(net->getUniqueIndex());

    net->addNode(n);

    nd.n = n;
    return nd;
}

gf_node* gf_nw_newNodep(gf_network* nw, const char* id, const char* name, gf_compartment* compartment) {
  gf_node* r = (gf_node*)malloc(sizeof(gf_node));
  gf_node q = gf_nw_newNode(nw,  id,  name, compartment);
  r->n = q.n;
  return r;
}

gf_node* gf_nw_newAliasNodep(gf_network* nw, gf_node* source) {
  gf_node* r = (gf_node*)malloc(sizeof(gf_node));
  gf_compartment* compartment = gf_nw_nodeHasCompartment(nw, source) ? gf_nw_nodeGetCompartment(nw, source) : NULL;
  gf_node q = gf_nw_newNode(nw,  gf_node_getID(source), gf_node_getName(source), compartment);
  r->n = q.n;

  //make sure both nodes are aliases
  gf_node_setIsAlias(r, 1);
  gf_node_setIsAlias(source, 1);

  return r;
}

int gf_nw_removeNode(gf_network* nw, gf_node* n) {
    Network* net = CastToNetwork(nw->n);
    Node* node = CastToNode(n->n);

    if(!net->containsNode(node)) {
        #if SAGITTARIUS_DEBUG_LEVEL >= 1
        fprintf(stderr, "gf_nw_removeNode: no such node in network\n");
        #endif
        return -1;
    }

    try {
        net->removeNode(node);
    } catch(...) {
        #if SAGITTARIUS_DEBUG_LEVEL >= 1
        fprintf(stderr, "gf_nw_removeNode: unable to remove node from network\n");
        #endif
        return -1;
    }

    return 0;
}

int gf_nw_connectNode(gf_network* nw, gf_node* n, gf_reaction* r, gf_specRole role) {
    Network* net = CastToNetwork(nw->n);
    Node* node = CastToNode(n->n);
    LibsbmlDraw::Reaction* reaction = CastToReaction(r->r);

    if(!net->containsNode(node)) {
        gf_emitError("gf_nw_removeNode: no such node in network\n");
        return -1;
    }

//     if(net->isNodeConnected(node, reaction)) {
//         gf_emitError("gf_nw_connectNode: connection already exists\n");
//         return -2;
//     }

    try {
        net->connectNode(node, reaction, gf_specRole2RxnRoleType(role));
    } catch(...) {
        fprintf(stderr, "gf_nw_connectNode: unable to connect node\n");
        return -1;
    }

    return 0;
}

int gf_nw_connectNodeRoleStr(gf_network* nw, gf_node* n, gf_reaction* r, const char* role_str) {
    gf_specRole role = gf_strToRole(role_str);
    if (gf_haveError())
        return -1;
    return gf_nw_connectNode(nw, n, r, role);
}

int gf_nw_isNodeConnected(gf_network* nw, gf_node* n, gf_reaction* r) {
    Network* net = CastToNetwork(nw->n);
    Node* node = CastToNode(n->n);
    LibsbmlDraw::Reaction* reaction = CastToReaction(r->r);

    if(!net->containsNode(node)) {
        gf_emitError("gf_nw_removeNode: no such node in network\n");
        return -1;
    }

    return net->isNodeConnected(node, reaction);
}

int gf_nw_isLayoutSpecified(gf_network* nw) {
    Network* net = CastToNetwork(nw->n);

    if(net->isLayoutSpecified())
        return 1;
    else
        return 0;
}

int gf_nw_getNumInstances(gf_network* nw, gf_node* n) {
    Network* net = CastToNetwork(nw->n);
    AN(net && net->doByteCheck(), "Not a network");
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");

    return net->getNumInstances(node);
}

int gf_nw_getNumAliasInstances(gf_network* nw, gf_node* n) {
    return gf_nw_getNumInstances(nw, n);
}

gf_node gf_nw_getInstance(gf_network* nw, gf_node* n, uint64_t i) {
    Network* net = CastToNetwork(nw->n);
    AN(net && net->doByteCheck(), "Not a network");
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");
    gf_node result;
    if (!node->isAlias()) {
        gf_emitError("gf_node_getInstance: Not an alias node");
        return result;
    }
    result.n = net->getInstance(node, i);
    return result;
}

gf_node* gf_nw_getInstancep(gf_network* nw, gf_node* n, uint64_t i) {
    gf_node* z = (gf_node*)malloc(sizeof(gf_node));
    *z = gf_nw_getInstance(nw, n, i);
    return z;
}

gf_node* gf_nw_getAliasInstancep(gf_network* nw, gf_node* n, uint64_t i) {
    return gf_nw_getInstancep(nw, n, i);
}

// Node

void gf_node_setCompartment(gf_node* n, gf_compartment* c) {
  LibsbmlDraw::Compartment* comp = (LibsbmlDraw::Compartment*)c->c;
  AN(comp, "No comp");
  Node* node = CastToNode(n->n);

  comp->addElt(node);
}

void gf_clearNode(gf_node* n) {
    n->n = NULL;
}

void gf_releaseNode(const gf_node* n) {
    Node* node = CastToNode(n->n);
    AN(node, "No node");

    delete node;
}

CPoint Point2CPoint(const LibsbmlDraw::Point& p) {
    CPoint q;
    q.x = p.x;
    q.y = p.y;
    return q;
}

gf_point Point2gf_point(const LibsbmlDraw::Point& p) {
    gf_point q;
    q.x = p.x;
    q.y = p.y;
    return q;
}

LibsbmlDraw::Point CPoint2Point(const CPoint& p) {
    LibsbmlDraw::Point q(p.x, p.y);
    return q;
}

LibsbmlDraw::Point gf_point2Point(const gf_point& p) {
    LibsbmlDraw::Point q(p.x, p.y);
    return q;
}

// alias a node
int gf_node_alias(gf_node* n, gf_network* m) {
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");
    Network* net = (Network*)m->n;
    AT(net->doByteCheck(), "Network has wrong type");

    return node->alias(net);
}

// alias a node
int gf_node_make_alias(gf_node* n, gf_network* m) {
    return gf_node_alias(n,m);
}

// is aliased?
int gf_node_isAliased(gf_node* n) {
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");
    return node->isAlias();
}

// is aliased?
void gf_node_setIsAlias(gf_node* n, int isAlias) {
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");
    return node->setAlias(isAlias);
}

// is locked?
int gf_node_isLocked(gf_node* n) {
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");
    return node->isLocked();
}

// lock
void gf_node_lock(gf_node* n) {
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");
    node->lock();
}

// unlock
void gf_node_unlock(gf_node* n) {
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");
    node->unlock();
}

// node.centroid
gf_point gf_node_getCentroid(gf_node* n) {
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");
    gf_point p = Point2gf_point(node->getCentroid(NetworkElement::COORD_SYSTEM_GLOBAL));

    return p;
}

void gf_node_setCentroid(gf_node* n, gf_point p) {
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");

    node->setGlobalCentroid(gf_point2Point(p));
}

// node.width
double gf_node_getWidth(gf_node* n) {
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");
    return node->getGlobalWidth();
}

void gf_node_setWidth(gf_node* n, double width) {
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");
    node->affectGlobalWidth(width);
}

// node.height
double gf_node_getHeight(gf_node* n) {
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");
    return node->getGlobalHeight();
}

void gf_node_setHeight(gf_node* n, double height) {
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");
    node->affectGlobalHeight(height);
}

char* gf_node_getID(gf_node* n) {
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");

    return gf_strclone(node->getId().c_str());
}

void gf_node_setID(gf_node* n, const char* id) {
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");
    if (!node || !node->doByteCheck()) {
        gf_emitError("gf_node_setName: bad node ptr");
        return;
    }

    node->setId(id);
}

const char* gf_node_getName(gf_node* n) {
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");

    if (node->getName().size())
        return gf_strclone(node->getName().c_str());
    else
        // missing name happens quite often: some researchers just want to watch the world burn...
        return gf_strclone(node->getId().c_str());
}

void gf_node_setName(gf_node* n, const char* name) {
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");
    if (!node || !node->doByteCheck()) {
        gf_emitError("gf_node_setName: bad node ptr");
        return;
    }

    node->setName(name);
}

int gf_node_getConnectedReactions(gf_node* n, gf_network* m, unsigned int* num, gf_reaction** rxns) {
    size_t k;
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");

    Network* net = CastToNetwork(m->n);
    AN(net && net->doByteCheck(), "No network");

    LibsbmlDraw::Network::AttachedRxnList rx = net->getConnectedReactions(node);

    *num = rx.size();

    *rxns = (gf_reaction*)malloc((*num)*sizeof(gf_reaction));

    for (k = 0; k < rx.size(); ++k) {
        (*rxns)[k].r = (void*)rx.at(k);
    }

    return 0;
}

int gf_node_getAttachedCurves(gf_node* n, gf_network* m, unsigned int* num, gf_curve** curves) {
    size_t k;
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");

    Network* net = CastToNetwork(m->n);
    AN(net && net->doByteCheck(), "No network");

    LibsbmlDraw::Network::AttachedCurveList rc = net->getAttachedCurves(node);

    *num = rc.size();

    *curves = (gf_curve*)malloc((*num)*sizeof(gf_curve));

    for (k = 0; k < rc.size(); ++k) {
        (*curves)[k].c = (void*)rc.at(k);
    }

    return 0;
}

int gf_node_isIdentical(gf_node* xu, gf_node* xv) {
    Node* u = CastToNode(xu->n);
    AN(u && u->doByteCheck(), "Not a node");

    Node* v = CastToNode(xv->n);
    AN(v && v->doByteCheck(), "Not a node");

    return u == v;
}

int gf_nw_nodeHasCompartment(gf_network* nw, gf_node* x) {
    Network* net = CastToNetwork(nw->n);
    AN(net && net->doByteCheck(), "No network");

    Node* v = CastToNode(x->n);
    AN(v && v->doByteCheck(), "Not a node");

    if(net->findContainingCompartment(v))
        return true;
    else
        return false;
}

gf_compartment* gf_nw_nodeGetCompartment(gf_network* nw, gf_node* x) {
    Network* net = CastToNetwork(nw->n);
    AN(net && net->doByteCheck(), "No network");

    Node* v = CastToNode(x->n);
    AN(v && v->doByteCheck(), "Not a node");

    LibsbmlDraw::Compartment* com = net->findContainingCompartment(v);
    gf_compartment* c = (gf_compartment*)malloc(sizeof(gf_compartment));
    c->c = com;
    return c;
}

// Reaction

void gf_releaseRxn(const gf_reaction* r) {
    LibsbmlDraw::Reaction* rxn = (LibsbmlDraw::Reaction*) r->r;
    AN(rxn, "No rxn");
    AT(rxn->doByteCheck(), "Type verification failed");

    delete rxn;
}

gf_reaction gf_nw_newReaction(gf_network* nw, const char* id, const char* name) {
    Network* net = CastToNetwork(nw->n);
    gf_reaction rxn;
    rxn.r = NULL;
    AN(net, "No network");

    std::cout << "gf_nw_newReaction started\n";
    LibsbmlDraw::Reaction* r = new LibsbmlDraw::Reaction();

    std::cout << "gf_nw_newReaction setting id\n";
    r->setName(name);
    if(id) {
        if(!net->findReactionById(id))
            r->setId(id);
        else {
            #if SAGITTARIUS_DEBUG_LEVEL >= 1
            fprintf(stderr, "A node with the specified id already exists\n");
            #endif
            return rxn;
        }
    } else
        r->setId(net->getUniqueId());

    net->addReaction(r);

    rxn.r = r;
    return rxn;
}

gf_reaction* gf_nw_newReactionp(gf_network* nw, const char* id, const char* name) {
    gf_reaction* r = (gf_reaction*)malloc(sizeof(gf_reaction));
    *r = gf_nw_newReaction(nw, id, name);
    return r;
}

char* gf_reaction_getID(gf_reaction* r) {
    LibsbmlDraw::Reaction* rxn = (LibsbmlDraw::Reaction*) r->r;
    AN(rxn, "No rxn");
    AT(rxn->doByteCheck(), "Type verification failed");

    return gf_strclone(rxn->getId().c_str());
}

// reaction.centroid
gf_point gf_reaction_getCentroid(gf_reaction* r) {
    LibsbmlDraw::Reaction* rxn = (LibsbmlDraw::Reaction*) r->r;
    AN(rxn, "No rxn");
    AT(rxn->doByteCheck(), "Type verification failed");

    gf_point p = Point2gf_point(rxn->getCentroid(NetworkElement::COORD_SYSTEM_GLOBAL));

    return p;
}

void gf_reaction_setCentroid(gf_reaction* r, gf_point p) {
    LibsbmlDraw::Reaction* rxn = (LibsbmlDraw::Reaction*) r->r;
    AN(rxn && rxn->doByteCheck(), "Not a reaction");

    rxn->setGlobalCentroid(gf_point2Point(p));
}

uint64_t gf_reaction_getNumSpec(const gf_reaction* r) {
    LibsbmlDraw::Reaction* rxn = (LibsbmlDraw::Reaction*) r->r;
    AN(rxn, "No rxn");
    AT(rxn->doByteCheck(), "Type verification failed");

    return rxn->numSpecies();
}

int gf_reaction_hasSpec(const gf_reaction* r, const gf_node* n) {
    LibsbmlDraw::Reaction* rxn = (LibsbmlDraw::Reaction*) r->r;
    AN(rxn, "No rxn");
    AT(rxn->doByteCheck(), "Type verification failed");
    Node* node = CastToNode(n->n);
    AN(node && node->doByteCheck(), "Not a node");

    return rxn->hasSpecies(node);
}

gf_specRole RxnRoleType2gf_specRole(RxnRoleType role) {
    switch(role) {
        case RXN_ROLE_SUBSTRATE: return GF_ROLE_SUBSTRATE;
        case RXN_ROLE_PRODUCT: return GF_ROLE_PRODUCT;
        case RXN_ROLE_SIDESUBSTRATE: return GF_ROLE_SIDESUBSTRATE;
        case RXN_ROLE_SIDEPRODUCT: return GF_ROLE_SIDEPRODUCT;
        case RXN_ROLE_MODIFIER: return GF_ROLE_MODIFIER;
        case RXN_ROLE_ACTIVATOR: return GF_ROLE_ACTIVATOR;
        case RXN_ROLE_INHIBITOR: return GF_ROLE_INHIBITOR;
        default:
            gf_emitError("Unknown role type");
            return GF_ROLE_SUBSTRATE;
    }
}

gf_specRole gf_reaction_getSpecRole(const gf_reaction* r, uint64_t i) {
    LibsbmlDraw::Reaction* rxn = (LibsbmlDraw::Reaction*) r->r;
    AN(rxn, "No rxn");
    AT(rxn->doByteCheck(), "Type verification failed");

    return RxnRoleType2gf_specRole(rxn->getSpeciesRole(i));
}

const char* gf_roleToStr(gf_specRole role) {
    switch(role) {
        case GF_ROLE_SUBSTRATE: return "SUBSTRATE";
        case GF_ROLE_PRODUCT: return "PRODUCT";
        case GF_ROLE_SIDESUBSTRATE: return "SIDESUBSTRATE";
        case GF_ROLE_SIDEPRODUCT: return "SIDEPRODUCT";
        case GF_ROLE_MODIFIER: return "MODIFIER";
        case GF_ROLE_ACTIVATOR: return "ACTIVATOR";
        case GF_ROLE_INHIBITOR: return "INHIBITOR";
        default:
            AN(0, "Unknown role type");
            return "UNKNOWN";
    }
}

gf_specRole gf_strToRole(const char* str) {
  if (!strcmp(str, "SUBSTRATE"))
    return GF_ROLE_SUBSTRATE;
  else if (!strcmp(str, "SIDESUBSTRATE"))
    return GF_ROLE_SIDESUBSTRATE;
  else if (!strcmp(str, "PRODUCT"))
    return GF_ROLE_PRODUCT;
  else if (!strcmp(str, "SIDEPRODUCT"))
    return GF_ROLE_SIDEPRODUCT;
  else if (!strcmp(str, "ACTIVATOR"))
    return GF_ROLE_ACTIVATOR;
  else if (!strcmp(str, "INHIBITOR"))
    return GF_ROLE_INHIBITOR;
  else if (!strcmp(str, "MODIFIER"))
    return GF_ROLE_MODIFIER;
  else {
    fprintf(stderr, "gf_strToRole unknown role type %s", str);
    gf_emitError("gf_strToRole: Unknown role type");
    AN(0, "gf_strToRole: Unknown role type");
    return GF_ROLE_SUBSTRATE; // to silence warnings
  }
}

uint64_t gf_reaction_specGeti(const gf_reaction* r, uint64_t i) {
    LibsbmlDraw::Reaction* rxn = (LibsbmlDraw::Reaction*) r->r;
    AN(rxn, "No rxn");
    AT(rxn->doByteCheck(), "Type verification failed");

    return rxn->getSpecies(i)->get_i();
}

uint64_t gf_reaction_getNumCurves(const gf_reaction* r) {
    LibsbmlDraw::Reaction* rxn = (LibsbmlDraw::Reaction*) r->r;
//     std::cerr << "gf_reaction_getNumCurves type verify\n";

    AN(rxn, "No rxn");
    AT(rxn->doByteCheck(), "Type verification failed");

//     std::cerr << "gf_reaction_getNumCurves type verified\n";

    return rxn->getNumCurves();
}

gf_curve gf_reaction_getCurve(const gf_reaction* r, uint64_t i) {
    LibsbmlDraw::Reaction* rxn = (LibsbmlDraw::Reaction*) r->r;
    AN(rxn, "No rxn");
    AT(rxn->doByteCheck(), "Type verification failed");
    gf_curve c;
    c.c = rxn->getCurve(i);

    return c;
}

gf_curve* gf_reaction_getCurvep(const gf_reaction* r, uint64_t i) {
    gf_curve q = gf_reaction_getCurve(r, i);
    gf_curve* p = (gf_curve*)malloc(sizeof(gf_curve));
    p->c = q.c;
    return p;
}

void gf_reaction_recenter(gf_reaction* r) {
    LibsbmlDraw::Reaction* rxn = (LibsbmlDraw::Reaction*) r->r;
    AN(rxn, "No rxn");
    AT(rxn->doByteCheck(), "Type verification failed");
    rxn->recenter();
}

void gf_reaction_recalcCurveCPs(gf_reaction* r) {
    LibsbmlDraw::Reaction* rxn = (LibsbmlDraw::Reaction*) r->r;
    AN(rxn, "No rxn");
    AT(rxn->doByteCheck(), "Type verification failed");
    rxn->recalcCurveCPs();
}

void gf_releaseCurve(const gf_curve* c) {
    RxnBezier* curve = (RxnBezier*)c->c;
    AN(curve, "No curve");

    delete curve;
}

gf_curveCP gf_getLocalCurveCPs(const gf_curve* c) {
    RxnBezier* curve = (RxnBezier*)c->c;
    AN(curve, "No curve");
    gf_curveCP cp;

    cp.s = Point2gf_point(curve->s);
    cp.e = Point2gf_point(curve->e);
    cp.c1 = Point2gf_point(curve->c1);
    cp.c2 = Point2gf_point(curve->c2);

    return cp;
}

gf_curveCP gf_getGlobalCurveCPs(const gf_curve* c) {
    RxnBezier* curve = (RxnBezier*)c->c;
    AN(curve, "No curve");
    gf_curveCP cp;

    cp.s = Point2gf_point(curve->getTransformedS());
    cp.e = Point2gf_point(curve->getTransformedE());
    cp.c1 = Point2gf_point(curve->getTransformedC1());
    cp.c2 = Point2gf_point(curve->getTransformedC2());

//     std::cerr << "  cps:  " << curve->getTransformedS() << "-" << curve->getTransformedC1() << "-" << curve->getTransformedC2() << "-" << curve->getTransformedE() << "\n";

    return cp;
}

gf_specRole gf_curve_getRole(gf_curve* c) {
  RxnBezier* curve = (RxnBezier*)c->c;
  AN(curve, "No curve");

  if (dynamic_cast<SubCurve*>(curve))
    return GF_ROLE_SUBSTRATE;

  if (dynamic_cast<PrdCurve*>(curve))
    return GF_ROLE_PRODUCT;

  if (dynamic_cast<ModCurve*>(curve))
    return GF_ROLE_MODIFIER;

  if (dynamic_cast<ActCurve*>(curve))
    return GF_ROLE_ACTIVATOR;

  if (dynamic_cast<InhCurve*>(curve))
    return GF_ROLE_INHIBITOR;

  // default
  return GF_ROLE_SUBSTRATE;
}

gf_curveCP gf_getCurveCPs(const gf_curve* c) {
    return gf_getGlobalCurveCPs(c);
}

int gf_curve_hasArrowhead(const gf_curve* c) {
  RxnBezier* curve = (RxnBezier*)c->c;
  AN(curve, "No curve");

  return curve->hasArrowhead();
}

int gf_curve_getArrowheadVerts(const gf_curve* c, unsigned int* n, gf_point** v) {
  RxnBezier* curve = (RxnBezier*)c->c;
  AN(curve, "No curve");

  Arrowhead* a = curve->getArrowhead();

//   std::cerr << "  a->getNumVerts() = " << a->getNumVerts() << "\n";
  *n = a->getNumVerts();
//   std::cerr << "  *n = " << *n << "\n";

  *v = (gf_point*)malloc((*n) *sizeof(gf_point));

  for (unsigned int k = 0; k<*n; ++k)
    (*v)[k] = Point2gf_point(a->getTransformedVert(k));

  delete a;
//   std::cerr << "  *n2 = " << *n << "\n";

  return 0;
}

void gf_releaseCompartment(const gf_compartment* c) {
    LibsbmlDraw::Compartment* comp = (LibsbmlDraw::Compartment*)c->c;
    AN(comp, "No comp");
    if(!comp->doByteCheck()) {
      gf_emitError("Type verification failed");
      return;
    }

    delete comp;
}

char* gf_compartment_getID(gf_compartment* c) {
    LibsbmlDraw::Compartment* comp = (LibsbmlDraw::Compartment*)c->c;
    if(!comp) {
      gf_emitError("Compartment is NULL");
      return NULL;
    }
    if(!comp->doByteCheck()) {
      gf_emitError("Type verification failed");
      return NULL;
    }

    return gf_strclone(comp->getId().c_str());
}

gf_point gf_compartment_getMinCorner(gf_compartment* c) {
    LibsbmlDraw::Compartment* comp = (LibsbmlDraw::Compartment*)c->c;
    AN(comp, "No comp");

    return Point2gf_point(comp->getMin(NetworkElement::COORD_SYSTEM_GLOBAL));
}

void gf_compartment_setMinCorner(gf_compartment* c, gf_point p) {
    LibsbmlDraw::Compartment* comp = (LibsbmlDraw::Compartment*)c->c;
    AN(comp, "No comp");

    comp->setMin(gf_point2Point(p));
}

gf_point gf_compartment_getMaxCorner(gf_compartment* c) {
    LibsbmlDraw::Compartment* comp = (LibsbmlDraw::Compartment*)c->c;
    AN(comp, "No comp");

    return Point2gf_point(comp->getMax(NetworkElement::COORD_SYSTEM_GLOBAL));
}

void gf_compartment_setMaxCorner(gf_compartment* c, gf_point p) {
    LibsbmlDraw::Compartment* comp = (LibsbmlDraw::Compartment*)c->c;
    AN(comp, "No comp");

    comp->setMax(gf_point2Point(p));
}

double gf_compartment_getWidth(gf_compartment* c) {
    LibsbmlDraw::Compartment* comp = (LibsbmlDraw::Compartment*)c->c;
    AN(comp, "No comp");

    return comp->getGlobalWidth();
}

double gf_compartment_getHeight(gf_compartment* c) {
    LibsbmlDraw::Compartment* comp = (LibsbmlDraw::Compartment*)c->c;
    AN(comp, "No comp");

    return comp->getGlobalHeight();
}

uint64_t gf_compartment_getNumElt(gf_compartment* c) {
    LibsbmlDraw::Compartment* comp = (LibsbmlDraw::Compartment*)c->c;
    AN(comp, "No comp");

    return comp->getNElts();
}

int gf_compartment_addNode(gf_compartment* c, gf_node* n) {
    LibsbmlDraw::Compartment* comp = (LibsbmlDraw::Compartment*)c->c;
    AN(comp, "No comp");
    Node* node = CastToNode(n->n);
    AN(node, "No node");

    if(!comp || !node) {
        gf_emitError("gf_compartment_addNode failed");
        return -1;
    }

    comp->addElt(node);
    return 0;
}

int gf_compartment_removeNode(gf_compartment* c, gf_node* n) {
    LibsbmlDraw::Compartment* comp = (LibsbmlDraw::Compartment*)c->c;
    AN(comp, "No comp");
    Node* node = CastToNode(n->n);
    AN(node, "No node");

    if(!comp || !node) {
        gf_emitError("gf_compartment_removeNode failed");
        return -1;
    }

    comp->removeElt(node);
    return 0;
}

int gf_compartment_containsNode(gf_compartment* c, gf_node* n) {
    LibsbmlDraw::Compartment* comp = (LibsbmlDraw::Compartment*)c->c;
    AN(comp, "No comp");
    Node* node = CastToNode(n->n);
    AN(node, "No node");

    if(!comp || !node) {
        gf_emitError("gf_compartment_containsNode failed");
        return -1;
    }

    comp->contains(node);
    return 0;
}

int gf_compartment_containsReaction(gf_compartment* c, gf_reaction* r) {
    LibsbmlDraw::Compartment* comp = (LibsbmlDraw::Compartment*)c->c;
    AN(comp, "No comp");
    LibsbmlDraw::Reaction* rxn = CastToReaction(r->r);
    AN(rxn, "No reaction");

    if(!comp || !rxn) {
        gf_emitError("gf_compartment_containsReaction failed");
        return -1;
    }

    comp->contains(rxn);
    return 0;
}

void gf_fit_to_window(gf_layoutInfo* l, double left, double top, double right, double bottom) {
    Network* net = (Network*)l->net;
    AN(net, "No network");

    LibsbmlDraw::Box bbox = net->getBoundingBox();

//     std::cerr << "Net bounding box: " << bbox << "\n";

    LibsbmlDraw::Box window(left, top, right, bottom);

//     std::cout << "Window: " << window << "\n";

    LibsbmlDraw::Affine2d tf = LibsbmlDraw::Affine2d::FitToWindow(bbox,
                                                   window);

//     std::cout << "Transform is\n" << tf;

    net->setTransform(tf);
    net->setInverseTransform(tf.inv());

//     std::cerr << "New bounding box: " << net->getBoundingBox() << "\n";
}

gf_transform* gf_tf_fitToWindow(gf_layoutInfo* l, double left, double top, double right, double bottom) {
    Network* net = (Network*)l->net;
    AN(net, "No network");

    LibsbmlDraw::Box bbox = net->getBoundingBox();

//     std::cerr << "Net bounding box: " << bbox << "\n";

    LibsbmlDraw::Box window(left, top, right, bottom);

//     std::cout << "Window: " << window << "\n";

    LibsbmlDraw::Affine2d* tf = new LibsbmlDraw::Affine2d(LibsbmlDraw::Affine2d::FitToWindow(bbox,
                                                   window));

//     std::cout << "Transform is\n" << tf;

//     net->setTransform(tf);
//     net->setInverseTransform(tf.inv());

    gf_transform* t = (gf_transform*)malloc(sizeof(gf_transform));
    t->tf = tf;
    return t;
}

void gf_moveNetworkToFirstQuad(gf_layoutInfo* l, double x_disp, double y_disp) {
    Network* net = (Network*)l->net;
    AN(net, "No network");

    LibsbmlDraw::Box bbox = net->getBoundingBox();

    net->applyDisplacement(-bbox.getMin() + LibsbmlDraw::Point(x_disp, y_disp));
    net->rebuildCurves();
}

CPoint gf_tf_apply_to_point(gf_transform* tf, CPoint p) {
    LibsbmlDraw::Affine2d* t = (LibsbmlDraw::Affine2d*)tf->tf;
    AN(t, "No transform");
    LibsbmlDraw::Point r = LibsbmlDraw::xformPoint(CPoint2Point(p), *t);
    return Point2CPoint(r);
}

gf_point gf_tf_getScale(gf_transform* tf) {
  LibsbmlDraw::Affine2d* t = (LibsbmlDraw::Affine2d*)tf->tf;
  AN(t, "No transform");
  return Point2gf_point(t->getScale());
}

gf_point gf_tf_getDisplacement(gf_transform* tf) {
  LibsbmlDraw::Affine2d* t = (LibsbmlDraw::Affine2d*)tf->tf;
  AN(t, "No transform");
//   std::cerr << "  gf_tf_getDisplacement: " << t->getDisplacement() << "\n";
  return Point2gf_point(t->getDisplacement());
}

gf_point gf_tf_getPostDisplacement(gf_transform* tf) {
  LibsbmlDraw::Affine2d* t = (LibsbmlDraw::Affine2d*)tf->tf;
  AN(t, "No transform");
  LibsbmlDraw::Point result(t->inv().applyLinearOnly(t->getDisplacement()));
//   std::cerr << "  gf_tf_getPostDisplacement: " << result << "\n";
  return Point2gf_point(result);
}

void gf_dump_transform(gf_transform* tf) {
    LibsbmlDraw::Affine2d* t = (LibsbmlDraw::Affine2d*)tf->tf;
    AN(t, "No transform");
//     std::cerr << *t;
}

void gf_release_transform(gf_transform* tf) {
    LibsbmlDraw::Affine2d* t = (LibsbmlDraw::Affine2d*)tf->tf;
    AN(t, "No transform");
    delete t;
}

gf_canvas gf_getCanvas(gf_layoutInfo* l) {
    gf_canvas c = {l->canv};
    return c;
}

gf_canvas* gf_getCanvasp(gf_layoutInfo* l) {
    gf_canvas c = {l->canv};
    gf_canvas* r = (gf_canvas*)malloc(sizeof(gf_canvas));
    r->canv = c.canv;
    return r;
}

void gf_clearCanvas(gf_canvas* c) {
    c->canv = NULL;
}

void gf_releaseCanvas(gf_canvas* c) {
    Canvas *canv = (Canvas*)c->canv;
    AN(canv, "No canvas");

    delete canv;
}

unsigned int gf_canvGetWidth(gf_canvas* c) {
    Canvas *canv = (Canvas*)c->canv;
    AN(canv, "No canvas");

    return canv->getWidth();
}

void gf_canvSetWidth(gf_canvas* c, unsigned long width) {
    Canvas *canv = (Canvas*)c->canv;
    AN(canv, "No canvas");

    canv->setWidth(width);
}

unsigned int gf_canvGetHeight(gf_canvas* c) {
    Canvas *canv = (Canvas*)c->canv;
    AN(canv, "No canvas");

    return canv->getHeight();
}

void gf_canvSetHeight(gf_canvas* c, unsigned long height) {
    Canvas *canv = (Canvas*)c->canv;
    AN(canv, "No canvas");

    canv->setHeight(height);
}

int gf_writeSBMLwithLayout(const char* filename, gf_SBMLModel* m, gf_layoutInfo* l, int use_transformed_coords) {
    #if SAGITTARIUS_DEBUG_LEVEL >= 2
//     std::cout << "gf_writeSBMLwithLayout started\n" << std::endl;
    #endif
    SBMLDocument* doc = populateSBMLdoc(m,l,
      use_transformed_coords ?
      NetworkElement::COORD_SYSTEM_GLOBAL :
		NetworkElement::COORD_SYSTEM_LOCAL);
    #if SAGITTARIUS_DEBUG_LEVEL >= 2
//     std::cout << "populateSBMLdoc finished\n" << std::endl;
    #endif
    SBMLWriter writer;
    writer.setProgramName("Graphfab");
    if(writer.writeSBML(doc, filename))
        return 0;
    else
        return -1;

    // appropriate?
    //delete lay;
}

int gf_writeSBML(const char* filename, gf_SBMLModel* m) {
    SBMLDocument* doc = populateSBMLdoc(m, NULL);
    SBMLWriter writer;
    writer.setProgramName("Graphfab");
    if(writer.writeSBML(doc, filename))
        return 0;
    else
        return -1;
}

const char* gf_getSBMLwithLayoutStr(gf_SBMLModel* m, gf_layoutInfo* l, int use_transformed_coords) {
    SBMLDocument* doc = populateSBMLdoc(m,l,use_transformed_coords? NetworkElement::COORD_SYSTEM_GLOBAL: NetworkElement::COORD_SYSTEM_LOCAL);
    SBMLWriter writer;
    writer.setProgramName("Graphfab");

    if(l->cont)
        free(l->cont);
    l->cont = writer.writeSBMLToString(doc);

    return gf_strclone(l->cont);
}

void gf_randomizeLayout(gf_layoutInfo* m) {
    Network* net = (Network*)m->net;
    AN(net, "No network");
    Canvas* can = (Canvas*)m->canv;
    AN(can, "No canvas");

    net->randomizePositions(LibsbmlDraw::Box(LibsbmlDraw::Point(0.,0.), LibsbmlDraw::Point(can->getWidth(), can->getHeight())));
}

void gf_randomizeLayout2(gf_network* n, gf_canvas* c) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");
    Canvas* can = (Canvas*)c->canv;
    AN(can, "No canvas");

    net->randomizePositions(LibsbmlDraw::Box(LibsbmlDraw::Point(0.,0.), LibsbmlDraw::Point(can->getWidth(), can->getHeight())));
}

void gf_randomizeLayout_fromExtents(gf_network* n, double left, double top, double right, double bottom) {
    Network* net = CastToNetwork(n->n);
    AN(net, "No network");

    net->randomizePositions(LibsbmlDraw::Box(LibsbmlDraw::Point(left,top), LibsbmlDraw::Point(right, bottom)));
}

//TODO: move to more appropriate place like core/version or something
// and rename to more succinct function - is anyone going to want to get the version
// for anything other than the CURRENT library?
const char* gf_getCurrentLibraryVersion() {
    return GF_EXPAND_AND_QUOTE(SBNW_MAJOR_VER) "." GF_EXPAND_AND_QUOTE(SBNW_MINOR_VER) "." GF_EXPAND_AND_QUOTE(SBNW_PATCHLEVEL);
}

void gf_free(void* x) {
  free(x);
}

gf_point gf_computeCubicBezierPoint(gf_curveCP* c, LibsbmlDraw::Real t) {
  CubicBezier2Desc b(gf_point2Point(c->s), gf_point2Point(c->c1), gf_point2Point(c->c2), gf_point2Point(c->e));
  return Point2gf_point(b.p(t));
}

gf_point* gf_computeCubicBezierLineIntersec(gf_curveCP* c, gf_point* line_start, gf_point* line_end) {
  Line2Desc l(gf_point2Point(*line_start), gf_point2Point(*line_end));

  CubicBezier2Desc b(gf_point2Point(c->s), gf_point2Point(c->c1), gf_point2Point(c->c2), gf_point2Point(c->e));

  CubicBezierIntersection r(l, b);

  gf_point* result = (gf_point*)malloc((r.getIntersectionPoints().size()+1)*sizeof(gf_point));

  for (int i = 0; i<r.getIntersectionPoints().size(); ++i) {
    result[i].x = b.p(r.getIntersectionPoints().at(i)).x;
    result[i].y = b.p(r.getIntersectionPoints().at(i)).y;
  }

  result[r.getIntersectionPoints().size()].x = 0;
  result[r.getIntersectionPoints().size()].y = 0;

  return result;
}
int gf_arrowheadStyleGetNumVerts(int style) {
  return LibsbmlDraw::ArrowheadStyles::getNumVerts(style);
}

gf_point gf_arrowheadStyleGetVert(int style, int n) {
  return Point2gf_point(LibsbmlDraw::ArrowheadStyles::getVert(style,  n));
}

int gf_arrowheadStyleIsFilled(int style) {
  return LibsbmlDraw::ArrowheadStyles::isFilled(style);
}

unsigned long gf_arrowheadNumStyles() {
  return LibsbmlDraw::ArrowheadStyles::count();
}

void gf_arrowheadSetStyle(gf_specRole role, int style) {
  switch(role) {
    case GF_ROLE_SUBSTRATE:
    case GF_ROLE_SIDESUBSTRATE:
      ArrowheadStyleControl<SubstrateArrowhead>::set(style);
      break;
    case GF_ROLE_PRODUCT:
    case GF_ROLE_SIDEPRODUCT:
      ArrowheadStyleControl<ProductArrowhead>::set(style);
      break;
    case GF_ROLE_MODIFIER:
      ArrowheadStyleControl<ModifierArrowhead>::set(style);
      break;
    case GF_ROLE_ACTIVATOR:
      ArrowheadStyleControl<ActivatorArrowhead>::set(style);
      break;
    case GF_ROLE_INHIBITOR:
      ArrowheadStyleControl<InhibitorArrowhead>::set(style);
      break;
    default:
      fprintf(stderr, "gf_arrowheadSetStyle unknown role type %s\n", gf_roleToStr(role));
      AN(0, "Unknown role type");
  }
}

int gf_arrowheadGetStyle(gf_specRole role) {
  switch(role) {
    case GF_ROLE_SUBSTRATE:
    case GF_ROLE_SIDESUBSTRATE:
      return ArrowheadStyleControl<SubstrateArrowhead>::get();
    case GF_ROLE_PRODUCT:
    case GF_ROLE_SIDEPRODUCT:
      return ArrowheadStyleControl<ProductArrowhead>::get();
    case GF_ROLE_MODIFIER:
      return ArrowheadStyleControl<ModifierArrowhead>::get();
    case GF_ROLE_ACTIVATOR:
      return ArrowheadStyleControl<ActivatorArrowhead>::get();
    case GF_ROLE_INHIBITOR:
      return ArrowheadStyleControl<InhibitorArrowhead>::get();
      break;
    default:
      fprintf(stderr, "gf_arrowheadSetStyle unknown role type %s\n", gf_roleToStr(role));
      AN(0, "Unknown role type");
  }
}
