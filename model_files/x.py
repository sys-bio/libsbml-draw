from libsbml_draw.model.sbml_layout import SBMLlayout
import glob

files = glob.glob('*.xml')
print(files)
# [SBMLlayout(i).drawNetwork() for i in files]

s = SBMLlayout('BIOMD0000000007_url.xml')
x = s.getCompartmentIds()
print(x)
s.drawNetwork('out.png')
