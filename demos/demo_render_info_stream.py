import libsbml

info = libsbml.LocalRenderInformation()

stream = libsbml.XMLInputStream("/Development/sbwBuild/source/SBMLLayout/SBMLExtension/SBGNstyles.xml")

info.read(stream)

