import tesbml as libsbml



f = r'sbmlmodel.xml'

def convertToLatestSBMLVersion(f):
    doc = libsbml.readSBML(f)
    latestLevel = doc.getDefaultLevel()
    latestVersion = doc.getDefaultVersion()
    print(doc.getLevel(), doc.getVersion())
    doc.setLevelAndVersion(3, 1)
    print(doc.getLevel(), doc.getVersion())
    libsbml.writeSBML(doc, f)

convertToLatestSBMLVersion(f)

















