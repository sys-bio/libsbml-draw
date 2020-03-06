# model generated using randMANetGen
schmierer2008 = """<?xml version='1.0' encoding='UTF-8' standalone='no'?>
<!-- This model was downloaded from BioModels Database -->
<!-- http://www.ebi.ac.uk/biomodels-static/                   -->
<!-- Fri Jan 24 06:18:39 GMT 2020                      -->
<sbml xmlns="http://www.sbml.org/sbml/level2" level="2" metaid="metaid_0000001" version="1">
    <model id="Schmierer_2008_Smad_Tgfb" metaid="metaid_0000002" name="Schmierer_2008_Smad_Tgfb">
        <notes>
            <html xmlns="http://www.w3.org/1999/xhtml">
                <head/>
                <body>
                    <p>This sbml file describes the RECI model from:
                        <br/>
                        "Mathematical modeling identifies Smad nucleocytoplasmic shuttling as a dynamic
                        signal-interpreting system" by Bernhard Schmierer, Alexander L. Tournier, Paul A. Bates and
                        Caroline S. Hill, Proc Natl Acad Sci U S A. 2008 May 6;105(18):6608-13.
                        <br/>
                        All parameter and species names are as in Figure S3 of the original publication. The original
                        model was done in copasi.<br/>SB-431542 addition to a concentration of 10000 nM is set at 2700
                        sec. The initial concentration of SB, the time point of addition and the final concentration can
                        be set by altering the parameters                                                               <b>
                            SB_0</b>,                                                               <b>t_SB</b> and                                                               <b>
                            SB_end</b>.
                        <br/>
                        This model file has been used to reproduce Figures 2D and 5A from the research paper using
                        SBMLodesolver. To get the results for the figures, sum the corresponding concentrations:<br/>fig
                        2D: nuclear EGFP-Smad2 = G_n + pG_n + G2_n + G4_n + 2* GG_n<br/>fig 5A (either n or c for
                        nucleus or cytosol):<br/>monomeric Smad2 = S2_n/c + G_n/c<br/>monomeric P-Smad2 = pS2_n/c +
                        pG_n/c<br/>Smad2/Smad4 complexes = S24_n/c + G4_n/c<br/>Smad2/Smad2 complexes = S22_n/c + G2_n/c
                        + GG_n/c
                        <br/>
                    </p>
                    <p>This model originates from BioModels Database: A Database of Annotated Published Models. It is
                        copyright (c) 2005-2009 The BioModels Team.<br/>For more information see the                               <a
                                href="http://www.ebi.ac.uk/biomodels/legal.html" target="_blank">terms of use</a>.<br/>
                        To cite BioModels Database, please use                               <a
                                href="http://www.pubmedcentral.nih.gov/articlerender.fcgi?tool=pubmed&amp;pubmedid=16381960"
                                target="_blank">Le Novère N., Bornstein B., Broicher A., Courtot M., Donizelli M.,
                            Dharuri H., Li L., Sauro H., Schilstra M., Shapiro B., Snoep J.L., Hucka M. (2006) BioModels
                            Database: A Free, Centralized Database of Curated, Published, Quantitative Kinetic Models of
                            Biochemical and Cellular Systems Nucleic Acids Res., 34: D689-D691.
                        </a>
                    </p>
                </body>
            </html>
        </notes>
        <annotation>
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/"
                     xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:dcterms="http://purl.org/dc/terms/"
                     xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                     xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                <rdf:Description rdf:about="#metaid_0000002">
                    <dc:creator>
                        <rdf:Bag>
                            <rdf:li rdf:parseType="Resource">
                                <vCard:N rdf:parseType="Resource">
                                    <vCard:Family>Endler</vCard:Family>
                                    <vCard:Given>Lukas</vCard:Given>
                                </vCard:N>
                                <vCard:EMAIL>lukas@ebi.ac.uk</vCard:EMAIL>
                                <vCard:ORG rdf:parseType="Resource">
                                    <vCard:Orgname>EMBL-EBI</vCard:Orgname>
                                </vCard:ORG>
                            </rdf:li>
                            <rdf:li rdf:parseType="Resource">
                                <vCard:N rdf:parseType="Resource">
                                    <vCard:Family>Schmierer</vCard:Family>
                                    <vCard:Given>Bernhard</vCard:Given>
                                </vCard:N>
                                <vCard:EMAIL>Bernhard.Schmierer@ymail.com</vCard:EMAIL>
                                <vCard:ORG rdf:parseType="Resource">
                                    <vCard:Orgname>Developmental Signalling Lab, Cancer Research UK London Research
                                        Institute
                                    </vCard:Orgname>
                                </vCard:ORG>
                            </rdf:li>
                        </rdf:Bag>
                    </dc:creator>
                    <dcterms:created rdf:parseType="Resource">
                        <dcterms:W3CDTF>2008-07-30T10:47:57Z</dcterms:W3CDTF>
                    </dcterms:created>
                    <dcterms:modified rdf:parseType="Resource">
                        <dcterms:W3CDTF>2016-04-08T15:39:46Z</dcterms:W3CDTF>
                    </dcterms:modified>
                    <bqmodel:is>
                        <rdf:Bag>
                            <rdf:li rdf:resource="http://identifiers.org/biomodels.db/MODEL0451870146"/>
                        </rdf:Bag>
                    </bqmodel:is>
                    <bqmodel:is>
                        <rdf:Bag>
                            <rdf:li rdf:resource="http://identifiers.org/biomodels.db/BIOMD0000000173"/>
                        </rdf:Bag>
                    </bqmodel:is>
                    <bqmodel:isDescribedBy>
                        <rdf:Bag>
                            <rdf:li rdf:resource="http://identifiers.org/pubmed/18443295"/>
                        </rdf:Bag>
                    </bqmodel:isDescribedBy>
                    <bqbiol:isVersionOf>
                        <rdf:Bag>
                            <rdf:li rdf:resource="http://identifiers.org/kegg.pathway/hsa04350"/>
                            <rdf:li rdf:resource="http://identifiers.org/go/GO:0007179"/>
                        </rdf:Bag>
                    </bqbiol:isVersionOf>
                    <bqbiol:hasTaxon>
                        <rdf:Bag>
                            <rdf:li rdf:resource="http://identifiers.org/taxonomy/9606"/>
                        </rdf:Bag>
                    </bqbiol:hasTaxon>
                </rdf:Description>
            </rdf:RDF>
        </annotation>
        <listOfUnitDefinitions>
            <unitDefinition id="substance" metaid="metaid_0000003">
                <listOfUnits>
                    <unit kind="mole" metaid="f7a61609-4fce-4515-9309-4f590b1908e6" scale="-9"/>
                </listOfUnits>
            </unitDefinition>
            <unitDefinition id="nM" metaid="metaid_0000075" name="nM">
                <listOfUnits>
                    <unit kind="mole" metaid="d464a1ad-4fb8-470f-b03b-559c05c67360" scale="-9"/>
                    <unit exponent="-1" kind="litre" metaid="_441b5f91-8714-4775-98fe-098ea7b909f6"/>
                </listOfUnits>
            </unitDefinition>
            <unitDefinition id="ps" metaid="metaid_0000076" name="persecond">
                <listOfUnits>
                    <unit exponent="-1" kind="second" metaid="_36efcad7-9d0c-4e6f-9cf6-e7a5b3343778"/>
                </listOfUnits>
            </unitDefinition>
            <unitDefinition id="pnMps" metaid="metaid_0000077" name="pernMpersecond">
                <listOfUnits>
                    <unit exponent="-1" kind="mole" metaid="c5d0e2a8-4513-44ca-9bda-fc3f6b8a0041" scale="-9"/>
                    <unit exponent="-1" kind="second" metaid="b79cc0c9-d033-45ef-802e-da968504ddda"/>
                    <unit kind="litre" metaid="e718b301-b91a-4e36-afc5-7c62aec9b7e3"/>
                </listOfUnits>
            </unitDefinition>
            <unitDefinition id="lps" metaid="metaid_0000078" name="litrepersecond">
                <listOfUnits>
                    <unit kind="litre" metaid="d3373584-f810-4f75-a516-ab2a45887b31"/>
                    <unit exponent="-1" kind="second" metaid="b54bc660-1ab8-4e86-b94a-56f2ddb55c3f"/>
                </listOfUnits>
            </unitDefinition>
        </listOfUnitDefinitions>
        <listOfCompartments>
            <compartment id="nucleus" metaid="metaid_0000018" name="Nuc" size="1E-12">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000018">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0005634"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </compartment>
            <compartment id="cytosol" metaid="metaid_0000019" name="Cyt" size="2.27E-12">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000019">
                            <bqbiol:is>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0005737"/>
                                </rdf:Bag>
                            </bqbiol:is>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </compartment>
        </listOfCompartments>
        <listOfSpecies>
            <species boundaryCondition="true" compartment="nucleus" constant="true" id="PPase" initialConcentration="1"
                     metaid="metaid_0000020" name="PPase">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000020">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/P35813"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0004721"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="nucleus" id="S2_n" initialConcentration="28.514773357617" metaid="metaid_0000021"
                     name="Smad2_n">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000021">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q15796"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="nucleus" id="pS2_n" initialConcentration="0" metaid="metaid_0000022" name="pSmad2_n">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000022">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q15796"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00562"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="nucleus" id="G_n" initialConcentration="28.514773357617" metaid="metaid_0000023"
                     name="GFP-Smad2_n">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000023">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q15796"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/interpro/IPR000786"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="nucleus" id="pG_n" initialConcentration="0" metaid="metaid_0000024"
                     name="pGFP-Smad2_n">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000024">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q15796"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00562"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/interpro/IPR000786"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="nucleus" id="S22_n" initialConcentration="0" metaid="metaid_0000025"
                     name="pSmad2/pSmad2_n">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000025">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0043234"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                            <bqbiol:hasPart>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q15796"/>
                                </rdf:Bag>
                            </bqbiol:hasPart>
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00562"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="nucleus" id="S24_n" initialConcentration="0" metaid="metaid_0000026"
                     name="pSmad2/Smad4_n">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000026">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0043234"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                            <bqbiol:hasPart>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q15796"/>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q13485"/>
                                </rdf:Bag>
                            </bqbiol:hasPart>
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00562"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="nucleus" id="S4_n" initialConcentration="50.78093897" metaid="metaid_0000027"
                     name="Smad4_n">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000027">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q13485"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="nucleus" id="G2_n" initialConcentration="0" metaid="metaid_0000028"
                     name="pGFP-Smad2/pSmad2_n">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000028">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0043234"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                            <bqbiol:hasPart>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q15796"/>
                                </rdf:Bag>
                            </bqbiol:hasPart>
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/interpro/IPR000786"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00562"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="nucleus" id="G4_n" initialConcentration="0" metaid="metaid_0000029"
                     name="pGFP-Smad2/Smad4_n">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000029">
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q15796"/>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q13485"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0043234"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/interpro/IPR000786"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00562"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="nucleus" id="GG_n" initialConcentration="0" metaid="metaid_0000030"
                     name="pGFP-Smad2/pGFP_Smad2_n">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000030">
                            <bqbiol:hasPart>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q15796"/>
                                </rdf:Bag>
                            </bqbiol:hasPart>
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0043234"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/interpro/IPR000786"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00562"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="S22_c" initialConcentration="0" metaid="metaid_0000031"
                     name="pSmad2/pSmad2_c">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000031">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0043234"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                            <bqbiol:hasPart>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q15796"/>
                                </rdf:Bag>
                            </bqbiol:hasPart>
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00562"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="S24_c" initialConcentration="0" metaid="metaid_0000032"
                     name="pSmad2/Smad4_c">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000032">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0043234"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                            <bqbiol:hasPart>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q15796"/>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q13485"/>
                                </rdf:Bag>
                            </bqbiol:hasPart>
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00562"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="S4_c" initialConcentration="50.78103407" metaid="metaid_0000033"
                     name="Smad4_c">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000033">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q13485"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="S2_c" initialConcentration="60.5899176013587" metaid="metaid_0000034"
                     name="Smad2_c">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000034">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q15796"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="pS2_c" initialConcentration="0" metaid="metaid_0000035" name="pSmad2_c">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000035">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q15796"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00562"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="G_c" initialConcentration="60.5899176013587" metaid="metaid_0000036"
                     name="GFP-Smad2_c">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000036">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q15796"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/interpro/IPR000786"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="pG_c" initialConcentration="0" metaid="metaid_0000037"
                     name="pGFP-Smad2_c">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000037">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q15796"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00562"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/interpro/IPR000786"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="G2_c" initialConcentration="0" metaid="metaid_0000038"
                     name="pGFP-Smad2/pSmad2_c">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000038">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0043234"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                            <bqbiol:hasPart>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q15796"/>
                                </rdf:Bag>
                            </bqbiol:hasPart>
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/interpro/IPR000786"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00562"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="G4_c" initialConcentration="0" metaid="metaid_0000039"
                     name="pGFP-Smad2/Smad4_c">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000039">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0043234"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                            <bqbiol:hasPart>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q15796"/>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q13485"/>
                                </rdf:Bag>
                            </bqbiol:hasPart>
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/interpro/IPR000786"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00562"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="GG_c" initialConcentration="0" metaid="metaid_0000040"
                     name="pGFP-Smad2/pGFP-Smad2_c">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000040">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0043234"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                            <bqbiol:hasPart>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q15796"/>
                                </rdf:Bag>
                            </bqbiol:hasPart>
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/interpro/IPR000786"/>
                                    <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00562"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species boundaryCondition="true" compartment="cytosol" constant="true" id="TGFb_c"
                     initialConcentration="0.0659999824780232" metaid="metaid_0000041" name="TGFb_c">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000041">
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/P01137"/>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/P61812"/>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/P10600"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="R_act" initialConcentration="0" metaid="metaid_0000042" name="R_act">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000042">
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/P36897"/>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q8NER5"/>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q5T7S2"/>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/P37173"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="R" initialConcentration="1" metaid="metaid_0000043" name="R">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000043">
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/P36897"/>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q5T7S2"/>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q8NER5"/>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/P37173"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="cytosol" id="R_inact" initialConcentration="0" metaid="metaid_0000044" name="R_inact">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000044">
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/P36897"/>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q5T7S2"/>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q8NER5"/>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/P37173"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species boundaryCondition="true" compartment="cytosol" id="SB" initialConcentration="0"
                     metaid="metaid_0000045" name="SB-431542">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000045">
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0030291"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
        </listOfSpecies>
        <listOfParameters>
            <parameter id="kin" metaid="metaid_0000004" name="kin (import rate for monomeric Smads)" units="lps"
                       value="5.93E-15"/>
            <parameter id="kex" metaid="metaid_0000005" name="kex (export rate for monomeric Smads)" units="lps"
                       value="1.26E-14"/>
            <parameter id="kphos" metaid="metaid_0000006" name="kphos (phosphorylation rate)" units="pnMps"
                       value="0.0004037081673984"/>
            <parameter id="kdephos" metaid="metaid_0000007" name="kdephos (dephosphorylation rate)" units="pnMps"
                       value="0.00656639"/>
            <parameter id="kin_CIF" metaid="metaid_0000008" name="kin*CIF (Complex import rate)" units="lps"
                       value="3.36347821E-14"/>
            <parameter id="kon" metaid="metaid_0000009" name="kon (Smad complex on-rate)" units="pnMps"
                       value="0.00183925592901392"/>
            <parameter id="koff" metaid="metaid_0000010" name="koff (Smad complex off-rate)" units="ps" value="0.016"/>
            <parameter constant="false" id="CIF" metaid="metaid_0000011" name="CIF (complex import factor)"
                       units="dimensionless" value="5.67197"/>
            <parameter constant="false" id="K_diss" metaid="metaid_0000012"
                       name="Kdiss (dissociation constant of Smad complexes)" units="nM" value="8.69917"/>
            <parameter id="kon_SB" metaid="metaid_0000013" name="kon_SB (on-rate of the SB/receptor interaction)"
                       units="pnMps" value="0.146422317103884"/>
            <parameter id="koff_SB" metaid="metaid_0000014" name="koff_SB (off-rate of the SB/receptor interaction)"
                       units="ps" value="100"/>
            <parameter id="k_TGFb" metaid="metaid_0000015" name="k_TGFb (rate of TGFb binding to receptors)"
                       units="pnMps" value="0.07423555020288"/>
            <parameter constant="false" id="K_dissSB" metaid="metaid_0000016"
                       name="Kdiss SB (dissociation constant of the SB/receptor interaction)" units="nM"
                       value="682.956"/>
            <parameter id="ntoN" metaid="metaid_0000017" name="quantity to number factor" units="dimensionless"
                       value="6.0221415E14"/>
            <parameter id="SB_0" metaid="metaid_0000150" name="SB conc at start" units="nM" value="0"/>
            <parameter id="SB_add" metaid="metaid_0000151" name="SB conc after addition" units="nM" value="10000"/>
            <parameter id="t_SB" metaid="metaid_0000152" name="time of SB addition" units="time" value="2700"/>
        </listOfParameters>
        <listOfRules>
            <assignmentRule metaid="metaid_0000046" variable="CIF">
                <math xmlns="http://www.w3.org/1998/Math/MathML">
                    <apply>
                        <divide/>
                        <ci>kin_CIF</ci>
                        <ci>kin</ci>
                    </apply>
                </math>
            </assignmentRule>
            <assignmentRule metaid="metaid_0000047" variable="K_diss">
                <math xmlns="http://www.w3.org/1998/Math/MathML">
                    <apply>
                        <divide/>
                        <ci>koff</ci>
                        <ci>kon</ci>
                    </apply>
                </math>
            </assignmentRule>
            <assignmentRule metaid="metaid_0000048" variable="K_dissSB">
                <math xmlns="http://www.w3.org/1998/Math/MathML">
                    <apply>
                        <divide/>
                        <ci>koff_SB</ci>
                        <ci>kon_SB</ci>
                    </apply>
                </math>
            </assignmentRule>
            <assignmentRule metaid="metaid_0000080" variable="SB">
                <math xmlns="http://www.w3.org/1998/Math/MathML">
                    <piecewise>
                        <piece>
                            <ci>SB_add</ci>
                            <apply>
                                <gt/>
                                <csymbol encoding="text" definitionURL="http://www.sbml.org/sbml/symbols/time">time
                                </csymbol>
                                <ci>t_SB</ci>
                            </apply>
                        </piece>
                        <otherwise>
                            <ci>SB_0</ci>
                        </otherwise>
                    </piecewise>
                </math>
            </assignmentRule>
        </listOfRules>
        <listOfReactions>
            <reaction id="reaction_1" metaid="metaid_0000049" name="Reaction  7 Shuttling S4">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000049">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006913"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_38b94ff8-083f-410d-ad38-36762d73b9ab" species="S4_c"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="fc96414e-e0cd-41d8-a846-dacd6adef006" species="S4_n"/>
                </listOfProducts>
                <kineticLaw metaid="_6b5dcb20-a036-4585-a74c-e98f5c319648">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <minus/>
                            <apply>
                                <times/>
                                <ci>kin</ci>
                                <ci>S4_c</ci>
                            </apply>
                            <apply>
                                <times/>
                                <ci>kin</ci>
                                <ci>S4_n</ci>
                            </apply>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_2" metaid="metaid_0000050" name="Reaction  5A Shuttling S2">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000050">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006913"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_0d4c057c-bf54-4011-8c0d-72f64b80c3c5" species="S2_c"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_5d7e3e56-30f7-49d0-8b0c-f928f85c0d92" species="S2_n"/>
                </listOfProducts>
                <kineticLaw metaid="c53a923c-cb84-4eb6-a344-a8231400c574">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <minus/>
                            <apply>
                                <times/>
                                <ci>kin</ci>
                                <ci>S2_c</ci>
                            </apply>
                            <apply>
                                <times/>
                                <ci>kex</ci>
                                <ci>S2_n</ci>
                            </apply>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_3" metaid="metaid_0000051" name="Reaction  6A Shuttling pS2">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000051">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006913"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_6384975d-4edd-44d7-bcd5-07b714a197bb" species="pS2_c"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="a0fdea59-8f44-4c11-af2f-758a712f045c" species="pS2_n"/>
                </listOfProducts>
                <kineticLaw metaid="_2e007756-e1cf-4c39-8903-b39bbbcd68e5">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <minus/>
                            <apply>
                                <times/>
                                <ci>kin</ci>
                                <ci>pS2_c</ci>
                            </apply>
                            <apply>
                                <times/>
                                <ci>kex</ci>
                                <ci>pS2_n</ci>
                            </apply>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_4" metaid="metaid_0000052" name="Reaction  2A Phosphorylation S2" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000052">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/2.7.11.30"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0004675"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="f6ed77ff-3d9e-485b-adf2-c58a5d9a4f02" species="R_act"/>
                    <speciesReference metaid="_3c199960-dc1b-41c0-8578-12657b0c8472" species="S2_c"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_3dfa3bb4-a31b-40f7-abd1-0026bf5af2d2" species="R_act"/>
                    <speciesReference metaid="_6462aee2-9641-4931-b83f-07dcec3f1682" species="pS2_c"/>
                </listOfProducts>
                <kineticLaw metaid="_8193bf55-6cf0-455a-8c60-966750f6886b">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>cytosol</ci>
                            <ci>kphos</ci>
                            <ci>R_act</ci>
                            <ci>S2_c</ci>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_5" metaid="metaid_0000053" name="Reaction  3A Formation S24_C">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000053">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006461"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_4fbda0bb-a12d-410e-8221-e17bb56d19d4" species="pS2_c"/>
                    <speciesReference metaid="_59cf8dee-0a19-472d-94ce-716028bd3e11" species="S4_c"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="db096b85-7fd7-46fc-b1d4-f3523744c462" species="S24_c"/>
                </listOfProducts>
                <kineticLaw metaid="_3525385a-733a-4585-b1ef-84337b6b6f7a">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>cytosol</ci>
                            <apply>
                                <minus/>
                                <apply>
                                    <times/>
                                    <ci>kon</ci>
                                    <ci>pS2_c</ci>
                                    <ci>S4_c</ci>
                                </apply>
                                <apply>
                                    <times/>
                                    <ci>koff</ci>
                                    <ci>S24_c</ci>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_6" metaid="metaid_0000054" name="Reaction  3B Formation S24_N">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000054">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006461"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_429fd6d7-06c2-41ee-a648-8ce553b08ae1" species="pS2_n"/>
                    <speciesReference metaid="b7dfaffc-23ef-48eb-8229-f0558ee70698" species="S4_n"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_0788fed0-eed3-41df-90f7-18b85069e335" species="S24_n"/>
                </listOfProducts>
                <kineticLaw metaid="_8c528b55-ddd5-45c0-8433-6b71e3f65ac0">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>nucleus</ci>
                            <apply>
                                <minus/>
                                <apply>
                                    <times/>
                                    <ci>kon</ci>
                                    <ci>pS2_n</ci>
                                    <ci>S4_n</ci>
                                </apply>
                                <apply>
                                    <times/>
                                    <ci>koff</ci>
                                    <ci>S24_n</ci>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_7" metaid="metaid_0000055" name="Reaction  8A Import S24" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000055">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006913"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_8772a0bd-38c3-40e0-96f2-aa5936580c01" species="S24_c"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="e2ed3a76-0ff1-49c4-a516-ff0444a486b6" species="S24_n"/>
                </listOfProducts>
                <kineticLaw metaid="_6b944c07-8f78-4757-b28d-961c217653ee">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>kin_CIF</ci>
                            <ci>S24_c</ci>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_8" metaid="metaid_0000056" name="Reaction  9A Import S22" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000056">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006913"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_51694bb7-cb6f-45f6-8c20-b5dd6078fad3" species="S22_c"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="eaae53bc-a8d5-4989-85b1-e3fca64e45ab" species="S22_n"/>
                </listOfProducts>
                <kineticLaw metaid="a41aeccf-887e-4d08-a174-3a77b1639f61">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>kin_CIF</ci>
                            <ci>S22_c</ci>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_9" metaid="metaid_0000057" name="Reaction  4A Formation S22_C">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000057">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006461"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_5f445ae4-a1a0-4b54-a82d-c6cef412d1a8" species="pS2_c" stoichiometry="2"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_17b7e69d-8ad7-44f6-97c5-28e59b91a187" species="S22_c"/>
                </listOfProducts>
                <kineticLaw metaid="_7d78c9d7-faae-46d3-8107-aa2aab7bca1f">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>cytosol</ci>
                            <apply>
                                <minus/>
                                <apply>
                                    <times/>
                                    <ci>kon</ci>
                                    <ci>pS2_c</ci>
                                    <ci>pS2_c</ci>
                                </apply>
                                <apply>
                                    <times/>
                                    <ci>koff</ci>
                                    <ci>S22_c</ci>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_10" metaid="metaid_0000058" name="Reaction  4B Formation S22_N">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000058">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006461"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_8040950c-5d68-4811-978b-52c85e30c04f" species="pS2_n" stoichiometry="2"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_02898ee0-acef-4524-9c51-f1951ef82ab8" species="S22_n"/>
                </listOfProducts>
                <kineticLaw metaid="b3dc87af-e43d-44b6-8c94-5db18f8f7e8e">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>nucleus</ci>
                            <apply>
                                <minus/>
                                <apply>
                                    <times/>
                                    <ci>kon</ci>
                                    <ci>pS2_n</ci>
                                    <ci>pS2_n</ci>
                                </apply>
                                <apply>
                                    <times/>
                                    <ci>koff</ci>
                                    <ci>S22_n</ci>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_11" metaid="metaid_0000059" name="Reaction 10A Dephos pS2 Nuc" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000059">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/3.1.3.16"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0004722"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_3320570d-2a80-4987-8351-b1640328996c" species="pS2_n"/>
                    <speciesReference metaid="ce86e9db-dd3c-4d26-99b3-b2b48d509d8b" species="PPase"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_433d3a51-64cc-4006-89d6-fdfcb7576574" species="S2_n"/>
                    <speciesReference metaid="_91100ebe-fc6c-445f-a251-8e30f2352bdb" species="PPase"/>
                </listOfProducts>
                <kineticLaw metaid="af71eb4a-c051-4674-b586-c077f172192a">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>nucleus</ci>
                            <ci>kdephos</ci>
                            <ci>pS2_n</ci>
                            <ci>PPase</ci>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_12" metaid="metaid_0000060" name="Reaction  1 TGFb Binding" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000060">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0005160"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_8ea35766-3c44-410f-8d3b-d8b35a91e7b6" species="R"/>
                    <speciesReference metaid="_1be23530-46f4-4fb6-b5a6-0dcb3911bf32" species="TGFb_c"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_5c62eb5a-e3d0-4f82-8879-465273543646" species="R_act"/>
                </listOfProducts>
                <kineticLaw metaid="_6eb99581-b2bb-42a2-afc3-9cbaae82bcf2">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>cytosol</ci>
                            <ci>k_TGFb</ci>
                            <ci>R</ci>
                            <ci>TGFb_c</ci>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_13" metaid="metaid_0000061" name="Reaction 11 Receptor Inhibition">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000061">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0030512"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="f9d04e9a-0909-41aa-816d-f43728663d0a" species="R_act"/>
                    <speciesReference metaid="_804466ce-c854-462b-9427-9af0fecc209a" species="SB"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_90f4980d-7b34-48ad-87e5-4ea4b727b8ad" species="R_inact"/>
                </listOfProducts>
                <kineticLaw metaid="_47fd09e4-7ab1-4d0b-9bee-4599081fec26">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>cytosol</ci>
                            <apply>
                                <minus/>
                                <apply>
                                    <times/>
                                    <ci>kon_SB</ci>
                                    <ci>R_act</ci>
                                    <ci>SB</ci>
                                </apply>
                                <apply>
                                    <times/>
                                    <ci>koff_SB</ci>
                                    <ci>R_inact</ci>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_14" metaid="metaid_0000062" name="Reaction  2B Phosphorylation GS2"
                      reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000062">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/2.7.11.30"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0004675"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_736a7ad0-2ba1-4f3b-9f98-1619a7a40a83" species="G_c"/>
                    <speciesReference metaid="c40e0c23-ddc8-4975-a1c6-892b13b3ee98" species="R_act"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="d7a8e8d9-6ce1-47b4-8825-dbd14888105e" species="pG_c"/>
                    <speciesReference metaid="_9b04a04f-745d-4c60-83cc-e366c89b32af" species="R_act"/>
                </listOfProducts>
                <kineticLaw metaid="_62a4da6d-2a51-41b4-ae16-9e74994d9e25">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>cytosol</ci>
                            <ci>kphos</ci>
                            <ci>G_c</ci>
                            <ci>R_act</ci>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_15" metaid="metaid_0000063" name="Reaction 10B Dephos pG Nuc" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000063">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/3.1.3.16"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0004722"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_6c2b631e-247e-4c13-b3c3-5aa3aa1f904d" species="pG_n"/>
                    <speciesReference metaid="_60031dcf-6ae7-439f-86af-da32c1096cd2" species="PPase"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="dffa51be-b6d4-482b-b29d-5df13c5eb92c" species="G_n"/>
                    <speciesReference metaid="_9277150a-1bea-4bf5-9480-a776d62795ea" species="PPase"/>
                </listOfProducts>
                <kineticLaw metaid="d32bb810-d3de-48b8-b2a3-14c1d22a448b">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>nucleus</ci>
                            <ci>kdephos</ci>
                            <ci>pG_n</ci>
                            <ci>PPase</ci>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_16" metaid="metaid_0000064" name="Reaction  5B Shuttling G">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000064">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006913"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="a1d9d886-398f-46f3-804d-aa7ba7ddf907" species="G_c"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_98b22d86-0792-4a1a-8615-6465c393a445" species="G_n"/>
                </listOfProducts>
                <kineticLaw metaid="c531fe8b-60df-4768-bc17-1b87703ccf57">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <minus/>
                            <apply>
                                <times/>
                                <ci>kin</ci>
                                <ci>G_c</ci>
                            </apply>
                            <apply>
                                <times/>
                                <ci>kex</ci>
                                <ci>G_n</ci>
                            </apply>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_17" metaid="metaid_0000065" name="Reaction  6B Shuttling pG">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000065">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006913"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="d040713f-8cde-4155-b530-dfd86c424315" species="pG_c"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="bbdf78cb-7505-49b9-bafa-4cec2c3007c3" species="pG_n"/>
                </listOfProducts>
                <kineticLaw metaid="_568afc85-a7f8-42d8-ad37-8f8472a13ddb">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <minus/>
                            <apply>
                                <times/>
                                <ci>kin</ci>
                                <ci>pG_c</ci>
                            </apply>
                            <apply>
                                <times/>
                                <ci>kex</ci>
                                <ci>pG_n</ci>
                            </apply>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_18" metaid="metaid_0000066" name="Reaction  4E Formation GG_C">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000066">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006461"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_868bc50e-31d4-43af-8a73-5ee8826e7d2d" species="pG_c" stoichiometry="2"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_728006e4-575c-4c39-a43b-18270b7e1f47" species="GG_c"/>
                </listOfProducts>
                <kineticLaw metaid="_457306f7-e227-4a7c-88da-31ab026ea7dc">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>cytosol</ci>
                            <apply>
                                <minus/>
                                <apply>
                                    <times/>
                                    <ci>kon</ci>
                                    <ci>pG_c</ci>
                                    <ci>pG_c</ci>
                                </apply>
                                <apply>
                                    <times/>
                                    <ci>koff</ci>
                                    <ci>GG_c</ci>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_19" metaid="metaid_0000067" name="Reaction  4F Formation GG_N">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000067">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006461"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_5785a4c5-e196-408b-b2e6-0db7561e4137" species="pG_n" stoichiometry="2"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_0d1ecbf8-50d7-400a-8058-cbc1cce2b4c1" species="GG_n"/>
                </listOfProducts>
                <kineticLaw metaid="a8943f93-bc54-42e2-845c-f87b1a3273cb">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>nucleus</ci>
                            <apply>
                                <minus/>
                                <apply>
                                    <times/>
                                    <ci>kon</ci>
                                    <ci>pG_n</ci>
                                    <ci>pG_n</ci>
                                </apply>
                                <apply>
                                    <times/>
                                    <ci>koff</ci>
                                    <ci>GG_n</ci>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_20" metaid="metaid_0000068" name="Reaction  4C Formation G2_C">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000068">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006461"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_5ec949b7-248c-45f0-91f7-8beb17fe41ef" species="pS2_c"/>
                    <speciesReference metaid="_97615f78-067a-47fe-b463-d9f5b11f80fd" species="pG_c"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_62324dea-5131-462e-ae7c-58975e47ca25" species="G2_c"/>
                </listOfProducts>
                <kineticLaw metaid="_8bc8ae39-9a3a-40c0-b260-0b97cef894c8">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>cytosol</ci>
                            <apply>
                                <minus/>
                                <apply>
                                    <times/>
                                    <ci>kon</ci>
                                    <ci>pS2_c</ci>
                                    <ci>pG_c</ci>
                                </apply>
                                <apply>
                                    <times/>
                                    <ci>koff</ci>
                                    <ci>G2_c</ci>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_21" metaid="metaid_0000069" name="Reaction  4D Formation G2_N">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000069">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006461"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_30fa9278-8968-43e8-a868-9bebd124b6d2" species="pS2_n"/>
                    <speciesReference metaid="_3457fb21-78dd-489c-b8d5-bbe6f5959654" species="pG_n"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="e00de826-3f49-417a-8b1b-f095e8c59bc4" species="G2_n"/>
                </listOfProducts>
                <kineticLaw metaid="a1b16470-47da-421a-b686-9ef11f1217d2">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>nucleus</ci>
                            <apply>
                                <minus/>
                                <apply>
                                    <times/>
                                    <ci>kon</ci>
                                    <ci>pS2_n</ci>
                                    <ci>pG_n</ci>
                                </apply>
                                <apply>
                                    <times/>
                                    <ci>koff</ci>
                                    <ci>G2_n</ci>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_22" metaid="metaid_0000070" name="Reaction  3C Formation G4_C">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000070">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006461"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_50d98ff4-1b1f-4386-8cd8-ba75d37a70d9" species="pG_c"/>
                    <speciesReference metaid="a55ec7a5-feed-421e-a897-9a634e015961" species="S4_c"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_97bfdb70-8685-475a-99e6-87e3233b105d" species="G4_c"/>
                </listOfProducts>
                <kineticLaw metaid="_2cad13ee-65d6-44fe-be90-510c3faab8ea">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>cytosol</ci>
                            <apply>
                                <minus/>
                                <apply>
                                    <times/>
                                    <ci>kon</ci>
                                    <ci>pG_c</ci>
                                    <ci>S4_c</ci>
                                </apply>
                                <apply>
                                    <times/>
                                    <ci>koff</ci>
                                    <ci>G4_c</ci>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_23" metaid="metaid_0000071" name="Reaction  3D Formation G4_N">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000071">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006461"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_0cc5a807-0b4e-4d2a-9500-0c261f0e2e3b" species="pG_n"/>
                    <speciesReference metaid="_62ec5d1c-128d-4147-bb4a-ab5872817284" species="S4_n"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_2ea16736-4fc0-4702-b0ec-fa1763ca4959" species="G4_n"/>
                </listOfProducts>
                <kineticLaw metaid="f411c22e-08e1-4e10-8395-a90afd41c0e3">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>nucleus</ci>
                            <apply>
                                <minus/>
                                <apply>
                                    <times/>
                                    <ci>kon</ci>
                                    <ci>pG_n</ci>
                                    <ci>S4_n</ci>
                                </apply>
                                <apply>
                                    <times/>
                                    <ci>koff</ci>
                                    <ci>G4_n</ci>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_24" metaid="metaid_0000072" name="Reaction  9C Import GG" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000072">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006913"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_6c12a218-12e4-4380-89b4-2990f6777953" species="GG_c"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_9308a207-db12-4082-a561-b9ead3c2b87b" species="GG_n"/>
                </listOfProducts>
                <kineticLaw metaid="fe7e67f6-e417-4873-9506-994fdeebd578">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>kin_CIF</ci>
                            <ci>GG_c</ci>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_25" metaid="metaid_0000073" name="Reaction  9B Import G2" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000073">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006913"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_10152cff-3069-45e8-9477-674d358f1407" species="G2_c"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="e087acb1-f3fa-4e74-bbb1-bb2789331a2f" species="G2_n"/>
                </listOfProducts>
                <kineticLaw metaid="de1d4551-2816-419e-853c-64155ce2304e">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>kin_CIF</ci>
                            <ci>G2_c</ci>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
            <reaction id="reaction_26" metaid="metaid_0000074" name="Reaction  8B Import G4" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#metaid_0000074">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006913"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_2cefdf90-1e6d-4802-9425-163caa526058" species="G4_c"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="a78e5dd3-4e13-4365-865f-e896141b30c0" species="G4_n"/>
                </listOfProducts>
                <kineticLaw metaid="_64b7a72e-bd7b-49cb-a4f2-9f9e444c749d">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <times/>
                            <ci>kin_CIF</ci>
                            <ci>G4_c</ci>
                        </apply>
                    </math>
                </kineticLaw>
            </reaction>
        </listOfReactions>
    </model>
</sbml>
"""

