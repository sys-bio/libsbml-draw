import unittest

from libsbml_draw.model.sbml_layout import ValidatedDict


class ValidatedDictChild(ValidatedDict):
    name: str = 'Jim'


class ValidatedDictTests(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_instantiation_of_base(self):
        cheese = ValidatedDict(cheese='blue')
        expected = 'blue'
        actual = list(cheese.values())[0]
        self.assertEqual(expected, actual)

    def test_error_in_base(self):
        cheese = ValidatedDict(cheese='blue')
        with self.assertRaises(TypeError):
            cheese['american'] = 'plastic'

    def test_ValidatedDictChild(self):
        child = ValidatedDict(cheese='blue')
        self.assertEqual('blue', child['cheese'])


if __name__ == '__main__':
    unittest.main()
