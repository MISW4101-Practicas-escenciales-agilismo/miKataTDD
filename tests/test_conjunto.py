import unittest
from KataTDD.conjunto import Conjunto

class TestConjunto(unittest.TestCase):
    
    def test_conjunto_vacio(self):
        newConjunto = Conjunto([])
        self.assertIsNone(newConjunto.promedio())

    def test_conjunto_un_elemento(self):
        newConjunto = Conjunto([4])
        self.assertEqual(newConjunto.promedio(),4)