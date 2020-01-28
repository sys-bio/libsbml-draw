from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

medium_models = ["random_network_12s_12r.xml",
                 "veronica-network.xml",
                 "TCA_ecoli_glucose_BIOMD222_url.xml",
                 ]


for model_file_name in medium_models:
    
    model_file = Path(pkg_resources.resource_filename(
            "libsbml_draw", "model/data/" + model_file_name))

    sl = SBMLlayout(str(model_file))

    sl.describeModel()

    sl.drawNetwork()

