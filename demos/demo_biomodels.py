from pathlib import Path
import pkg_resources

from libsbml_draw.model.sbml_layout import SBMLlayout

bio_models = ["BIOMD0000000042_url.xml",
              "BIOMD0000000061_url.xml",
              "BIOMD0000000247_url.xml",
              "BIOMD0000000281_url.xml", 
              "BIOMD0000000606_url.xml",
              "BIOMD0000000691_url.xml",
              "MODEL1202170000_url.xml",
              "MODEL1209260000_url.xml",
              "MODEL1303260016_url.xml",
              "MODEL1504290001_url.xml"
              ]

bio_models = ["BIOMD0000000393_url.xml",
              "BIOMD0000000051_url.xml"]


for model_file_name in bio_models:
    
    model_file = Path(pkg_resources.resource_filename(
            "libsbml_draw", "model/data/" + model_file_name))

    sl = SBMLlayout(str(model_file))

    sl._describeModel()

    sl.drawNetwork(scaling_factor=.5)

#    sl.aliasNode("ADP")
    
    