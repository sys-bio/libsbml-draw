# todo the cpp and include folder literally do nothing. They have nver been compiled. Delete them.

import libsbml_draw.sbnw as sbnw
from libsbml_draw.layout import SBMLlayout
from libsbml_draw.render import Render
from libsbml_draw.styles import Style, black_and_white
from libsbml_draw.utils import biomodels_download

# turn off matplotlib debugging messages
import logging

mpl_logger = logging.getLogger('matplotlib')
mpl_logger.setLevel(logging.WARNING)

MAJOR = 0
MINOR = 0
MICRO = 17

__version__ = f"{MAJOR}.{MICRO}.{MICRO}"
