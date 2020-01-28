from pathlib import Path
import pkg_resources

from libsbml_draw.sbml_layout import SBMLlayout

model_file_name = "model.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/libs/" + model_file_name))

s = SBMLlayout(str(model_file))

# s._describeModel()

s.setNodeFontSize('all', 15)
s.setReactionCurveWidth ('all', 3)
s.setNodeColor('all', 'red')
s.setNodeFontColor ('all', 'white')

s.drawNetwork()

s.regenerateLayout()

s.drawNetwork()