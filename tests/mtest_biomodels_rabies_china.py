from libsbml_draw.model.sbml_layout import SBMLlayout

model_file_name = "rabies.xml"



sl = SBMLlayout(model_file_name, applyRender=False)

sl._describeModel()


sl.drawNetwork("rabies_China.pdf")
