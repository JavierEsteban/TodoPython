
""""
1- Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
(Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
"""

def mayor(n1,n2):
    if(n1 > n2 ):
        valor = n1
    else:
        valor = n2
    return valor

def main():
    n1 = int(input("Ingresar el primer valor .... : "))
    n2 = int(input("Ingresar el primer valor .... : "))
    maximo = mayor(n1,n2)
    print("El número mayor es {} ....". format(maximo))

if __name__=='__main__':
    main()


"""
2- Definir una función max_de_tres(), que tome tres números 
como argumentos y devuelva el mayor de ellos.
"""

def max_de_tres(n1,n2,n3):

    if(n1 > n2 and n2 > n3):
        valor = n1
    elif(n2 > n3 and n3 > n1 ):
        valor = n2
    else:
        valor = 'No ahí valor mayor...'

    return valor


def main():
    n1 = int(input("Ingrese el primer valor..."))
    n2 = int(input("Ingrese el primer valor..."))
    n3 = int(input("Ingrese el primer valor..."))
    valor = max(n1,n2,n3)
    print("El resultado de los números ingresados es :   {} ".format(valor))

if __name__ == '__main__':
    main()

"""
3- Definir una función que calcule la longitud de una lista o una cadena dada. 
(Es cierto que python tiene la función len() incorporada, 
pero escribirla por nosotros mismos resulta un muy buen ejercicio.
"""

def len_personalizada(listado):
    contador = 0
    for i in listado:
        contador += 1

    return contador

def main():
    listado = list()
    value = True
    while(value == True):
        listado.append(input("Ingrese el valor : "))
        value = int(input("Desea Continuar FALSE o TRUE ..."))
    tamanio = len_personalizada(listado)
    print("El tamaño de la lista es {} ...".format(tamanio))


if __name__ == '__main__':
    main()


"""
4- Escribir una función que tome un carácter y devuelva 
True si es una vocal, de lo contrario devuelve False.
"""

vocal = str(input("Ingrese el caracter....."))
Bdvocal = ['a','e','i','o','u']
if(vocal in Bdvocal):
    print("True")
else:
    print("False")


"""
5- Escribir una funcion sum() y una función multip() 
que sumen y multipliquen respectivamente todos los números de una lista. 
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

def sum(l):
    acumulador = 0
    for i in l:
        acumulador = acumulador + i
    return acumulador

def multip(l):
    acumulador = 1
    for i in l:
        acumulador = acumulador * i
    return acumulador


numero1 = int(input("Ingrese el tamaño del listado..."))
listado = list()
contador = 0
while(contador < numero1):
    listado.append(int(input("Ingrese el numero ...")))
    contador += 1



print("\n El valor de la suma es {}".format(sum(listado)))
print("\n"*2)
print("\n El valor de la multiplicación es {}".format(multip(listado)))

"""
6- Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""
string1 = 'javier'
string2 = string1[::-1]

print(string2)


"""
7 - Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas), 
ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

string1 = 'radar'
string2 = string1[::-1]

if(string1 == string2):
    print("son palindromos")
else:
    print("No son palindromos")

"""
8- Definir una función superposicion() que tome dos listas 
y devuelva True si tienen al menos 1 miembro en común o devuelva 
False de lo contrario. Escribir la función usando el bucle for anidado.
"""

def superposicion(n , m):
    for i in n:
        if(i in m):
            valor = True
            break
    if(valor == True):
        print("True")
    else:
        print("False")


n = int(input("Ingrese la cantidad de valores de la lista 1..."))
m = int(input("Ingrese la cantidad de valores de la lista 2..."))
contador1 = 0
contador2 = 0
lista1 =[]
lista2 =[]

while(contador1 < n):
    lista1.append(input("Ingrese el valor listado 1.."))
    contador1 += 1

while(contador2 < m):
    lista2.append(input("Ingrese el valor Listado 2.."))
    contador2 += 1

superposicion(lista1, lista2)


"""
9- Definir una función generar_n_caracteres() que tome un entero n y 
devuelva el caracter multiplicado por n. 
Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""

def generar_n_caracteres(n, m):
    print(n*m)

n = str(input("Ingrese el caracter a repetirse :"))
m = int(input("Ingrese la cantidad de repeticiones: "))
generar_n_caracteres(n, m)

"""
10- Definir un histograma procedimiento() que tome una 
lista de números enteros e imprima un histograma en la pantalla. 
Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:

****
*********
*******

"""

def procedimiento(lista):
    for index, values in enumerate(lista):
        print("*"*lista[index])

cantidad_numeros = int(input("Ingresar la cantidad de números:"))
contador = 0
listado = list()
while(contador < cantidad_numeros):
    numero = int(input("Ingrese el número : "))
    listado.append(numero)
    contador += 1

procedimiento(listado)

'''
listas = [1, 2,3,4,5]
indice = 0
for i in listas:
    print(listas[indice])
    indice += 1

listas2 = [2,3,4,5]
for index, values in enumerate(listas2):
    print(index)
    print(values)
    print(listas2[index])

'''
