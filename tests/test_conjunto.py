import unittest
from KataTDD.conjunto import Conjunto

class TestConjunto(unittest.TestCase):
    
    def test_conjunto_vacio(self):
        newConjunto = Conjunto([])
        self.assertIsNone(newConjunto.promedio())