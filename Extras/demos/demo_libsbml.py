#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import pkg_resources

from libsbml import SBMLReader 


model_file_name = "example-network.xml"

model_file = Path(pkg_resources.resource_filename("libsbml_draw", "model/libs/" + model_file_name))

print("model file: ", model_file)
    
reader = SBMLReader()    

doc = reader.readSBMLFromFile(str(model_file))    

model = doc.getModel()

speciesList = model.getListOfSpecies()

print("num species: ", model.getNumSpecies())
print("num species: ", len(speciesList))


def getBoundarySpeciesIds(doc):

        model = doc.getModel()
        speciesList = model.getListOfSpecies()    
    
        boundarySpeciesIds = list()
    
        for species in speciesList:
            if species.getBoundaryCondition() == True:
                boundarySpeciesIds.append(species.getId())            

        return boundarySpeciesIds  


boundarySpeciesIds = getBoundarySpeciesIds(doc)

print("boundarySpeciesIds: \n", boundarySpeciesIds)


def getFloatingSpeciesIds(doc):
    
    model = doc.getModel()
    speciesList = model.getListOfSpecies()    
    
    floatingSpeciesIds = list()
    
    for species in speciesList:
        if species.getBoundaryCondition() == False:
            floatingSpeciesIds.append(species.getId())           
    
    return floatingSpeciesIds

    
floatingSpeciesIds = getFloatingSpeciesIds(doc)

print("floatingSpeciesIds: \n", floatingSpeciesIds)

