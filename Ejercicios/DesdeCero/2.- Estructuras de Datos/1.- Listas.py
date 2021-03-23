##Las listas en Python son muy parecidas a los strings
##Para el slicing
#Declaración de una lista
numeros = [1,2,3,4,5]
datos = [4, "Una Cadena", "Dos", -12]
ConjuntoListas = list()

#Agregar Listas
ConjuntoListas.append(numeros)
ConjuntoListas.append(datos)


print(numeros)
print(datos)
print(ConjuntoListas)

#Actualizar las listas
vocales = ["a","e","i","o","z"]
print(vocales)
vocales[-1] = "u"
print(vocales)

# Actualizar con slicing
vocales = ["m","n","p","o","u"]
print(vocales)
vocales[:3] = ["a","e","i"]
print(vocales)

#Eliminando datos de las listas..

vocales = ["a","e","i","o","u","j","k","l"]
print(vocales)
vocales[5:] = []
print(vocales)

#Listas Anidadas o concatenar Listas.

numeros = [1,2,3,4,5]
datos = [4, "Una Cadena", "Dos", -12]
ConjuntoListas =[numeros, datos]
print(ConjuntoListas)


def main():
    ListaNombres = list()
    while(True):
        name = str(input("Ingrese su Nombre .......  : ")).title()
        Evaluar = str(input("Desea Continuar SI/NO")).lower()
        ListaNombres.append(name)
        if Evaluar == "no":
            break
    print(ListaNombres)


if __name__ == '__main__':
    main()








