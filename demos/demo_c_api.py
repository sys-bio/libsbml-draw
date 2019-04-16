#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 11:32:39 2019

@author: natalieh
"""

import libsbml_draw.c_api.sbnw_c_api as sbnw

print(sbnw.getCurrentLibraryVersion())

model_file = "/Users/natalieh/repos/libsbml-draw/model_files/model.xml"

h_model = sbnw.loadSBML(model_file)

print(h_model)

# h_lo_info = sbnw.processLayout(h_model)

h_model_new = sbnw.SBMLModel_newp()

print(h_model_new)

print(sbnw.arrowheadStyleGetNumVerts(1))





