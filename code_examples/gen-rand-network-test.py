# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:53:59 2019

@author: Veronica Porubsky

Title: Test random network generator
"""
import tellurium as te
from randMANetGen import randMANetGen # imports the random network generator function
#import tesbml # need this library to help read SBML models

#%% Generate random network
# specify number of species, number of reactions, number of floating and boundary species in randMANetGen function call
sbmlMod = randMANetGen(numSpecies = 5, numReactions = 4) # assign SBML string to 'sbmlMod' 
r = te.loadSBMLModel(sbmlMod) # load SBML model with tellurium to generate roadrunner instance, 'r'
r.exportToSBML('random_network_5s_4r.xml', current = True) # exports SBML model (.xml) named 'examplenetwork' to current directory