compartment_model = """<?xml version="1.0" encoding="UTF-8"?>
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

kholodenko2000 = """<?xml version='1.0' encoding='UTF-8' standalone='no'?>
<!-- This model was downloaded from BioModels Database -->
<!-- http://www.ebi.ac.uk/biomodels-static/                   -->
<!-- Fri Jan 24 19:16:57 GMT 2020                      -->
<sbml xmlns="http://www.sbml.org/sbml/level2/version4" level="2" metaid="_492719" version="4">
    <model id="BIOMD0000000010" metaid="_000001"
           name="Kholodenko2000 - Ultrasensitivity and negative feedback bring oscillations in MAPK cascade">
        <notes>
            <body xmlns="http://www.w3.org/1999/xhtml">
                <div class="dc:title">Kholodenko2000 - Ultrasensitivity and negative feedback bring oscillations in MAPK
                    cascade
                </div>
                <div class="dc:description">
                    <p>The combination of ultrasensitivity and negative feedback bring sustained oscillations in the
                        mitogen-activated protein kinase cascades.
                    </p>
                </div>
                <div class="dc:bibliographicCitation">
                    <p>This model is described in the article:</p>
                    <div class="bibo:title">
                        <a href="http://identifiers.org/pubmed/10712587" title="Access to this publication">Negative
                            feedback and ultrasensitivity can bring about oscillations in the mitogen-activated protein
                            kinase cascades.
                        </a>
                    </div>
                    <div class="bibo:authorList">Kholodenko BN</div>
                    <div class="bibo:Journal">Eur. J. Biochem. 2000; 267(6):1583-8</div>
                    <p>Abstract:</p>
                    <div class="bibo:abstract">
                        <p>Functional organization of signal transduction into protein phosphorylation cascades, such as
                            the mitogen-activated protein kinase (MAPK) cascades, greatly enhances the sensitivity of
                            cellular targets to external stimuli. The sensitivity increases multiplicatively with the
                            number of cascade levels, so that a tiny change in a stimulus results in a large change in
                            the response, the phenomenon referred to as ultrasensitivity. In a variety of cell types,
                            the MAPK cascades are imbedded in long feedback loops, positive or negative, depending on
                            whether the terminal kinase stimulates or inhibits the activation of the initial level. Here
                            we demonstrate that a negative feedback loop combined with intrinsic ultrasensitivity of the
                            MAPK cascade can bring about sustained oscillations in MAPK phosphorylation. Based on recent
                            kinetic libs on the MAPK cascades, we predict that the period of oscillations can range from
                            minutes to hours. The phosphorylation level can vary between the base level and almost 100%
                            of the total protein. The oscillations of the phosphorylation cascades and slow protein
                            diffusion in the cytoplasm can lead to intracellular waves of phospho-proteins.
                        </p>
                    </div>
                </div>
                <div class="dc:publisher">
                    <p>This model is hosted on        <a href="http://www.ebi.ac.uk/biomodels/">BioModels Database</a>            and
                        identified by:        <a href="http://identifiers.org/biomodels.db/BIOMD0000000010">
                            BIOMD0000000010
                        </a>            .
                    </p>
                    <p>To cite BioModels Database, please use:        <a href="http://identifiers.org/pubmed/20587024"
                                                                         title="Latest BioModels Database publication">
                        BioModels Database: An enhanced, curated and annotated resource for published quantitative
                        kinetic models
                    </a>            .
                    </p>
                </div>
                <div class="dc:license">
                    <p>To the extent possible under law, all copyright and related or neighbouring rights to this
                        encoded model have been dedicated to the public domain worldwide. Please refer to        <a
                                href="http://creativecommons.org/publicdomain/zero/1.0/"
                                title="Access to: CC0 1.0 Universal (CC0 1.0), Public Domain Dedication">CC0 Public
                            Domain Dedication
                        </a>            for more information.
                    </p>
                </div>
            </body>
        </notes>
        <annotation>
            <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dc="http://purl.org/dc/elements/1.1/"
                     xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:dcterms="http://purl.org/dc/terms/"
                     xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                     xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                <rdf:Description rdf:about="#_000001">
                    <dc:creator>
                        <rdf:Bag>
                            <rdf:li rdf:parseType="Resource">
                                <vCard:N rdf:parseType="Resource">
                                    <vCard:Family>Sauro</vCard:Family>
                                    <vCard:Given>Herbert</vCard:Given>
                                </vCard:N>
                                <vCard:EMAIL>Herbert_Sauro@kgi.edu</vCard:EMAIL>
                                <vCard:ORG rdf:parseType="Resource">
                                    <vCard:Orgname>Keck Graduate Institute</vCard:Orgname>
                                </vCard:ORG>
                            </rdf:li>
                        </rdf:Bag>
                    </dc:creator>
                    <dcterms:created rdf:parseType="Resource">
                        <dcterms:W3CDTF>2005-02-12T00:18:12Z</dcterms:W3CDTF>
                    </dcterms:created>
                    <dcterms:modified rdf:parseType="Resource">
                        <dcterms:W3CDTF>2015-06-02T12:04:33Z</dcterms:W3CDTF>
                    </dcterms:modified>
                    <bqmodel:is>
                        <rdf:Bag>
                            <rdf:li rdf:resource="http://identifiers.org/biomodels.db/MODEL6615119181"/>
                        </rdf:Bag>
                    </bqmodel:is>
                    <bqmodel:is>
                        <rdf:Bag>
                            <rdf:li rdf:resource="http://identifiers.org/biomodels.db/BIOMD0000000010"/>
                        </rdf:Bag>
                    </bqmodel:is>
                    <bqmodel:isDescribedBy>
                        <rdf:Bag>
                            <rdf:li rdf:resource="http://identifiers.org/pubmed/10712587"/>
                        </rdf:Bag>
                    </bqmodel:isDescribedBy>
                    <bqbiol:isVersionOf>
                        <rdf:Bag>
                            <rdf:li rdf:resource="http://identifiers.org/go/GO:0000165"/>
                        </rdf:Bag>
                    </bqbiol:isVersionOf>
                    <bqbiol:isHomologTo>
                        <rdf:Bag>
                            <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_634"/>
                        </rdf:Bag>
                    </bqbiol:isHomologTo>
                    <bqbiol:hasTaxon>
                        <rdf:Bag>
                            <rdf:li rdf:resource="http://identifiers.org/taxonomy/8355"/>
                        </rdf:Bag>
                    </bqbiol:hasTaxon>
                </rdf:Description>
            </rdf:RDF>
        </annotation>
        <listOfUnitDefinitions>
            <unitDefinition id="substance" metaid="metaid_0000022" name="nanomole">
                <listOfUnits>
                    <unit kind="mole" metaid="_653149" scale="-9"/>
                </listOfUnits>
            </unitDefinition>
        </listOfUnitDefinitions>
        <listOfCompartments>
            <compartment id="uVol" metaid="_584463" size="1"/>
        </listOfCompartments>
        <listOfSpecies>
            <species compartment="uVol" id="MKKK" initialConcentration="90" metaid="_584475" name="Mos">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#_584475">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/P09560"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="uVol" id="MKKK_P" initialConcentration="10" metaid="_584495" name="Mos-P">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#_584495">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/P09560"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="uVol" id="MKK" initialConcentration="280" metaid="_584515" name="Mek1">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#_584515">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q05116"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="uVol" id="MKK_P" initialConcentration="10" metaid="_584535" name="Mek1-P">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#_584535">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q05116"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="uVol" id="MKK_PP" initialConcentration="10" metaid="_584555" name="Mek1-PP">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#_584555">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/Q05116"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="uVol" id="MAPK" initialConcentration="280" metaid="_584575" name="Erk2">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#_584575">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/P26696"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="uVol" id="MAPK_P" initialConcentration="10" metaid="_584595" name="Erk2-P">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#_584595">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/P26696"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
            <species compartment="uVol" id="MAPK_PP" initialConcentration="10" metaid="_584615" name="Erk2-PP">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#_584615">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/uniprot/P26696"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
            </species>
        </listOfSpecies>
        <listOfReactions>
            <reaction id="J0" metaid="_584635" name="MAPKKK activation" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#_584635">
                            <bqbiol:isHomologTo>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_525"/>
                                </rdf:Bag>
                            </bqbiol:isHomologTo>
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/2.7.11.1"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0000185"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0008349"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_653161" species="MKKK"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_653173" species="MKKK_P"/>
                </listOfProducts>
                <listOfModifiers>
                    <modifierSpeciesReference metaid="_653185" species="MAPK_PP"/>
                </listOfModifiers>
                <kineticLaw metaid="_653197">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <ci>uVol</ci>
                                <ci>V1</ci>
                                <ci>MKKK</ci>
                            </apply>
                            <apply>
                                <times/>
                                <apply>
                                    <plus/>
                                    <cn type="integer">1</cn>
                                    <apply>
                                        <power/>
                                        <apply>
                                            <divide/>
                                            <ci>MAPK_PP</ci>
                                            <ci>Ki</ci>
                                        </apply>
                                        <ci>n</ci>
                                    </apply>
                                </apply>
                                <apply>
                                    <plus/>
                                    <ci>K1</ci>
                                    <ci>MKKK</ci>
                                </apply>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="V1" metaid="_001327" value="2.5"/>
                        <parameter id="Ki" metaid="_001328" value="9"/>
                        <parameter id="n" metaid="_001329" value="1"/>
                        <parameter id="K1" metaid="_001331" value="10"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="J1" metaid="_584655" name="MAPKKK inactivation" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#_584655">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/3.1.3.16"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0051390"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006470"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_653209" species="MKKK_P"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_653221" species="MKKK"/>
                </listOfProducts>
                <kineticLaw metaid="_653233">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <ci>uVol</ci>
                                <ci>V2</ci>
                                <ci>MKKK_P</ci>
                            </apply>
                            <apply>
                                <plus/>
                                <ci>KK2</ci>
                                <ci>MKKK_P</ci>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="V2" metaid="_001333" value="0.25"/>
                        <parameter id="KK2" metaid="_001335" value="8"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="J2" metaid="_584675" name="phosphorylation of MAPKK" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#_584675">
                            <bqbiol:isHomologTo>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_614"/>
                                </rdf:Bag>
                            </bqbiol:isHomologTo>
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/2.7.11.25"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0004709"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006468"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_653245" species="MKK"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_653257" species="MKK_P"/>
                </listOfProducts>
                <listOfModifiers>
                    <modifierSpeciesReference metaid="_653269" species="MKKK_P"/>
                </listOfModifiers>
                <kineticLaw metaid="_653281">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <ci>uVol</ci>
                                <ci>k3</ci>
                                <ci>MKKK_P</ci>
                                <ci>MKK</ci>
                            </apply>
                            <apply>
                                <plus/>
                                <ci>KK3</ci>
                                <ci>MKK</ci>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="k3" metaid="_001337" value="0.025"/>
                        <parameter id="KK3" metaid="_001339" value="15"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="J3" metaid="_584695" name="phosphorylation of MAPKK-P" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#_584695">
                            <bqbiol:isHomologTo>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_614"/>
                                </rdf:Bag>
                            </bqbiol:isHomologTo>
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/2.7.11.25"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0000186"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006468"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0004709"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_653293" species="MKK_P"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_653305" species="MKK_PP"/>
                </listOfProducts>
                <listOfModifiers>
                    <modifierSpeciesReference metaid="_653317" species="MKKK_P"/>
                </listOfModifiers>
                <kineticLaw metaid="_653329">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <ci>uVol</ci>
                                <ci>k4</ci>
                                <ci>MKKK_P</ci>
                                <ci>MKK_P</ci>
                            </apply>
                            <apply>
                                <plus/>
                                <ci>KK4</ci>
                                <ci>MKK_P</ci>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="k4" metaid="_001341" value="0.025"/>
                        <parameter id="KK4" metaid="_001343" value="15"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="J4" metaid="_584715" name="dephosphorylation of MAPKK-PP" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#_584715">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/3.1.3.16"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006470"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0051389"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_653341" species="MKK_PP"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_653353" species="MKK_P"/>
                </listOfProducts>
                <kineticLaw metaid="_653365">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <ci>uVol</ci>
                                <ci>V5</ci>
                                <ci>MKK_PP</ci>
                            </apply>
                            <apply>
                                <plus/>
                                <ci>KK5</ci>
                                <ci>MKK_PP</ci>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="V5" metaid="_001345" value="0.75"/>
                        <parameter id="KK5" metaid="_001347" value="15"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="J5" metaid="_584735" name="dephosphorylation of MAPKK-P" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#_584735">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/3.1.3.16"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006470"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_653377" species="MKK_P"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_653389" species="MKK"/>
                </listOfProducts>
                <kineticLaw metaid="_653402">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <ci>uVol</ci>
                                <ci>V6</ci>
                                <ci>MKK_P</ci>
                            </apply>
                            <apply>
                                <plus/>
                                <ci>KK6</ci>
                                <ci>MKK_P</ci>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="V6" metaid="_001349" value="0.75"/>
                        <parameter id="KK6" metaid="_001351" value="15"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="J6" metaid="_584755" name="phosphorylation of MAPK" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#_584755">
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_136"/>
                                    <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_2247"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/2.7.12.2"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0004708"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006468"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_653414" species="MAPK"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_653426" species="MAPK_P"/>
                </listOfProducts>
                <listOfModifiers>
                    <modifierSpeciesReference metaid="_653438" species="MKK_PP"/>
                </listOfModifiers>
                <kineticLaw metaid="_653450">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <ci>uVol</ci>
                                <ci>k7</ci>
                                <ci>MKK_PP</ci>
                                <ci>MAPK</ci>
                            </apply>
                            <apply>
                                <plus/>
                                <ci>KK7</ci>
                                <ci>MAPK</ci>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="k7" metaid="_001353" value="0.025"/>
                        <parameter id="KK7" metaid="_001355" value="15"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="J7" metaid="_584775" name="phosphorylation of MAPK-P" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#_584775">
                            <bqbiol:hasVersion>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_136"/>
                                    <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_2247"/>
                                </rdf:Bag>
                            </bqbiol:hasVersion>
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/2.7.12.2"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006468"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0004708"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0000187"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_653463" species="MAPK_P"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_653475" species="MAPK_PP"/>
                </listOfProducts>
                <listOfModifiers>
                    <modifierSpeciesReference metaid="_653487" species="MKK_PP"/>
                </listOfModifiers>
                <kineticLaw metaid="_653499">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <ci>uVol</ci>
                                <ci>k8</ci>
                                <ci>MKK_PP</ci>
                                <ci>MAPK_P</ci>
                            </apply>
                            <apply>
                                <plus/>
                                <ci>KK8</ci>
                                <ci>MAPK_P</ci>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="k8" metaid="_001357" value="0.025"/>
                        <parameter id="KK8" metaid="_001359" value="15"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="J8" metaid="_584795" name="dephosphorylation of MAPK-PP" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#_584795">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/3.1.3.16"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0000188"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006470"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_653511" species="MAPK_PP"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_653523" species="MAPK_P"/>
                </listOfProducts>
                <kineticLaw metaid="_653535">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <ci>uVol</ci>
                                <ci>V9</ci>
                                <ci>MAPK_PP</ci>
                            </apply>
                            <apply>
                                <plus/>
                                <ci>KK9</ci>
                                <ci>MAPK_PP</ci>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="V9" metaid="_001361" value="0.5"/>
                        <parameter id="KK9" metaid="_001363" value="15"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
            <reaction id="J9" metaid="_584815" name="dephosphorylation of MAPK-P" reversible="false">
                <annotation>
                    <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
                             xmlns:bqmodel="http://biomodels.net/model-qualifiers/"
                             xmlns:bqbiol="http://biomodels.net/biology-qualifiers/">
                        <rdf:Description rdf:about="#_584815">
                            <bqbiol:isVersionOf>
                                <rdf:Bag>
                                    <rdf:li rdf:resource="http://identifiers.org/ec-code/3.1.3.16"/>
                                    <rdf:li rdf:resource="http://identifiers.org/go/GO:0006470"/>
                                </rdf:Bag>
                            </bqbiol:isVersionOf>
                        </rdf:Description>
                    </rdf:RDF>
                </annotation>
                <listOfReactants>
                    <speciesReference metaid="_653547" species="MAPK_P"/>
                </listOfReactants>
                <listOfProducts>
                    <speciesReference metaid="_653559" species="MAPK"/>
                </listOfProducts>
                <kineticLaw metaid="_653571">
                    <math xmlns="http://www.w3.org/1998/Math/MathML">
                        <apply>
                            <divide/>
                            <apply>
                                <times/>
                                <ci>uVol</ci>
                                <ci>V10</ci>
                                <ci>MAPK_P</ci>
                            </apply>
                            <apply>
                                <plus/>
                                <ci>KK10</ci>
                                <ci>MAPK_P</ci>
                            </apply>
                        </apply>
                    </math>
                    <listOfParameters>
                        <parameter id="V10" metaid="_001365" value="0.5"/>
                        <parameter id="KK10" metaid="_001367" value="15"/>
                    </listOfParameters>
                </kineticLaw>
            </reaction>
        </listOfReactions>
    </model>
