model_xml = """<?xml version="1.0" encoding="UTF-8"?>
<sbml xmlns="http://www.sbml.org/sbml/level3/version1/core" level="3" version="1">
  <model metaid="__main" id="__main">
    <listOfCompartments>
      <compartment sboTerm="SBO:0000410" id="default_compartment" spatialDimensions="3" size="1" constant="true"/>
    </listOfCompartments>
    <listOfSpecies>
      <species id="S0" compartment="default_compartment" initialConcentration="2.36875591992985" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species id="S1" compartment="default_compartment" initialConcentration="1.25693371799227" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species id="S2" compartment="default_compartment" initialConcentration="1.47638610786975" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species id="S3" compartment="default_compartment" initialConcentration="7.74568563617834" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species id="S4" compartment="default_compartment" initialConcentration="1.44539874344625" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species id="S5" compartment="default_compartment" initialConcentration="5.16769647924638" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species id="S6" compartment="default_compartment" initialConcentration="8.45397868543523" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false"/>
      <species id="S7" compartment="default_compartment" initialConcentration="1.36465635209562" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false"/>
    </listOfSpecies>
    <listOfParameters>
      <parameter id="k0" value="2.04064036451476" constant="true"/>
      <parameter id="k1" value="6.10103647670621" constant="true"/>
      <parameter id="k2" value="5.38212977343208" constant="true"/>
      <parameter id="k3" value="8.18340043351905" constant="true"/>
      <parameter id="k4" value="9.27323237102482" constant="true"/>
      <parameter id="k5" value="0.216739908559331" constant="true"/>
      <parameter id="k6" value="2.67645867211235" constant="true"/>
      <parameter id="k7" value="2.96146047594227" constant="true"/>
      <parameter id="k8" value="9.27708381920083" constant="true"/>
      <parameter id="k9" value="8.87558455165279" constant="true"/>
      <parameter id="k10" value="7.30714476162246" constant="true"/>
      <parameter id="k11" value="7.80175525423323" constant="true"/>
      <parameter id="k12" value="1.75821281291885" constant="true"/>
      <parameter id="k13" value="7.96573082615547" constant="true"/>
      <parameter id="k14" value="7.04368996951667" constant="true"/>
      <parameter id="k15" value="9.06536702641853" constant="true"/>
      <parameter id="k16" value="3.03636681019936" constant="true"/>
      <parameter id="k17" value="5.39267151269359" constant="true"/>
      <parameter id="k18" value="2.69684237775308" constant="true"/>
      <parameter id="k19" value="4.89019128861609" constant="true"/>
    </listOfParameters>
    <listOfReactions>
      <reaction id="_J0" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S1" stoichiometry="1" constant="true"/>
          <speciesReference species="S0" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S6" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k0 </ci>
              <ci> S1 </ci>
              <ci> S0 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="_J1" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S6" stoichiometry="1" constant="true"/>
          <speciesReference species="S6" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S3" stoichiometry="1" constant="true"/>
          <speciesReference species="S4" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k1 </ci>
              <ci> S6 </ci>
              <ci> S6 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="_J2" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S6" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S1" stoichiometry="1" constant="true"/>
          <speciesReference species="S2" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k2 </ci>
              <ci> S6 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="_J3" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S7" stoichiometry="1" constant="true"/>
          <speciesReference species="S3" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S0" stoichiometry="1" constant="true"/>
          <speciesReference species="S4" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k3 </ci>
              <ci> S7 </ci>
              <ci> S3 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="_J4" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S6" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S3" stoichiometry="1" constant="true"/>
          <speciesReference species="S0" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k4 </ci>
              <ci> S6 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="_J5" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S3" stoichiometry="1" constant="true"/>
          <speciesReference species="S6" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S6" stoichiometry="1" constant="true"/>
          <speciesReference species="S7" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k5 </ci>
              <ci> S3 </ci>
              <ci> S6 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="_J6" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S4" stoichiometry="1" constant="true"/>
          <speciesReference species="S4" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S5" stoichiometry="1" constant="true"/>
          <speciesReference species="S0" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k6 </ci>
              <ci> S4 </ci>
              <ci> S4 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="_J7" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S3" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S7" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k7 </ci>
              <ci> S3 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="_J8" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S5" stoichiometry="1" constant="true"/>
          <speciesReference species="S2" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S7" stoichiometry="1" constant="true"/>
          <speciesReference species="S2" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k8 </ci>
              <ci> S5 </ci>
              <ci> S2 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="_J9" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S7" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S1" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k9 </ci>
              <ci> S7 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="_J10" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S7" stoichiometry="1" constant="true"/>
          <speciesReference species="S5" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S0" stoichiometry="1" constant="true"/>
          <speciesReference species="S7" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k10 </ci>
              <ci> S7 </ci>
              <ci> S5 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="_J11" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S2" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S6" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k11 </ci>
              <ci> S2 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="_J12" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S4" stoichiometry="1" constant="true"/>
          <speciesReference species="S2" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S0" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k12 </ci>
              <ci> S4 </ci>
              <ci> S2 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="_J13" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S0" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S4" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k13 </ci>
              <ci> S0 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="_J14" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S0" stoichiometry="1" constant="true"/>
          <speciesReference species="S0" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S3" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k14 </ci>
              <ci> S0 </ci>
              <ci> S0 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="_J15" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S6" stoichiometry="1" constant="true"/>
          <speciesReference species="S1" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S5" stoichiometry="1" constant="true"/>
          <speciesReference species="S6" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k15 </ci>
              <ci> S6 </ci>
              <ci> S1 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="_J16" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S3" stoichiometry="1" constant="true"/>
          <speciesReference species="S4" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S6" stoichiometry="1" constant="true"/>
          <speciesReference species="S2" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k16 </ci>
              <ci> S3 </ci>
              <ci> S4 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="_J17" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S5" stoichiometry="1" constant="true"/>
          <speciesReference species="S6" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S6" stoichiometry="1" constant="true"/>
          <speciesReference species="S1" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k17 </ci>
              <ci> S5 </ci>
              <ci> S6 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="_J18" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S4" stoichiometry="1" constant="true"/>
          <speciesReference species="S7" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S3" stoichiometry="1" constant="true"/>
          <speciesReference species="S3" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k18 </ci>
              <ci> S4 </ci>
              <ci> S7 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction id="_J19" reversible="true" fast="false">
        <listOfReactants>
          <speciesReference species="S5" stoichiometry="1" constant="true"/>
          <speciesReference species="S4" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="S2" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> k19 </ci>
              <ci> S5 </ci>
              <ci> S4 </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
    </listOfReactions>
  </model>
</sbml>
"""