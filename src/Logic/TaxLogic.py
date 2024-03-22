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
def calculateTax(total_labor_income_per_year: int, other_taxable_income_per_year: int, other_non_taxable_income_per_year: int, source_retention_value_per_year: int, mortgage_loan_payment_per_year: int, donation_value_per_year: int, educational_expenses_per_year: int):
    
    """
    total_labor_income_per_year: Total ingresos laborales al año
    other_taxable_income_per_year: Otros ingresos gravables al año
    other_non_taxable_income_per_year: Otros ingresos no gravables al año
    source_retention_value_per_year: Valor retencion en la fuente al año
    mortgage_loan_payment_per_year: Pago credito Hipotecario al año
    donation_value_per_year: Valor donaciones al año
    educational_expenses_per_year: Gastos en educacion al año
    social_security_payment_in_the_year: Valor a la seguridad social al año
    pension_contributions_in_the_year: Aporte a la pension al año
    """

    #CONSTANTES

    #Porcentaje seguridad social
    SOCIALSECURITYPERCENTAGE = 4

    #Porcentaje aporte a la pension
    PENSIONCONTRIBUTIONPERCENTAGE = 4

    #Maximo de digitos
    MAXDIGITS = 10

    #Limite de cifras
    NUMBERLIMIT = 6


    #CONTROL DE ERROR
    if type(total_labor_income_per_year) == str or type(other_taxable_income_per_year) == str or type(other_non_taxable_income_per_year) == str or type(source_retention_value_per_year) == str or type(mortgage_loan_payment_per_year) == str or type(donation_value_per_year) == str or type(educational_expenses_per_year) == str:
        raise InvalidEntryException
    
    if (total_labor_income_per_year < 0 or other_non_taxable_income_per_year < 0) and other_taxable_income_per_year < 0:
        raise NegativeValueEnteredException

    if source_retention_value_per_year > total_labor_income_per_year:
        raise HigherIncomeRetentionException

    if len(str(total_labor_income_per_year)) > MAXDIGITS or len(str(other_taxable_income_per_year)) > MAXDIGITS or len(str(other_non_taxable_income_per_year)) > MAXDIGITS or len(str(source_retention_value_per_year)) > MAXDIGITS or len(str(mortgage_loan_payment_per_year)) > MAXDIGITS or len(str(donation_value_per_year)) > MAXDIGITS or len(str(educational_expenses_per_year)) > MAXDIGITS:
        raise DigitsVeryLargeError
    
    if other_taxable_income_per_year == 0 and other_non_taxable_income_per_year == 0:
        raise AssetsNotEnteredException

    if total_labor_income_per_year == 0:
        raise DataNotAggregatedError

    if total_labor_income_per_year > 0 and total_labor_income_per_year < 1:
        num_str = str(total_labor_income_per_year)

        if '.' in num_str:
            decimal_part = num_str.split('.')[1]
        
        if len(decimal_part) == NUMBERLIMIT:
            raise IncoherentFiguresExpection
    

    #Calcular el valor a la seguridad social en el año y el aporte a la pension en el año
    social_security_payment_in_the_year = ( total_labor_income_per_year * SOCIALSECURITYPERCENTAGE ) / 100
    pension_contributions_in_the_year = ( total_labor_income_per_year * PENSIONCONTRIBUTIONPERCENTAGE ) / 100

    #Calcular Total de Ingresos NO Gravables
    total_untaxed_income = other_non_taxable_income_per_year

    #Calcular el Total de Ingresos Gravados
    total_taxed_income =  ( total_labor_income_per_year + other_taxable_income_per_year + other_non_taxable_income_per_year) - total_untaxed_income

    #Calcular Total Costos Deducibles
    total_deductible_costs = social_security_payment_in_the_year + pension_contributions_in_the_year + mortgage_loan_payment_per_year + donation_value_per_year + educational_expenses_per_year


    #Validacion deducibles no sean menores que cero
    if total_deductible_costs < 0:
        raise DeductiblesNegativeError


    #Calcular las unidades de valor tributario
    tax_value_units = total_taxed_income / 46076

    #Calculamos tasa impositiva
    if tax_value_units <= 1090:
        tax_rate = 0
    elif tax_value_units > 1090 and tax_value_units <= 1700:
        tax_rate = 0.19
    elif tax_value_units > 1700 and tax_value_units <= 4100:
        tax_rate = 0.28
    elif tax_value_units > 4100 and tax_value_units <= 8670:
        tax_rate = 0.33
    elif tax_value_units > 8670 and tax_value_units <= 18970:
        tax_rate = 0.35
    elif tax_value_units > 18970 and tax_value_units <= 31000:
        tax_rate = 0.37
    elif tax_value_units > 31000:
        tax_rate = 0.39

    #Calcular el valor a pagar por impuestos de rentas
    if tax_rate == 0:
        amount_to_pay_income_taxes = 0
    else:
        amount_to_pay_income_taxes = (( total_taxed_income - total_deductible_costs ) * tax_rate ) - source_retention_value_per_year

    #Lista de resultados
    results = []
    results.append(total_taxed_income)
    results.append(total_untaxed_income)
    results.append(total_deductible_costs)
    results.append(round(amount_to_pay_income_taxes))

    return results