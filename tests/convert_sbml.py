import tesbml as libsbml
import unittest
import site
import os
site.addsitedir(os.path.dirname(__file__))

import tellurium as te

from add_to_path import add_to_path
add_to_path()
from libsbml_draw.layout import SBMLlayout


f = r'sbmlmodel.xml'

def convertToLatestSBMLVersion(f):
    doc = libsbml.readSBML(f)
    latestLevel = doc.getDefaultLevel()
    latestVersion = doc.getDefaultVersion()
    print(doc.getLevel(), doc.getVersion())
    doc.setLevelAndVersion(3, 1)
    print(doc.getLevel(), doc.getVersion())
    libsbml.writeSBML(doc, f)

# convertToLatestSBMLVersion(f)


f = 'model.xml'
# doc = libsbml.readSBML(f)
# print(doc.getLevel(), doc.getVersion())
# doc.setLevelAndVersion(3, 1)
# libsbml.writeSBML(doc, 'f.xml')
# print(doc.getLevel(), doc.getVersion())
#
# print(doc)

d = SBMLlayout(os.path.abspath(f))
print(d)

















