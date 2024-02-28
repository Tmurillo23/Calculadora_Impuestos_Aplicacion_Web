#Aplicacion realizada por Luis Pablo Goez Y Valentina Carmona

def calcularImpuesto(TILA: int, OIGA: int, OINGA: int, VRFA: int, PCHA: int, VDA: int, GEA: int):
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
    """

    #Calcular El VSSA y APA

    PSSA = ( TILA * 4 ) / 100
    APA = ( TILA * 4 ) / 100


    #Calcular el Total de Ingresos Gravados
    TIG =  ( TILA + OIGA) - OINGA


    #Calcular Total de Ingresos NO Gravables
    TING = OINGA


    #Calcular Total Costos Deducibles
    TCD = PSSA + APA + PCHA + VDA + GEA