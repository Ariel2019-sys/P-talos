from django.test import TestCase
from .prueba import prueba,resta
# Create your tests here.



class TestPrueba(TestCase):
    def test_sumar(self):
        self.assertAlmostEqual(prueba(7,4),11)
        self.assertAlmostEqual(prueba(7,3),10)
        self.assertAlmostEqual(prueba(2,4),2)         
class TestPrueba2(TestCase):
    def test_restar(self):
        self.assertAlmostEqual(resta(9,2),7)
        self.assertAlmostEqual(resta(100,100),0)
        self.assertAlmostEqual(resta(50,70),-20)
