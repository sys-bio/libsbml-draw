import libsbml

info = libsbml.LocalRenderInformation()

#stream = libsbml.XMLInputStream("/Development/sbwBuild/source/SBMLLayout/SBMLExtension/SBGNstyles.xml")
stream = libsbml.XMLInputStream("SBGNstyles.xml")

info.read(stream)

print("lri: ", info.getLevel(), info.getVersion())

les = info.getListOfLineEndings()

print("les: ", type(les), len(les))



