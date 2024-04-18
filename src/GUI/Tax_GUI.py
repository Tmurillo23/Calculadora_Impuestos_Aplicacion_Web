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
        self.resultado = Label(color=(0, 0, 0, 1))
        container.add_widget(self.resultado)
        self.calcular = Button(text="Calcular")
        container.add_widget(self.calcular)


        self.calcular.bind( on_press=self.calcular_cuota )

        return container
    
    def _update_background(self, instance, *args):
        instance.canvas.before.clear()
        with instance.canvas.before:
            Color(1, 1, 1, 1)
            Rectangle(pos=instance.pos, size=instance.size)
    
    def mostrar_error(self, mensaje):
        ventana = GridLayout(cols=1)
        ventana.add_widget(Label(text=mensaje))
        close_button = Button(text='Cerrar y volver a empezar')
        close_button.bind(on_press=self.cerrar_popup)
        ventana.add_widget(close_button)
        
        popup = Popup(title='Error', content=ventana, size=(400, 200))
        popup.open()

    def cerrar_popup(self, instance):
        instance.parent.parent.parent.parent.dismiss()
        self.total_labor_income_per_year.text = ''
        self.other_taxable_income_per_year.text = ''
        self.interes.text = ''
        self.resultado.text = ''
    
    def calcular_cuota(self, sender):
        try:
            total_labor_income_per_year = int( self.total_labor_income_per_year.text )
            other_taxable_income_per_year = int( self.other_taxable_income_per_year.text )
            result = calculateTax( total_labor_income_per_year, other_taxable_income_per_year)
            self.resultado.text = str( result )
        except ValueError:
            self.resultado.text = "Por favor, ingrese valores numéricos válidos."
        except Exception as e:
            self.mostrar_error("Se produjo un error: {}".format(e)) 
    
if __name__ == "__main__":
    TaxApp().run()