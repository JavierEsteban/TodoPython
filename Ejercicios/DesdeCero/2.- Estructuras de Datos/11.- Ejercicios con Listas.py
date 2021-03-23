

"""
Ejercicio 1:
Escriba un programa que permita crear una lista de palabras.
Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista.
Por último, el programa tiene que escribir la lista y Mostrar la Lista.
"""

def InsertarLista(numero):
    if numero > 0:
        Lista_nombres = list()
        contador = 0
        while contador < numero:
            Lista_nombres.append(input("Ingrese la Primera Palabra..."))
            contador += 1
        return Lista_nombres
    else:
        print("Ingrese un número positivo")
        return  None

def main():

    try:
        numero_veces = int(input("Ingrese el número de Veces : "))
        Lista_nombres = InsertarLista(numero_veces)
        print("Lista nombres : {}".format(Lista_nombres))
    except ValueError:
        print("Error - Favor ingresar un número...")

    except Exception as e:
        print(type(e).__name__)
    finally:
        print("Terminado Programa...")


if __name__ == '__main__':
    main()


"""
Ejercicio 2:
Escriba un programa que permita crear una lista de palabras y que, 
a continuación, pida una palabra y diga cuántas veces aparece esa palabra en la lista.

"""
def Buscar_Lista(lista):
    palabrabuscada = str(input("Dígame la palabra a buscar: "))
    conteopersonas = 0
    for i in  lista:
        if palabrabuscada == i :
            conteopersonas += 1
    return palabrabuscada, conteopersonas

def Insertar_Lista(numero):
    rellenarlista = list()
    contador = 1
    while(contador <= numero):
        rellenarlista.append(str(input("Dígame la palabra {}: ".format(contador))))
        contador += 1
    return rellenarlista

def main():
    try:
        numero_veces = int(input("Dígame cuántas palabras tiene la lista: "))
        if(numero_veces>0):
            listapersonas = Insertar_Lista(numero_veces)
            nombrePersona, numero = Buscar_Lista(listapersonas)
            if(numero == 1):
                print("La palabra '{}' aparece una vez en la lista.".format(nombrePersona))
            elif(numero == 0):
                print("La palabra '{}' no aparece en la lista".format(nombrePersona))
            else:
                print("La palabra '{}' aparece {} veces en la lista.".format(nombrePersona, numero))

        else:
            print("El número debe de ser Positivo...")

    except Exception as e:
        print(type(e).__name__)

    finally:
        print("Programa Terminado....")

if __name__=='__main__':
    main()


"""
Ejercicio 3
Escriba un programa que permita crear una lista de palabras y que, 
a continuación, pida dos palabras y sustituya la primera por la segunda en la lista.
"""

def Actualizar_Lista(lista):
    palabrasustituta = str(input("Sustituir la palabra: "))
    palabraabuscar = str(input("por la palabra: "))
    for indice , i in enumerate(lista):
        if palabrasustituta == i:
            lista[indice] = palabraabuscar
            break

    return lista


def Insertar_Lista(numero_veces):
    contador = 1
    Listado = list()
    while(contador <= numero_veces):
        Listado.append(input("Dígame la palabra {}:".format(contador)))
        contador += 1
    return Listado

def main():
    try:
        numero_veces = int(input("Dígame cuántas palabras tiene la lista: "))
        listapersonas = Insertar_Lista(numero_veces)
        print("La lista creada es: {}".format(listapersonas))

        actualizarpersonas = Actualizar_Lista(listapersonas)
        print("La lista es ahora: {}".format(actualizarpersonas))

    except Exception as e:
        print(type(e).__name__)

if __name__=='__main__':
    main()

"""
Ejercicio4:
Escriba un programa que permita crear una lista de palabras y que, 
a continuación, pida una palabra y elimine esa palabra de la lista.
"""


def main():
    pass

if __name__=='__main__':
    main()

"""
Ejercicio5:
Escriba un programa que permita crear dos listas de palabras y que, 
a continuación, elimine de la primera lista los nombres de la segunda lista.

"""


"""
Ejercicio6:
Escriba un programa que permita crear una lista de palabras y que, a continuación, 
cree una segunda lista igual a la primera, pero al revés (no se trata de escribir la lista al revés, 
sino de crear una lista distinta).
"""


"""
Ejercicio7:
Escriba un programa que permita crear una lista de palabras y que, a continuación, 
elimine los elementos repetidos (dejando únicamente el primero de los elementos repetidos).
"""


"""
Ejercicio8:
Escriba un programa que permita crear dos listas de palabras y que, a continuación, 
escriba las siguientes listas (en las que no debe haber repeticiones):

Lista de palabras que aparecen en las dos listas.
Lista de palabras que aparecen en la primera lista, pero no en la segunda.
Lista de palabras que aparecen en la segunda lista, pero no en la primera.
Lista de palabras que aparecen en ambas listas.
Nota: Para evitar las repeticiones, el programa deberá empezar eliminando los elementos repetidos en cada lista.

"""
