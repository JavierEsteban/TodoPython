
""""
Ejercicio 1
Escribir un programa que pregunte al usuario su edad
y muestre por pantalla si es mayor de edad o no.
"""

edad = int(input("Ingrese la edad a analizar : "))

if(edad >= 18):
    print("Es mayor de Edad...")
else:
    print("Es menor de Edad...")



"""
Ejercicio 2
Escribir un programa que almacene la cadena de caracteres 
contraseña en una variable, pregunte al usuario por la contraseña 
e imprima por pantalla si la contraseña introducida por el usuario 
coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
"""

contador = 0
contraseña = 'Javier'

while(contador < 3):
    contraseña2 =  str(input("Ingrese la nueva contraseña..."))

    if(contraseña.upper() == contraseña2.upper()):
        print("La contraseña es la correcta...")
        break

    contador = contador + 1
    print("Contraseña incorrecta...............")
    print("Te quedan {}".format( 3 - contador))




"""
Ejercicio 3
Escribir un programa que pida al usuario dos números
 y muestre por pantalla su división.
  Si el divisor es cero el programa debe mostrar un error.
"""

numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el primer número: "))

if(numero2 == 0):
    print("Sale error , no se puede dividir entre cero")
else:
    valor = numero1 / numero2
    print("El valor de la división es {} ...".format(valor))


"""
Ejercicio 4
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
"""

numero = int(input("Ingresar el número a analizar..."))
if(numero % 2 == 0 ):
    print("Es un número par...")
else:
    print("Es un número Impar.....")



"""
Ejercicio 5
Para tributar un determinado impuesto se debe ser mayor de 16 años y 
tener unos ingresos iguales o superiores a 1000 € mensuales. 
Escribir un programa que pregunte al usuario su edad y
 sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.
"""

edad = int(input("Ingrese la edad del usuario ...."))
contribucion = float(input("Ingrese el sueldo....."))

if(edad > 16 and contribucion > 1000):
    print("Puede contribuir...")
else:
    print("No puede contribuir...")


"""
Ejercicio 6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un 
nombre posterior a la N y el grupo B por el resto. 
Escribir un programa que pregunte al usuario su nombre y sexo, 
y muestre por pantalla el grupo que le corresponde.
"""

''' a b c d e f g h i j k l m 
n
'''

muestra = int(input("Ingrese la cantidad de la Muestra:"))
contador = 0
Base_Datos = ['a','b', 'c', 'd', 'e', 'f', 'g' ,'h', 'i', 'j', 'k', 'l', 'm']
Grupob = {}
Grupoa = dict()
while(contador < muestra):

    nombre = str(input("Ingresar el Nombre :"))
    edad = int(input("Ingresar la edad: "))
    validacion = nombre[0]

    if validacion in Base_Datos:
        Grupoa[nombre] = edad
    else:
        Grupob[nombre] = edad
    contador += 1

print("La cantidad del personas en el grupo a es {}".format(Grupoa.__len__()))
print("La cantidad del personas en el grupo b es {}".format(Grupob.__len__()))


"""
Ejercicio 7
Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:


Renta	Tipo impositivo
Menos de 10000€	5%
Entre 10000€ y 20000€	15%
Entre 200000€ y 35000€	20%
Entre 350000€ y 60000€	30%
Más de 60000€	45%
Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.
"""
def calcula_impositivo(r):
    if (r < 10000):
        print("El tipo impositivo es 5%")
    if (r >= 10000 and r < 20000):
        print("El tipo impositivo es 15%")
    if (r >= 20000 and r < 35000):
        print("El tipo impositivo es 20%")
    if (r >= 35000 and r < 60000):
        print("El tipo impositivo es 30%")
    if (r >= 60000):
        print("El tipo impositivo es 45%")


renta_anual =  float(input("Ingrese la renta anual : "))
calcula_impositivo(renta_anual)

"""

Ejercicio 8
En una determinada empresa, sus empleados son evaluados al final de cada año. 
Los puntos que pueden obtener en la evaluación comienzan en 0.0 y 
pueden ir aumentando, traduciéndose en mejores beneficios. 
Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, 
pero no valores intermedios entre las cifras mencionadas. 
A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. 
La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más
Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, 
así como la cantidad de dinero que recibirá el usuario.

"""


"""
Ejercicio 9
Escribir un programa para una empresa que tiene salas de juegos para 
todas las edades y quiere calcular de forma automática el precio que debe 
cobrar a sus clientes por entrar. El programa debe preguntar al usuario la
 edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años 
 puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.
"""


"""
Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
Los ingredientes para cada tipo de pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
 y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. 
 Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. 
 Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
"""


