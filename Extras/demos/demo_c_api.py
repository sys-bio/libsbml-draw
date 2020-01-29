#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pathlib import Path
import pkg_resources

model_file_name = "model.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/libs/" + model_file_name))


import libsbml_draw.sbnw as sbnw

print(sbnw.getCurrentLibraryVersion())

#model_file = "/Users/natalieh/repos/libsbml-draw/model_files/model.xml"

h_model = sbnw.loadSBMLFile(str(model_file))

print(h_model)

# h_lo_info = sbnw.processLayout(h_model)

h_model_new = sbnw.SBMLModel_newp()

print(h_model_new)

print(sbnw.arrowheadStyleGetNumVerts(1))

doc = sbnw.readSBMLFromFile(str(model_file))


out_file_name = "/home/radix/tmp/model.xml"

sbnw.writeSBMLToFile(doc, out_file_name)


print("substrate: ", sbnw.GF_ROLE_SUBSTRATE)
print("substrate: ", sbnw.GF_ROLE_INHIBITOR)

print("x == 0: ", sbnw.GF_ROLE_SUBSTRATE == 0)

print("type roles: ", type(sbnw.ROLES), ", ", len(sbnw.ROLES))
