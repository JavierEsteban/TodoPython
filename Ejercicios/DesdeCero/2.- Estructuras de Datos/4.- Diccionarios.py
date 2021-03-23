
##Dicionarios
"""
Estructura de datos de clave - valor

Ejemplo :

Diccionario ={ 'clave' : "Valor"}

"""


nombres = {'Primera':"Javier Tiburcio", 'Segundo':"Roy Tiburcio", 'Tercero':"Mirian Tiburcio"}
print(nombres['Primera'])



## Declaración de dicccionario

diccionario = {}

## Agregar datos....
diccionario['Peru'] = "Lima"
diccionario['Bolivia'] = "Sucre"
diccionario['Argentina'] = "Buenos Aires"
diccionario['Colombia']="Bogota"
diccionario['Paraguay']="Asunción"
diccionario['Brasil']='Brasilia'
diccionario['Venezuela'] = "Caracas"
diccionario['Uruguay']="Montevideo"

#Visualización de Diccionario
print(diccionario)
print(diccionario['Peru'])
print(diccionario['Argentina'])

#Recorriendo de Diccionario
for clave in diccionario:
    print("El País {}, Tiene Capital {}".format(clave,diccionario[clave]))

