from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

small_models = ["model.xml", 
                "largerpathway.xml",
                "modexmpl.xml",
                "random_network_5s_8r.xml",
                "random_network_5s_6r.xml"
                ]

for model_file_name in small_models:
    
    model_file = Path(pkg_resources.resource_filename(
            "libsbml_draw", "model/data/" + model_file_name))

    sl = SBMLlayout(str(model_file))

    sl._describeModel()

    sl.drawNetwork()
    
    