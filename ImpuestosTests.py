# Todas las prueba sunitarias importan la biblioteca unittest
import unittest

# Las pruebas importan los modulos que hacen el trabajo
import Logica

class ImpuestosTest(unittest.TestCase):

    def test_impuesto1(self):

        #Datos de entrada
        TILA: int = 15600000
        OIGA: int = 9600000
        OINGA: int = 516000
        VRFA: int = 600000
        PSSA: int = 624000
        APA: int = 624000
        PCHA: int = 0
        VDA: int = 0
        GEA: int = 0

        #Proceso
        resultado = Logica.calcularImpuesto(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA)

        #Datos de salida esperados
        