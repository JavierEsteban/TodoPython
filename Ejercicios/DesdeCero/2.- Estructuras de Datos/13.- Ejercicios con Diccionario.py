
#Ejercicios con Diccionarios
"""
Ejercicio 1
Escribe un programa python que pida un número por teclado y que cree un diccionario cuyas claves sean desde el número 1 hasta el número indicado, y los valores sean los cuadrados de las claves.
"""
def ingresavalores(n):
    diccionario = {}
    contador = 1
    while contador <= n:
        diccionario [contador] = str(input("Ingrese el valor : "))
        contador += 1
    print("######Valores del diccionario.....")
    print(diccionario)

    for index, valor in diccionario.items():
        print("El valor del Indice es : {} , el valor es : {}".format(index, valor))

def main():
    print("########################")
    numero = int(input("Ingrese la Cantidad de valores a Ingresar....."))
    ingresavalores(numero)

if __name__=='__main__':
    main()

"""
Ejercicio 2Permalink
Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena.
"""

######### Forma Larga ###############
def Distinct_leter(tx = []):
    Databaseleter = set()
    for indice in tx:
        for indice2 in indice:
            Databaseleter.update([indice2])
    return Databaseleter


def Diccionario(database = [], tx1 = []):
    Dictionario = {}
    #Cargando El diccionario Precviamente
    for i in tx1:
        Dictionario[i] = 0
    #Contanto y cargando caracteres faltantea
    for caracter in tx1:
        if caracter in database:
            Dictionario[caracter] += 1
        else:
            Dictionario[caracter] = 1

    for index, value in Dictionario.items():
            print(" {}  -> {}".format(index, value))

def main():
    text = str(input("Ingrese el Texto a Iniciar el Programa....")).lower()
    databaseleter = list(Distinct_leter(text.split(" ")))
    Diccionario(database= databaseleter, tx1 = text)

if __name__ == '__main__':
    main()


######### Forma Corta ###############

def main():
    text = input("Por favor ingrese el Texto a analizar....").lower()
    dict = {}
    for i in text:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for indice, valores in dict.items():
        print("{}  ->  {}".format(indice, valores))


if __name__ == '__main__':
    main()


## otra forma
dict = {}
cadena = input("Dame una cadena:")
for caracter in cadena:
	if caracter in dict:
		dict[caracter]+=1
	else:
		dict[caracter]=1

for campo,valor in dict.items():
	print (campo,"->",valor)



"""
Ejercicio 3Permalink
Vamos a crear un programa en python donde vamos a declarar un diccionario para guardar los precios de las distintas frutas. 
El programa pedirá el nombre de la fruta y la cantidad que se ha vendido y nos mostrará el precio final de la fruta a 
partir de los datos guardados en el diccionario. 
Si la fruta no existe nos dará un error. Tras cada consulta el programa nos preguntará si queremos hacer otra consulta.
"""

def Ingresar_Datos(dicc):
    try:
        fruta = str(input("Favor Ingresar la Fruta ... "))
        cantidad = int(input("Favor de Ingresar La cantidad de Productos ... "))
    except ValueError:
        print("Error - El valor indicado es incorrecto ")
        return
    except Exception as e:
        print(type(e).__name__)

    if fruta in dicc:
        print(" La fruta {} , tiene como precio {}  el monto total por las {} es {}".format(fruta, dicc[fruta], cantidad,dicc[fruta]* cantidad))
    else:
        print("Error - La fruta no se encuentra en la BD...")

def main():
    dict = {'Manzana' : 3.5 , 'Pera' : 5.5 , 'Mandarina' : 4.5}
    while(True):
        Ingresar_Datos(dict)
        valor = str(input("Desea Continuar....")).upper()
        if (valor == 'NO'):
            break

if __name__ == '__main__':
    main()

"""
Ejercicio 4Permalink
Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y 
las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. 
Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y 
los valores serán listas con las notas de cada alumno.

El programa pedirá el número de alumnos que vamos a introducir, 
pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo. 
Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos. 
Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.
"""



"""
Ejercicio 5Permalink
Escribir un programa que implemente una agenda. 
En la agenda se podrán guardar nombres y números de teléfono. 
El programa nos dará el siguiente menú:

Añadir/modificar: Nos pide un nombre. Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, 
opcionalmente, permitir modificarlo si no es correcto. Si el nombre no se encuentra, 
debe permitir ingresar el teléfono correspondiente.
Buscar: Nos pide una cadena de caracteres, y nos muestras todos los contactos cuyos nombres comiencen por dicha cadena.
Borrar: Nos pide un nombre y si existe nos preguntará si queremos borrarlo de la agenda.
Listar: Nos muestra todos los contactos de la agenda.
Implementar el programa con un diccionario.
"""

