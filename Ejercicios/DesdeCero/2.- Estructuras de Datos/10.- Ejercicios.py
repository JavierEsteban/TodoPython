
"""
Ejercicios:

Hacer un aplicativo que pida un número positivo y que el programa sume los
impares desde el cero hasta el número ingresado inclusive.

Si se ingresa un número negativo, se deberá mostrar: La suma es cero.

"""

def main():
    print("###########Inicio de Programa###########")
    print("\n"*1)
    numero = int(input("Ingresar un número entero......"))
    contador = 0
    acumulador_impares = 0
    acumulador_pares = 0
    if(numero >= 0):
        while contador <= numero:
            if contador % 2 == 0:
                acumulador_pares = contador + acumulador_pares
            else:
                acumulador_impares = acumulador_impares + contador
            contador += 1
    else:
        print("###########Resultados###########")
        print("La suma es cero.")

    print("###########Resultados###########")
    print("La suma de los Impares es : {}".format(acumulador_impares))
    print("La suma de los Pares es : {}".format(acumulador_pares))


if __name__ == '__main__':
    main()

