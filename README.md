# Calculadora de impuestos 

## ¿Quién hizo esto? (Autores)

-Valentina Carmona Guzmán. 

-Luis Pablo Goez 

## ¿Qué es y para qué es?

Una calculadora de impuestos, tiene como propósito principal automatizar y simplificar el proceso de preparación y presentación de las declaraciones de impuestos. Esto puede ayudar a reducir errores y minimizar el tiempo necesario para completar las tareas relacionadas con los impuestos.

## ¿Cómo lo hago funcionar?

### Prerequisitos
-Saber cuales son los datos (cantidades) para ingresarlos en el sistema.

### Ejecución 
- Primeramente aparecera un menu, en el cual aparecen dos opciones, la primera es para entrar al programa e ingresar los datos, la segunda opcion de es para salir del menu. 

Los datos a tener en cuenta para ingresar el programa son: 
Total, de ingresos laborales en el año: suma del salario por todo el año. 
Valor otros ingresos gravables: Son los ingresos que según las leyes colombianas tienen un % de impuestos, por ejemplo (Lotería, negocios, inversiones, alquileres, etc). 
Valor otros ingresos no gravables: Son los que no tienen un % de impuesto, ejemplo (Subsidios, indemnizaciones, herencias, donaciones, etc.).
Pago créditos hipoteca en el año: Es un deducible y entra todo lo que tiene que ver con la vivienda, seguros o hipotecas. 
Valor donaciones en el año: Es un deducible. 
Gastos en educación en el año: Es un deducible.  
Total, de ingresos gravados: (Ingresos laborales + otros ingresos gravados + otros ingresos no gravables) – otros ingresos gravables. 
Total, ingresos no gravables: Todos los ingresos no grabables del año. 
Total, costos deducibles: pago seguridad social + aportes pensión en el año + pago créditos hipotecarios en el año + valor donaciones en al año + gastos educación en el año. 
Valor a pagar por impuesto de renta: Es el total de ingresos gravables, pero hay unos porcentajes que dependiendo de la cantidad de total de ingresos gravables se define. 

## ¿Cómo esta hecho?

El proyecto, esta diseñado con clases, funciones, erroes y excepciones, tambien tenemos dos bibliotecas importadas, las cuales son, unittes para ejecutar las pruebas y sys para poder guiar la ruta completa y de manera segura en las carpetas del programa.

En este proyecto tenemos dos carpetas principales, las cuales son src(en esta carpeta, esta una carpeta llamada Logic con un archivo llamado TaxLogic en el cual esta toda la logica del proyecta y tambien tenemos otra carpeta llamada console, en donde hay un archivo llamdado TaxConsole en el cual esta la interfaz de usuario) y por ultimo tenemos una carpeta llamada TaxTest, en donde hay un archivo, en el cuak estan todos los test d eel programa.


## Estructura sugerida
    -Carpeta scr, en la cual se encuentran dos carpetas, en una esta la consola y en otra la logica del proyecto.
    -Carpeta test, en esta carpeta estan las pruebas unitarias. 
    
## Uso 
Para poder ejecutar las pruebas unitarias nos vamos ha la carpeta tets y entramos al archivo TaxTest, tambien podemos acceder a la carpeta src, a la cual tenemos otras dos carpetas, en una se encuentra la cosola de en la otra la logica del proyecto, en la consola encontraremos el menú, en el cual ingresaremos la opcion que necesitemos, si queremos ingresar los datos, ingresamos el número 1 en la cosola, de lo contario ingresamos el número 2 y esta opcion inmediatamente te saca del menú; cuando ingresas a la opcion 1 te pedira los siguientes datos:
-Total de ingresos laborales en el año
-Total de otros ingresos gravables al año
-Total de otros ingresos no gravables al año
-Total del valor de retención en la fuente al año
-Total del valor de pago de credito hipotecario al año
-Total del valor de donaciones del año
-Total del valor de gasto de educación al año

## Tener en cuenta lo siguiente para que no lance casos de error:
-No ingresar los ingresos laborales totales en el año
-Ingresar valores en texto 
-Ingresar valores muy grandes > 10 digitos 
-No ingresar los datos obligatorios como por ejemplo 
-Ingresar los deducibles negativos 
-No ingresar los activos 
-Ingresar un valor negativo en los ingresos 
