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
        totalLaborIncomePerYear: int = 15600000
        otherTaxableIncomePerYear: int = 9600000
        otherNonTaxableIncomePerYear: int = 516000 
        sourceRetentionValuePerYear: int = 600000 
        socialSecurityPaymentInTheYear: int = 624000 
        pensionContributionsInTheYear: int = 624000 
        mortgageLoanPaymentPerYear: int = 0 
        donationValuePerYear: int = 0 
        educationalExpensesPerYear: int = 0 

        #Proceso
        result = TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear)

        #Datos de salida esperados
        totalTaxedIncome = 25200000 
        totalUntaxedIncome = 516000 
        totalDeductibleCosts = 1248000 
        amountToPayIncomeTaxes = 0 


        #Validacion de datos
        self.assertEqual( totalTaxedIncome, result[0] )
        self.assertEqual( totalUntaxedIncome, result[1] )
        self.assertEqual( totalDeductibleCosts, result[2] )
        self.assertEqual( amountToPayIncomeTaxes, result[3] )
    

    def test_normal2(self):

        #Datos de entrada
        totalLaborIncomePerYear: int = 24000000
        otherTaxableIncomePerYear: int = 13000000
        otherNonTaxableIncomePerYear: int = 0
        sourceRetentionValuePerYear: int = 1000000
        socialSecurityPaymentInTheYear: int = 960000
        pensionContributionsInTheYear: int = 960000
        mortgageLoanPaymentPerYear: int = 9600000
        donationValuePerYear: int = 200000
        educationalExpensesPerYear: int = 100000

        #Proceso
        result = TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear)

        #Datos de salida esperados
        totalTaxedIncome = 37000000
        totalUntaxedIncome = 0
        totalDeductibleCosts = 11820000
        amountToPayIncomeTaxes = 0


        #Validacion de datos
        self.assertEqual( totalTaxedIncome, result[0] )
        self.assertEqual( totalUntaxedIncome, result[1] )
        self.assertEqual( totalDeductibleCosts, result[2] )
        self.assertEqual( amountToPayIncomeTaxes, result[3] )

    
    def test_normal3(self):

        #Datos de entrada
        totalLaborIncomePerYear: int = 60000000
        otherTaxableIncomePerYear: int = 30000000
        otherNonTaxableIncomePerYear: int = 1200000
        sourceRetentionValuePerYear: int = 4000000
        socialSecurityPaymentInTheYear: int = 2400000
        pensionContributionsInTheYear: int = 2400000
        mortgageLoanPaymentPerYear: int = 0
        donationValuePerYear: int = 0
        educationalExpensesPerYear: int = 10000000

        #Proceso
        result = TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear)

        #Datos de salida esperados
        totalTaxedIncome = 90000000
        totalUntaxedIncome = 1200000
        totalDeductibleCosts = 14800000
        amountToPayIncomeTaxes = 2300000


        #Validacion de datos
        self.assertEqual( totalTaxedIncome, result[0] )
        self.assertEqual( totalUntaxedIncome, result[1] )
        self.assertEqual( totalDeductibleCosts, result[2] )
        self.assertEqual( amountToPayIncomeTaxes, result[3] )

    
    def test_normal4(self):

        #Datos de entrada
        totalLaborIncomePerYear: int = 96000000
        otherTaxableIncomePerYear: int = 35500000
        otherNonTaxableIncomePerYear: int = 3000000
        sourceRetentionValuePerYear: int = 4800000
        socialSecurityPaymentInTheYear: int = 3840000
        pensionContributionsInTheYear: int = 3840000
        mortgageLoanPaymentPerYear: int = 12000000
        donationValuePerYear: int = 0
        educationalExpensesPerYear: int = 1000000

        #Proceso
        result = TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear)

        #Datos de salida esperados
        totalTaxedIncome = 131500000
        totalUntaxedIncome = 3000000
        totalDeductibleCosts = 20680000
        amountToPayIncomeTaxes = 4305000


        #Validacion de datos
        self.assertEqual( totalTaxedIncome, result[0] )
        self.assertEqual( totalUntaxedIncome, result[1] )
        self.assertEqual( totalDeductibleCosts, result[2] )
        self.assertEqual( amountToPayIncomeTaxes, result[3] )

    
    def test_normal5(self):

        #Datos de entrada
        totalLaborIncomePerYear: int = 120000000
        otherTaxableIncomePerYear: int = 0
        otherNonTaxableIncomePerYear: int = 5000000
        sourceRetentionValuePerYear: int = 5000000
        socialSecurityPaymentInTheYear: int = 4800000
        pensionContributionsInTheYear: int = 4800000
        mortgageLoanPaymentPerYear: int = 1300000
        donationValuePerYear: int = 3000000
        educationalExpensesPerYear: int = 7000000

        #Proceso
        result = TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear)

        #Datos de salida esperados
        totalTaxedIncome = 120000000
        totalUntaxedIncome = 5000000
        totalDeductibleCosts = 20900000
        amountToPayIncomeTaxes = 1900000


        #Validacion de datos
        self.assertEqual( totalTaxedIncome, result[0] )
        self.assertEqual( totalUntaxedIncome, result[1] )
        self.assertEqual( totalDeductibleCosts, result[2] )
        self.assertEqual( amountToPayIncomeTaxes, result[3] )

    
    def test_normal6(self):

        #Datos de entrada
        totalLaborIncomePerYear: int = 420000000
        otherTaxableIncomePerYear: int = 180000000
        otherNonTaxableIncomePerYear: int = 10000000
        sourceRetentionValuePerYear: int = 120000000
        socialSecurityPaymentInTheYear: int = 16800000
        pensionContributionsInTheYear: int = 16800000
        mortgageLoanPaymentPerYear: int = 36000000
        donationValuePerYear: int = 5000000
        educationalExpensesPerYear: int = 24000000

        #Proceso
        result = TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear)

        #Datos de salida esperados
        totalTaxedIncome = 600000000
        totalUntaxedIncome = 10000000
        totalDeductibleCosts = 98600000
        amountToPayIncomeTaxes = 15400000


        #Validacion de datos
        self.assertEqual( totalTaxedIncome, result[0] )
        self.assertEqual( totalUntaxedIncome, result[1] )
        self.assertEqual( totalDeductibleCosts, result[2] )
        self.assertEqual( amountToPayIncomeTaxes, result[3] )
    


    #PRUEBAS UNITARIAS EXTRAORDINARIAS
    
    #Ingresos no gravables son mayores
    def test_extraordinary1(self):

        #Datos de entrada
        totalLaborIncomePerYear: int = 15600000
        otherTaxableIncomePerYear: int = 0
        otherNonTaxableIncomePerYear: int = 20000000
        sourceRetentionValuePerYear: int = 600000
        socialSecurityPaymentInTheYear: int = 624000
        pensionContributionsInTheYear: int = 624000
        mortgageLoanPaymentPerYear: int = 0
        donationValuePerYear: int = 0
        educationalExpensesPerYear: int = 0

        #Proceso
        result = TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear)

        #Datos de salida esperados
        totalTaxedIncome = 15600000
        totalUntaxedIncome = 20000000
        totalDeductibleCosts = 1248000
        amountToPayIncomeTaxes = 0


        #Validacion de datos
        self.assertEqual( totalTaxedIncome, result[0] )
        self.assertEqual( totalUntaxedIncome, result[1] )
        self.assertEqual( totalDeductibleCosts, result[2] )
        self.assertEqual( amountToPayIncomeTaxes, result[3] )

    
    #Ganarse la loteria
    def test_extraordinary2(self):

        #Datos de entrada
        totalLaborIncomePerYear: int = 15600000
        otherTaxableIncomePerYear: int = 5000000000
        otherNonTaxableIncomePerYear: int = 0
        sourceRetentionValuePerYear: int = 1000000
        socialSecurityPaymentInTheYear: int = 624000
        pensionContributionsInTheYear: int = 624000
        mortgageLoanPaymentPerYear: int = 0
        donationValuePerYear: int = 0
        educationalExpensesPerYear: int = 20000000

        #Proceso
        result = TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear)

        #Datos de salida esperados
        totalTaxedIncome = 5015600000
        totalUntaxedIncome = 0
        totalDeductibleCosts = 21248000
        amountToPayIncomeTaxes = 931716000


        #Validacion de datos
        self.assertEqual( totalTaxedIncome, result[0] )
        self.assertEqual( totalUntaxedIncome, result[1] )
        self.assertEqual( totalDeductibleCosts, result[2] )
        self.assertEqual( amountToPayIncomeTaxes, result[3] )
    

    #Perdida en otros ingresos gravables
    def test_extraordinary3(self):

        #Datos de entrada
        totalLaborIncomePerYear: int = 70000000
        otherTaxableIncomePerYear: int = -100000000
        otherNonTaxableIncomePerYear: int = 0
        sourceRetentionValuePerYear: int = 4800000
        socialSecurityPaymentInTheYear: int = 2800000
        pensionContributionsInTheYear: int = 2800000
        mortgageLoanPaymentPerYear: int = 12000000
        donationValuePerYear: int = 0
        educationalExpensesPerYear: int = 15000000

        #Proceso
        result = TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear)

        #Datos de salida esperados
        totalTaxedIncome = -30000000
        totalUntaxedIncome = 0
        totalDeductibleCosts = 32600000
        amountToPayIncomeTaxes = 0


        #Validacion de datos
        self.assertEqual( totalTaxedIncome, result[0] )
        self.assertEqual( totalUntaxedIncome, result[1] )
        self.assertEqual( totalDeductibleCosts, result[2] )
        self.assertEqual( amountToPayIncomeTaxes, result[3] )

    
    #Donaciones de alto valor
    def test_extraordinary4(self):

        #Datos de entrada
        totalLaborIncomePerYear: int = 30000000
        otherTaxableIncomePerYear: int = 15000000
        otherNonTaxableIncomePerYear: int = 5000000
        sourceRetentionValuePerYear: int = 3000000
        socialSecurityPaymentInTheYear: int = 1200000
        pensionContributionsInTheYear: int = 1200000
        mortgageLoanPaymentPerYear: int = 10000000
        donationValuePerYear: int = 50000000
        educationalExpensesPerYear: int = 0

        #Proceso
        result = TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear)

        #Datos de salida esperados
        totalTaxedIncome = 45000000
        totalUntaxedIncome = 5000000
        totalDeductibleCosts = 62400000
        amountToPayIncomeTaxes = 0


        #Validacion de datos
        self.assertEqual( totalTaxedIncome, result[0] )
        self.assertEqual( totalUntaxedIncome, result[1] )
        self.assertEqual( totalDeductibleCosts, result[2] )
        self.assertEqual( amountToPayIncomeTaxes, result[3] )

    
    #Herencia
    def test_extraordinary5(self):

        #Datos de entrada
        totalLaborIncomePerYear: int = 24000000
        otherTaxableIncomePerYear: int = 9600000
        otherNonTaxableIncomePerYear: int = 350000000
        sourceRetentionValuePerYear: int = 1500000
        socialSecurityPaymentInTheYear: int = 960000
        pensionContributionsInTheYear: int = 960000
        mortgageLoanPaymentPerYear: int = 500000
        donationValuePerYear: int = 0
        educationalExpensesPerYear: int = 5000000

        #Proceso
        result = TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear)

        #Datos de salida esperados
        totalTaxedIncome = 33600000
        totalUntaxedIncome = 350000000
        totalDeductibleCosts = 7420000
        amountToPayIncomeTaxes = 0


        #Validacion de datos
        self.assertEqual( totalTaxedIncome, result[0] )
        self.assertEqual( totalUntaxedIncome, result[1] )
        self.assertEqual( totalDeductibleCosts, result[2] )
        self.assertEqual( amountToPayIncomeTaxes, result[3] )

    
    #Gastos extraordinarios en educacion
    def test_extraordinary6(self):

        #Datos de entrada
        totalLaborIncomePerYear: int = 17000000
        otherTaxableIncomePerYear: int = 5000000
        otherNonTaxableIncomePerYear: int = 0
        sourceRetentionValuePerYear: int = 1500000
        socialSecurityPaymentInTheYear: int = 680000
        pensionContributionsInTheYear: int = 680000
        mortgageLoanPaymentPerYear: int = 1000000
        donationValuePerYear: int = 800000
        educationalExpensesPerYear: int = 20000000

        #Proceso
        result = TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear)

        #Datos de salida esperados
        totalTaxedIncome = 22000000
        totalUntaxedIncome = 0
        totalDeductibleCosts = 23160000
        amountToPayIncomeTaxes = 0


        #Validacion de datos
        self.assertEqual( totalTaxedIncome, result[0] )
        self.assertEqual( totalUntaxedIncome, result[1] )
        self.assertEqual( totalDeductibleCosts, result[2] )
        self.assertEqual( amountToPayIncomeTaxes, result[3] )


    
    #PRUEBAS UNITARIAS DE ERROR

    #Retencion en la fuente superior a los ingresos laborales    
    def test_error1(self):

        #Datos de entrada
        totalLaborIncomePerYear: int = 15000000
        otherTaxableIncomePerYear: int = 10000000
        otherNonTaxableIncomePerYear: int = 1000000
        sourceRetentionValuePerYear: int = 30000000
        socialSecurityPaymentInTheYear: int = 600000
        pensionContributionsInTheYear: int = 600000
        mortgageLoanPaymentPerYear: int = 0
        donationValuePerYear: int = 0
        educationalExpensesPerYear: int = 5000000

        #Validacion
        self.assertRaises( TaxLogic.HigherIncomeRetentionException, TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear) )

    
    #Error por ingresar texto
    def test_error2(self):

        #Datos de entrada
        totalLaborIncomePerYear: int = "Mil millones"
        otherTaxableIncomePerYear: int = 0
        otherNonTaxableIncomePerYear: int = 0
        sourceRetentionValuePerYear: int = 0
        socialSecurityPaymentInTheYear: int = 0
        pensionContributionsInTheYear: int = 0
        mortgageLoanPaymentPerYear: int = 0
        donationValuePerYear: int = 0
        educationalExpensesPerYear: int = 0

        #Validacion
        self.assertRaises( TaxLogic.InvalidEntryException, TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear) )

    
    #Error digitos muy grandes
    def test_error3(self):

        #Datos de entrada
        totalLaborIncomePerYear: int = 8000000000
        otherTaxableIncomePerYear: int = 1000000000
        otherNonTaxableIncomePerYear: int = 3000000
        sourceRetentionValuePerYear: int = 6000000
        socialSecurityPaymentInTheYear: int = 320000000
        pensionContributionsInTheYear: int = 320000000
        mortgageLoanPaymentPerYear: int = 0
        donationValuePerYear: int = 0
        educationalExpensesPerYear: int = 0

        #Validacion
        self.assertRaises( TaxLogic.DigitsVeryLargeError, TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear) )

    
    #Error por datos obligatorios no agregados
    def test_error4(self):

        #Datos de entrada
        totalLaborIncomePerYear: int = 0
        otherTaxableIncomePerYear: int = 0
        otherNonTaxableIncomePerYear: int = 0
        sourceRetentionValuePerYear: int = 0
        socialSecurityPaymentInTheYear: int = 0
        pensionContributionsInTheYear: int = 0
        mortgageLoanPaymentPerYear: int = 0
        donationValuePerYear: int = 0
        educationalExpensesPerYear: int = 0

        #Validacion
        self.assertRaises( TaxLogic.DataNotAggregatedError, TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear) )

    
    #Error por deduccibles negativos
    def test_error5(self):

        #Datos de entrada
        totalLaborIncomePerYear: int = 15000000
        otherTaxableIncomePerYear: int = 0
        otherNonTaxableIncomePerYear: int = 0
        sourceRetentionValuePerYear: int = 500000
        socialSecurityPaymentInTheYear: int = 600000
        pensionContributionsInTheYear: int = 600000
        mortgageLoanPaymentPerYear: int = -15000000
        donationValuePerYear: int = 0
        educationalExpensesPerYear: int = 0

        #Validacion
        self.assertRaises( TaxLogic.DeductiblesNegativeError, TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear) )

    
    #No ingresar los activos
    def test_error6(self):

        #Datos de entrada
        totalLaborIncomePerYear: int = 0
        otherTaxableIncomePerYear: int = 0
        otherNonTaxableIncomePerYear: int = 0
        sourceRetentionValuePerYear: int = 4000000
        socialSecurityPaymentInTheYear: int = 0
        pensionContributionsInTheYear: int = 0
        mortgageLoanPaymentPerYear: int = 2000000
        donationValuePerYear: int = 0
        educationalExpensesPerYear: int = 0

        #Validacion
        self.assertRaises( TaxLogic.AssetsNotEnteredException, TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear) )

    
    #Ingresar un valor negativo en los ingresos.
    def test_error7(self):

        #Datos de entrada
        totalLaborIncomePerYear: int = -15600000
        otherTaxableIncomePerYear: int = -1000000
        otherNonTaxableIncomePerYear: int = -300000
        sourceRetentionValuePerYear: int = 0
        socialSecurityPaymentInTheYear: int = -624000
        pensionContributionsInTheYear: int = -624000
        mortgageLoanPaymentPerYear: int = 0
        donationValuePerYear: int = 0
        educationalExpensesPerYear: int = 0

        #Validacion
        self.assertRaises( TaxLogic.NegativeValueEnteredException, TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear) )

    
    #Caso de error en caso de ingresar cifras no coherentes
    def test_error8(self):

        #Datos de entrada
        totalLaborIncomePerYear: int = 0.000525
        otherTaxableIncomePerYear: int = 0
        otherNonTaxableIncomePerYear: int = 0
        sourceRetentionValuePerYear: int = 0
        socialSecurityPaymentInTheYear: int = 0
        pensionContributionsInTheYear: int = 0
        mortgageLoanPaymentPerYear: int = 0
        donationValuePerYear: int = 0
        educationalExpensesPerYear: int = 0

        #Validacion
        self.assertRaises( TaxLogic.IncoherentFiguresExpection, TaxLogic.CalculateTax(totalLaborIncomePerYear, otherTaxableIncomePerYear, otherNonTaxableIncomePerYear, sourceRetentionValuePerYear, socialSecurityPaymentInTheYear, pensionContributionsInTheYear, mortgageLoanPaymentPerYear, donationValuePerYear, educationalExpensesPerYear) )



# Este fragmento de codigo permite ejecutar el formato individualmente
if __name__ == '__main__':
    unittest.main()