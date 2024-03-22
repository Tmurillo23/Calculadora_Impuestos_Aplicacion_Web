import sys
sys.path.append("src")

from Logic import TaxLogic

def showMenu():
    print("Bienvenido a la calculadora de impuestos, por favor seleccione una opción")
    print("1. Ingresar datos (1)")
    print("2. Salir")

def option_1():
    total_labor_income_per_year = input ("Ingrese el total de ingresos laborales en el año: ")
    other_taxable_income_per_year = input ("Ingrese el total de otros ingresos gravables al año: ")
    other_non_taxable_income_per_year = input ("Ingrese el totral de otros ingresos no gravables al año: ")
    source_retention_value_per_year = input ("Ingrese el valor de retención en la fuente al año: ")
    mortgage_loan_payment_per_year = input ("Ingrese el valor de pago de credito hipotecario al año: ")
    donation_value_per_year = input ("Ingrese el valor de donaciones del año: ")
    educational_expenses_per_year = input ("Ingrese el valor de gasto de edicaión al año: ")

    tax =TaxLogic.CalculateTax (total_labor_income_per_year, other_taxable_income_per_year, other_non_taxable_income_per_year, source_retention_value_per_year, mortgage_loan_payment_per_year, donation_value_per_year, educational_expenses_per_year)   

    print ("El valor de renta a pagar es: ")
    print (tax)
def main():
    while True:
        showMenu()
        seleccion = input("Por favor, selecciona una opción: ")

        if seleccion == "1":
            option_1()
        elif seleccion == "2":
            print("Usted ha salido del programa")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()



