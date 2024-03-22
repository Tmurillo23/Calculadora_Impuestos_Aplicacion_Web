import sys
sys.path.append("src")

from Logic import TaxLogic

def showMenu():
    print("Bienvenido a la calculadora de impuestos, por favor seleccione una opción")
    print("1. Ingresar datos")
    print("2. Salir")

def showOption_1():
    print("--------------------------------------------")
    print("            Formulario Impuestos            ")
    print("--------------------------------------------")
    print("NOTA: Evite dejar celdas vacias agregue 0.")
    total_labor_income_per_year = int(input("Ingrese el total de ingresos laborales en el año: "))
    other_taxable_income_per_year = int(input("Ingrese el total de otros ingresos gravables al año: "))
    other_non_taxable_income_per_year = int(input("Ingrese el total de otros ingresos no gravables al año: "))
    source_retention_value_per_year = int(input("Ingrese el valor de retención en la fuente al año: "))
    mortgage_loan_payment_per_year = int(input("Ingrese el valor de pago de credito hipotecario al año: "))
    donation_value_per_year = int(input("Ingrese el valor de donaciones del año: "))
    educational_expenses_per_year = int(input("Ingrese el valor de gasto de educación al año: "))

    tax = TaxLogic.calculateTax(total_labor_income_per_year, other_taxable_income_per_year, other_non_taxable_income_per_year, source_retention_value_per_year, mortgage_loan_payment_per_year, donation_value_per_year, educational_expenses_per_year)   

    print("--------------------------------------------")
    print("                   Resultado                ")
    print("--------------------------------------------")
    print(f"El total de ingresos gravados fue: {tax[0]}.")
    print(f"El total de ingresos no gravados fue: {tax[1]}.")
    print(f"El total de costos deducibles fue: {tax[2]}.")
    print("--------------------------------------------")
    print(f"El valor a pagar de inpuesto de renta es: {tax[3]}.")

def main():

    while True:

        showMenu()

        seleccion = int(input("Por favor, selecciona una opción: "))

        if seleccion == 1:
            showOption_1()
        elif seleccion == 2:
            print("Usted ha salido del programa")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()



