# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:53:59 2019

@author: Veronica Porubsky

Title: Test random network generator
"""
import unittest
import tellurium as te
from randMANetGen import randMANetGen  # imports the random network generator function
from lxml import etree
from bs4 import BeautifulSoup


class RandMANetGenTests(unittest.TestCase):

    def setUp(self) -> None:
        """
        Generate random network
        :return:
        """
        # Specify number of species, number of reactions, number of floating and boundary species in randMANetGen function call
        sbmlMod = randMANetGen(numSpecies=8, numReactions=4)  # assign SBML string to 'sbmlMod'
        r = te.loadSBMLModel(sbmlMod)  # load SBML model with tellurium to generate roadrunner instance, 'r'
        r.exportToSBML('random_network.xml',
                       current=True)  # exports SBML model (.xml) named 'examplenetwork' to current directory
        self.r = r

        self.xml = BeautifulSoup(sbmlMod, 'lxml')

    def test_number_of_species(self):
        expected = 8
        actual = len(self.xml.find_all('species'))
        self.assertEqual(expected, actual)

    def test_number_of_reactions(self):
        expected = 4
        actual = len(self.xml.find_all('reaction'))
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
