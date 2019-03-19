def theRest():    
                # globalInformation
                info_global = render_plugin.getRenderInformation(0)

                if(info_global):
                    # -- add color definitions
                    for j in range(info_global.getNumColorDefinitions()):
                        color = info_global.getColorDefinition(j)
                        color_definitions[color.getId()
                                          ] = color.createValueString()
                    print("color definitions: ", len(color_definitions))

                    # -- styles - rolelist, typelist
                    print("styles: ", info_global.getNumStyles())

                    for j in range(info_global.getNumStyles()):
                        style = info_global.getStyle(j)

                        # print("\tstyle: ", style.getId())
                        # print("\t\troles: ", style.createRoleString())
                        # print("\t\ttypes string: ", style.createTypeString())
                        # types = style.getTypeList()
                        # print("\t\ttypes list: ", len(types))
                        if style.isInTypeList("SPECIESGLYPH"):
                            # print("\t\tApply this style to nodes.")
                            # print("\t\tFill is: ",
                            # style.getGroup().getFillColor())
                            if style.getGroup().isSetFillColor():
                                node_color = style.getGroup().getFillColor()
                                for node in self.network.nodes.values():
                                    node.fill_color = node_color
                                    print("set node color: ", node.fill_color)

                        if(style.isInTypeList("REACTIONGLYPH")):
                            # print("\t\tApply this style to reactions.")
                            for edge in self.network.edges.values():
                                if style.getGroup().isSetStroke():
                                    reaction_color = style.getGroup(
                                            ).getStroke()
                                    # print("\t\tStroke is: ", stroke_color)
                                    if reaction_color in color_definitions:
                                        reaction_color = color_definitions[
                                                reaction_color]
                                    edge.fill_color = reaction_color
                                if style.getGroup().isSetStrokeWidth():
                                    edge.curve_width = style.getGroup(
                                            ).getStrokeWidth()

                        if(style.isInTypeList("TEXTGLYPH")):
                            # print("\t\tApply this style to node text.")
                            # print("\t\tFont-family is: ",
                            # style.getGroup().getFontFamily
                            for node in self.network.nodes.values():
                                if(style.getGroup().isSetFontFamily()):
                                    node.font_name = style.getGroup(
                                            ).getFontFamily()
                                    print("set node font_name to: ",
                                          node.font_name)
                # localInformation
                # styles - idlist
                info_local = rPlugin.getRenderInformation(0)
                if(info_local):
                    for j in range(info_local.getNumStyles()):
                        style = info_local.getStyle(j)
                        print("\t\tids: ", style.createIdString())
                        print("\t\tfill color: ",
                              style.getGroup().getFillColor())


 def _addRenderInformation(self, sbml_file_name):
        # sbml_str = self.getSBMLWithLayout()
        # print("render in sbml_str: ", "render" in sbml_str)
        doc = libsbml.readSBMLFromString(self.getSBMLWithLayoutString())
        # doc = libsbml.readSBMLFromFile(sbml_file_name)
        model = doc.getModel()
        layout_plugin = model.getPlugin("layout")
        # lol_plugin = layout_plugin.getListOfLayouts().getPlugin("render")
        # info_global = lol_plugin.getRenderInformation(0)

        print("num layouts: ", layout_plugin.getNumLayouts())

        # get first layout, there may be only 1
        layout = layout_plugin.getLayout(0)
        print("layout type: ", type(layout))
        print("layout num plugins: ", layout.getNumPlugins())

        rPlugin = layout.getPlugin("render")
        print("rPlugin type: ", type(rPlugin))

        if (rPlugin is not None and
                rPlugin.getNumLocalRenderInformationObjects() > 0):
            print("num local render info objects: ",
                  rPlugin.getNumLocalRenderInformationObjects())
        else:
            uri = libsbml.RenderExtension.getXmlnsL2() if doc.getLevel(
                    ) == 2 else libsbml.RenderExtension.getXmlnsL3V1V1()

            # enable render package
            doc.enablePackage(uri, "render", True)
            doc.setPackageRequired("render", False)

            rPlugin = layout.getPlugin("render")

            rInfo = rPlugin.createLocalRenderInformation()

            rInfo.setId("localRenderInfo")
            rInfo.setName("Fill_Color Render Information")
            # add color definitions
            # add linear gradients
            # add styles
            style = rInfo.createStyle("substrateStyle")
            style.getGroup().setFillColor("pink")
            style.getGroup().setStroke("black")
            style.getGroup().setStrokeWidth(2.0)
            style.addId("S1")
            style.addType("SPECIESGLYPH")

            style = rInfo.createStyle("productStyle")
            style.getGroup().setFillColor("green")
            style.getGroup().setStroke("black")
            style.getGroup().setStrokeWidth(2.0)
            style.addId("S2")
            style.addType("SPECIESGLYPH")

        return doc




