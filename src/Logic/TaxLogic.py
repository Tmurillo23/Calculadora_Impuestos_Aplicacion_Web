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


#Clase con la informacion
class TaxInformation:
    def __init__(self, total_labor_income_per_year: int, other_taxable_income_per_year: int, other_non_taxable_income_per_year: int, source_retention_value_per_year: int, mortgage_loan_payment_per_year: int, donation_value_per_year: int, educational_expenses_per_year: int ):    
        self.total_labor_income_per_year = total_labor_income_per_year
        self.other_taxable_income_per_year = other_taxable_income_per_year
        self.other_non_taxable_income_per_year = other_non_taxable_income_per_year
        self.source_retention_value_per_year = source_retention_value_per_year
        self.mortgage_loan_payment_per_year = mortgage_loan_payment_per_year
        self.donation_value_per_year = donation_value_per_year
        self.educational_expenses_per_year = educational_expenses_per_year

#Calcular el valor del impuesto a pagar
def calculateTax(objeto):
    
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

    # Definir los rangos y tasas impositivas como una lista de tuplas
    TAX_RATES = [
        (float('-inf'), 1090, 0),
        (1090, 1700, 0.19),
        (1700, 4100, 0.28),
        (4100, 8670, 0.33),
        (8670, 18970, 0.35),
        (18970, 31000, 0.37),
        (31000, float('inf'), 0.39)
    ]

    #Valor unidad tributaria
    TAXUNITVALUE = 46076


    #CONTROL DE ERROR
    if type(objeto.total_labor_income_per_year) == str or type(objeto.other_taxable_income_per_year) == str or type(objeto.other_non_taxable_income_per_year) == str or type(objeto.source_retention_value_per_year) == str or type(objeto.mortgage_loan_payment_per_year) == str or type(objeto.donation_value_per_year) == str or type(objeto.educational_expenses_per_year) == str:
        raise InvalidEntryException("Ingresaste un valor invalido.")
    
    if (objeto.total_labor_income_per_year < 0 or objeto.other_non_taxable_income_per_year < 0) and objeto.other_taxable_income_per_year < 0:
        raise NegativeValueEnteredException("No puedes ingresar valor negativos en esta casilla.")

    if objeto.source_retention_value_per_year > objeto.total_labor_income_per_year:
        raise HigherIncomeRetentionException("La retencion en la fuente no puede ser mayor al valor total de ingresos.")

    if len(str(objeto.total_labor_income_per_year)) > MAXDIGITS or len(str(objeto.other_taxable_income_per_year)) > MAXDIGITS or len(str(objeto.other_non_taxable_income_per_year)) > MAXDIGITS or len(str(objeto.source_retention_value_per_year)) > MAXDIGITS or len(str(objeto.mortgage_loan_payment_per_year)) > MAXDIGITS or len(str(objeto.donation_value_per_year)) > MAXDIGITS or len(str(objeto.educational_expenses_per_year)) > MAXDIGITS:
        raise DigitsVeryLargeError("Numeros ingresados muy grandes, exceden el valor normal a calcular.")
    
    if objeto.other_taxable_income_per_year == 0 and objeto.other_non_taxable_income_per_year == 0:
        raise AssetsNotEnteredException("Activos no agregados, ingrese activos para continuar.")

    if objeto.total_labor_income_per_year == 0:
        raise DataNotAggregatedError("Error! Datos obligatorios no agregados. Ingreselos para poder continuar.")

    if objeto.total_labor_income_per_year > 0 and objeto.total_labor_income_per_year < 1:
        num_str = str(objeto.total_labor_income_per_year)

        if '.' in num_str:
            decimal_part = num_str.split('.')[1]
        
        if len(decimal_part) == NUMBERLIMIT:
            raise IncoherentFiguresExpection("Ingresaste un valor incoherente, verifique y cambie")
    

    #Calcular el valor a la seguridad social en el año y el aporte a la pension en el año
    social_security_payment_in_the_year = ( objeto.total_labor_income_per_year * SOCIALSECURITYPERCENTAGE ) / 100
    pension_contributions_in_the_year = ( objeto.total_labor_income_per_year * PENSIONCONTRIBUTIONPERCENTAGE ) / 100

    #Calcular Total de Ingresos NO Gravables
    pension_contributions_in_the_year = ( objeto.total_labor_income_per_year * PENSIONCONTRIBUTIONPERCENTAGE ) / 100
    total_untaxed_income = objeto.other_non_taxable_income_per_year

    #Calcular el Total de Ingresos Gravados
    total_taxed_income =  ( objeto.total_labor_income_per_year + objeto.other_taxable_income_per_year + objeto.other_non_taxable_income_per_year) - total_untaxed_income

    #Calcular Total Costos Deducibles
    total_deductible_costs = social_security_payment_in_the_year + pension_contributions_in_the_year + objeto.mortgage_loan_payment_per_year + objeto.donation_value_per_year + objeto.educational_expenses_per_year


    #Validacion deducibles no sean menores que cero
    if total_deductible_costs < 0:
        raise DeductiblesNegativeError("Error! Algo anda mal, el total de tus deducibles es menor que cero(0).")


    #Calcular las unidades de valor tributario
    tax_value_units = total_taxed_income / TAXUNITVALUE

    # Iterar sobre las tuplas de rangos y tasas impositivas para encontrar la tasa impositiva adecuada
    for lower_limit, upper_limit, rate in TAX_RATES:
        if lower_limit < tax_value_units <= upper_limit:
            tax_rate = rate
            break

    
    #Calcular el valor a pagar por impuestos de rentas
    if tax_rate == 0:
        amount_to_pay_income_taxes = 0
    else:
        amount_to_pay_income_taxes = (( total_taxed_income - total_deductible_costs ) * tax_rate ) - objeto.source_retention_value_per_year

    #Lista de resultados
    results = []
    results.append(total_taxed_income)
    results.append(total_untaxed_income)
    results.append(total_deductible_costs)
    results.append(round(amount_to_pay_income_taxes))

    return results