import tellurium as te
import numpy as np # needed for matrices
import random # needed to choose random number
import networkx as nx # needed for graph theory - used to find subnetworks


def randMANetGen(numReactions = None, numSpecies = None, numFloating = None, numBoundary = None, reactionTypeWeights = [1, 1, 1, 1], acceptOrphans = False, acceptSubnetworks = False):
    """
    Author: Megan Freer, Veronica Porubsky
    
    Generates a random network with a defined number of floating and boundary species.
    
    The user has the option of accepting networks that have orphan species or 
    independent, disconnected subnetworks. 
    
    If orphan species are allowed, the user should note that the specified number
    of floating and boundary species may not be adhered to.
    
    Inputs:
        
    numReactions : int
        Specifies the number of mass-action reactions in the network.
    
    numSpecies : int
        Specifies total number of species in the network, including both 
        floating and boundary species.
             
    numFloating : int
        Specifies the number of floating species in the network.
    
    numBoundary : int
        Specifies the number of boundary species in the network.
        
    reactionTypeWeights : list
        Changes the probability of selecting a given reaction type by applying 
        a weight to each. All four mass-action reaction types should be specified 
        with a scalar of type int in the following order: 
        reactionTypeWeights = [uni-uni, uni-bi, bi-uni, bi-bi]. For example, 
        if the following is entered: reactionTypeWeights = [10, 30, 40, 20]
        the approximate frequencies would be computed by dividing each entry
        by the sum of all entries, such that the approximate frequency of 
        the types are uni-uni: 10/100 = 0.1, uni-bi: 30/100 = 0.3, bi-uni:
        40/100 = 0.4, bi-bi: 20/100 = 0.2. 
        
        Note: these are the approximate frequencies that would be observed if 
        a population of random networks generated under these conditions 
        were analyzed.
        
    acceptOrphans : bool
        Determines whether networks containing orphans will be returned to user.
        If acceptOrphans = False, genRandNetwork will continue to generate 
        random networks until a network is created that contains no orphans.
        
        Note: for very large networks, or networks with a large ratio of 
        number of species to number of reactions, removing networks with orphaned
        species will substantially increase computational costs.

    acceptSubnetworks : bool
        Determines whether networks containing disconnected subnetworks will be 
        returned to user. If acceptSubnetworks = False, genRandNetwork will 
        continue to generate random networks until a fully-connected network is
        returned.
        
        Note: for very large networks, or networks with a large ratio of 
        number of species to number of reactions, removing networks with 
        disconnected subnetworks will substantially increase computational costs.

    Outputs:
            
    randomNetwork : str
        Returns a random network model as an Antimony string, which can 
        be loaded for simulation using the functionality available in Tellurium. 
        
    """
    numSpecies = checkInputs(numReactions, numSpecies, numFloating, numBoundary, reactionTypeWeights, acceptOrphans)
    interactionCount, antStr = getNetwork(numReactions, numSpecies, numFloating, numBoundary, reactionTypeWeights)
    orphans = hasOrphans(interactionCount)
    subnetworks = hasSubnetworks(interactionCount)
    if not acceptOrphans and not acceptSubnetworks:
        while (orphans == True or subnetworks == True):
            interactionCount, antStr = getNetwork(numReactions, numSpecies, numFloating, numBoundary, reactionTypeWeights)
            orphans = hasOrphans(interactionCount)
            subnetworks = hasSubnetworks(interactionCount)            
    elif acceptOrphans and not acceptSubnetworks:   
        while subnetworks == True:
            interactionCount, antStr = getNetwork(numReactions, numSpecies, numFloating, numBoundary, reactionTypeWeights)
            subnetworks = hasSubnetworks(interactionCount)
    elif acceptSubnetworks and not acceptOrphans:
        while orphans == True:
            interactionCount, antStr = getNetwork(numReactions, numSpecies, numFloating, numBoundary, reactionTypeWeights)
            subnetworks = hasSubnetworks(interactionCount)
            orphans = hasOrphans(interactionCount)  
    loadedNet = te.loada(antStr)
    randMANetModel = loadedNet.getCurrentSBML()
    # Pass randMANetModel SBML to Natalie's code
    # Generate plot, return as an object named randMANetPlot that can be stored by user and shown later
    return randMANetModel #, randMANetPlot

