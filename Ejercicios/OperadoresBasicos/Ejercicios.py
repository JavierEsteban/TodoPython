## Ejercicios

#Ejercicios 1 :

'''
Ejercicio 1
Escribir un programa que pregunte al usuario su nombre, y luego lo salude.
'''

Nombre = input("Ingrese SU nombre : ")
SaludoCompleto = "Hola Buenas Noches, {}.".format(Nombre)

print(SaludoCompleto)


'''
Ejercicio 2
Calcular el perímetro y área de un rectángulo dada su base y su altura.
'''


Lado1 = int(input("Ingrese el primer Lado :"))
Lado2 = int(input("Ingrese el Segundo Lado :"))

Area = Lado1 * Lado2
Perimetro = 2* (Lado1 + Lado2)

print("El rectangulo tiene los siguientes lados, Lado 1 es igual a {}, el segundo lado es igual a {}, el área es igual a {} y el perimetro es {}.".format(Lado1, Lado2, Area, Perimetro))

'''
Ejercicio 3
Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
'''

LadoTriangulo1 = int(input("Ingrese primer cateto : "))
LadoTriangulo2 = int(input("Ingrese segundo cateto : "))

if LadoTriangulo1 == 0 or LadoTriangulo2 == 0:
    Hipotenusa = "Uno de los catetos es cero y no se puede calcular la Hipotenusa."
    print(Hipotenusa)

else :
    Hipotenuesa =  pow( pow(LadoTriangulo1,2) + pow(LadoTriangulo2,2), 0.5)
    print("La hipotenusa de los lados es el siguiente : {}".format(Hipotenuesa))





'''
Ejercicio 4
Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
'''

Numero1 = int(input("Ingresar el Primer numero : "))
Numero2 = int(input("Ingresar el Segundo numero : "))

Suma = Numero1 + Numero2
Resta = Numero1 - Numero2
Multiplicacion = Numero1 * Numero2

if(Numero2 == 0):
    Division = "No se puede realizar la Division entre Cero. "
else:
    Division = Numero1 / Numero2

print("La Suma es : {}".format(Suma))
print("La Resta es : {}".format(Resta))
print("La Multiplicacion es : {}".format(Multiplicacion))
print("La Division es : {}".format(Division))


'''

Ejercicio 5
Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
Recordar que la fórmula para la conversión es:
1.	C = (F-32)*5/9

'''

ValorFah = int(input("Ingresar el valor en Fahrenheit : "))
ValorCel = ( ( ValorFah - 32 ) * 5 ) / 9

print("El valor fahre es {} y su conversión en celsius es : {} .".format(ValorFah, ValorCel))



'''
Ejercicio 6
Calcular la media de tres números pedidos por teclado.
'''



'''
Ejercicio 7
Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a cuantas horas y minutos corresponde.
Por ejemplo: 1000 minutos son 16 horas y 40 minutos.
'''




'''
Ejercicio 8
Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su sueldo base y comisiones.
'''




'''
Ejercicio 9
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto deberá pagar finalmente por su compra.
'''





'''
Ejercicio 10
Un alumno desea saber cual será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los siguientes porcentajes:
•	55% del promedio de sus tres calificaciones parciales.
•	30% de la calificación del examen final.
•	15% de la calificación de un trabajo final.
'''


