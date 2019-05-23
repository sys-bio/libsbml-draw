"""Test libsbml_draw on an SBML file which has a complicated node structure.
"""
from pathlib import Path
import pkg_resources

from libsbml import SBMLReader, SBMLValidator

from libsbml_draw.model.sbml_layout import SBMLlayout

MODEL_FILE_NAME = "complicated_nodes.xml"

MODEL_FILE = Path(pkg_resources.resource_filename(
        "libsbml_draw",
        "model/data/" + MODEL_FILE_NAME))

print("model file: ", str(MODEL_FILE))

SL = SBMLlayout(str(MODEL_FILE))


def test_complicated_nodes():
    SL.drawNetwork()

