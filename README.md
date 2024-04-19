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
    
## ¿Cómo lo hago funcionar?
Tener en cuenta: primeramente debe descargar el repositorio, para hacerlo debe tener instalada la aplicación Git bash, el siguiente paso es copiar el link del repositorio, luego entra a el escritorio de su computadora, le da click derecho y presiona la opción open git bash here, y en la consola de git bash escribe el siguiente comando "git clone" y pega el link del repositorio, recuerde que para pegar el link tiene que precionar clink derecho y luego presiona en pegar, despues le da entrer y el repositorio se comenzara a descargar en el escritorio. 


## Para ejecutar por consola 
1. Abra la terminal en su computadora
2. En la terminal utilice el comando cd para entrar al escritorio; "cd Escritorio" (depende del nombre que tenga su escritorio o que ruta tiene para llegar a este.)
3. Utilice el mismo comando para entrar a la aplicación "cd Calculadora_Impuestos". 
4. Utilice el mismo comando para entrar a la carpeta src, que es donde estan organizadas las carpetas con los archivos necesarios para que la aplicación funcione "cd src". 
5. luego copie la ruta que lleva hasta el momento en la terminal y luego escriba el comando set PYTHONPATH= aqui va la ruta que copio, ejemplo
set PYTHONPATH=C:\ruta\Escritorio\Calculadora_Impuestos\src
6. utilice el  comando cd para entrar a la carpeta console que es donde se encuentra el menú "cd console".
7. Despues utilice el comando "python TaxConsole.py"
8. Aparecera un menú y usted digita la opción que necesita 

    
## Ejecutar pruebas e información de más
Para poder ejecutar las pruebas unitarias, abrimos Visual o el programa que este utilizando, abrimos la calpeta Calcular_Impuestos y luego nos vamos ha la carpeta tets y entramos al archivo TaxTest y ejecutamos esta carpeta. 
Tambien podemos acceder a la carpeta src, a la cual tenemos otras tres carpetas, en una se encuentra la cosola de en la otra la logica del proyecto, y en otra la interfaz grafica del proyacto; en la consola encontraremos el menú, en el cual ingresaremos la opcion que necesitemos, si queremos ingresar los datos, ingresamos el número 1 en la cosola, de lo contario ingresamos el número 2 y esta opcion inmediatamente te saca del menú; cuando ingresas a la opcion 1 te pedira los siguientes datos:
-Total de ingresos laborales en el año
-Total de otros ingresos gravables al año
-Total de otros ingresos no gravables al año
-Total del valor de retención en la fuente al año
-Total del valor de pago de credito hipotecario al año
-Total del valor de donaciones del año
-Total del valor de gasto de educación al año

## Ejecuatar la interfaz grafica 
1. abrir visual studio code 
2. abrir la carpeta Calcular_Impuestos
3. entrar a la carpeta src
4. entrar a la carpeta GUI
5. entrar al archivo Tax_GUI.PY
6. ejecutar este archivo.
 

## Tener en cuenta lo siguiente para que no lance casos de error:
-No ingresar los ingresos laborales totales en el año
-Ingresar valores en texto 
-Ingresar valores muy grandes > 10 digitos 
-No ingresar los datos obligatorios como por ejemplo 
-Ingresar los deducibles negativos 
-No ingresar los activos 
-Ingresar un valor negativo en los ingresos 