</sbml>
"""

teusink2000 = """<?xml version="1.0" encoding="UTF-8"?>
<sbml xmlns="http://www.sbml.org/sbml/level3/version1/core" level="3" version="1">
  <model metaid="Teusink2000_Glycolysis" id="Teusink2000_Glycolysis" name="Teusink2000_Glycolysis_1" substanceUnits="substance" timeUnits="time_unit">
    <annotation>
      <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
        <rdf:Description rdf:about="#Teusink2000_Glycolysis">
          <bqbiol:is>
            <rdf:Bag>
              <rdf:li rdf:resource="http://identifiers.org/biomodels.db/MODEL6623915522"/>
              <rdf:li rdf:resource="http://identifiers.org/biomodels.db/BIOMD0000000064"/>
              <rdf:li rdf:resource="http://identifiers.org/go/GO:0006096"/>
              <rdf:li rdf:resource="http://identifiers.org/kegg.pathway/sce00010"/>
            </rdf:Bag>
          </bqbiol:is>
          <bqbiol:isHomologTo>
            <rdf:Bag>
              <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_723"/>
            </rdf:Bag>
          </bqbiol:isHomologTo>
          <bqbiol:hasTaxon>
            <rdf:Bag>
              <rdf:li rdf:resource="http://identifiers.org/taxonomy/4932"/>
            </rdf:Bag>
          </bqbiol:hasTaxon>
          <bqbiol:isDescribedBy>
            <rdf:Bag>
              <rdf:li rdf:resource="http://identifiers.org/pubmed/10951190"/>
            </rdf:Bag>
          </bqbiol:isDescribedBy>
        </rdf:Description>
      </rdf:RDF>
    </annotation>
    <listOfFunctionDefinitions>
      <functionDefinition id="Constant_flux__irreversible" name="Constant flux (irreversible)">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <lambda>
            <bvar>
              <ci> v </ci>
            </bvar>
            <ci> v </ci>
          </lambda>
        </math>
      </functionDefinition>
      <functionDefinition id="Function_for_Alcohol_dehydrogenase" name="Function for Alcohol dehydrogenase">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <lambda>
            <bvar>
              <ci> ACE </ci>
            </bvar>
            <bvar>
              <ci> ETOH </ci>
            </bvar>
            <bvar>
              <ci> KeqADH </ci>
            </bvar>
            <bvar>
              <ci> KiADHACE </ci>
            </bvar>
            <bvar>
              <ci> KiADHETOH </ci>
            </bvar>
            <bvar>
              <ci> KiADHNAD </ci>
            </bvar>
            <bvar>
              <ci> KiADHNADH </ci>
            </bvar>
            <bvar>
              <ci> KmADHACE </ci>
            </bvar>
            <bvar>
              <ci> KmADHETOH </ci>
            </bvar>
            <bvar>
              <ci> KmADHNAD </ci>
            </bvar>
            <bvar>
              <ci> KmADHNADH </ci>
            </bvar>
            <bvar>
              <ci> NAD </ci>
            </bvar>
            <bvar>
              <ci> NADH </ci>
            </bvar>
            <bvar>
              <ci> VmADH </ci>
            </bvar>
            <bvar>
              <ci> cytosol </ci>
            </bvar>
            <apply>
              <divide/>
              <apply>
                <times/>
                <apply>
                  <minus/>
                  <ci> cytosol </ci>
                </apply>
                <apply>
                  <divide/>
                  <apply>
                    <times/>
                    <apply>
                      <divide/>
                      <ci> VmADH </ci>
                      <apply>
                        <times/>
                        <ci> KiADHNAD </ci>
                        <ci> KmADHETOH </ci>
                      </apply>
                    </apply>
                    <apply>
                      <minus/>
                      <apply>
                        <times/>
                        <ci> NAD </ci>
                        <ci> ETOH </ci>
                      </apply>
                      <apply>
                        <divide/>
                        <apply>
                          <times/>
                          <ci> NADH </ci>
                          <ci> ACE </ci>
                        </apply>
                        <ci> KeqADH </ci>
                      </apply>
                    </apply>
                  </apply>
                  <apply>
                    <plus/>
                    <cn type="integer"> 1 </cn>
                    <apply>
                      <divide/>
                      <ci> NAD </ci>
                      <ci> KiADHNAD </ci>
                    </apply>
                    <apply>
                      <divide/>
                      <apply>
                        <times/>
                        <ci> KmADHNAD </ci>
                        <ci> ETOH </ci>
                      </apply>
                      <apply>
                        <times/>
                        <ci> KiADHNAD </ci>
                        <ci> KmADHETOH </ci>
                      </apply>
                    </apply>
                    <apply>
                      <divide/>
                      <apply>
                        <times/>
                        <ci> KmADHNADH </ci>
                        <ci> ACE </ci>
                      </apply>
                      <apply>
                        <times/>
                        <ci> KiADHNADH </ci>
                        <ci> KmADHACE </ci>
                      </apply>
                    </apply>
                    <apply>
                      <divide/>
                      <ci> NADH </ci>
                      <ci> KiADHNADH </ci>
                    </apply>
                    <apply>
                      <divide/>
                      <apply>
                        <times/>
                        <ci> NAD </ci>
                        <ci> ETOH </ci>
                      </apply>
                      <apply>
                        <times/>
                        <ci> KiADHNAD </ci>
                        <ci> KmADHETOH </ci>
                      </apply>
                    </apply>
                    <apply>
                      <divide/>
                      <apply>
                        <times/>
                        <ci> KmADHNADH </ci>
                        <ci> NAD </ci>
                        <ci> ACE </ci>
                      </apply>
                      <apply>
                        <times/>
                        <ci> KiADHNAD </ci>
                        <ci> KiADHNADH </ci>
                        <ci> KmADHACE </ci>
                      </apply>
                    </apply>
                    <apply>
                      <divide/>
                      <apply>
                        <times/>
                        <ci> KmADHNAD </ci>
                        <ci> ETOH </ci>
                        <ci> NADH </ci>
                      </apply>
                      <apply>
                        <times/>
                        <ci> KiADHNAD </ci>
                        <ci> KmADHETOH </ci>
                        <ci> KiADHNADH </ci>
                      </apply>
                    </apply>
                    <apply>
                      <divide/>
                      <apply>
                        <times/>
                        <ci> NADH </ci>
                        <ci> ACE </ci>
                      </apply>
                      <apply>
                        <times/>
                        <ci> KiADHNADH </ci>
                        <ci> KmADHACE </ci>
                      </apply>
                    </apply>
                    <apply>
                      <divide/>
                      <apply>
                        <times/>
                        <ci> NAD </ci>
                        <ci> ETOH </ci>
                        <ci> ACE </ci>
                      </apply>
                      <apply>
                        <times/>
                        <ci> KiADHNAD </ci>
                        <ci> KmADHETOH </ci>
                        <ci> KiADHACE </ci>
                      </apply>
                    </apply>
                    <apply>
                      <divide/>
                      <apply>
                        <times/>
                        <ci> ETOH </ci>
                        <ci> NADH </ci>
                        <ci> ACE </ci>
                      </apply>
                      <apply>
                        <times/>
                        <ci> KiADHETOH </ci>
                        <ci> KiADHNADH </ci>
                        <ci> KmADHACE </ci>
                      </apply>
                    </apply>
                  </apply>
                </apply>
              </apply>
              <ci> cytosol </ci>
            </apply>
          </lambda>
        </math>
      </functionDefinition>
      <functionDefinition id="Function_for_Glycerol_3_phosphate_dehydrogenase" name="Function for Glycerol 3-phosphate dehydrogenase">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <lambda>
            <bvar>
              <ci> GLY </ci>
            </bvar>
            <bvar>
              <ci> KeqG3PDH </ci>
            </bvar>
            <bvar>
              <ci> KeqTPI </ci>
            </bvar>
            <bvar>
              <ci> KmG3PDHDHAP </ci>
            </bvar>
            <bvar>
              <ci> KmG3PDHGLY </ci>
            </bvar>
            <bvar>
              <ci> KmG3PDHNAD </ci>
            </bvar>
            <bvar>
              <ci> KmG3PDHNADH </ci>
            </bvar>
            <bvar>
              <ci> NAD </ci>
            </bvar>
            <bvar>
              <ci> NADH </ci>
            </bvar>
            <bvar>
              <ci> TRIO </ci>
            </bvar>
            <bvar>
              <ci> VmG3PDH </ci>
            </bvar>
            <apply>
              <divide/>
              <apply>
                <times/>
                <apply>
                  <divide/>
                  <ci> VmG3PDH </ci>
                  <apply>
                    <times/>
                    <ci> KmG3PDHDHAP </ci>
                    <ci> KmG3PDHNADH </ci>
                  </apply>
                </apply>
                <apply>
                  <minus/>
                  <apply>
                    <times/>
                    <apply>
                      <divide/>
                      <cn type="integer"> 1 </cn>
                      <apply>
                        <plus/>
                        <cn type="integer"> 1 </cn>
                        <ci> KeqTPI </ci>
                      </apply>
                    </apply>
                    <ci> TRIO </ci>
                    <ci> NADH </ci>
                  </apply>
                  <apply>
                    <divide/>
                    <apply>
                      <times/>
                      <ci> GLY </ci>
                      <ci> NAD </ci>
                    </apply>
                    <ci> KeqG3PDH </ci>
                  </apply>
                </apply>
              </apply>
              <apply>
                <times/>
                <apply>
                  <plus/>
                  <cn type="integer"> 1 </cn>
                  <apply>
                    <divide/>
                    <apply>
                      <times/>
                      <apply>
                        <divide/>
                        <cn type="integer"> 1 </cn>
                        <apply>
                          <plus/>
                          <cn type="integer"> 1 </cn>
                          <ci> KeqTPI </ci>
                        </apply>
                      </apply>
                      <ci> TRIO </ci>
                    </apply>
                    <ci> KmG3PDHDHAP </ci>
                  </apply>
                  <apply>
                    <divide/>
                    <ci> GLY </ci>
                    <ci> KmG3PDHGLY </ci>
                  </apply>
                </apply>
                <apply>
                  <plus/>
                  <cn type="integer"> 1 </cn>
                  <apply>
                    <divide/>
                    <ci> NADH </ci>
                    <ci> KmG3PDHNADH </ci>
                  </apply>
                  <apply>
                    <divide/>
                    <ci> NAD </ci>
                    <ci> KmG3PDHNAD </ci>
                  </apply>
                </apply>
              </apply>
            </apply>
          </lambda>
        </math>
      </functionDefinition>
      <functionDefinition id="R_PFK" name="R_PFK">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <lambda>
            <bvar>
              <ci> KmF6P </ci>
            </bvar>
            <bvar>
              <ci> KmATP </ci>
            </bvar>
            <bvar>
              <ci> g </ci>
            </bvar>
            <bvar>
              <ci> AT_ </ci>
            </bvar>
            <bvar>
              <ci> F6 </ci>
            </bvar>
            <apply>
              <plus/>
              <cn type="integer"> 1 </cn>
              <apply>
                <divide/>
                <ci> F6 </ci>
                <ci> KmF6P </ci>
              </apply>
              <apply>
                <divide/>
                <ci> AT_ </ci>
                <ci> KmATP </ci>
              </apply>
              <apply>
                <times/>
                <ci> g </ci>
                <apply>
                  <divide/>
                  <ci> F6 </ci>
                  <ci> KmF6P </ci>
                </apply>
                <apply>
                  <divide/>
                  <ci> AT_ </ci>
                  <ci> KmATP </ci>
                </apply>
              </apply>
            </apply>
          </lambda>
        </math>
      </functionDefinition>
      <functionDefinition id="T_PFK" name="T_PFK">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <lambda>
            <bvar>
              <ci> CATP </ci>
            </bvar>
            <bvar>
              <ci> KmATP </ci>
            </bvar>
            <bvar>
              <ci> AT_ </ci>
            </bvar>
            <apply>
              <plus/>
              <cn type="integer"> 1 </cn>
              <apply>
                <times/>
                <ci> CATP </ci>
                <apply>
                  <divide/>
                  <ci> AT_ </ci>
                  <ci> KmATP </ci>
                </apply>
              </apply>
            </apply>
          </lambda>
        </math>
      </functionDefinition>
      <functionDefinition id="L_PFK" name="L_PFK">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <lambda>
            <bvar>
              <ci> L </ci>
            </bvar>
            <bvar>
              <ci> CiATP </ci>
            </bvar>
            <bvar>
              <ci> KiATP </ci>
            </bvar>
            <bvar>
              <ci> CAMP </ci>
            </bvar>
            <bvar>
              <ci> KAMP </ci>
            </bvar>
            <bvar>
              <ci> CF26BP </ci>
            </bvar>
            <bvar>
              <ci> KF26BP </ci>
            </bvar>
            <bvar>
              <ci> CF16BP </ci>
            </bvar>
            <bvar>
              <ci> KF16BP </ci>
            </bvar>
            <bvar>
              <ci> AT_ </ci>
            </bvar>
            <bvar>
              <ci> AM </ci>
            </bvar>
            <bvar>
              <ci> F16 </ci>
            </bvar>
            <bvar>
              <ci> F26 </ci>
            </bvar>
            <apply>
              <times/>
              <ci> L </ci>
              <apply>
                <power/>
                <apply>
                  <divide/>
                  <apply>
                    <plus/>
                    <cn type="integer"> 1 </cn>
                    <apply>
                      <times/>
                      <ci> CiATP </ci>
                      <apply>
                        <divide/>
                        <ci> AT_ </ci>
                        <ci> KiATP </ci>
                      </apply>
                    </apply>
                  </apply>
                  <apply>
                    <plus/>
                    <cn type="integer"> 1 </cn>
                    <apply>
                      <divide/>
                      <ci> AT_ </ci>
                      <ci> KiATP </ci>
                    </apply>
                  </apply>
                </apply>
                <cn type="integer"> 2 </cn>
              </apply>
              <apply>
                <power/>
                <apply>
                  <divide/>
                  <apply>
                    <plus/>
                    <cn type="integer"> 1 </cn>
                    <apply>
                      <times/>
                      <ci> CAMP </ci>
                      <apply>
                        <divide/>
                        <ci> AM </ci>
                        <ci> KAMP </ci>
                      </apply>
                    </apply>
                  </apply>
                  <apply>
                    <plus/>
                    <cn type="integer"> 1 </cn>
                    <apply>
                      <divide/>
                      <ci> AM </ci>
                      <ci> KAMP </ci>
                    </apply>
                  </apply>
                </apply>
                <cn type="integer"> 2 </cn>
              </apply>
              <apply>
                <power/>
                <apply>
                  <divide/>
                  <apply>
                    <plus/>
                    <cn type="integer"> 1 </cn>
                    <apply>
                      <divide/>
                      <apply>
                        <times/>
                        <ci> CF26BP </ci>
                        <ci> F26 </ci>
                      </apply>
                      <ci> KF26BP </ci>
                    </apply>
                    <apply>
                      <divide/>
                      <apply>
                        <times/>
                        <ci> CF16BP </ci>
                        <ci> F16 </ci>
                      </apply>
                      <ci> KF16BP </ci>
                    </apply>
                  </apply>
                  <apply>
                    <plus/>
                    <cn type="integer"> 1 </cn>
                    <apply>
                      <divide/>
                      <ci> F26 </ci>
                      <ci> KF26BP </ci>
                    </apply>
                    <apply>
                      <divide/>
                      <ci> F16 </ci>
                      <ci> KF16BP </ci>
                    </apply>
                  </apply>
                </apply>
                <cn type="integer"> 2 </cn>
              </apply>
            </apply>
          </lambda>
        </math>
      </functionDefinition>
      <functionDefinition id="Function_for_Hexokinase" name="Function for Hexokinase">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <lambda>
            <bvar>
              <ci> ADP </ci>
            </bvar>
            <bvar>
              <ci> ATP </ci>
            </bvar>
            <bvar>
              <ci> G6P </ci>
            </bvar>
            <bvar>
              <ci> GLCi </ci>
            </bvar>
            <bvar>
              <ci> KeqGLK </ci>
            </bvar>
            <bvar>
              <ci> KmGLKADP </ci>
            </bvar>
            <bvar>
              <ci> KmGLKATP </ci>
            </bvar>
            <bvar>
              <ci> KmGLKG6P </ci>
            </bvar>
            <bvar>
              <ci> KmGLKGLCi </ci>
            </bvar>
            <bvar>
              <ci> VmGLK </ci>
            </bvar>
            <apply>
              <divide/>
              <apply>
                <times/>
                <apply>
                  <divide/>
                  <ci> VmGLK </ci>
                  <apply>
                    <times/>
                    <ci> KmGLKGLCi </ci>
                    <ci> KmGLKATP </ci>
                  </apply>
                </apply>
                <apply>
                  <minus/>
                  <apply>
                    <times/>
                    <ci> GLCi </ci>
                    <ci> ATP </ci>
                  </apply>
                  <apply>
                    <divide/>
                    <apply>
                      <times/>
                      <ci> G6P </ci>
                      <ci> ADP </ci>
                    </apply>
                    <ci> KeqGLK </ci>
                  </apply>
                </apply>
              </apply>
              <apply>
                <times/>
                <apply>
                  <plus/>
                  <cn type="integer"> 1 </cn>
                  <apply>
                    <divide/>
                    <ci> GLCi </ci>
                    <ci> KmGLKGLCi </ci>
                  </apply>
                  <apply>
                    <divide/>
                    <ci> G6P </ci>
                    <ci> KmGLKG6P </ci>
                  </apply>
                </apply>
                <apply>
                  <plus/>
                  <cn type="integer"> 1 </cn>
                  <apply>
                    <divide/>
                    <ci> ATP </ci>
                    <ci> KmGLKATP </ci>
                  </apply>
                  <apply>
                    <divide/>
                    <ci> ADP </ci>
                    <ci> KmGLKADP </ci>
                  </apply>
                </apply>
              </apply>
            </apply>
          </lambda>
        </math>
      </functionDefinition>
      <functionDefinition id="Function_for_Glucose_6_phosphate_isomerase" name="Function for Glucose-6-phosphate isomerase">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <lambda>
            <bvar>
              <ci> F6P </ci>
            </bvar>
            <bvar>
              <ci> G6P </ci>
            </bvar>
            <bvar>
              <ci> KeqPGI_2 </ci>
            </bvar>
            <bvar>
              <ci> KmPGIF6P_2 </ci>
            </bvar>
            <bvar>
              <ci> KmPGIG6P_2 </ci>
            </bvar>
            <bvar>
              <ci> VmPGI_2 </ci>
            </bvar>
            <apply>
              <divide/>
              <apply>
                <times/>
                <apply>
                  <divide/>
                  <ci> VmPGI_2 </ci>
                  <ci> KmPGIG6P_2 </ci>
                </apply>
                <apply>
                  <minus/>
                  <ci> G6P </ci>
                  <apply>
                    <divide/>
                    <ci> F6P </ci>
                    <ci> KeqPGI_2 </ci>
                  </apply>
                </apply>
              </apply>
              <apply>
                <plus/>
                <cn type="integer"> 1 </cn>
                <apply>
                  <divide/>
                  <ci> G6P </ci>
                  <ci> KmPGIG6P_2 </ci>
                </apply>
                <apply>
                  <divide/>
                  <ci> F6P </ci>
                  <ci> KmPGIF6P_2 </ci>
                </apply>
              </apply>
            </apply>
          </lambda>
        </math>
      </functionDefinition>
      <functionDefinition id="Function_for_Aldolase" name="Function for Aldolase">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <lambda>
            <bvar>
              <ci> F16P </ci>
            </bvar>
            <bvar>
              <ci> KeqALD </ci>
            </bvar>
            <bvar>
              <ci> KeqTPI </ci>
            </bvar>
            <bvar>
              <ci> KmALDDHAP </ci>
            </bvar>
            <bvar>
              <ci> KmALDF16P </ci>
            </bvar>
            <bvar>
              <ci> KmALDGAP </ci>
            </bvar>
            <bvar>
              <ci> KmALDGAPi </ci>
            </bvar>
            <bvar>
              <ci> TRIO </ci>
            </bvar>
            <bvar>
              <ci> VmALD </ci>
            </bvar>
            <apply>
              <divide/>
              <apply>
                <times/>
                <apply>
                  <divide/>
                  <ci> VmALD </ci>
                  <ci> KmALDF16P </ci>
                </apply>
                <apply>
                  <minus/>
                  <ci> F16P </ci>
                  <apply>
                    <divide/>
                    <apply>
                      <times/>
                      <apply>
                        <divide/>
                        <ci> KeqTPI </ci>
                        <apply>
                          <plus/>
                          <cn type="integer"> 1 </cn>
                          <ci> KeqTPI </ci>
                        </apply>
                      </apply>
                      <ci> TRIO </ci>
                      <apply>
                        <divide/>
                        <cn type="integer"> 1 </cn>
                        <apply>
                          <plus/>
                          <cn type="integer"> 1 </cn>
                          <ci> KeqTPI </ci>
                        </apply>
                      </apply>
                      <ci> TRIO </ci>
                    </apply>
                    <ci> KeqALD </ci>
                  </apply>
                </apply>
              </apply>
              <apply>
                <plus/>
                <cn type="integer"> 1 </cn>
                <apply>
                  <divide/>
                  <ci> F16P </ci>
                  <ci> KmALDF16P </ci>
                </apply>
                <apply>
                  <divide/>
                  <apply>
                    <times/>
                    <apply>
                      <divide/>
                      <ci> KeqTPI </ci>
                      <apply>
                        <plus/>
                        <cn type="integer"> 1 </cn>
                        <ci> KeqTPI </ci>
                      </apply>
                    </apply>
                    <ci> TRIO </ci>
                  </apply>
                  <ci> KmALDGAP </ci>
                </apply>
                <apply>
                  <divide/>
                  <apply>
                    <times/>
                    <apply>
                      <divide/>
                      <cn type="integer"> 1 </cn>
                      <apply>
                        <plus/>
                        <cn type="integer"> 1 </cn>
                        <ci> KeqTPI </ci>
                      </apply>
                    </apply>
                    <ci> TRIO </ci>
                  </apply>
                  <ci> KmALDDHAP </ci>
                </apply>
                <apply>
                  <divide/>
                  <apply>
                    <times/>
                    <apply>
                      <divide/>
                      <ci> KeqTPI </ci>
                      <apply>
                        <plus/>
                        <cn type="integer"> 1 </cn>
                        <ci> KeqTPI </ci>
                      </apply>
                    </apply>
                    <ci> TRIO </ci>
                    <apply>
                      <divide/>
                      <cn type="integer"> 1 </cn>
                      <apply>
                        <plus/>
                        <cn type="integer"> 1 </cn>
                        <ci> KeqTPI </ci>
                      </apply>
                    </apply>
                    <ci> TRIO </ci>
                  </apply>
                  <apply>
                    <times/>
                    <ci> KmALDGAP </ci>
                    <ci> KmALDDHAP </ci>
                  </apply>
                </apply>
                <apply>
                  <divide/>
                  <apply>
                    <times/>
                    <ci> F16P </ci>
                    <apply>
                      <divide/>
                      <ci> KeqTPI </ci>
                      <apply>
                        <plus/>
                        <cn type="integer"> 1 </cn>
                        <ci> KeqTPI </ci>
                      </apply>
                    </apply>
                    <ci> TRIO </ci>
                  </apply>
                  <apply>
                    <times/>
                    <ci> KmALDGAPi </ci>
                    <ci> KmALDF16P </ci>
                  </apply>
                </apply>
              </apply>
            </apply>
          </lambda>
        </math>
      </functionDefinition>
      <functionDefinition id="Function_for_Phosphoglycerate_kinase" name="Function for Phosphoglycerate kinase">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <lambda>
            <bvar>
              <ci> ADP </ci>
            </bvar>
            <bvar>
              <ci> ATP </ci>
            </bvar>
            <bvar>
              <ci> BPG </ci>
            </bvar>
            <bvar>
              <ci> KeqPGK </ci>
            </bvar>
            <bvar>
              <ci> KmPGKADP </ci>
            </bvar>
            <bvar>
              <ci> KmPGKATP </ci>
            </bvar>
            <bvar>
              <ci> KmPGKBPG </ci>
            </bvar>
            <bvar>
              <ci> KmPGKP3G </ci>
            </bvar>
            <bvar>
              <ci> P3G </ci>
            </bvar>
            <bvar>
              <ci> VmPGK </ci>
            </bvar>
            <apply>
              <divide/>
              <apply>
                <times/>
                <apply>
                  <divide/>
                  <ci> VmPGK </ci>
                  <apply>
                    <times/>
                    <ci> KmPGKP3G </ci>
                    <ci> KmPGKATP </ci>
                  </apply>
                </apply>
                <apply>
                  <minus/>
                  <apply>
                    <times/>
                    <ci> KeqPGK </ci>
                    <ci> BPG </ci>
                    <ci> ADP </ci>
                  </apply>
                  <apply>
                    <times/>
                    <ci> P3G </ci>
                    <ci> ATP </ci>
                  </apply>
                </apply>
              </apply>
              <apply>
                <times/>
                <apply>
                  <plus/>
                  <cn type="integer"> 1 </cn>
                  <apply>
                    <divide/>
                    <ci> BPG </ci>
                    <ci> KmPGKBPG </ci>
                  </apply>
                  <apply>
                    <divide/>
                    <ci> P3G </ci>
                    <ci> KmPGKP3G </ci>
                  </apply>
                </apply>
                <apply>
                  <plus/>
                  <cn type="integer"> 1 </cn>
                  <apply>
                    <divide/>
                    <ci> ATP </ci>
                    <ci> KmPGKATP </ci>
                  </apply>
                  <apply>
                    <divide/>
                    <ci> ADP </ci>
                    <ci> KmPGKADP </ci>
                  </apply>
                </apply>
              </apply>
            </apply>
          </lambda>
        </math>
      </functionDefinition>
      <functionDefinition id="Function_for_Glyceraldehyde_3_phosphate_dehydrogenase" name="Function for Glyceraldehyde 3-phosphate dehydrogenase">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <lambda>
            <bvar>
              <ci> BPG </ci>
            </bvar>
            <bvar>
              <ci> KeqTPI </ci>
            </bvar>
            <bvar>
              <ci> KmGAPDHBPG </ci>
            </bvar>
            <bvar>
              <ci> KmGAPDHGAP </ci>
            </bvar>
            <bvar>
              <ci> KmGAPDHNAD </ci>
            </bvar>
            <bvar>
              <ci> KmGAPDHNADH </ci>
            </bvar>
            <bvar>
              <ci> NAD </ci>
            </bvar>
            <bvar>
              <ci> NADH </ci>
            </bvar>
            <bvar>
              <ci> TRIO </ci>
            </bvar>
            <bvar>
              <ci> VmGAPDHf </ci>
            </bvar>
            <bvar>
              <ci> VmGAPDHr </ci>
            </bvar>
            <apply>
              <divide/>
              <apply>
                <minus/>
                <apply>
                  <divide/>
                  <apply>
                    <times/>
                    <ci> VmGAPDHf </ci>
                    <apply>
                      <divide/>
                      <ci> KeqTPI </ci>
                      <apply>
                        <plus/>
                        <cn type="integer"> 1 </cn>
                        <ci> KeqTPI </ci>
                      </apply>
                    </apply>
                    <ci> TRIO </ci>
                    <ci> NAD </ci>
                  </apply>
                  <apply>
                    <times/>
                    <ci> KmGAPDHGAP </ci>
                    <ci> KmGAPDHNAD </ci>
                  </apply>
                </apply>
                <apply>
                  <divide/>
                  <apply>
                    <times/>
                    <ci> VmGAPDHr </ci>
                    <ci> BPG </ci>
                    <ci> NADH </ci>
                  </apply>
                  <apply>
                    <times/>
                    <ci> KmGAPDHBPG </ci>
                    <ci> KmGAPDHNADH </ci>
                  </apply>
                </apply>
              </apply>
              <apply>
                <times/>
                <apply>
                  <plus/>
                  <cn type="integer"> 1 </cn>
                  <apply>
                    <divide/>
                    <apply>
                      <times/>
                      <apply>
                        <divide/>
                        <ci> KeqTPI </ci>
                        <apply>
                          <plus/>
                          <cn type="integer"> 1 </cn>
                          <ci> KeqTPI </ci>
                        </apply>
                      </apply>
                      <ci> TRIO </ci>
                    </apply>
                    <ci> KmGAPDHGAP </ci>
                  </apply>
                  <apply>
                    <divide/>
                    <ci> BPG </ci>
                    <ci> KmGAPDHBPG </ci>
                  </apply>
                </apply>
                <apply>
                  <plus/>
                  <cn type="integer"> 1 </cn>
                  <apply>
                    <divide/>
                    <ci> NAD </ci>
                    <ci> KmGAPDHNAD </ci>
                  </apply>
                  <apply>
                    <divide/>
                    <ci> NADH </ci>
                    <ci> KmGAPDHNADH </ci>
                  </apply>
                </apply>
              </apply>
            </apply>
          </lambda>
        </math>
      </functionDefinition>
      <functionDefinition id="Function_for_Enolase" name="Function for Enolase">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <lambda>
            <bvar>
              <ci> KeqENO </ci>
            </bvar>
            <bvar>
              <ci> KmENOP2G </ci>
            </bvar>
            <bvar>
              <ci> KmENOPEP </ci>
            </bvar>
            <bvar>
              <ci> P2G </ci>
            </bvar>
            <bvar>
              <ci> PEP </ci>
            </bvar>
            <bvar>
              <ci> VmENO </ci>
            </bvar>
            <apply>
              <divide/>
              <apply>
                <times/>
                <apply>
                  <divide/>
                  <ci> VmENO </ci>
                  <ci> KmENOP2G </ci>
                </apply>
                <apply>
                  <minus/>
                  <ci> P2G </ci>
                  <apply>
                    <divide/>
                    <ci> PEP </ci>
                    <ci> KeqENO </ci>
                  </apply>
                </apply>
              </apply>
              <apply>
                <plus/>
                <cn type="integer"> 1 </cn>
                <apply>
                  <divide/>
                  <ci> P2G </ci>
                  <ci> KmENOP2G </ci>
                </apply>
                <apply>
                  <divide/>
                  <ci> PEP </ci>
                  <ci> KmENOPEP </ci>
                </apply>
              </apply>
            </apply>
          </lambda>
        </math>
      </functionDefinition>
      <functionDefinition id="Function_for_Pyruvate_decarboxylase" name="Function for Pyruvate decarboxylase">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <lambda>
            <bvar>
              <ci> KmPDCPYR </ci>
            </bvar>
            <bvar>
              <ci> PYR </ci>
            </bvar>
            <bvar>
              <ci> VmPDC </ci>
            </bvar>
            <bvar>
              <ci> nPDC </ci>
            </bvar>
            <apply>
              <divide/>
              <apply>
                <times/>
                <ci> VmPDC </ci>
                <apply>
                  <divide/>
                  <apply>
                    <power/>
                    <ci> PYR </ci>
                    <ci> nPDC </ci>
                  </apply>
                  <apply>
                    <power/>
                    <ci> KmPDCPYR </ci>
                    <ci> nPDC </ci>
                  </apply>
                </apply>
              </apply>
              <apply>
                <plus/>
                <cn type="integer"> 1 </cn>
                <apply>
                  <divide/>
                  <apply>
                    <power/>
                    <ci> PYR </ci>
                    <ci> nPDC </ci>
                  </apply>
                  <apply>
                    <power/>
                    <ci> KmPDCPYR </ci>
                    <ci> nPDC </ci>
                  </apply>
                </apply>
              </apply>
            </apply>
          </lambda>
        </math>
      </functionDefinition>
      <functionDefinition id="Function_for_Succinate_synthesis" name="Function for Succinate synthesis">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <lambda>
            <bvar>
              <ci> ACE </ci>
            </bvar>
            <bvar>
              <ci> KSUCC </ci>
            </bvar>
            <apply>
              <times/>
              <ci> KSUCC </ci>
              <ci> ACE </ci>
            </apply>
          </lambda>
        </math>
      </functionDefinition>
      <functionDefinition id="Function_for_Glucose_transport" name="Function for Glucose transport">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <lambda>
            <bvar>
              <ci> GLCi </ci>
            </bvar>
            <bvar>
              <ci> GLCo </ci>
            </bvar>
            <bvar>
              <ci> KeqGLT </ci>
            </bvar>
            <bvar>
              <ci> KmGLTGLCi </ci>
            </bvar>
            <bvar>
              <ci> KmGLTGLCo </ci>
            </bvar>
            <bvar>
              <ci> VmGLT </ci>
            </bvar>
            <apply>
              <divide/>
              <apply>
                <times/>
                <apply>
                  <divide/>
                  <ci> VmGLT </ci>
                  <ci> KmGLTGLCo </ci>
                </apply>
                <apply>
                  <minus/>
                  <ci> GLCo </ci>
                  <apply>
                    <divide/>
                    <ci> GLCi </ci>
                    <ci> KeqGLT </ci>
                  </apply>
                </apply>
              </apply>
              <apply>
                <plus/>
                <cn type="integer"> 1 </cn>
                <apply>
                  <divide/>
                  <ci> GLCo </ci>
                  <ci> KmGLTGLCo </ci>
                </apply>
                <apply>
                  <divide/>
                  <ci> GLCi </ci>
                  <ci> KmGLTGLCi </ci>
                </apply>
                <apply>
                  <divide/>
                  <apply>
                    <times/>
                    <cn> 0.91 </cn>
                    <ci> GLCo </ci>
                    <ci> GLCi </ci>
                  </apply>
                  <apply>
                    <times/>
                    <ci> KmGLTGLCo </ci>
                    <ci> KmGLTGLCi </ci>
                  </apply>
                </apply>
              </apply>
            </apply>
          </lambda>
        </math>
      </functionDefinition>
      <functionDefinition id="Function_for_Phosphoglycerate_mutase" name="Function for Phosphoglycerate mutase">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <lambda>
            <bvar>
              <ci> KeqPGM </ci>
            </bvar>
            <bvar>
              <ci> KmPGMP2G </ci>
            </bvar>
            <bvar>
              <ci> KmPGMP3G </ci>
            </bvar>
            <bvar>
              <ci> P2G </ci>
            </bvar>
            <bvar>
              <ci> P3G </ci>
            </bvar>
            <bvar>
              <ci> VmPGM </ci>
            </bvar>
            <apply>
              <divide/>
              <apply>
                <times/>
                <apply>
                  <divide/>
                  <ci> VmPGM </ci>
                  <ci> KmPGMP3G </ci>
                </apply>
                <apply>
                  <minus/>
                  <ci> P3G </ci>
                  <apply>
                    <divide/>
                    <ci> P2G </ci>
                    <ci> KeqPGM </ci>
                  </apply>
                </apply>
              </apply>
              <apply>
                <plus/>
                <cn type="integer"> 1 </cn>
                <apply>
                  <divide/>
                  <ci> P3G </ci>
                  <ci> KmPGMP3G </ci>
                </apply>
                <apply>
                  <divide/>
                  <ci> P2G </ci>
                  <ci> KmPGMP2G </ci>
                </apply>
              </apply>
            </apply>
          </lambda>
        </math>
      </functionDefinition>
      <functionDefinition id="Function_for_Pyruvate_kinase" name="Function for Pyruvate kinase">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <lambda>
            <bvar>
              <ci> ADP </ci>
            </bvar>
            <bvar>
              <ci> ATP </ci>
            </bvar>
            <bvar>
              <ci> KeqPYK </ci>
            </bvar>
            <bvar>
              <ci> KmPYKADP </ci>
            </bvar>
            <bvar>
              <ci> KmPYKATP </ci>
            </bvar>
            <bvar>
              <ci> KmPYKPEP </ci>
            </bvar>
            <bvar>
              <ci> KmPYKPYR </ci>
            </bvar>
            <bvar>
              <ci> PEP </ci>
            </bvar>
            <bvar>
              <ci> PYR </ci>
            </bvar>
            <bvar>
              <ci> VmPYK </ci>
            </bvar>
            <apply>
              <divide/>
              <apply>
                <times/>
                <apply>
                  <divide/>
                  <ci> VmPYK </ci>
                  <apply>
                    <times/>
                    <ci> KmPYKPEP </ci>
                    <ci> KmPYKADP </ci>
                  </apply>
                </apply>
                <apply>
                  <minus/>
                  <apply>
                    <times/>
                    <ci> PEP </ci>
                    <ci> ADP </ci>
                  </apply>
                  <apply>
                    <divide/>
                    <apply>
                      <times/>
                      <ci> PYR </ci>
                      <ci> ATP </ci>
                    </apply>
                    <ci> KeqPYK </ci>
                  </apply>
                </apply>
              </apply>
              <apply>
                <times/>
                <apply>
                  <plus/>
                  <cn type="integer"> 1 </cn>
                  <apply>
                    <divide/>
                    <ci> PEP </ci>
                    <ci> KmPYKPEP </ci>
                  </apply>
                  <apply>
                    <divide/>
                    <ci> PYR </ci>
                    <ci> KmPYKPYR </ci>
                  </apply>
                </apply>
                <apply>
                  <plus/>
                  <cn type="integer"> 1 </cn>
                  <apply>
                    <divide/>
                    <ci> ATP </ci>
                    <ci> KmPYKATP </ci>
                  </apply>
                  <apply>
                    <divide/>
                    <ci> ADP </ci>
                    <ci> KmPYKADP </ci>
                  </apply>
                </apply>
              </apply>
            </apply>
          </lambda>
        </math>
      </functionDefinition>
      <functionDefinition id="Function_for_ATPase_activity" name="Function for ATPase activity">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <lambda>
            <bvar>
              <ci> ATP </ci>
            </bvar>
            <bvar>
              <ci> KATPASE </ci>
            </bvar>
            <apply>
              <times/>
              <ci> KATPASE </ci>
              <ci> ATP </ci>
            </apply>
          </lambda>
        </math>
      </functionDefinition>
      <functionDefinition id="Function_for_Phosphofructokinase" name="Function for Phosphofructokinase">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <lambda>
            <bvar>
              <ci> AMP </ci>
            </bvar>
            <bvar>
              <ci> ATP </ci>
            </bvar>
            <bvar>
              <ci> CPFKAMP </ci>
            </bvar>
            <bvar>
              <ci> CPFKATP </ci>
            </bvar>
            <bvar>
              <ci> CPFKF16BP </ci>
            </bvar>
            <bvar>
              <ci> CPFKF26BP </ci>
            </bvar>
            <bvar>
              <ci> CiPFKATP </ci>
            </bvar>
            <bvar>
              <ci> F16P </ci>
            </bvar>
            <bvar>
              <ci> F26BP </ci>
            </bvar>
            <bvar>
              <ci> F6P </ci>
            </bvar>
            <bvar>
              <ci> KPFKAMP </ci>
            </bvar>
            <bvar>
              <ci> KPFKF16BP </ci>
            </bvar>
            <bvar>
              <ci> KPFKF26BP </ci>
            </bvar>
            <bvar>
              <ci> KiPFKATP </ci>
            </bvar>
            <bvar>
              <ci> KmPFKATP </ci>
            </bvar>
            <bvar>
              <ci> KmPFKF6P </ci>
            </bvar>
            <bvar>
              <ci> Lzero </ci>
            </bvar>
            <bvar>
              <ci> VmPFK </ci>
            </bvar>
            <bvar>
              <ci> gR </ci>
            </bvar>
            <apply>
              <divide/>
              <apply>
                <times/>
                <ci> VmPFK </ci>
                <ci> gR </ci>
                <apply>
                  <divide/>
                  <ci> F6P </ci>
                  <ci> KmPFKF6P </ci>
                </apply>
                <apply>
                  <divide/>
                  <ci> ATP </ci>
                  <ci> KmPFKATP </ci>
                </apply>
                <apply>
                  <ci> R_PFK </ci>
                  <ci> KmPFKF6P </ci>
                  <ci> KmPFKATP </ci>
                  <ci> gR </ci>
                  <ci> ATP </ci>
                  <ci> F6P </ci>
                </apply>
              </apply>
              <apply>
                <plus/>
                <apply>
                  <power/>
                  <apply>
                    <ci> R_PFK </ci>
                    <ci> KmPFKF6P </ci>
                    <ci> KmPFKATP </ci>
                    <ci> gR </ci>
                    <ci> ATP </ci>
                    <ci> F6P </ci>
                  </apply>
                  <cn type="integer"> 2 </cn>
                </apply>
                <apply>
                  <times/>
                  <apply>
                    <ci> L_PFK </ci>
                    <ci> Lzero </ci>
                    <ci> CiPFKATP </ci>
                    <ci> KiPFKATP </ci>
                    <ci> CPFKAMP </ci>
                    <ci> KPFKAMP </ci>
                    <ci> CPFKF26BP </ci>
                    <ci> KPFKF26BP </ci>
                    <ci> CPFKF16BP </ci>
                    <ci> KPFKF16BP </ci>
                    <ci> ATP </ci>
                    <ci> AMP </ci>
                    <ci> F16P </ci>
                    <ci> F26BP </ci>
                  </apply>
                  <apply>
                    <power/>
                    <apply>
                      <ci> T_PFK </ci>
                      <ci> CPFKATP </ci>
                      <ci> KmPFKATP </ci>
                      <ci> ATP </ci>
                    </apply>
                    <cn type="integer"> 2 </cn>
                  </apply>
                </apply>
              </apply>
            </apply>
          </lambda>
        </math>
      </functionDefinition>
    </listOfFunctionDefinitions>
    <listOfUnitDefinitions>
      <unitDefinition id="unit_0" name="1">
        <listOfUnits>
          <unit kind="dimensionless" exponent="-0" scale="0" multiplier="1"/>
        </listOfUnits>
      </unitDefinition>
      <unitDefinition id="unit_1" name="mmol/l">
        <listOfUnits>
          <unit kind="mole" exponent="1" scale="-3" multiplier="1"/>
          <unit kind="litre" exponent="-1" scale="0" multiplier="1"/>
        </listOfUnits>
      </unitDefinition>
      <unitDefinition id="time_unit" name="time">
        <listOfUnits>
          <unit kind="second" exponent="1" scale="1" multiplier="6"/>
        </listOfUnits>
      </unitDefinition>
      <unitDefinition id="substance">
        <listOfUnits>
          <unit kind="mole" exponent="1" scale="-3" multiplier="1"/>
        </listOfUnits>
      </unitDefinition>
    </listOfUnitDefinitions>
    <listOfCompartments>
      <compartment metaid="Teusink2000_Glycolysis.extracellular" id="extracellular" spatialDimensions="3" size="1" constant="true">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.extracellular">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/go/GO:0005576"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </compartment>
      <compartment metaid="Teusink2000_Glycolysis.cytosol" id="cytosol" spatialDimensions="3" size="1" constant="true">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.cytosol">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/go/GO:0005829"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </compartment>
    </listOfCompartments>
    <listOfSpecies>
      <species metaid="Teusink2000_Glycolysis.GLCi" id="GLCi" name="Glucose in Cytosol" compartment="cytosol" initialConcentration="0.087" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.GLCi">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:17234"/>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00293"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.G6P" id="G6P" name="Glucose 6 Phosphate" compartment="cytosol" initialConcentration="2.45" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.G6P">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00668"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:17665"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.F6P" id="F6P" name="Fructose 6 Phosphate" compartment="cytosol" initialConcentration="0.62" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.F6P">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C05345"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:15946"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.F16P" id="F16P" name="Fructose-1,6 bisphosphate" compartment="cytosol" initialConcentration="5.51" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.F16P">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:16905"/>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00354"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.TRIO" id="TRIO" name="Triose-phosphate" compartment="cytosol" initialConcentration="0.96" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.TRIO">
              <bqbiol:hasPart>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:16108"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:29052"/>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00118"/>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00111"/>
                </rdf:Bag>
              </bqbiol:hasPart>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.BPG" id="BPG" name="1,3-bisphosphoglycerate" compartment="cytosol" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.BPG">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:16001"/>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00236"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.P3G" id="P3G" name="3-phosphoglycerate" compartment="cytosol" initialConcentration="0.9" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.P3G">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00197"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:17794"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.P2G" id="P2G" name="2-phosphoglycerate" compartment="cytosol" initialConcentration="0.12" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.P2G">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00631"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:17835"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.PEP" id="PEP" name="Phosphoenolpyruvate" compartment="cytosol" initialConcentration="0.07" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.PEP">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:18021"/>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00074"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.PYR" id="PYR" name="Pyruvate" compartment="cytosol" initialConcentration="1.85" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.PYR">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00022"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:32816"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:15361"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.ACE" id="ACE" name="Acetaldehyde" compartment="cytosol" initialConcentration="0.17" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.ACE">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00084"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:15343"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.P" id="P" name="High energy phosphates" compartment="cytosol" initialConcentration="6.31" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.P">
              <bqbiol:hasPart>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:16761"/>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00008"/>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00002"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:15422"/>
                </rdf:Bag>
              </bqbiol:hasPart>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.NAD" id="NAD" compartment="cytosol" initialConcentration="1.2" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.NAD">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00003"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:15846"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.NADH" id="NADH" compartment="cytosol" initialConcentration="0.39" hasOnlySubstanceUnits="false" boundaryCondition="false" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.NADH">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:16908"/>
                  <rdf:li rdf:resource="http://identifiers.org//C00004"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.Glyc" id="Glyc" name="Glycogen" compartment="cytosol" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.Glyc">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00182"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:28087"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.Trh" id="Trh" name="Trehalose" compartment="cytosol" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.Trh">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C01083"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:27082"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.CO2" id="CO2" compartment="cytosol" initialConcentration="1" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.CO2">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00011"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:16526"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.SUCC" id="SUCC" name="Succinate" compartment="cytosol" initialConcentration="0" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.SUCC">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:30031"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.GLCo" id="GLCo" name="Extracellular Glucose" compartment="extracellular" initialConcentration="50" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.GLCo">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00293"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:17234"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.ETOH" id="ETOH" name="Ethanol" compartment="cytosol" initialConcentration="50" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.ETOH">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00469"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:16236"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.GLY" id="GLY" name="Glycerol" compartment="cytosol" initialConcentration="0.15" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.GLY">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00116"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:17754"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.ATP" id="ATP" name="ATP concentration" compartment="cytosol" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.ATP">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00002"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:15422"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.ADP" id="ADP" name="ADP concentration" compartment="cytosol" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.ADP">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00008"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:16761"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.SUM_P" id="SUM_P" name="sum of AXP conc" compartment="cytosol" initialConcentration="4.1" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.SUM_P">
              <bqbiol:hasPart>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:16027"/>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00008"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:15422"/>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00002"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:16761"/>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00020"/>
                </rdf:Bag>
              </bqbiol:hasPart>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.AMP" id="AMP" name="AMP concentration" compartment="cytosol" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.AMP">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:16027"/>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00020"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
      <species metaid="Teusink2000_Glycolysis.F26BP" id="F26BP" name="F2,6P" compartment="cytosol" initialConcentration="0.02" hasOnlySubstanceUnits="false" boundaryCondition="true" constant="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.F26BP">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.compound/C00665"/>
                  <rdf:li rdf:resource="http://identifiers.org/chebi/CHEBI:28602"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
      </species>
    </listOfSpecies>
    <listOfParameters>
      <parameter id="KeqAK" name="AK eq constant" value="0.45" units="unit_0" constant="true"/>
      <parameter id="vGLK_KeqGLK" value="3800" constant="true"/>
      <parameter id="vGLK_KmGLKADP" value="0.23" constant="true"/>
      <parameter id="vGLK_KmGLKATP" value="0.15" constant="true"/>
      <parameter id="vGLK_KmGLKG6P" value="30" constant="true"/>
      <parameter id="vGLK_KmGLKGLCi" value="0.08" constant="true"/>
      <parameter id="vGLK_VmGLK" value="226.452" constant="true"/>
      <parameter id="vPGI_KeqPGI_2" value="0.314" constant="true"/>
      <parameter id="vPGI_KmPGIF6P_2" value="0.3" constant="true"/>
      <parameter id="vPGI_KmPGIG6P_2" value="1.4" constant="true"/>
      <parameter id="vPGI_VmPGI_2" value="339.677" constant="true"/>
      <parameter id="vGLYCO_v" value="6" constant="true"/>
      <parameter id="vTreha_v" value="2.4" constant="true"/>
      <parameter id="CPFKAMP" value="0.0845" units="unit_0" constant="true"/>
      <parameter id="CPFKATP" value="3" units="unit_0" constant="true"/>
      <parameter id="CPFKF16BP" value="0.397" units="unit_0" constant="true"/>
      <parameter id="CPFKF26BP" value="0.0174" units="unit_0" constant="true"/>
      <parameter id="CiPFKATP" value="100" units="unit_0" constant="true"/>
      <parameter id="KPFKAMP" value="0.0995" units="unit_1" constant="true"/>
      <parameter id="KPFKF16BP" value="0.111" units="unit_1" constant="true"/>
      <parameter id="KPFKF26BP" value="0.000682" units="unit_1" constant="true"/>
      <parameter id="KiPFKATP" value="0.65" units="unit_1" constant="true"/>
      <parameter id="KmPFKATP" value="0.71" units="unit_1" constant="true"/>
      <parameter id="KmPFKF6P" value="0.1" units="unit_1" constant="true"/>
      <parameter id="Lzero" value="0.66" units="unit_0" constant="true"/>
      <parameter id="vPFK_VmPFK" value="182.903" constant="true"/>
      <parameter id="gR" value="5.12" units="unit_0" constant="true"/>
      <parameter id="vALD_KeqALD" value="0.069" constant="true"/>
      <parameter id="KeqTPI" name="TPI eq constant" value="0.045" units="unit_0" constant="true"/>
      <parameter id="vALD_KmALDDHAP" value="2.4" constant="true"/>
      <parameter id="vALD_KmALDF16P" value="0.3" constant="true"/>
      <parameter id="vALD_KmALDGAP" value="2" constant="true"/>
      <parameter id="vALD_KmALDGAPi" value="10" constant="true"/>
      <parameter id="vALD_VmALD" value="322.258" constant="true"/>
      <parameter id="vGAPDH_KmGAPDHBPG" value="0.0098" constant="true"/>
      <parameter id="vGAPDH_KmGAPDHGAP" value="0.21" constant="true"/>
      <parameter id="vGAPDH_KmGAPDHNAD" value="0.09" constant="true"/>
      <parameter id="vGAPDH_KmGAPDHNADH" value="0.06" constant="true"/>
      <parameter id="vGAPDH_VmGAPDHf" value="1184.52" constant="true"/>
      <parameter id="vGAPDH_VmGAPDHr" value="6549.8" constant="true"/>
      <parameter id="vPGK_KeqPGK" value="3200" constant="true"/>
      <parameter id="vPGK_KmPGKADP" value="0.2" constant="true"/>
      <parameter id="vPGK_KmPGKATP" value="0.3" constant="true"/>
      <parameter id="vPGK_KmPGKBPG" value="0.003" constant="true"/>
      <parameter id="vPGK_KmPGKP3G" value="0.53" constant="true"/>
      <parameter id="vPGK_VmPGK" value="1306.45" constant="true"/>
      <parameter id="vPGM_KeqPGM" value="0.19" constant="true"/>
      <parameter id="vPGM_KmPGMP2G" value="0.08" constant="true"/>
      <parameter id="vPGM_KmPGMP3G" value="1.2" constant="true"/>
      <parameter id="vPGM_VmPGM" value="2525.81" constant="true"/>
      <parameter id="vENO_KeqENO" value="6.7" constant="true"/>
      <parameter id="vENO_KmENOP2G" value="0.04" constant="true"/>
      <parameter id="vENO_KmENOPEP" value="0.5" constant="true"/>
      <parameter id="vENO_VmENO" value="365.806" constant="true"/>
      <parameter id="vPYK_KeqPYK" value="6500" constant="true"/>
      <parameter id="vPYK_KmPYKADP" value="0.53" constant="true"/>
      <parameter id="vPYK_KmPYKATP" value="1.5" constant="true"/>
      <parameter id="vPYK_KmPYKPEP" value="0.14" constant="true"/>
      <parameter id="vPYK_KmPYKPYR" value="21" constant="true"/>
      <parameter id="vPYK_VmPYK" value="1088.71" constant="true"/>
      <parameter id="vPDC_KmPDCPYR" value="4.33" constant="true"/>
      <parameter id="vPDC_VmPDC" value="174.194" constant="true"/>
      <parameter id="vPDC_nPDC" value="1.9" constant="true"/>
      <parameter id="vSUC_KSUCC" value="21.4" constant="true"/>
      <parameter id="vGLT_KeqGLT" value="1" constant="true"/>
      <parameter id="vGLT_KmGLTGLCi" value="1.1918" constant="true"/>
      <parameter id="vGLT_KmGLTGLCo" value="1.1918" constant="true"/>
      <parameter id="vGLT_VmGLT" value="97.264" constant="true"/>
      <parameter id="vADH_KeqADH" value="6.9e-05" constant="true"/>
      <parameter id="vADH_KiADHACE" value="1.1" constant="true"/>
      <parameter id="vADH_KiADHETOH" value="90" constant="true"/>
      <parameter id="vADH_KiADHNAD" value="0.92" constant="true"/>
      <parameter id="vADH_KiADHNADH" value="0.031" constant="true"/>
      <parameter id="vADH_KmADHACE" value="1.11" constant="true"/>
      <parameter id="vADH_KmADHETOH" value="17" constant="true"/>
      <parameter id="vADH_KmADHNAD" value="0.17" constant="true"/>
      <parameter id="vADH_KmADHNADH" value="0.11" constant="true"/>
      <parameter id="vADH_VmADH" value="810" constant="true"/>
      <parameter id="vG3PDH_KeqG3PDH" value="4300" constant="true"/>
      <parameter id="vG3PDH_KmG3PDHDHAP" value="0.4" constant="true"/>
      <parameter id="vG3PDH_KmG3PDHGLY" value="1" constant="true"/>
      <parameter id="vG3PDH_KmG3PDHNAD" value="0.93" constant="true"/>
      <parameter id="vG3PDH_KmG3PDHNADH" value="0.023" constant="true"/>
      <parameter id="vG3PDH_VmG3PDH" value="70.15" constant="true"/>
      <parameter id="vATP_KATPASE" value="33.7" constant="true"/>
    </listOfParameters>
    <listOfRules>
      <assignmentRule variable="ATP">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <divide/>
            <apply>
              <minus/>
              <ci> P </ci>
              <ci> ADP </ci>
            </apply>
            <cn type="integer"> 2 </cn>
          </apply>
        </math>
      </assignmentRule>
      <assignmentRule variable="ADP">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <divide/>
            <apply>
              <minus/>
              <ci> SUM_P </ci>
              <apply>
                <power/>
                <apply>
                  <plus/>
                  <apply>
                    <times/>
                    <apply>
                      <power/>
                      <ci> P </ci>
                      <cn type="integer"> 2 </cn>
                    </apply>
                    <apply>
                      <minus/>
                      <cn type="integer"> 1 </cn>
                      <apply>
                        <times/>
                        <cn type="integer"> 4 </cn>
                        <ci> KeqAK </ci>
                      </apply>
                    </apply>
                  </apply>
                  <apply>
                    <times/>
                    <cn type="integer"> 2 </cn>
                    <ci> SUM_P </ci>
                    <ci> P </ci>
                    <apply>
                      <minus/>
                      <apply>
                        <times/>
                        <cn type="integer"> 4 </cn>
                        <ci> KeqAK </ci>
                      </apply>
                      <cn type="integer"> 1 </cn>
                    </apply>
                  </apply>
                  <apply>
                    <power/>
                    <ci> SUM_P </ci>
                    <cn type="integer"> 2 </cn>
                  </apply>
                </apply>
                <cn> 0.5 </cn>
              </apply>
            </apply>
            <apply>
              <minus/>
              <cn type="integer"> 1 </cn>
              <apply>
                <times/>
                <cn type="integer"> 4 </cn>
                <ci> KeqAK </ci>
              </apply>
            </apply>
          </apply>
        </math>
      </assignmentRule>
      <assignmentRule variable="AMP">
        <math xmlns="http://www.w3.org/1998/Math/MathML">
          <apply>
            <minus/>
            <apply>
              <minus/>
              <ci> SUM_P </ci>
              <ci> ATP </ci>
            </apply>
            <ci> ADP </ci>
          </apply>
        </math>
      </assignmentRule>
    </listOfRules>
    <listOfReactions>
      <reaction metaid="Teusink2000_Glycolysis.vGLK" id="vGLK" name="Hexokinase" reversible="true" fast="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.vGLK">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R00299"/>
                  <rdf:li rdf:resource="http://identifiers.org/ec-code/2.7.1.2"/>
                </rdf:Bag>
              </bqbiol:is>
              <bqbiol:isHomologTo>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_1318"/>
                </rdf:Bag>
              </bqbiol:isHomologTo>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
        <listOfReactants>
          <speciesReference species="GLCi" stoichiometry="1" constant="true"/>
          <speciesReference species="P" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="G6P" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <listOfModifiers>
          <modifierSpeciesReference species="ATP"/>
          <modifierSpeciesReference species="ADP"/>
        </listOfModifiers>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> cytosol </ci>
              <apply>
                <ci> Function_for_Hexokinase </ci>
                <ci> ADP </ci>
                <ci> ATP </ci>
                <ci> G6P </ci>
                <ci> GLCi </ci>
                <ci> vGLK_KeqGLK </ci>
                <ci> vGLK_KmGLKADP </ci>
                <ci> vGLK_KmGLKATP </ci>
                <ci> vGLK_KmGLKG6P </ci>
                <ci> vGLK_KmGLKGLCi </ci>
                <ci> vGLK_VmGLK </ci>
              </apply>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction metaid="Teusink2000_Glycolysis.vPGI" id="vPGI" name="Glucose-6-phosphate isomerase" reversible="true" fast="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.vPGI">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/ec-code/5.3.1.9"/>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R00771"/>
                </rdf:Bag>
              </bqbiol:is>
              <bqbiol:isHomologTo>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_116"/>
                </rdf:Bag>
              </bqbiol:isHomologTo>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
        <listOfReactants>
          <speciesReference species="G6P" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="F6P" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> cytosol </ci>
              <apply>
                <ci> Function_for_Glucose_6_phosphate_isomerase </ci>
                <ci> F6P </ci>
                <ci> G6P </ci>
                <ci> vPGI_KeqPGI_2 </ci>
                <ci> vPGI_KmPGIF6P_2 </ci>
                <ci> vPGI_KmPGIG6P_2 </ci>
                <ci> vPGI_VmPGI_2 </ci>
              </apply>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction metaid="Teusink2000_Glycolysis.vGLYCO" id="vGLYCO" name="Glycogen synthesis" reversible="false" fast="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.vGLYCO">
              <bqbiol:isHomologTo>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_1736"/>
                </rdf:Bag>
              </bqbiol:isHomologTo>
              <bqbiol:isVersionOf>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/go/GO:0005978"/>
                </rdf:Bag>
              </bqbiol:isVersionOf>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
        <listOfReactants>
          <speciesReference species="G6P" stoichiometry="1" constant="true"/>
          <speciesReference species="P" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="Glyc" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> cytosol </ci>
              <apply>
                <ci> Constant_flux__irreversible </ci>
                <ci> vGLYCO_v </ci>
              </apply>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction metaid="Teusink2000_Glycolysis.vTreha" id="vTreha" name="Trehalose 6-phosphate synthase" reversible="false" fast="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.vTreha">
              <bqbiol:isVersionOf>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/go/GO:0005992"/>
                </rdf:Bag>
              </bqbiol:isVersionOf>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
        <listOfReactants>
          <speciesReference species="G6P" stoichiometry="2" constant="true"/>
          <speciesReference species="P" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="Trh" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> cytosol </ci>
              <apply>
                <ci> Constant_flux__irreversible </ci>
                <ci> vTreha_v </ci>
              </apply>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction metaid="Teusink2000_Glycolysis.vPFK" id="vPFK" name="Phosphofructokinase" reversible="false" fast="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.vPFK">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/ec-code/2.7.1.11"/>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R00756"/>
                </rdf:Bag>
              </bqbiol:is>
              <bqbiol:isHomologTo>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_736"/>
                </rdf:Bag>
              </bqbiol:isHomologTo>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
        <listOfReactants>
          <speciesReference species="F6P" stoichiometry="1" constant="true"/>
          <speciesReference species="P" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="F16P" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <listOfModifiers>
          <modifierSpeciesReference species="AMP"/>
          <modifierSpeciesReference species="F26BP"/>
          <modifierSpeciesReference species="ATP"/>
        </listOfModifiers>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> cytosol </ci>
              <apply>
                <ci> Function_for_Phosphofructokinase </ci>
                <ci> AMP </ci>
                <ci> ATP </ci>
                <ci> CPFKAMP </ci>
                <ci> CPFKATP </ci>
                <ci> CPFKF16BP </ci>
                <ci> CPFKF26BP </ci>
                <ci> CiPFKATP </ci>
                <ci> F16P </ci>
                <ci> F26BP </ci>
                <ci> F6P </ci>
                <ci> KPFKAMP </ci>
                <ci> KPFKF16BP </ci>
                <ci> KPFKF26BP </ci>
                <ci> KiPFKATP </ci>
                <ci> KmPFKATP </ci>
                <ci> KmPFKF6P </ci>
                <ci> Lzero </ci>
                <ci> vPFK_VmPFK </ci>
                <ci> gR </ci>
              </apply>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction metaid="Teusink2000_Glycolysis.vALD" id="vALD" name="Aldolase" reversible="true" fast="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.vALD">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/ec-code/4.1.2.13"/>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R01070"/>
                </rdf:Bag>
              </bqbiol:is>
              <bqbiol:isHomologTo>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_1602"/>
                </rdf:Bag>
              </bqbiol:isHomologTo>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
        <listOfReactants>
          <speciesReference species="F16P" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="TRIO" stoichiometry="2" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> cytosol </ci>
              <apply>
                <ci> Function_for_Aldolase </ci>
                <ci> F16P </ci>
                <ci> vALD_KeqALD </ci>
                <ci> KeqTPI </ci>
                <ci> vALD_KmALDDHAP </ci>
                <ci> vALD_KmALDF16P </ci>
                <ci> vALD_KmALDGAP </ci>
                <ci> vALD_KmALDGAPi </ci>
                <ci> TRIO </ci>
                <ci> vALD_VmALD </ci>
              </apply>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction metaid="Teusink2000_Glycolysis.vGAPDH" id="vGAPDH" name="Glyceraldehyde 3-phosphate dehydrogenase" reversible="true" fast="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.vGAPDH">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/ec-code/1.2.1.12"/>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R01061"/>
                </rdf:Bag>
              </bqbiol:is>
              <bqbiol:isHomologTo>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_1847"/>
                </rdf:Bag>
              </bqbiol:isHomologTo>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
        <listOfReactants>
          <speciesReference species="TRIO" stoichiometry="1" constant="true"/>
          <speciesReference species="NAD" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="BPG" stoichiometry="1" constant="true"/>
          <speciesReference species="NADH" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> cytosol </ci>
              <apply>
                <ci> Function_for_Glyceraldehyde_3_phosphate_dehydrogenase </ci>
                <ci> BPG </ci>
                <ci> KeqTPI </ci>
                <ci> vGAPDH_KmGAPDHBPG </ci>
                <ci> vGAPDH_KmGAPDHGAP </ci>
                <ci> vGAPDH_KmGAPDHNAD </ci>
                <ci> vGAPDH_KmGAPDHNADH </ci>
                <ci> NAD </ci>
                <ci> NADH </ci>
                <ci> TRIO </ci>
                <ci> vGAPDH_VmGAPDHf </ci>
                <ci> vGAPDH_VmGAPDHr </ci>
              </apply>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction metaid="Teusink2000_Glycolysis.vPGK" id="vPGK" name="Phosphoglycerate kinase" reversible="true" fast="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.vPGK">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R01512"/>
                  <rdf:li rdf:resource="http://identifiers.org/ec-code/2.7.2.3"/>
                </rdf:Bag>
              </bqbiol:is>
              <bqbiol:isHomologTo>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_1771"/>
                </rdf:Bag>
              </bqbiol:isHomologTo>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
        <listOfReactants>
          <speciesReference species="BPG" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="P3G" stoichiometry="1" constant="true"/>
          <speciesReference species="P" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <listOfModifiers>
          <modifierSpeciesReference species="ATP"/>
          <modifierSpeciesReference species="ADP"/>
        </listOfModifiers>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> cytosol </ci>
              <apply>
                <ci> Function_for_Phosphoglycerate_kinase </ci>
                <ci> ADP </ci>
                <ci> ATP </ci>
                <ci> BPG </ci>
                <ci> vPGK_KeqPGK </ci>
                <ci> vPGK_KmPGKADP </ci>
                <ci> vPGK_KmPGKATP </ci>
                <ci> vPGK_KmPGKBPG </ci>
                <ci> vPGK_KmPGKP3G </ci>
                <ci> P3G </ci>
                <ci> vPGK_VmPGK </ci>
              </apply>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction metaid="Teusink2000_Glycolysis.vPGM" id="vPGM" name="Phosphoglycerate mutase" reversible="true" fast="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.vPGM">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R01518"/>
                  <rdf:li rdf:resource="http://identifiers.org/ec-code/5.4.2.1"/>
                </rdf:Bag>
              </bqbiol:is>
              <bqbiol:isHomologTo>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_576"/>
                </rdf:Bag>
              </bqbiol:isHomologTo>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
        <listOfReactants>
          <speciesReference species="P3G" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="P2G" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> cytosol </ci>
              <apply>
                <ci> Function_for_Phosphoglycerate_mutase </ci>
                <ci> vPGM_KeqPGM </ci>
                <ci> vPGM_KmPGMP2G </ci>
                <ci> vPGM_KmPGMP3G </ci>
                <ci> P2G </ci>
                <ci> P3G </ci>
                <ci> vPGM_VmPGM </ci>
              </apply>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction metaid="Teusink2000_Glycolysis.vENO" id="vENO" name="Enolase" reversible="true" fast="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.vENO">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/ec-code/4.2.1.11"/>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R00658"/>
                </rdf:Bag>
              </bqbiol:is>
              <bqbiol:isHomologTo>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_1400"/>
                </rdf:Bag>
              </bqbiol:isHomologTo>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
        <listOfReactants>
          <speciesReference species="P2G" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="PEP" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> cytosol </ci>
              <apply>
                <ci> Function_for_Enolase </ci>
                <ci> vENO_KeqENO </ci>
                <ci> vENO_KmENOP2G </ci>
                <ci> vENO_KmENOPEP </ci>
                <ci> P2G </ci>
                <ci> PEP </ci>
                <ci> vENO_VmENO </ci>
              </apply>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction metaid="Teusink2000_Glycolysis.vPYK" id="vPYK" name="Pyruvate kinase" reversible="true" fast="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.vPYK">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R00200"/>
                  <rdf:li rdf:resource="http://identifiers.org/ec-code/2.7.1.40"/>
                </rdf:Bag>
              </bqbiol:is>
              <bqbiol:isHomologTo>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_1911"/>
                </rdf:Bag>
              </bqbiol:isHomologTo>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
        <listOfReactants>
          <speciesReference species="PEP" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="PYR" stoichiometry="1" constant="true"/>
          <speciesReference species="P" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <listOfModifiers>
          <modifierSpeciesReference species="ATP"/>
          <modifierSpeciesReference species="ADP"/>
        </listOfModifiers>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> cytosol </ci>
              <apply>
                <ci> Function_for_Pyruvate_kinase </ci>
                <ci> ADP </ci>
                <ci> ATP </ci>
                <ci> vPYK_KeqPYK </ci>
                <ci> vPYK_KmPYKADP </ci>
                <ci> vPYK_KmPYKATP </ci>
                <ci> vPYK_KmPYKPEP </ci>
                <ci> vPYK_KmPYKPYR </ci>
                <ci> PEP </ci>
                <ci> PYR </ci>
                <ci> vPYK_VmPYK </ci>
              </apply>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction metaid="Teusink2000_Glycolysis.vPDC" id="vPDC" name="Pyruvate decarboxylase" reversible="false" fast="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.vPDC">
              <bqbiol:is>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R00224"/>
                  <rdf:li rdf:resource="http://identifiers.org/ec-code/4.1.1.1"/>
                </rdf:Bag>
              </bqbiol:is>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
        <listOfReactants>
          <speciesReference species="PYR" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="ACE" stoichiometry="1" constant="true"/>
          <speciesReference species="CO2" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> cytosol </ci>
              <apply>
                <ci> Function_for_Pyruvate_decarboxylase </ci>
                <ci> vPDC_KmPDCPYR </ci>
                <ci> PYR </ci>
                <ci> vPDC_VmPDC </ci>
                <ci> vPDC_nPDC </ci>
              </apply>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction metaid="Teusink2000_Glycolysis.vSUC" id="vSUC" name="Succinate synthesis" reversible="false" fast="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.vSUC">
              <bqbiol:isVersionOf>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/go/GO:0006105"/>
                </rdf:Bag>
              </bqbiol:isVersionOf>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
        <listOfReactants>
          <speciesReference species="ACE" stoichiometry="2" constant="true"/>
          <speciesReference species="NAD" stoichiometry="3" constant="true"/>
          <speciesReference species="P" stoichiometry="4" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="NADH" stoichiometry="3" constant="true"/>
          <speciesReference species="SUCC" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> cytosol </ci>
              <apply>
                <ci> Function_for_Succinate_synthesis </ci>
                <ci> ACE </ci>
                <ci> vSUC_KSUCC </ci>
              </apply>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction metaid="Teusink2000_Glycolysis.vGLT" id="vGLT" name="Glucose transport" reversible="true" fast="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.vGLT">
              <bqbiol:isHomologTo>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_2092"/>
                </rdf:Bag>
              </bqbiol:isHomologTo>
              <bqbiol:isVersionOf>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/go/GO:0046323"/>
                </rdf:Bag>
              </bqbiol:isVersionOf>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
        <listOfReactants>
          <speciesReference species="GLCo" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="GLCi" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <ci> Function_for_Glucose_transport </ci>
              <ci> GLCi </ci>
              <ci> GLCo </ci>
              <ci> vGLT_KeqGLT </ci>
              <ci> vGLT_KmGLTGLCi </ci>
              <ci> vGLT_KmGLTGLCo </ci>
              <ci> vGLT_VmGLT </ci>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction metaid="Teusink2000_Glycolysis.vADH" id="vADH" name="Alcohol dehydrogenase" reversible="true" fast="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.vADH">
              <bqbiol:isHomologTo>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/reactome/REACT_799"/>
                </rdf:Bag>
              </bqbiol:isHomologTo>
              <bqbiol:isVersionOf>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/kegg.reaction/R00746"/>
                  <rdf:li rdf:resource="http://identifiers.org/ec-code/1.1.1.2"/>
                </rdf:Bag>
              </bqbiol:isVersionOf>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
        <listOfReactants>
          <speciesReference species="ACE" stoichiometry="1" constant="true"/>
          <speciesReference species="NADH" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="NAD" stoichiometry="1" constant="true"/>
          <speciesReference species="ETOH" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> cytosol </ci>
              <apply>
                <ci> Function_for_Alcohol_dehydrogenase </ci>
                <ci> ACE </ci>
                <ci> ETOH </ci>
                <ci> vADH_KeqADH </ci>
                <ci> vADH_KiADHACE </ci>
                <ci> vADH_KiADHETOH </ci>
                <ci> vADH_KiADHNAD </ci>
                <ci> vADH_KiADHNADH </ci>
                <ci> vADH_KmADHACE </ci>
                <ci> vADH_KmADHETOH </ci>
                <ci> vADH_KmADHNAD </ci>
                <ci> vADH_KmADHNADH </ci>
                <ci> NAD </ci>
                <ci> NADH </ci>
                <ci> vADH_VmADH </ci>
                <ci> cytosol </ci>
              </apply>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction metaid="Teusink2000_Glycolysis.vG3PDH" id="vG3PDH" name="Glycerol 3-phosphate dehydrogenase" reversible="false" fast="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.vG3PDH">
              <bqbiol:isVersionOf>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/ec-code/1.1.1.8"/>
                </rdf:Bag>
              </bqbiol:isVersionOf>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
        <listOfReactants>
          <speciesReference species="TRIO" stoichiometry="1" constant="true"/>
          <speciesReference species="NADH" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfProducts>
          <speciesReference species="NAD" stoichiometry="1" constant="true"/>
          <speciesReference species="GLY" stoichiometry="1" constant="true"/>
        </listOfProducts>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> cytosol </ci>
              <apply>
                <ci> Function_for_Glycerol_3_phosphate_dehydrogenase </ci>
                <ci> GLY </ci>
                <ci> vG3PDH_KeqG3PDH </ci>
                <ci> KeqTPI </ci>
                <ci> vG3PDH_KmG3PDHDHAP </ci>
                <ci> vG3PDH_KmG3PDHGLY </ci>
                <ci> vG3PDH_KmG3PDHNAD </ci>
                <ci> vG3PDH_KmG3PDHNADH </ci>
                <ci> NAD </ci>
                <ci> NADH </ci>
                <ci> TRIO </ci>
                <ci> vG3PDH_VmG3PDH </ci>
              </apply>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
      <reaction metaid="Teusink2000_Glycolysis.vATP" id="vATP" name="ATPase activity" reversible="true" fast="false">
        <annotation>
          <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:vCard="http://www.w3.org/2001/vcard-rdf/3.0#" xmlns:vCard4="http://www.w3.org/2006/vcard/ns#" xmlns:bqbiol="http://biomodels.net/biology-qualifiers/" xmlns:bqmodel="http://biomodels.net/model-qualifiers/">
            <rdf:Description rdf:about="#Teusink2000_Glycolysis.vATP">
              <bqbiol:isVersionOf>
                <rdf:Bag>
                  <rdf:li rdf:resource="http://identifiers.org/go/GO:0016887"/>
                  <rdf:li rdf:resource="http://identifiers.org/ec-code/3.6.1.3"/>
                </rdf:Bag>
              </bqbiol:isVersionOf>
            </rdf:Description>
          </rdf:RDF>
        </annotation>
        <listOfReactants>
          <speciesReference species="P" stoichiometry="1" constant="true"/>
        </listOfReactants>
        <listOfModifiers>
          <modifierSpeciesReference species="ATP"/>
        </listOfModifiers>
        <kineticLaw>
          <math xmlns="http://www.w3.org/1998/Math/MathML">
            <apply>
              <times/>
              <ci> cytosol </ci>
              <apply>
                <ci> Function_for_ATPase_activity </ci>
                <ci> ATP </ci>
                <ci> vATP_KATPASE </ci>
              </apply>
            </apply>
          </math>
        </kineticLaw>
      </reaction>
    </listOfReactions>
  </model>
</sbml>
"""