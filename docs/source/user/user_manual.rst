User Guide
============

Sample session in libsbml_draw
--------------------------------
from libsbml_draw import SBMLlayout

s = SBMLlayout("original_sbml_model.xml")

s.drawNetwork("my_sbml_model.pdf")

s.writeSBML("my_sbml_model.xml")
