#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import pkg_resources

from libsbml_draw import SBMLlayout


model_file_name = "model.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/data/" + model_file_name))

sl = SBMLlayout(str(model_file))


sl._describeModel()




