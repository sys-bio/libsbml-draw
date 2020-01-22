# import libsbml
from bs4 import BeautifulSoup
import os

class Patch:
    """

    A couple of items were not working in the original code and I had problems recompiling the
    C end. To get around this problem, for now, we will directly use libsbml. This class
    contains the required methods
    """

    def __init__(self, sbml):
        self.sbml = sbml  # an sbml string
        # self._doc = self.read_into_libsbml()
        # self._model = self._doc.getModel()
        if self.sbml.startswith('<?xml'):
            self._soup = BeautifulSoup(self.sbml, 'lxml')
        elif os.path.isfile(self.sbml):
            with open(self.sbml, 'r') as f:
                self._soup = BeautifulSoup(f.read())
        else:
            raise ValueError('I dont know how to read this sbml argument')

        self.compartment_ids = self.get_compartments_with_bs4()
        self.boundary_species_ids, self.floating_species_ids = self.get_species_with_bs4()

    def read_into_libsbml(self):
        """

        Returns: an sbml document from libsbml
        """
        reader = libsbml.SBMLReader()
        return reader.readSBMLFromString(self.sbml)

    def get_compartments(self):
        """
        From this example, we should be able to get
        compartments:
        http://sbml.org/Software/libSBML/5.18.0/docs/python-api/print_notes_8py-example.html

        Returns:

        """
        print("num compartments: ", self._model.getNumCompartments())
        return [self._model.getCompartment(i) for i in range(self._model.getNumCompartments())]

    def get_floating_species(self):
        for i in range(self._model.getNumSpecies()):
            print(self._model.getSpecies(i))

    def get_compartments_with_bs4(self):
        compartments = self._soup.find_all('compartment')
        return [i['id'] for i in compartments]

    def get_species_with_bs4(self):
        species = self._soup.find_all('species')
        boundary_species = [i['id'] for i in species if i['boundarycondition'] == 'true']
        floating_species = [i['id'] for i in species if i['boundarycondition'] == 'false']
        assert len(boundary_species) + len(floating_species) == len(species)
        return boundary_species, floating_species
