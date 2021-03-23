

'''
##Ejercicio 6
Calcular la media de tres números pedidos por teclado.
'''

Poblacion = int( input( "Ingrese el tamaño de la Poblacion : " ) )
ListadoNumero = []
Contador = 1

while  ( Contador <= Poblacion ) :
    Numero = int(input("Ingrese el Numero :" ))
    ListadoNumero.append(Numero)
    Contador = Contador + 1
'''
Media = 0
for i in ListadoNumero :
    print(len(ListadoNumero))
    Media = ( Media + i )

Moda = 0
NumeroMayor = 0
'''
print(len( ListadoNumero) - 1)

for i in range(0, len(ListadoNumero) - 1 ) :
    print(ListadoNumero[i])




# print(Media / len(ListadoNumero))
# print(sum(ListadoNumero)/len(ListadoNumero))

#print(Moda)


