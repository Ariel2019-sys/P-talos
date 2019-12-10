import unittest
from .prueba import prueba


class TestPrueba(unittest.TestCase):
    def test_sumar(self):
        self.assertAlmostEqual(prueba(7,4),11)
        self.assertAlmostEqual(prueba(7,3),10)
        self.assertAlmostEqual(prueba(2,4),2) 