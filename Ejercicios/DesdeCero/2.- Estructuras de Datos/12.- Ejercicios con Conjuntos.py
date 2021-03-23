
"""
Ejercicio 1:
A) Solicitar al usuario que ingrese números, los cuales se guardarán en una lista.
    Finalizar al ingresar el número 0, el cual no debe guardarse.

B) A continuación, solicitar al usuario que ingrese un número y, si el número está en la lista,
eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.

C) Recorrer la lista para imprimir la sumatoria de todos los elementos.

D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original que sean menores que el número dado.
Imprimir esta nueva lista, iterando por ella.

E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos,
cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella.
Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]

"""



"""
Ejercicio 2:
Escribir un programa que permita procesar datos de pasajeros de viaje en una 
lista de tuplas con la siguiente forma: (nombre, dni, destino). 
Ejemplo: [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), 
        ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hernandez", 38981374, "Lisboa")] Además, 
        en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. 
        Ejemplo: [("Buenos Aires","Argentina"), ("Glasgow","Escocia"), ("Lisboa", "Portugal"), ("Liverpool","Inglaterra"), 
        ("Madrid","España")] Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
-Agregar pasajeros a la lista de viajeros.
-Agregar ciudades a la lista de ciudades.
-Dado el DNI de un pasajero, ver a qué ciudad viaja.
-Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
-Dado el DNI de un pasajero, ver a qué país viaja.
-Dado un país, mostrar cuántos pasajeros viajan a ese país.
-Salir del programa.
"""



"""
Ejercicio 3:
Solicitar al usuario que ingrese los nombres de pila de los alumnos de nivel primario de una escuela, finalizando al ingresar “x”. A continuación, solicitar que ingrese los nombres de los alumnos de nivel secundario, finalizando al ingresar “x”.
- Informar los nombres de todos los alumnos de nivel primario y los de nivel secundario, sin repeticiones.<>
- Informar qué nombres se repiten entre los alumnos de nivel primario y secundario.hy line brown
-Informar qué nombres de nivel primario no se repiten en los de nivel secundario.
"""



"""
Ejercicio 4:
Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, 
la cual contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio del cliente). Ejemplo:
[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"), 
("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"), 
("Jorge Russo", 15, 958, "Mirasol 218")]
Escribir una función que reciba como parámetro una lista con el formato mencionado anteriormente y 
retorne los domicilios de cada cliente al cual se le debe enviar una factura de compra. 
Notar que cada cliente puede haber hecho más de una compra en el mes, 
por lo que la función debe retornar una estructura que contenga cada domicilio una sola vez.
"""


"""
Ejercicio 5:
Escribir un programa que procese strings ingresados por el usuario. 
La lectura finaliza cuando se hayan procesado 50 strings. 
Al finalizar, informar la cantidad total de ocurrencias de cada carácter, en todos los strings ingresados. 
Ejemplo: "r":5, "%":3, "a":8, "9":1.
¿Cómo se podrían informar las ocurrencias de las letras del alfabeto únicamente, 
incluyendo el valor 0 para las letras que no aparecieron?
"""


"""
Ejercicio 6:
Crear un programa para gestionar datos de los socios de un club, permitiendo: 
-Cargar información de los socios en un diccionario para acceder por número de socio. 
Los datos a almacenar son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al día (s/n). 
El programa debe iniciar con los datos de los socios fundadores ya cargados:

Socio nº1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
Socio nº2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
Socio nº3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
-Informar cantidad de socios del club.
-Solicitar al usuario el número de un socio y registrar que ha pagado todas las cuotas adeudadas.
-Modificar la fecha de ingreso de todos los socios ingresados el 13/03/2018, para indicar que en realidad ingresaron el 14/03/2018.
-Solicitar el nombre y apellido de un socio y darlo de baja (eliminarlo del listado).
-Imprimir el listado de socios completo.
"""


