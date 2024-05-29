import sys
sys.path.append("src")
sys.path.append("templates")
from flask import Flask,request,render_template
from model import TaxLogic
from controller import ControllerRegistros
from model.TaxLogic import calculateTax

app = Flask(__name__)
@app.route('/')
def main():
    return render_template("index.html")

@app.route('/form')
def form():
    return render_template("form.html")
@app.route('/id_form')
def id_form():
    return render_template("id_form.html")
@app.route('/update_record_form')
def update_record_form():
    return render_template("update_record_form.html")
@app.route('/calculate_fee')
def calculate_fee(): #calcula pero no guarda
    id = request.args["id"]
    total_labor_income_per_year = int(request.args["total_labor_income_per_year"])
    other_taxable_income_per_year = int(request.args["other_taxable_income_per_year"])
    other_non_taxable_income_per_year = int(request.args["other_non_taxable_income_per_year"])
    source_retention_value_per_year = int(request.args["source_retention_value_per_year"])
    mortgage_loan_payment_per_year = int(request.args["mortgage_loan_payment_per_year"])
    donation_value_per_year = int(request.args["donation_value_per_year"])
    educational_expenses_per_year = int(request.args["educational_expenses_per_year"])

    TaxInformation = TaxLogic.TaxInformation(
        id,
        total_labor_income_per_year,
        other_taxable_income_per_year,
        other_non_taxable_income_per_year,
        source_retention_value_per_year,
        mortgage_loan_payment_per_year,
        donation_value_per_year,
        educational_expenses_per_year)
    result = calculateTax(TaxInformation)
    return render_template("result_fee.html", tax = result, message = "Valor calculado correctamente")


@app.route('/create_record') #Calcula pero si guarda
def create_new_record():
    id = request.args["id"]
    total_labor_income_per_year = int(request.args["total_labor_income_per_year"])
    other_taxable_income_per_year = int(request.args["other_taxable_income_per_year"])
    other_non_taxable_income_per_year = int(request.args["other_non_taxable_income_per_year"])
    source_retention_value_per_year = int(request.args["source_retention_value_per_year"])
    mortgage_loan_payment_per_year = int(request.args["mortgage_loan_payment_per_year"])
    donation_value_per_year = int(request.args["donation_value_per_year"])
    educational_expenses_per_year = int(request.args["educational_expenses_per_year"])

    TaxInformation = TaxLogic.TaxInformation(
        id,
        total_labor_income_per_year,
        other_taxable_income_per_year,
        other_non_taxable_income_per_year,
        source_retention_value_per_year,
        mortgage_loan_payment_per_year,
        donation_value_per_year,
        educational_expenses_per_year, )
    calculateTax(TaxInformation)
    ControllerRegistros.CreateTable()
    ControllerRegistros.InsertRecord(TaxInformation)
    result = ControllerRegistros.SearchRecordByID( id )
    return render_template("show_record.html", user=result, message = "El usuario creado fue:")

@app.route('/search_record') # buscar un registro
def search_record():
    id = request.args["id"]
    result = ControllerRegistros.SearchRecordByID( id )
    return render_template("show_record.html", user=result, message = "El usuario solicitado fue:")
@app.route("/delete_record") #borra un registro
def delete_record():
    id = request.args["id"]
    result = ControllerRegistros.SearchRecordByID(id)
    ControllerRegistros.DeleteRecord(id = id)
    return render_template("show_record.html", user=result, message = "El usuario eliminado fue:")


@app.route("/update_record") #actualiza un registro
def update_record():
    id = request.args["id"]
    total_labor_income_per_year = int(request.args["total_labor_income_per_year"])
    other_taxable_income_per_year = int(request.args["other_taxable_income_per_year"])
    other_non_taxable_income_per_year = int(request.args["other_non_taxable_income_per_year"])
    source_retention_value_per_year = int(request.args["source_retention_value_per_year"])
    mortgage_loan_payment_per_year = int(request.args["mortgage_loan_payment_per_year"])
    donation_value_per_year = int(request.args["donation_value_per_year"])
    educational_expenses_per_year = int(request.args["educational_expenses_per_year"])

    TaxInformation = TaxLogic.TaxInformation(
        id,
        total_labor_income_per_year,
        other_taxable_income_per_year,
        other_non_taxable_income_per_year,
        source_retention_value_per_year,
        mortgage_loan_payment_per_year,
        donation_value_per_year,
        educational_expenses_per_year)

    ControllerRegistros.UpdateRecord(TaxInformation)
    return render_template("update_record.html")


if __name__ == '__main--':
    app.run()