from libsbml_draw.sbml_layout import SBMLlayout

model_string = """<?xml version="1.0" encoding="UTF-8"?>
<!-- Created by XMLPrettyPrinter on 1/24/2020 from pathwayDesigner version.dll -->
<sbml xmlns = "http://www.sbml.org/sbml/level2" level = "2" version = "1" xmlns:jd2 = "http://www.sys-bio.org/sbml/jd2">
   <!--                     -->
   <!--  Model Starts Here  -->
   <!--                     -->
   <model id = "untitled">
      <notes>
         <body xmlns = "http://www.w3.org/1999/xhtml">
            <p/>
         </body>
      </notes>
      <annotation>
         <jd2:PathwayDesignerLayout version = "2.0" MajorVersion = "4" MinorVersion = "3" BuildVersion = "54"
                                    xmlns:jd2 = "http://www.sys-bio.org/sbml/jd2">
            <jd2:header>
               <jd2:VersionHeader PathwayVersion = "2.0"/>
               <jd2:ModelHeader Author = "" ModelVersion = "0.0" ModelTitle = "untitled"/>
               <jd2:TimeCourseDetails timeStart = "0" timeEnd = "10" numberOfPoints = "100" selectionList = ""/>
               <jd2:SteadyStateDetails selectionList = ""/>
               <jd2:ModifierOptions enableModifierDecorations = "false" enableAutoAddModifiers = "true"/>
               <jd2:TimeCourseNumerics deprecated = "True" BDFOrder = "5" AdamsOrder = "12" rtol = "1E-6"
                                       atol = "1E-12" maxsteps = "10000" initstep = "0" maxstep = "0"
                                       minstep = "0"/>
               <jd2:SteadyStateNumerics deprecated = "True" MaxIterations = "100" relativeTolerance = "0.0001"/>
               <jd2:TimeCourseSolverSettings>
                  <jd2:listOfSettings solver = "cvode">
                     <jd2:setting name = "relative_tolerance" value = "1E-5"/>
                     <jd2:setting name = "absolute_tolerance" value = "1E-10"/>
                     <jd2:setting name = "stiff" value = "true"/>
                     <jd2:setting name = "maximum_bdf_order" value = "5"/>
                     <jd2:setting name = "maximum_adams_order" value = "12"/>
                     <jd2:setting name = "maximum_num_steps" value = "20000"/>
                     <jd2:setting name = "maximum_time_step" value = "0"/>
                     <jd2:setting name = "minimum_time_step" value = "0"/>
                     <jd2:setting name = "initial_time_step" value = "0"/>
                     <jd2:setting name = "multiple_steps" value = "false"/>
                     <jd2:setting name = "variable_step_size" value = "false"/>
                  </jd2:listOfSettings>
               </jd2:TimeCourseSolverSettings>
               <jd2:SteadyStateSolverSettings>
                  <jd2:listOfSettings solver = "nleq">
                     <jd2:setting name = "maximum_iterations" value = "100"/>
                     <jd2:setting name = "minimum_damping" value = "1E-16"/>
                     <jd2:setting name = "relative_tolerance" value = "0.0001"/>
                  </jd2:listOfSettings>
               </jd2:SteadyStateSolverSettings>
            </jd2:header>
            <jd2:JDGraphicsHeader BackGroundColor = "FFFFFFEF" NodeEdgeGapDistance = "20"/>
            <jd2:listOfCompartments>
               <jd2:compartment id = "compartment" size = "1" visible = "false">
                  <jd2:boundingBox x = "0" y = "0" w = "64" h = "64"/>
                  <jd2:membraneStyle thickness = "12" color = "FF00A5FF"/>
                  <jd2:interiorStyle color = "FFEEEEFF"/>
                  <jd2:text value = "compartment" visible = "true">
                     <jd2:position rx = "32" ry = "57.6"/>
                     <jd2:font fontName = "Arial" fontSize = "12" fontStyle = "" fontColor = "FF000000"/>
                  </jd2:text>
               </jd2:compartment>
               <jd2:compartment id = "vol1" size = "1" visible = "true">
                  <jd2:boundingBox x = "152" y = "70" w = "340" h = "190"/>
                  <jd2:membraneStyle thickness = "12" color = "FF00A5FF"/>
                  <jd2:interiorStyle color = "FFEEEEFF"/>
                  <jd2:text value = "vol1" visible = "true">
                     <jd2:position rx = "160" ry = "174"/>
                     <jd2:font fontName = "Arial" fontSize = "12" fontStyle = "" fontColor = "FF000000"/>
                  </jd2:text>
               </jd2:compartment>
               <jd2:compartment id = "vol2" size = "1" visible = "true">
                  <jd2:boundingBox x = "161" y = "317" w = "340" h = "190"/>
                  <jd2:membraneStyle thickness = "12" color = "FF00A5FF"/>
                  <jd2:interiorStyle color = "FFEEEEFF"/>
                  <jd2:text value = "vol2" visible = "true">
                     <jd2:position rx = "160" ry = "174"/>
                     <jd2:font fontName = "Arial" fontSize = "12" fontStyle = "" fontColor = "FF000000"/>
                  </jd2:text>
               </jd2:compartment>
            </jd2:listOfCompartments>
            <jd2:listOfSpecies>
               <jd2:species id = "Node0" boundaryCondition = "false" compartment = "vol1" initialConcentration = "0">
                  <jd2:visible value = "true"/>
                  <jd2:positionLocked value = "false"/>
                  <jd2:sizeLocked value = "false"/>
                  <jd2:boundingBox x = "255" y = "89"/>
                  <jd2:displayNameVisible value = "" visible = "false"/>
                  <jd2:displayValue visible = "false">
                     <jd2:position rx = "0" ry = "0"/>
                     <jd2:displayStatus value = "dvInitialValue"/>
                     <jd2:font fontName = "Arial" fontSize = "8" fontColor = "FF000000" fontStyle = ""/>
                  </jd2:displayValue>
                  <jd2:text value = "Node0" visible = "true">
                     <jd2:position rx = "9.108" ry = "11.926"/>
                     <jd2:font fontName = "Arial" fontSize = "10" fontStyle = "" fontColor = "FF000000"/>
                  </jd2:text>
                  <jd2:complex id = "C2592840" displayName = "untitled" w = "62" h = "40"
                               boundarySpeciesStyle = "bsShadow" boundaryStyleColor = "FF0000FF" captionPosition = "npCenter" captionVisible = "true"
                               aliasBoundaryStyle = "abRectangle" aliasBoundaryColor = "FFFF0000" aliasBoundaryThickness = "3">
                     <jd2:subunit shape = "suOvalSquare">
                        <jd2:boundingBox rx = "0" ry = "0" w = "62" h = "40"/>
                        <jd2:text value = "S13" visible = "false">
                           <jd2:position rx = "19.5" ry = "12"/>
                           <jd2:font fontName = "Arial" fontSize = "8" fontColor = "FF000000" fontStyle = ""/>
                        </jd2:text>
                        <jd2:color scheme = "gtVertLinear" startColor = "FFFFCC99" endColor = "FFFFFFFF"/>
                        <jd2:edgeStyle color = "FFFF6600" thickness = "2" stroke = "dsSolid"/>
                     </jd2:subunit>
                  </jd2:complex>
               </jd2:species>
               <jd2:species id = "Node1" boundaryCondition = "false" compartment = "vol1" initialConcentration = "0">
                  <jd2:visible value = "true"/>
                  <jd2:positionLocked value = "false"/>
                  <jd2:sizeLocked value = "false"/>
                  <jd2:boundingBox x = "390" y = "180"/>
                  <jd2:displayNameVisible value = "" visible = "false"/>
                  <jd2:displayValue visible = "false">
                     <jd2:position rx = "0" ry = "0"/>
                     <jd2:displayStatus value = "dvInitialValue"/>
                     <jd2:font fontName = "Arial" fontSize = "8" fontColor = "FF000000" fontStyle = ""/>
                  </jd2:displayValue>
                  <jd2:text value = "Node1" visible = "true">
                     <jd2:position rx = "9.108" ry = "11.926"/>
                     <jd2:font fontName = "Arial" fontSize = "10" fontStyle = "" fontColor = "FF000000"/>
                  </jd2:text>
                  <jd2:complex id = "C2592840" displayName = "untitled" w = "62" h = "40"
                               boundarySpeciesStyle = "bsShadow" boundaryStyleColor = "FF0000FF" captionPosition = "npCenter" captionVisible = "true"
                               aliasBoundaryStyle = "abRectangle" aliasBoundaryColor = "FFFF0000" aliasBoundaryThickness = "3">
                     <jd2:subunit shape = "suOvalSquare">
                        <jd2:boundingBox rx = "0" ry = "0" w = "62" h = "40"/>
                        <jd2:text value = "S13" visible = "false">
                           <jd2:position rx = "19.5" ry = "12"/>
                           <jd2:font fontName = "Arial" fontSize = "8" fontColor = "FF000000" fontStyle = ""/>
                        </jd2:text>
                        <jd2:color scheme = "gtVertLinear" startColor = "FFFFCC99" endColor = "FFFFFFFF"/>
                        <jd2:edgeStyle color = "FFFF6600" thickness = "2" stroke = "dsSolid"/>
                     </jd2:subunit>
                  </jd2:complex>
               </jd2:species>
               <jd2:species id = "Node2" boundaryCondition = "false" compartment = "vol2" initialConcentration = "0">
                  <jd2:visible value = "true"/>
                  <jd2:positionLocked value = "false"/>
                  <jd2:sizeLocked value = "false"/>
                  <jd2:boundingBox x = "191" y = "372"/>
                  <jd2:displayNameVisible value = "" visible = "false"/>
                  <jd2:displayValue visible = "false">
                     <jd2:position rx = "0" ry = "0"/>
                     <jd2:displayStatus value = "dvInitialValue"/>
                     <jd2:font fontName = "Arial" fontSize = "8" fontColor = "FF000000" fontStyle = ""/>
                  </jd2:displayValue>
                  <jd2:text value = "Node2" visible = "true">
                     <jd2:position rx = "9.108" ry = "11.926"/>
                     <jd2:font fontName = "Arial" fontSize = "10" fontStyle = "" fontColor = "FF000000"/>
                  </jd2:text>
                  <jd2:complex id = "C2592840" displayName = "untitled" w = "62" h = "40"
                               boundarySpeciesStyle = "bsShadow" boundaryStyleColor = "FF0000FF" captionPosition = "npCenter" captionVisible = "true"
                               aliasBoundaryStyle = "abRectangle" aliasBoundaryColor = "FFFF0000" aliasBoundaryThickness = "3">
                     <jd2:subunit shape = "suOvalSquare">
                        <jd2:boundingBox rx = "0" ry = "0" w = "62" h = "40"/>
                        <jd2:text value = "S13" visible = "false">
                           <jd2:position rx = "19.5" ry = "12"/>
                           <jd2:font fontName = "Arial" fontSize = "8" fontColor = "FF000000" fontStyle = ""/>
                        </jd2:text>
                        <jd2:color scheme = "gtVertLinear" startColor = "FFFFCC99" endColor = "FFFFFFFF"/>
                        <jd2:edgeStyle color = "FFFF6600" thickness = "2" stroke = "dsSolid"/>
                     </jd2:subunit>
                  </jd2:complex>
               </jd2:species>
               <jd2:species id = "Node3" boundaryCondition = "false" compartment = "vol2" initialConcentration = "0">
                  <jd2:visible value = "true"/>
                  <jd2:positionLocked value = "false"/>
                  <jd2:sizeLocked value = "false"/>
                  <jd2:boundingBox x = "415" y = "402"/>
                  <jd2:displayNameVisible value = "" visible = "false"/>
                  <jd2:displayValue visible = "false">
                     <jd2:position rx = "0" ry = "0"/>
                     <jd2:displayStatus value = "dvInitialValue"/>
                     <jd2:font fontName = "Arial" fontSize = "8" fontColor = "FF000000" fontStyle = ""/>
                  </jd2:displayValue>
                  <jd2:text value = "Node3" visible = "true">
                     <jd2:position rx = "9.108" ry = "11.926"/>
                     <jd2:font fontName = "Arial" fontSize = "10" fontStyle = "" fontColor = "FF000000"/>
                  </jd2:text>
                  <jd2:complex id = "C2592840" displayName = "untitled" w = "62" h = "40"
                               boundarySpeciesStyle = "bsShadow" boundaryStyleColor = "FF0000FF" captionPosition = "npCenter" captionVisible = "true"
                               aliasBoundaryStyle = "abRectangle" aliasBoundaryColor = "FFFF0000" aliasBoundaryThickness = "3">
                     <jd2:subunit shape = "suOvalSquare">
                        <jd2:boundingBox rx = "0" ry = "0" w = "62" h = "40"/>
                        <jd2:text value = "S13" visible = "false">
                           <jd2:position rx = "19.5" ry = "12"/>
                           <jd2:font fontName = "Arial" fontSize = "8" fontColor = "FF000000" fontStyle = ""/>
                        </jd2:text>
                        <jd2:color scheme = "gtVertLinear" startColor = "FFFFCC99" endColor = "FFFFFFFF"/>
                        <jd2:edgeStyle color = "FFFF6600" thickness = "2" stroke = "dsSolid"/>
                     </jd2:subunit>
                  </jd2:complex>
               </jd2:species>
               <jd2:species id = "Node4" boundaryCondition = "true" compartment = "compartment" initialConcentration = "0">
                  <jd2:visible value = "true"/>
                  <jd2:positionLocked value = "false"/>
                  <jd2:sizeLocked value = "false"/>
                  <jd2:boundingBox x = "40" y = "92"/>
                  <jd2:displayNameVisible value = "" visible = "false"/>
                  <jd2:displayValue visible = "false">
                     <jd2:position rx = "0" ry = "0"/>
                     <jd2:displayStatus value = "dvInitialValue"/>
                     <jd2:font fontName = "Arial" fontSize = "8" fontColor = "FF000000" fontStyle = ""/>
                  </jd2:displayValue>
                  <jd2:text value = "Node4" visible = "true">
                     <jd2:position rx = "9.108" ry = "11.926"/>
                     <jd2:font fontName = "Arial" fontSize = "10" fontStyle = "" fontColor = "FF000000"/>
                  </jd2:text>
                  <jd2:complex id = "C2592840" displayName = "untitled" w = "62" h = "40"
                               boundarySpeciesStyle = "bsShadow" boundaryStyleColor = "FF0000FF" captionPosition = "npCenter" captionVisible = "true"
                               aliasBoundaryStyle = "abRectangle" aliasBoundaryColor = "FFFF0000" aliasBoundaryThickness = "3">
                     <jd2:subunit shape = "suOvalSquare">
                        <jd2:boundingBox rx = "0" ry = "0" w = "62" h = "40"/>
                        <jd2:text value = "S13" visible = "false">
                           <jd2:position rx = "19.5" ry = "12"/>
                           <jd2:font fontName = "Arial" fontSize = "8" fontColor = "FF000000" fontStyle = ""/>
                        </jd2:text>
                        <jd2:color scheme = "gtVertLinear" startColor = "FFFFCC99" endColor = "FFFFFFFF"/>
                        <jd2:edgeStyle color = "FFFF6600" thickness = "2" stroke = "dsSolid"/>
                     </jd2:subunit>
                  </jd2:complex>
               </jd2:species>
            </jd2:listOfSpecies>
            <jd2:listOfReactions>
               <jd2:reaction id = "J0" reversible = "false">
                  <jd2:listOfReactants>
                     <jd2:speciesReference species = "Node0" stoichiometry = "1"/>
                  </jd2:listOfReactants>
                  <jd2:listOfProducts>
                     <jd2:speciesReference species = "Node1" stoichiometry = "1"/>
                  </jd2:listOfProducts>
                  <jd2:listOfModifierEdges>
                     <jd2:modifierEdge visible = "true">
                        <jd2:speciesReference species = "Node2"/>
                        <jd2:destinationReaction name = "J0" regulatorType = "rtPositive" relativePosition = "0.5" destinationArcId = "0"
                                                 destinationLineSegmentId = "0"/>
                        <jd2:display lineThickness = "2" lineColor = "FF0000FF" lineDashStyle = "dsSolid" positiveMarkerStyle = "rmEmptyCircle">
                           <jd2:lineType type = "ltLine">
                              <jd2:pt x = "222" y = "392" type = "modifier" speciesRef = "Node2"/>
                              <jd2:pt x = "330.77" y = "165.47"/>
                           </jd2:lineType>
                        </jd2:display>
                     </jd2:modifierEdge>
                  </jd2:listOfModifierEdges>
                  <jd2:kineticLaw type = "explicit">
                     <jd2:rateEquation value = "J0_k*Node0*Node2"/>
                     <jd2:listOfSymbols>
                        <jd2:parameter id = "J0_k" value = "0.1"/>
                     </jd2:listOfSymbols>
                  </jd2:kineticLaw>
                  <jd2:display lineColor = "FF008000" lineThickness = "2">
                     <jd2:arrowTip visible = "true" fillColor = "FFFFA500" outLineColor = "FFFFA500" outlineThickness = "2"
                                   displacement = "6">
                        <jd2:vertices>
                           <jd2:pt x = "0" y = "14"/>
                           <jd2:pt x = "3" y = "7"/>
                           <jd2:pt x = "0" y = "0"/>
                           <jd2:pt x = "14" y = "7"/>
                        </jd2:vertices>
                     </jd2:arrowTip>
                     <jd2:lineType type = "ltBezier">
                        <jd2:edge>
                           <jd2:pt x = "286" y = "109" type = "substrate" speciesRef = "Node0"/>
                           <jd2:pt x = "337" y = "159.24" type = "controlPoint"/>
                           <jd2:pt x = "337" y = "159.24" type = "controlPoint"/>
                           <jd2:pt x = "421" y = "200" type = "product" speciesRef = "Node1"/>
                        </jd2:edge>
                     </jd2:lineType>
                     <jd2:displayValue visible = "false" showValue = "false" value = "0">
                        <jd2:position rx = "0" ry = "0"/>
                        <jd2:font fontName = "Arial" fontSize = "10" fontColor = "FF000000" fontStyle = ""/>
                     </jd2:displayValue>
                  </jd2:display>
               </jd2:reaction>
               <jd2:reaction id = "J1" reversible = "false">
                  <jd2:listOfReactants>
                     <jd2:speciesReference species = "Node1" stoichiometry = "1"/>
                  </jd2:listOfReactants>
                  <jd2:listOfProducts>
                     <jd2:speciesReference species = "Node2" stoichiometry = "1"/>
                  </jd2:listOfProducts>
                  <jd2:listOfModifierEdges/>
                  <jd2:kineticLaw type = "builtin">
                     <jd2:rateEquation value = "imm"/>
                     <jd2:listOfSymbols>
                        <jd2:parameter id = "J1_k" value = "0.1"/>
                     </jd2:listOfSymbols>
                  </jd2:kineticLaw>
                  <jd2:display lineColor = "FF008000" lineThickness = "2">
                     <jd2:arrowTip visible = "true" fillColor = "FFFFA500" outLineColor = "FFFFA500" outlineThickness = "2"
                                   displacement = "6">
                        <jd2:vertices>
                           <jd2:pt x = "0" y = "14"/>
                           <jd2:pt x = "3" y = "7"/>
                           <jd2:pt x = "0" y = "0"/>
                           <jd2:pt x = "14" y = "7"/>
                        </jd2:vertices>
                     </jd2:arrowTip>
                     <jd2:lineType type = "ltLine">
                        <jd2:edge>
                           <jd2:pt x = "421" y = "200" type = "substrate" speciesRef = "Node1"/>
                           <jd2:pt x = "222" y = "392" type = "product" speciesRef = "Node2"/>
                        </jd2:edge>
                     </jd2:lineType>
                     <jd2:displayValue visible = "false" showValue = "false" value = "0">
                        <jd2:position rx = "0" ry = "0"/>
                        <jd2:font fontName = "Arial" fontSize = "10" fontColor = "FF000000" fontStyle = ""/>
                     </jd2:displayValue>
                  </jd2:display>
               </jd2:reaction>
               <jd2:reaction id = "J2" reversible = "false">
                  <jd2:listOfReactants>
                     <jd2:speciesReference species = "Node2" stoichiometry = "1"/>
                  </jd2:listOfReactants>
                  <jd2:listOfProducts>
                     <jd2:speciesReference species = "Node3" stoichiometry = "1"/>
                  </jd2:listOfProducts>
                  <jd2:listOfModifierEdges/>
                  <jd2:kineticLaw type = "builtin">
                     <jd2:rateEquation value = "imm"/>
                     <jd2:listOfSymbols>
                        <jd2:parameter id = "J2_k" value = "0.1"/>
                     </jd2:listOfSymbols>
                  </jd2:kineticLaw>
                  <jd2:display lineColor = "FF008000" lineThickness = "2">
                     <jd2:arrowTip visible = "true" fillColor = "FFFFA500" outLineColor = "FFFFA500" outlineThickness = "2"
                                   displacement = "6">
                        <jd2:vertices>
                           <jd2:pt x = "0" y = "14"/>
                           <jd2:pt x = "3" y = "7"/>
                           <jd2:pt x = "0" y = "0"/>
                           <jd2:pt x = "14" y = "7"/>
                        </jd2:vertices>
                     </jd2:arrowTip>
                     <jd2:lineType type = "ltBezier">
                        <jd2:edge>
                           <jd2:pt x = "222" y = "392" type = "substrate" speciesRef = "Node2"/>
                           <jd2:pt x = "349.5" y = "405.3" type = "controlPoint"/>
                           <jd2:pt x = "349.5" y = "405.3" type = "controlPoint"/>
                           <jd2:pt x = "446" y = "422" type = "product" speciesRef = "Node3"/>
                        </jd2:edge>
                     </jd2:lineType>
                     <jd2:displayValue visible = "false" showValue = "false" value = "0">
                        <jd2:position rx = "0" ry = "0"/>
                        <jd2:font fontName = "Arial" fontSize = "10" fontColor = "FF000000" fontStyle = ""/>
                     </jd2:displayValue>
                  </jd2:display>
               </jd2:reaction>
               <jd2:reaction id = "J3" reversible = "false">
                  <jd2:listOfReactants>
                     <jd2:speciesReference species = "Node4" stoichiometry = "1"/>
                  </jd2:listOfReactants>
                  <jd2:listOfProducts>
                     <jd2:speciesReference species = "Node0" stoichiometry = "1"/>
                  </jd2:listOfProducts>
                  <jd2:listOfModifierEdges/>
                  <jd2:kineticLaw type = "builtin">
                     <jd2:rateEquation value = "imm"/>
                     <jd2:listOfSymbols>
                        <jd2:parameter id = "J3_k" value = "0.1"/>
                     </jd2:listOfSymbols>
                  </jd2:kineticLaw>
                  <jd2:display lineColor = "FF008000" lineThickness = "2">
                     <jd2:arrowTip visible = "true" fillColor = "FFFFA500" outLineColor = "FFFFA500" outlineThickness = "2"
                                   displacement = "6">
                        <jd2:vertices>
                           <jd2:pt x = "0" y = "14"/>
                           <jd2:pt x = "3" y = "7"/>
                           <jd2:pt x = "0" y = "0"/>
                           <jd2:pt x = "14" y = "7"/>
                        </jd2:vertices>
                     </jd2:arrowTip>
                     <jd2:lineType type = "ltBezier">
                        <jd2:edge>
                           <jd2:pt x = "71" y = "112" type = "substrate" speciesRef = "Node4"/>
                           <jd2:pt x = "165.5" y = "112.86" type = "controlPoint"/>
                           <jd2:pt x = "165.5" y = "112.86" type = "controlPoint"/>
                           <jd2:pt x = "286" y = "109" type = "product" speciesRef = "Node0"/>
                        </jd2:edge>
                     </jd2:lineType>
                     <jd2:displayValue visible = "false" showValue = "false" value = "0">
                        <jd2:position rx = "0" ry = "0"/>
                        <jd2:font fontName = "Arial" fontSize = "10" fontColor = "FF000000" fontStyle = ""/>
                     </jd2:displayValue>
                  </jd2:display>
               </jd2:reaction>
            </jd2:listOfReactions>
         </jd2:PathwayDesignerLayout>
      </annotation>
      <listOfFunctionDefinitions>
         <functionDefinition id = "mod">
            <math xmlns = "http://www.w3.org/1998/Math/MathML">
               <lambda>
                  <bvar>
                     <ci>
                           x
                     </ci>
                  </bvar>
                  <bvar>
                     <ci>
                           y
                     </ci>
                  </bvar>
                  <apply>
                     <minus/>
                     <ci>
                           x
                     </ci>
                     <apply>
                        <times/>
                        <ci>
                              y
                        </ci>
                        <apply>
                           <floor/>
                           <apply>
                              <divide/>
                              <ci>
                                    x
                              </ci>
                              <ci>
                                    y
                              </ci>
                           </apply>
                        </apply>
                     </apply>
                  </apply>
               </lambda>
            </math>
         </functionDefinition>
         <functionDefinition id = "normal">
            <annotation>
               <distribution xmlns = "http://sbml.org/annotations/distribution" definition = "http://en.wikipedia.org/wiki/Normal_distribution"/>
            </annotation>
            <math xmlns = "http://www.w3.org/1998/Math/MathML">
               <lambda>
                  <bvar>
                     <ci>
                           m
                     </ci>
                  </bvar>
                  <bvar>
                     <ci>
                           s
                     </ci>
                  </bvar>
                  <ci>
                        m
                  </ci>
               </lambda>
            </math>
         </functionDefinition>
         <functionDefinition id = "uniform">
            <annotation>
               <distribution xmlns = "http://sbml.org/annotations/distribution" definition = "http://en.wikipedia.org/wiki/Uniform_distribution_(continuous)"/>
            </annotation>
            <math xmlns = "http://www.w3.org/1998/Math/MathML">
               <lambda>
                  <bvar>
                     <ci>
                           a
                     </ci>
                  </bvar>
                  <bvar>
                     <ci>
                           b
                     </ci>
                  </bvar>
                  <apply>
                     <divide/>
                     <apply>
                        <plus/>
                        <ci>
                              a
                        </ci>
                        <ci>
                              b
                        </ci>
                     </apply>
                     <cn type = "integer">
                           2
                     </cn>
                  </apply>
               </lambda>
            </math>
         </functionDefinition>
         <functionDefinition id = "sawTooth">
            <math xmlns = "http://www.w3.org/1998/Math/MathML">
               <lambda>
                  <bvar>
                     <csymbol encoding = "text" definitionURL = "http://www.sbml.org/sbml/symbols/time">
                           time
                     </csymbol>
                  </bvar>
                  <bvar>
                     <ci>
                           period
                     </ci>
                  </bvar>
                  <bvar>
                     <ci>
                           center
                     </ci>
                  </bvar>
                  <bvar>
                     <ci>
                           amplitude
                     </ci>
                  </bvar>
                  <apply>
                     <plus/>
                     <ci>
                           center
                     </ci>
                     <apply>
                        <times/>
                        <ci>
                              amplitude
                        </ci>
                        <apply>
                           <minus/>
                           <apply>
                              <divide/>
                              <csymbol encoding = "text" definitionURL = "http://www.sbml.org/sbml/symbols/time">
                                    time
                              </csymbol>
                              <ci>
                                    period
                              </ci>
                           </apply>
                           <apply>
                              <floor/>
                              <apply>
                                 <plus/>
                                 <apply>
                                    <divide/>
                                    <csymbol encoding = "text" definitionURL = "http://www.sbml.org/sbml/symbols/time">
                                          time
                                    </csymbol>
                                    <ci>
                                          period
                                    </ci>
                                 </apply>
                                 <cn>
                                       0.5
                                 </cn>
                              </apply>
                           </apply>
                        </apply>
                     </apply>
                  </apply>
               </lambda>
            </math>
         </functionDefinition>
         <functionDefinition id = "squareWave">
            <math xmlns = "http://www.w3.org/1998/Math/MathML">
               <lambda>
                  <bvar>
                     <csymbol encoding = "text" definitionURL = "http://www.sbml.org/sbml/symbols/time">
                           time
                     </csymbol>
                  </bvar>
                  <bvar>
                     <ci>
                           period
                     </ci>
                  </bvar>
                  <bvar>
                     <ci>
                           center
                     </ci>
                  </bvar>
                  <bvar>
                     <ci>
                           amplitude
                     </ci>
                  </bvar>
                  <apply>
                     <plus/>
                     <apply>
                        <times/>
                        <ci>
                              amplitude
                        </ci>
                        <apply>
                           <gt/>
                           <apply>
                              <sin/>
                              <apply>
                                 <divide/>
                                 <apply>
                                    <times/>
                                    <cn type = "integer">
                                          2
                                    </cn>
                                    <cn>
                                          3.1414926
                                    </cn>
                                    <csymbol encoding = "text" definitionURL = "http://www.sbml.org/sbml/symbols/time">
                                          time
                                    </csymbol>
                                 </apply>
                                 <ci>
                                       period
                                 </ci>
                              </apply>
                           </apply>
                           <cn type = "integer">
                                 0
                           </cn>
                        </apply>
                     </apply>
                     <ci>
                           center
                     </ci>
                  </apply>
               </lambda>
            </math>
         </functionDefinition>
         <functionDefinition id = "triangleWave">
            <math xmlns = "http://www.w3.org/1998/Math/MathML">
               <lambda>
                  <bvar>
                     <csymbol encoding = "text" definitionURL = "http://www.sbml.org/sbml/symbols/time">
                           time
                     </csymbol>
                  </bvar>
                  <bvar>
                     <ci>
                           period
                     </ci>
                  </bvar>
                  <bvar>
                     <ci>
                           center
                     </ci>
                  </bvar>
                  <bvar>
                     <ci>
                           amplitude
                     </ci>
                  </bvar>
                  <apply>
                     <plus/>
                     <ci>
                           center
                     </ci>
                     <apply>
                        <times/>
                        <ci>
                              amplitude
                        </ci>
                        <apply>
                           <abs/>
                           <apply>
                              <minus/>
                              <apply>
                                 <divide/>
                                 <csymbol encoding = "text" definitionURL = "http://www.sbml.org/sbml/symbols/time">
                                       time
                                 </csymbol>
                                 <ci>
                                       period
                                 </ci>
                              </apply>
                              <apply>
                                 <floor/>
                                 <apply>
                                    <plus/>
                                    <apply>
                                       <divide/>
                                       <csymbol encoding = "text" definitionURL = "http://www.sbml.org/sbml/symbols/time">
                                             time
                                       </csymbol>
                                       <ci>
                                             period
                                       </ci>
                                    </apply>
                                    <cn>
                                          0.5
                                    </cn>
                                 </apply>
                              </apply>
                           </apply>
                        </apply>
                     </apply>
                  </apply>
               </lambda>
            </math>
         </functionDefinition>
         <functionDefinition id = "max">
            <math xmlns = "http://www.w3.org/1998/Math/MathML">
               <lambda>
                  <bvar>
                     <ci>
                           x
                     </ci>
                  </bvar>
                  <bvar>
                     <ci>
                           y
                     </ci>
                  </bvar>
                  <piecewise>
                     <piece>
                        <ci>
                              x
                        </ci>
                        <apply>
                           <gt/>
                           <ci>
                                 x
                           </ci>
                           <ci>
                                 y
                           </ci>
                        </apply>
                     </piece>
                     <otherwise>
                        <ci>
                              y
                        </ci>
                     </otherwise>
                  </piecewise>
               </lambda>
            </math>
         </functionDefinition>
         <functionDefinition id = "min">
            <math xmlns = "http://www.w3.org/1998/Math/MathML">
               <lambda>
                  <bvar>
                     <ci>
                           x
                     </ci>
                  </bvar>
                  <bvar>
                     <ci>
                           y
                     </ci>
                  </bvar>
                  <piecewise>
                     <piece>
                        <ci>
                              x
                        </ci>
                        <apply>
                           <lt/>
                           <ci>
                                 x
                           </ci>
                           <ci>
                                 y
                           </ci>
                        </apply>
                     </piece>
                     <otherwise>
                        <ci>
                              y
                        </ci>
                     </otherwise>
                  </piecewise>
               </lambda>
            </math>
         </functionDefinition>
      </listOfFunctionDefinitions>
      <listOfCompartments>
         <compartment id = "compartment" size = "1"/>
         <compartment id = "vol1" size = "1"/>
         <compartment id = "vol2" size = "1"/>
      </listOfCompartments>
      <listOfSpecies>
         <species id = "Node0" boundaryCondition = "false" initialConcentration = "0" compartment = "vol1"/>
         <species id = "Node1" boundaryCondition = "false" initialConcentration = "0" compartment = "vol1"/>
         <species id = "Node2" boundaryCondition = "false" initialConcentration = "0" compartment = "vol2"/>
         <species id = "Node3" boundaryCondition = "false" initialConcentration = "0" compartment = "vol2"/>
         <species id = "Node4" boundaryCondition = "true" initialConcentration = "0" compartment = "compartment"/>
      </listOfSpecies>
      <listOfParameters>
         <parameter id = "J1_k" value = "0.1"/>
         <parameter id = "J2_k" value = "0.1"/>
         <parameter id = "J3_k" value = "0.1"/>
         <parameter id = "J0_k" value = "0.1"/>
      </listOfParameters>
      <listOfReactions>
         <reaction id = "J0" reversible = "false">
            <listOfReactants>
               <speciesReference species = "Node0" stoichiometry = "1"/>
            </listOfReactants>
            <listOfProducts>
               <speciesReference species = "Node1" stoichiometry = "1"/>
            </listOfProducts>
            <listOfModifiers>
               <modifierSpeciesReference species = "Node2"/>
            </listOfModifiers>
            <kineticLaw>
               <math xmlns = "http://www.w3.org/1998/Math/MathML">
                  <apply>
                     <times/>
                     <ci>
                           J0_k
                     </ci>
                     <ci>
                           Node0
                     </ci>
                     <ci>
                           Node2
                     </ci>
                  </apply>
               </math>
            </kineticLaw>
         </reaction>
         <reaction id = "J1" reversible = "false">
            <listOfReactants>
               <speciesReference species = "Node1" stoichiometry = "1"/>
            </listOfReactants>
            <listOfProducts>
               <speciesReference species = "Node2" stoichiometry = "1"/>
            </listOfProducts>
            <kineticLaw>
               <math xmlns = "http://www.w3.org/1998/Math/MathML">
                  <apply>
                     <times/>
                     <ci>
                           J1_k
                     </ci>
                     <ci>
                           Node1
                     </ci>
                  </apply>
               </math>
            </kineticLaw>
         </reaction>
         <reaction id = "J2" reversible = "false">
            <listOfReactants>
               <speciesReference species = "Node2" stoichiometry = "1"/>
            </listOfReactants>
            <listOfProducts>
               <speciesReference species = "Node3" stoichiometry = "1"/>
            </listOfProducts>
            <kineticLaw>
               <math xmlns = "http://www.w3.org/1998/Math/MathML">
                  <apply>
                     <times/>
                     <ci>
                           J2_k
                     </ci>
                     <ci>
                           Node2
                     </ci>
                  </apply>
               </math>
            </kineticLaw>
         </reaction>
         <reaction id = "J3" reversible = "false">
            <listOfReactants>
               <speciesReference species = "Node4" stoichiometry = "1"/>
            </listOfReactants>
            <listOfProducts>
               <speciesReference species = "Node0" stoichiometry = "1"/>
            </listOfProducts>
            <kineticLaw>
               <math xmlns = "http://www.w3.org/1998/Math/MathML">
                  <apply>
                     <times/>
                     <ci>
                           J3_k
                     </ci>
                     <ci>
                           Node4
                     </ci>
                  </apply>
               </math>
            </kineticLaw>
         </reaction>
      </listOfReactions>
   </model>
</sbml>
"""


s = SBMLlayout()

s.drawNetwork()








