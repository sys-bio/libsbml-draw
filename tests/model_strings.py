# model generated using randMANetGen
model_xml = """<?xml version='1.0' encoding='UTF-8' standalone='no'?>
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