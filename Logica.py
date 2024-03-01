#Aplicacion realizada por Luis Pablo Goez Y Valentina Carmona

def calcularImpuesto(TILA: int, OIGA: int, OINGA: int, VRFA: int, PSSA: int, APA: int, PCHA: int, VDA: int, GEA: int):
    """
    Calcular el valor del impuesto a pagar
    TILA: Total ingresos laborales al año
    OIGA: Otros ingresos gravables al año
    OINGA: Otros ingresos no gravables al año
    VRFA: Valor retencion en la fuente al año
    PCHA: Pago credito Hipotecario al año
    VDA: Valor donaciones al año
    GEA: Gastos en educacion al año
    VSSA: Valor a la seguridad social al año
    APA: Aporte a la pension al año
    

    #Calcular El VSSA y APA
    PSSA = ( TILA * 4 ) / 100
    APA = ( TILA * 4 ) / 100

    #Calcular Total de Ingresos NO Gravables
    TING = OINGA

    #Calcular el Total de Ingresos Gravados
    TIG =  ( TILA + OIGA) - TING

    #Calcular Total Costos Deducibles
    TCD = PSSA + APA + PCHA + VDA + GEA

    #Calcular UVT (Unidades de valor tributario)
    UVT = TIG / 46076

    #Calculamos tasa impositiva
    if UVT <= 1090:
        TI = 0
    elif UVT > 1090 or UVT <= 1700:
        TI = 0,19
    elif UVT > 1700 or UVT <= 4100:
        TI = 0,28
    elif UVT > 4100 or UVT <= 8670:
        TI = 0,33
    elif UVT > 8670 or UVT <= 18970:
        TI = 0,35
    elif UVT > 18970 or UVT <= 31000:
        TI = 0,37
    elif UVT > 31000:
        TI = 0,39

    #Calcular el valor a pagar por impuestos de rentas
    if TI == 0:
        VPIR = 0
    else:
        VPIR = (( TIG - TCD ) * TI ) - VRFA
    
    """
    pass

class RetencionMayorIngresosError( Exception ):
    """La retencion en la fuente no puede ser mayor al valor total de ingresos."""

class IngresoInvalidoExcepcion( Exception ):
    """Ingresaste un valor invalido."""

class DigitosMuyGrandesError( Exception ):
    """Numeros ingresados muy grandes, exceden el valor normal a calcular."""

class DatosNoAgregadosError( Exception ):
    """Error! Datos obligatorios no agregados. Ingreselos para poder continuar."""

class DeduciblesNegrativosError( Exception ):
    """Error! Algo anda mal, el total de tus deducibles es menor que cero(0)."""

class ActivosNoIngresadosExcepcion( Exception ):
    """Activos no agregados, ingrese activos para continuar."""

class ValorNegrativoIngresadoExcepcion( Exception ):
    """No puedes ingresar valor negativos en esta casilla."""

class CifrasIncoherentesExpecion( Exception ):
    """Ingresaste un valor incoherente, verifique y cambie"""