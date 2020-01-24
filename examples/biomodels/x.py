import os, glob
from libsbml_draw.model.sbml_layout import SBMLlayout
files = glob.glob(os.path.join(os.path.dirname(__file__), '*.xml'))
print(files)

