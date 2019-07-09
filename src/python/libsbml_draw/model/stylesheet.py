from pathlib import Path
import pkg_resources

import xml.etree.ElementTree as ET 


stylesheet_file_name = "SBGNstyles.xml"

stylesheet_file = Path(pkg_resources.resource_filename("libsbml_draw", 
        "model/data/" + stylesheet_file_name))


def parseXML(xmlfile): 
  
    # create element tree object 
    tree = ET.parse(xmlfile) 
  
    # get root element 
    root = tree.getroot()
  
    print("root: ", root)
    
    # create empty list for news items 
    line_endings = [] 
  
    # iterate news items 
    for item in root.findall('listOfLineEndings'): 
  
        print("lole")
        # empty news dictionary 
        line_ending = {} 
  
        # iterate child elements of item 
        for child in item: 
  
            # special checking for namespace object content:media 
#            if child.tag == '{http://search.yahoo.com/mrss/}content': 
#                news['media'] = child.attrib['url'] 
#            else: 
#                news[child.tag] = child.text.encode('utf8') 
  
        # append news dictionary to news items list 
            line_endings.append(child) 
      
    # return news items list 
    return line_endings 


line_endings = parseXML(str(stylesheet_file))


print("num line endings: ", len(line_endings))



