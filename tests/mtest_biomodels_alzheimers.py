import site
site.addsitedir('../src/python')

from libsbml_draw.model.sbml_layout import SBMLlayout


model_file_name = "BIOMD0000000091_url.xml"
# Proctor2005 - Actions of chaperones and their role in ageing


sl = SBMLlayout(model_file_name, applyRender=False)


sl._describeModel()



sl.drawNetwork("alzheimers_chaperones_aging.pdf")


