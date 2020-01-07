import site
site.addsitedir('../src/python')

from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "BIOMD0000000013_url.xml"
# Poolman2004_CalvinCycle


sl = SBMLlayout(model_file_name, applyRender=False)

sl._describeModel()

#sl.drawNetwork("plant_metabolism.pdf")

sl.aliasNode("ATP_ch")
sl.aliasNode("ADP_ch")
sl.aliasNode("GAP_ch")
sl.aliasNode("PGA_ch")


sl.regenerateLayout()

sl.drawNetwork("plant_metabolism_alias.pdf")

