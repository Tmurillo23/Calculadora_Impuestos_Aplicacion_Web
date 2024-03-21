#Aplicacion realizada por Luis Pablo Goez Y Valentina Carmona

# EXCEPCIONES

#Mayor retencion de ingresos 
class HigherIncomeRetentionException( Exception ):
    """La retencion en la fuente no puede ser mayor al valor total de ingresos."""

#Ingreso invalido
class InvalidEntryException( Exception ):
    """Ingresaste un valor invalido."""

#Digitos muy grandes 
class DigitsVeryLargeError( Exception ):
    """Numeros ingresados muy grandes, exceden el valor normal a calcular."""

#Datos no agregados 
class DataNotAggregatedError( Exception ):
    """Error! Datos obligatorios no agregados. Ingreselos para poder continuar."""
    
#Duducibles negativos  
class DeductiblesNegativeError( Exception ):
    """Error! Algo anda mal, el total de tus deducibles es menor que cero(0)."""

# Activos no ingresados
class AssetsNotEnteredException( Exception ):
    """Activos no agregados, ingrese activos para continuar."""

# Valor negativo ingresos
class NegativeValueEnteredException( Exception ):
    """No puedes ingresar valor negativos en esta casilla."""

#Cifras incoherentes
class IncoherentFiguresExpection( Exception ):
    """Ingresaste un valor incoherente, verifique y cambie"""


#LOGICA
    
#Calcular el valor del impuesto a pagar
def CalculateTax(totalLaborIncomePerYear: int, otherTaxableIncomePerYear: int, otherNonTaxableIncomePerYear: int, sourceRetentionValuePerYear: int, mortgageLoanPaymentPerYear: int, donationValuePerYear: int, educationalExpensesPerYear: int):
    
    """
    totalLaborIncomePerYear: Total ingresos laborales al año
    otherTaxableIncomePerYear: Otros ingresos gravables al año
    otherNonTaxableIncomePerYear: Otros ingresos no gravables al año
    sourceRetentionValuePerYear: Valor retencion en la fuente al año
    mortgageLoanPaymentPerYear: Pago credito Hipotecario al año
    donationValuePerYear: Valor donaciones al año
    educationalExpensesPerYear: Gastos en educacion al año
    socialSecurityPaymentInTheYear: Valor a la seguridad social al año
    pensionContributionsInTheYear: Aporte a la pension al año
    """
    #Porcentaje seguridad social
    SOCIALSECURITYPERCENTAGE = 4

    #Porcentaje aporte a la pension
    PENSIONCONTRIBUTIONPERCENTAGE = 4


    #Calcular el valor a la seguridad social en el año y el aporte a la pension en el año
    socialSecurityPaymentInTheYear = ( totalLaborIncomePerYear * SOCIALSECURITYPERCENTAGE ) / 100
    pensionContributionsInTheYear = ( totalLaborIncomePerYear * PENSIONCONTRIBUTIONPERCENTAGE ) / 100

    #Calcular Total de Ingresos NO Gravables
    totalUntaxedIncome = otherNonTaxableIncomePerYear

    #Calcular el Total de Ingresos Gravados
    totalTaxedIncome =  ( totalLaborIncomePerYear + otherTaxableIncomePerYear + otherNonTaxableIncomePerYear) - totalUntaxedIncome

    #Calcular Total Costos Deducibles
    totalDeductibleCosts = socialSecurityPaymentInTheYear + pensionContributionsInTheYear + mortgageLoanPaymentPerYear + donationValuePerYear + educationalExpensesPerYear

    #Calcular las unidades de valor tributario
    taxValueUnits = totalTaxedIncome / 46076

    #Calculamos tasa impositiva
    if taxValueUnits <= 1090:
        taxRate = 0
    elif taxValueUnits > 1090 and taxValueUnits <= 1700:
        taxRate = 0.19
    elif taxValueUnits > 1700 and taxValueUnits <= 4100:
        taxRate = 0.28
    elif taxValueUnits > 4100 and taxValueUnits <= 8670:
        taxRate = 0.33
    elif taxValueUnits > 8670 and taxValueUnits <= 18970:
        taxRate = 0.35
    elif taxValueUnits > 18970 and taxValueUnits <= 31000:
        taxRate = 0.37
    elif taxValueUnits > 31000:
        taxRate = 0.39

    #Calcular el valor a pagar por impuestos de rentas
    if taxRate == 0:
        amountToPayIncomeTaxes = 0
    else:
        amountToPayIncomeTaxes = (( totalTaxedIncome - totalDeductibleCosts ) * taxRate ) - sourceRetentionValuePerYear
        round(amountToPayIncomeTaxes)
        print(amountToPayIncomeTaxes)

    #Lista de resultados
    results = []
    results.append(totalTaxedIncome)
    results.append(totalUntaxedIncome)
    results.append(totalDeductibleCosts)
    results.append(amountToPayIncomeTaxes)

    return results