def checkInputs(numReactions, numSpecies, numFloating, numBoundary, reactionTypeWeights, acceptOrphans):
    # Checks that numReactions and either numSpecies or both numFloating and numBoundary are specified
    if (not numSpecies and not (numFloating and numBoundary)) or not numReactions:
        raise RuntimeError('Must specify either the total number of species (numSpecies) or both the number of floating (numFloating) and boundary species (numBoundary). The number of reactions must always be specified by the user.')
    # If numSpecies is not specified, compute the total number from the floating and boundary components
    if not numSpecies:
        numSpecies = numFloating + numBoundary
    # If numFloating, numBoundary, and numSpecies are all specified, if numSpecies
    # does not equal the sum of the floating and boundary components, reset 
    # numSpecies to this sum
    if (numFloating and numBoundary) and numSpecies:
        if not numSpecies == numFloating + numBoundary:
            numSpecies = numFloating + numBoundary
    # If the total number of species is not a multiple of 4, the number of reactions 
    # must be greater than or equal to the floor value of the total number
    # of species divided by 4, plus 1.
    if int(numSpecies/4) < (numSpecies/4):
        if (not numReactions >= (int(numSpecies/4) + 1)) and acceptOrphans == False:
            raise RuntimeError('There are not enough reactions to construct a network without orphan species. Increase the number of reactions.')
    # If the total number of species is a multiple of 4, the number of reactions 
    # must be greater than or equal to the total number of species divided by 4.
    elif int(numSpecies/4) == numSpecies/4:
        if (not numReactions >= (numSpecies/4)) and acceptOrphans == False:
            raise RuntimeError('There are not enough reactions to construct a network without orphan species. Increase the number of reactions.')
    # Check that all reaction type weights are integer values. 
    if not all(isinstance(x, int) for x in reactionTypeWeights):
        raise RuntimeError('reactionTypeWeights list must contain only integer values.')
    return numSpecies

def getNetwork(numReactions, numSpecies, numFloating, numBoundary, reactionTypeWeights):
    uniUniFreq, uniBiFreq, biUniFreq, biBiFreq = reactionTypeWeights
    reactionTypeList = ['uni-uni'] * uniUniFreq + ['uni-bi'] * uniBiFreq + ['bi-uni'] * biUniFreq + ['bi-bi'] * biBiFreq
    random.shuffle(reactionTypeList)
    # make matrix containing the number of occurences for each species in each reaction
    # number of rows = numReactions
    # number of columns = numSpecies
    interactionCount = np.zeros((numReactions, numSpecies)) # initializes to all zeros
    speciesArray = np.zeros(numSpecies)
    numBoundaryChosen = 0 # starts at 0
    if not numBoundary:
        numBoundary = random.randint(1, numSpecies - 1)
        numFloating = numSpecies - numBoundary
    # choose which are boundary species- 1 in array means boundary
    while numBoundaryChosen < numBoundary:
            randomPosition = random.randint(0, numSpecies - 1) # choose random position in speciesArray
            if speciesArray[randomPosition] != 1:
                speciesArray[randomPosition] = 1
                numBoundaryChosen += 1
    
    # floating species
    antStr = "var "
    currentFloatingNum = 0 # used for fencepost problem with commas
    for currentSpeciesNum in range(numSpecies):
        if speciesArray[currentSpeciesNum] == 0: # if floating
            antStr += "S" + str(currentSpeciesNum)
            currentFloatingNum += 1
            if currentFloatingNum != numFloating: # if not the last floating species- fence post problem
                antStr += ", "
    
    # boundary species
    antStr += "\next "
    currentBoundaryNum = 0 # used for fencepost problem with commas
    for currentSpeciesNum in range(numSpecies):
        if speciesArray[currentSpeciesNum] == 1: # if boundary
            antStr += "S" + str(currentSpeciesNum)
            currentBoundaryNum += 1
            if currentBoundaryNum != numBoundary: # if not the last boundary species- fence post problem
                antStr += ", "
     
    antStr += ";\n"
    for currentReactionNum in range(numReactions): # loops through for each reaction
        reactionType = random.choice(reactionTypeList)
        # 'uni-uni' = unimolecular-unimolecular: A -> B
        # 'uni-bi' = unimolecular-bimolecular: A -> B + C
        # 'bi-uni' = bimolecular-unimolecular: A + B -> C
        # 'bi-bi' = bimolecular-bimolecular: A + B -> C + D
        
        if reactionType == 'uni-uni':
            # random A, B
            reactantNum = random.randint(0, numSpecies - 1)
            productNum = reactantNum # random staring value
            while productNum == reactantNum:
                productNum = random.randint(0, numSpecies - 1) # productNum cannot be same as reactantNum- exits loop when different
            
            interactionCount[currentReactionNum, reactantNum] += 1 # reactants negative
            interactionCount[currentReactionNum, productNum] += 1 # products positive
            
            # add reaction onto antStr
            antStr += "S" + str(reactantNum) + " -> S" + str(productNum) + "; "
            antStr += "k" + str(currentReactionNum) + "*S" + str(reactantNum) + "; \n"
        elif reactionType == 'uni-bi':
            # random A, B, C
            reactantNum = random.randint(0, numSpecies - 1)
            productNum1 = reactantNum # random starting value to enter while loop
            while productNum1 == reactantNum:
                productNum1 = random.randint(0, numSpecies - 1) # cannot be reactantNum
            productNum2 = reactantNum #random starting value to enter while loop
            while productNum2 == reactantNum:
                productNum2 = random.randint(0, numSpecies - 1) # cannot be reactantNum
            
            interactionCount[currentReactionNum, reactantNum] += 1 # reactants negative
            interactionCount[currentReactionNum, productNum1] += 1 # products positive
            interactionCount[currentReactionNum, productNum2] += 1 # products positive
            
            # add reaction onto antStr
            antStr += "S" + str(reactantNum) + " -> S" + str(productNum1) + " + S" + str(productNum2) + "; "
            antStr += "k" + str(currentReactionNum) + "*S" + str(reactantNum) + "; \n"
        
        elif reactionType == 'bi-uni':
            # random A, B, C
            reactantNum1 = random.randint(0, numSpecies - 1)
            reactantNum2 = random.randint(0, numSpecies - 1)
            productNum = reactantNum1 # random starting value
            while productNum == reactantNum1 or productNum == reactantNum2:
                productNum = random.randint(0, numSpecies - 1)
            
            interactionCount[currentReactionNum, reactantNum1] += 1 # reactants negative
            interactionCount[currentReactionNum, reactantNum2] += 1 # reactants negative
            interactionCount[currentReactionNum, productNum] += 1 # products positive
    
            # add reaction onto antStr
            antStr += "S" + str(reactantNum1) + " + S" + str(reactantNum2) + " -> S" + str(productNum) + "; "
            antStr += "k" + str(currentReactionNum) + "*S" + str(reactantNum1) + "*S" + str(reactantNum2) + "; \n"
            
        elif reactionType == 'bi-bi':
            # random A, B, C, D
            reactantNum1 = random.randint(0, numSpecies - 1)
            reactantNum2 = random.randint(0, numSpecies - 1)
            productNum1 = random.randint(0, numSpecies - 1)
            
            if reactantNum1 == reactantNum2:
                productNum2 = productNum1 # random number to enter into while loop
                while productNum1 == productNum2: # productNum1 cannot equal productNum2
                    productNum2 = random.randint(0, numSpecies - 1)
            elif productNum1 == reactantNum1:
                productNum2 = reactantNum2 # random number to enter into while loop
                while productNum2 == reactantNum2: # productNum2 cannot equal reactantNum2
                    productNum2 = random.randint(0, numSpecies - 1)
            elif productNum1 == reactantNum2:
                productNum2 = reactantNum1 # random number to enter into while loop
                while productNum2 == reactantNum1: # productNum2 cannot equal reactantNum1
                    productNum2 = random.randint(0, numSpecies - 1)
            else:       
                productNum2 = random.randint(0, numSpecies - 1)
            
            interactionCount[currentReactionNum, reactantNum1] += 1 # reactants negative
            interactionCount[currentReactionNum, reactantNum2] += 1 # reactants negative
            interactionCount[currentReactionNum, productNum1] += 1 # products positive
            interactionCount[currentReactionNum, productNum2] += 1 # products positive
    
            # add reaction onto antStr
            antStr += "S" + str(reactantNum1) + " + S" + str(reactantNum2) + " -> S" + str(productNum1) + " + S" + str(productNum2) + "; "
            antStr += "k" + str(currentReactionNum) + "*S" + str(reactantNum1) + "*S" + str(reactantNum2) + "; \n"
        
    antStr += "\n"  
    for currentReactionNum in range(numReactions): # loops through reactions and declares rate constants
        antStr += "k" + str(currentReactionNum) + " = " + str(10*random.random()) + "\n" # random number 1-10
    
    antStr += "\n"        
    for currentSpeciesNum in range(numSpecies): # loops through and initializes all species
        # if speciesArray[currentSpeciesNum] == 1: # if boundary species- declare starting value- took this out so no warning
        antStr += "S" + str(currentSpeciesNum) + " = " + str(10*random.random()) + "\n"
    
    outputList = [interactionCount, antStr]
    return outputList

