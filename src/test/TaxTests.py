# Todas las prueba sunitarias importan la biblioteca unittest
import unittest

# Las pruebas importan los modulos que hacen el trabajo
import sys
sys.path.append("src")

from Logic import TaxLogic
class ImpuestosTest(unittest.TestCase):


    #PRUEBAS UNITARIAS NORMALES

    def test_normal1(self):

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
        resultado = TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA)

        #Datos de salida esperados
        TIG = 25200000
        TING = 516000
        TCD = 1248000
        VPIR = 0


        #Validacion de datos
        self.assertEqual( TIG, resultado[0] )
        self.assertEqual( TING, resultado[1] )
        self.assertEqual( TCD, resultado[2] )
        self.assertEqual( VPIR, resultado[3] )
    

    def test_normal2(self):

        #Datos de entrada
        TILA: int = 24000000
        OIGA: int = 13000000
        OINGA: int = 0
        VRFA: int = 1000000
        PSSA: int = 960000
        APA: int = 960000
        PCHA: int = 9600000
        VDA: int = 200000
        GEA: int = 100000

        #Proceso
        resultado = TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA)

        #Datos de salida esperados
        TIG = 37000000
        TING = 0
        TCD = 11820000
        VPIR = 0


        #Validacion de datos
        self.assertEqual( TIG, resultado[0] )
        self.assertEqual( TING, resultado[1] )
        self.assertEqual( TCD, resultado[2] )
        self.assertEqual( VPIR, resultado[3] )

    
    def test_normal3(self):

        #Datos de entrada
        TILA: int = 60000000
        OIGA: int = 30000000
        OINGA: int = 1200000
        VRFA: int = 4000000
        PSSA: int = 2400000
        APA: int = 2400000
        PCHA: int = 0
        VDA: int = 0
        GEA: int = 10000000

        #Proceso
        resultado = TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA)

        #Datos de salida esperados
        TIG = 90000000
        TING = 1200000
        TCD = 14800000
        VPIR = 2300000


        #Validacion de datos
        self.assertEqual( TIG, resultado[0] )
        self.assertEqual( TING, resultado[1] )
        self.assertEqual( TCD, resultado[2] )
        self.assertEqual( VPIR, resultado[3] )

    
    def test_normal4(self):

        #Datos de entrada
        TILA: int = 96000000
        OIGA: int = 35500000
        OINGA: int = 3000000
        VRFA: int = 4800000
        PSSA: int = 3840000
        APA: int = 3840000
        PCHA: int = 12000000
        VDA: int = 0
        GEA: int = 1000000

        #Proceso
        resultado = TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA)

        #Datos de salida esperados
        TIG = 131500000
        TING = 3000000
        TCD = 20680000
        VPIR = 4305000


        #Validacion de datos
        self.assertEqual( TIG, resultado[0] )
        self.assertEqual( TING, resultado[1] )
        self.assertEqual( TCD, resultado[2] )
        self.assertEqual( VPIR, resultado[3] )

    
    def test_normal5(self):

        #Datos de entrada
        TILA: int = 120000000
        OIGA: int = 0
        OINGA: int = 5000000
        VRFA: int = 5000000
        PSSA: int = 4800000
        APA: int = 4800000
        PCHA: int = 1300000
        VDA: int = 3000000
        GEA: int = 7000000

        #Proceso
        resultado = TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA)

        #Datos de salida esperados
        TIG = 120000000
        TING = 5000000
        TCD = 20900000
        VPIR = 1900000


        #Validacion de datos
        self.assertEqual( TIG, resultado[0] )
        self.assertEqual( TING, resultado[1] )
        self.assertEqual( TCD, resultado[2] )
        self.assertEqual( VPIR, resultado[3] )

    
    def test_normal6(self):

        #Datos de entrada
        TILA: int = 420000000
        OIGA: int = 180000000
        OINGA: int = 10000000
        VRFA: int = 120000000
        PSSA: int = 16800000
        APA: int = 16800000
        PCHA: int = 36000000
        VDA: int = 5000000
        GEA: int = 24000000

        #Proceso
        resultado = TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA)

        #Datos de salida esperados
        TIG = 600000000
        TING = 10000000
        TCD = 98600000
        VPIR = 15400000


        #Validacion de datos
        self.assertEqual( TIG, resultado[0] )
        self.assertEqual( TING, resultado[1] )
        self.assertEqual( TCD, resultado[2] )
        self.assertEqual( VPIR, resultado[3] )
    


    #PRUEBAS UNITARIAS EXTRAORDINARIAS
    
    def test_extraordinario1(self):

        #Ingresos no gravables son mayores

        #Datos de entrada
        TILA: int = 15600000
        OIGA: int = 0
        OINGA: int = 20000000
        VRFA: int = 600000
        PSSA: int = 624000
        APA: int = 624000
        PCHA: int = 0
        VDA: int = 0
        GEA: int = 0

        #Proceso
        resultado = TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA)

        #Datos de salida esperados
        TIG = 15600000
        TING = 20000000
        TCD = 1248000
        VPIR = 0


        #Validacion de datos
        self.assertEqual( TIG, resultado[0] )
        self.assertEqual( TING, resultado[1] )
        self.assertEqual( TCD, resultado[2] )
        self.assertEqual( VPIR, resultado[3] )

    
    def test_extraordinario2(self):

        #Ganarse la loteria

        #Datos de entrada
        TILA: int = 15600000
        OIGA: int = 5000000000
        OINGA: int = 0
        VRFA: int = 1000000
        PSSA: int = 624000
        APA: int = 624000
        PCHA: int = 0
        VDA: int = 0
        GEA: int = 20000000

        #Proceso
        resultado = TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA)

        #Datos de salida esperados
        TIG = 5015600000
        TING = 0
        TCD = 21248000
        VPIR = 931716000


        #Validacion de datos
        self.assertEqual( TIG, resultado[0] )
        self.assertEqual( TING, resultado[1] )
        self.assertEqual( TCD, resultado[2] )
        self.assertEqual( VPIR, resultado[3] )
    

    def test_extraordinario3(self):

        #Perdida en otros ingresos gravables

        #Datos de entrada
        TILA: int = 70000000
        OIGA: int = -100000000
        OINGA: int = 0
        VRFA: int = 4800000
        PSSA: int = 2800000
        APA: int = 2800000
        PCHA: int = 12000000
        VDA: int = 0
        GEA: int = 15000000

        #Proceso
        resultado = TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA)

        #Datos de salida esperados
        TIG = -30000000
        TING = 0
        TCD = 32600000
        VPIR = 0


        #Validacion de datos
        self.assertEqual( TIG, resultado[0] )
        self.assertEqual( TING, resultado[1] )
        self.assertEqual( TCD, resultado[2] )
        self.assertEqual( VPIR, resultado[3] )

    
    def test_extraordinario4(self):

        #Donaciones de alto valor

        #Datos de entrada
        TILA: int = 30000000
        OIGA: int = 15000000
        OINGA: int = 5000000
        VRFA: int = 3000000
        PSSA: int = 1200000
        APA: int = 1200000
        PCHA: int = 10000000
        VDA: int = 50000000
        GEA: int = 0

        #Proceso
        resultado = TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA)

        #Datos de salida esperados
        TIG = 45000000
        TING = 5000000
        TCD = 62400000
        VPIR = 0


        #Validacion de datos
        self.assertEqual( TIG, resultado[0] )
        self.assertEqual( TING, resultado[1] )
        self.assertEqual( TCD, resultado[2] )
        self.assertEqual( VPIR, resultado[3] )

    
    def test_extraordinario5(self):

        #Herencia

        #Datos de entrada
        TILA: int = 24000000
        OIGA: int = 9600000
        OINGA: int = 350000000
        VRFA: int = 1500000
        PSSA: int = 960000
        APA: int = 960000
        PCHA: int = 500000
        VDA: int = 0
        GEA: int = 5000000

        #Proceso
        resultado = TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA)

        #Datos de salida esperados
        TIG = 33600000
        TING = 350000000
        TCD = 7420000
        VPIR = 0


        #Validacion de datos
        self.assertEqual( TIG, resultado[0] )
        self.assertEqual( TING, resultado[1] )
        self.assertEqual( TCD, resultado[2] )
        self.assertEqual( VPIR, resultado[3] )

    
    def test_extraordinario6(self):

        #Gastos extraordinarios en educacion

        #Datos de entrada
        TILA: int = 17000000
        OIGA: int = 5000000
        OINGA: int = 0
        VRFA: int = 1500000
        PSSA: int = 680000
        APA: int = 680000
        PCHA: int = 1000000
        VDA: int = 800000
        GEA: int = 20000000

        #Proceso
        resultado = TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA)

        #Datos de salida esperados
        TIG = 22000000
        TING = 0
        TCD = 23160000
        VPIR = 0


        #Validacion de datos
        self.assertEqual( TIG, resultado[0] )
        self.assertEqual( TING, resultado[1] )
        self.assertEqual( TCD, resultado[2] )
        self.assertEqual( VPIR, resultado[3] )


    
    #PRUEBAS UNITARIAS DE ERROR
        
    def test_error1(self):

        #Retencion en la fuente superior a los ingresos laborales

        #Datos de entrada
        TILA: int = 15000000
        OIGA: int = 10000000
        OINGA: int = 1000000
        VRFA: int = 30000000
        PSSA: int = 600000
        APA: int = 600000
        PCHA: int = 0
        VDA: int = 0
        GEA: int = 5000000

        #Validacion
        self.assertRaises( TaxLogic.HigherIncomeRetentionException, TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA) )

    
    def test_error2(self):

        #Error por ingresar texto

        #Datos de entrada
        TILA: int = "Mil millones"
        OIGA: int = 0
        OINGA: int = 0
        VRFA: int = 0
        PSSA: int = 0
        APA: int = 0
        PCHA: int = 0
        VDA: int = 0
        GEA: int = 0

        #Validacion
        self.assertRaises( TaxLogic.InvalidEntryException, TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA) )

    
    def test_error3(self):

        #Error digitos muy grandes

        #Datos de entrada
        TILA: int = 8000000000
        OIGA: int = 1000000000
        OINGA: int = 3000000
        VRFA: int = 6000000
        PSSA: int = 320000000
        APA: int = 320000000
        PCHA: int = 0
        VDA: int = 0
        GEA: int = 0

        #Validacion
        self.assertRaises( TaxLogic.DigitsVeryLargeError, TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA) )

    
    def test_error4(self):

        #Error por datos obligatorios no agregados

        #Datos de entrada
        TILA: int = 0
        OIGA: int = 0
        OINGA: int = 0
        VRFA: int = 0
        PSSA: int = 0
        APA: int = 0
        PCHA: int = 0
        VDA: int = 0
        GEA: int = 0

        #Validacion
        self.assertRaises( TaxLogic.DataNotAggregatedError, TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA) )

    
    def test_error5(self):

        #Error por deduccibles negativos

        #Datos de entrada
        TILA: int = 15000000
        OIGA: int = 0
        OINGA: int = 0
        VRFA: int = 500000
        PSSA: int = 600000
        APA: int = 600000
        PCHA: int = -15000000
        VDA: int = 0
        GEA: int = 0

        #Validacion
        self.assertRaises( TaxLogic.DeductiblesNegativeError, TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA) )

    
    def test_error6(self):

        #No ingresar los activos

        #Datos de entrada
        TILA: int = 0
        OIGA: int = 0
        OINGA: int = 0
        VRFA: int = 4000000
        PSSA: int = 0
        APA: int = 0
        PCHA: int = 2000000
        VDA: int = 0
        GEA: int = 0

        #Validacion
        self.assertRaises( TaxLogic.AssetsNotEnteredException, TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA) )

    
    def test_error7(self):

        #Ingresar un valor negativo en los ingresos.

        #Datos de entrada
        TILA: int = -15600000
        OIGA: int = -1000000
        OINGA: int = -300000
        VRFA: int = 0
        PSSA: int = -624000
        APA: int = -624000
        PCHA: int = 0
        VDA: int = 0
        GEA: int = 0

        #Validacion
        self.assertRaises( TaxLogic.NegativeValueEnteredException, TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA) )

    
    def test_error8(self):

        #Caso de error en caso de ingresar cifras no coherentes

        #Datos de entrada
        TILA: int = 0.000525
        OIGA: int = 0
        OINGA: int = 0
        VRFA: int = 0
        PSSA: int = 0
        APA: int = 0
        PCHA: int = 0
        VDA: int = 0
        GEA: int = 0

        #Validacion
        self.assertRaises( TaxLogic.IncoherentFiguresExpection, TaxLogic.CalculateTax(TILA, OIGA, OINGA, VRFA, PSSA, APA, PCHA, VDA, GEA) )



# Este fragmento de codigo permite ejecutar la prueba individualmente
        
if __name__ == '__main__':
    unittest.main()