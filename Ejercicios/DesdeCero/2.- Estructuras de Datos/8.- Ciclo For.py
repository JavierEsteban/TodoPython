##Ciclo for

#Ejemplo con while
numeros = [1,2,3,4,5,6,7,8,9]
indice = 0

while (indice < len(numeros)):
    print(numeros[indice])
    indice += 1


#Ejemplo con un for
numeros = [1,2,3,4,5,6,7,8,9]

for numero in numeros:
    print(numero)


#Recorrido del ciclo for y alterar los arreglos...
numeros = [1,2,3,4,5,6,7,8,9]
for numero in numeros:
    numero *= 10 #solo multiplica más no modifica el arreglo.
print(numeros)


#modificar con indice....

numeros = [1,2,3,4,5,6,7,8,9]
indice = 0
for numero in numeros:
    numeros[indice] = numero*10
    indice +=1
print(numeros)

#modificar con enumerate...
numeros = [1,2,3,4,5,6,7,8,9]
for index, numero in enumerate(numeros):
    numeros[index] *= 10
print(numeros)