def hasOrphans(interactionCount):
    orphans = False
    numRows, numCols = np.shape(interactionCount)
    for currentSpecies in range(numCols): # loop through columns
        numZeros = 0 # used for counting number of zeros in a column
        for currentReaction in range(numRows): # check if all rows 0
            if interactionCount[currentReaction, currentSpecies] == 0:
                numZeros += 1
        if numZeros == numRows: # if a column of all zeros
            orphans = True
    return orphans

def hasSubnetworks(interactionCount):
    subnetworks = False
    G = nx.Graph()
    G.clear()
    numRows, numCols = np.shape(interactionCount)
    speciesList = np.linspace(0, numCols, numCols + 1)
    for currentReaction in range(numRows): # each row is a reaction --> for each reaction run through all species
        for species1 in range(numCols): # each column is a species
            for species2 in range(numCols):
                if interactionCount[currentReaction, species1] != 0 and species1 != species2: 
                    if interactionCount[currentReaction, species2] != 0:
                        G.add_edge( 'S' + str(int(speciesList[species1])), 'S' + str(int(speciesList[species2])))
    numSubGraphs = len(list(nx.connected_components(G)))
    if numSubGraphs != 1:
        subnetworks = True
    return subnetworks 


if __name__ == '__main__':
    x = randMANetGen(numReactions=20, numSpecies=8, numBoundary=1, numFloating=7)
    with open("random_model.xml", 'w') as f:
        f.write(x)
