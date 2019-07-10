from pathlib import Path
import pkg_resources

import xml.etree.ElementTree as ET 

import libsbml

#stylesheet_file_name = "SBGNstyles.xml"
stylesheet_file_name = "LineEnding_styles.xml"

stylesheet_file = Path(pkg_resources.resource_filename("libsbml_draw", 
        "model/data/" + stylesheet_file_name))

#doc = libsbml.readSBMLFromFile(str(stylesheet_file))
#print("doc: ", type(doc))
#model = doc.getModel()
# SBasePlugin, LayoutModelPlugin
#layout_plugin = model.getPlugin("layout")
#layout = layout_plugin.getLayout(0)
#rPlugin = model.getPlugin("render")

def parseXML(xmlfile): 
  
    # create element tree object 
    tree = ET.parse(xmlfile) 
  
    line_endings = {}
    
    ns_lole = "{http://projects.eml.org/bcb/sbml/render/level2}listOfLineEndings"
    ns_le = "{http://projects.eml.org/bcb/sbml/render/level2}lineEnding"

    nns_lole = "listOfLineEndings"
    nns_le = "lineEnding"    
    
    # get root element 
    root = tree.getroot()
    print("root: ", root)
    
    for le in root.findall(nns_le):
  
        print("le", le)
        line_endings[le.attrib["id"]] = le
        
#        for le in lole.findall(nns_le):
#            print("le", le.attrib, type(le), le.attrib["id"])
#            line_endings[le.attrib["id"]] = le
   
    return line_endings


line_endings = parseXML(str(stylesheet_file))


print("num line endings: ", len(line_endings))
lep = line_endings["product"]
print("lep: ", lep.attrib)
print("lep:")
lep_xml = ET.tostring(lep, encoding="unicode")
print(lep_xml)

