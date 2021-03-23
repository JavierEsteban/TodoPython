## Las tuplas son parecidas a las listas
## pero con la diferencia que son inmutables.

#Declaración de las Tuplas

datos = tuple()
print(type(datos))

datos = (1, 2, "Javier")
print(datos)

data = ([1,2,3,4], 34,23,53)
#Recorrido de las Tuplas...

print( datos[2] )
print( datos[::-1] )
print(datos[:2])

print(data[0][0])


#Modificando Tupla y controlando con Excepciones
try:
    data[1] = 4
except TypeError:
    print("ERROR - Tipo de Dato Erroneo...................")
except NameError:
    print("ERROR - No se Pueden Modificar llas Tuplas.....")
except Exception as e:
    print(type(e).__name__)



