from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image


import sys
sys.path.append("src")

from Logic import TaxLogic

from Logic.TaxLogic import calculateTax

class TaxApp(App):
    def build(self):

        #Creacion del contenedor para la app
        container = GridLayout(cols=2, padding=20, spacing=10)
        container.bind(size=self._update_background, pos=self._update_background)
        self._update_background(container)


        #Icono app
        icono = Image(source='image/impuestos.png')
        container.add_widget(icono)

        #Titulo app
        title = Label(text='CALCULADORA DE IMPUESTOS', font_size=35, color=(0, 0, 0, 1), bold=True)
        container.add_widget(title)
        

        #Campo de texto para el total de ingresos laborales por año.
        container.add_widget(Label(text="Total de ingresos laborales por año", color=(0, 0, 0, 1)))
        self.total_labor_income_per_year = TextInput(font_size=30, foreground_color=(0, 0, 0, 1))
        container.add_widget(self.total_labor_income_per_year)


        #Campo de texto para el total de otros ingresos gravables por año.
        container.add_widget(Label(text="Total de otros ingresos gravables por año", color=(0, 0, 0, 1)))
        self.other_taxable_income_per_year = TextInput(font_size=30, foreground_color=(0, 0, 0, 1))
        container.add_widget(self.other_taxable_income_per_year)


        #Campo de texto para el total de otros ingresos no gravables por año.
        container.add_widget(Label(text="Total de otros ingresos no gravables por año", color=(0, 0, 0, 1)))
        self.other_non_taxable_income_per_year = TextInput(font_size=30, foreground_color=(0, 0, 0, 1))
        container.add_widget(self.other_non_taxable_income_per_year)


        #Campo de texto para el valor de retencion en la fuente por año.
        container.add_widget(Label(text="Valor de retencion en la fuente por año", color=(0, 0, 0, 1)))
        self.source_retention_value_per_year = TextInput(font_size=30, foreground_color=(0, 0, 0, 1))
        container.add_widget(self.source_retention_value_per_year)


        #Campo de texto para el valor de pago de credito hipoptecario por año.
        container.add_widget(Label(text="Valor de pago de credito hipoptecario por año", color=(0, 0, 0, 1)))
        self.mortgage_loan_payment_per_year = TextInput(font_size=30, foreground_color=(0, 0, 0, 1))
        container.add_widget(self.mortgage_loan_payment_per_year)


        #Campo de texto para el valor de donaciones por año.
        container.add_widget(Label(text="Valor de donaciones por año", color=(0, 0, 0, 1)))
        self.donation_value_per_year = TextInput(font_size=30, foreground_color=(0, 0, 0, 1))
        container.add_widget(self.donation_value_per_year)


        #Campo de texto para el valor de gastos en educacion por año.
        container.add_widget(Label(text="Valor de gastos en educacion por año", color=(0, 0, 0, 1)))
        self.educational_expenses_per_year = TextInput(font_size=30, foreground_color=(0, 0, 0, 1))
        container.add_widget(self.educational_expenses_per_year)


        #Campo de texto para el resultado y boton calcular.
        self.result = Label(color=(0, 0, 0, 1))
        container.add_widget(self.result)
        self.calculate = Button(text="Calcular", size_hint_x=None, width=200)
        container.add_widget(self.calculate)


        self.calculate.bind( on_press=self.calculate_fee )

        return container
    

    #Color del fondo
    def _update_background(self, instance, *args):
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(1, 1, 1, 1)
            Rectangle(pos=instance.pos, size=instance.size)
    

    #Mostrar resultados
    def show_result_popup(self, result):
        popup_content = GridLayout(cols=1, padding=10)
        popup_content.add_widget(Label(text="Resultado del cálculo:", bold=True))
        popup_content.add_widget(Label(text=f"Ingresos totales gravados: {str(result[0])}"))
        popup_content.add_widget(Label(text=f"Ingresos totales NO gravados: {str(result[1])}"))
        popup_content.add_widget(Label(text=f"Costos totales deducibles: {str(result[2])}"))
        popup_content.add_widget(Label(text=f"Cantidad a pagar ingresos de renta: {str(result[3])}"))
        close_button = Button(text='Cerrar y volver a empezar')
        close_button.bind(on_press=self.close_popup)
        popup_content.add_widget(close_button)

        popup = Popup(title="Resultado", content=popup_content, size_hint=(None, None), size=(550, 350))
        popup.open()

    #Mostrar error
    def show_error(self, mensaje):
        popup_error = GridLayout(cols=1)
        popup_error.add_widget(Label(text=mensaje))

        """
        close_button = Button(text='Cerrar y volver a empezar')
        close_button.bind(on_press=self.close_popup)
        popup_error.add_widget(close_button)
        """
        
        popup = Popup(title='Error', content=popup_error, size_hint=(None, None), size=(750, 200))
        popup.open()


    #Cerrar pestaña emergente
    def close_popup(self, instance):
        instance.parent.parent.parent.parent.dismiss()
        self.total_labor_income_per_year.text = ''
        self.other_taxable_income_per_year.text = ''
        self.other_non_taxable_income_per_year.text = ''
        self.source_retention_value_per_year.text = ''
        self.mortgage_loan_payment_per_year.text = ''
        self.donation_value_per_year.text = ''
        self.educational_expenses_per_year.text = ''
        self.result.text = ''
    

    #Calcular cuota
    def calculate_fee(self, sender):
        try:
            total_labor_income_per_year = int( self.total_labor_income_per_year.text )
            other_taxable_income_per_year = int( self.other_taxable_income_per_year.text )
            other_non_taxable_income_per_year = int( self.other_non_taxable_income_per_year.text )
            source_retention_value_per_year = int( self.source_retention_value_per_year.text )
            mortgage_loan_payment_per_year = int( self.mortgage_loan_payment_per_year.text )
            donation_value_per_year = int( self.donation_value_per_year.text )
            educational_expenses_per_year = int( self.educational_expenses_per_year.text )

            TaxInformation = TaxLogic.TaxInformation(
                total_labor_income_per_year, 
                other_taxable_income_per_year, 
                other_non_taxable_income_per_year, 
                source_retention_value_per_year, 
                mortgage_loan_payment_per_year, 
                donation_value_per_year, 
                educational_expenses_per_year)
            
            result = calculateTax( TaxInformation )

            self.show_result_popup(result)

        except ValueError:
            self.result.text = "Por favor, llene todos los campos con\n valores numéricos válidos(Enteros)."

        except Exception as e:
            self.show_error("Error: {}".format(e)) 
    
if __name__ == "__main__":
    TaxApp().run()