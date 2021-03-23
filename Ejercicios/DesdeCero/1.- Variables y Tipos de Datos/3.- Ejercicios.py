## Hallar el promedio de notas con los pesos enviados

def main():
    nota_1 = 10
    nota_2 = 7
    nota_3 = 4
    notafinal = 10*0.15 + 7*0.35 + 4*0.5
    print(notafinal)

# Completa el ejercicio aquí

if __name__ =='__main__':
    main()



#Ejercicio que cada ultimo registro de la matriz sume los 3 primeros.
def main():
    matriz = [
        [1, 1, 1, 3],
        [2, 2, 2, 7],
        [3, 3, 3, 9],
        [4, 4, 4, 13]
    ]
    ##print(matriz[1][:])
    ##print(len(matriz))
    ##print(sum(matriz))
    print("########### Antes ###############")
    print(matriz)
    contador = 0
    while contador < len(matriz):
        print(matriz[contador][:3])
        matriz[contador][3] = sum(matriz[contador][:3])
        contador = contador + 1
    print("########### Después ###############")
    print(matriz)

if __name__ == '__main__':
    print("################# Ejecutando Programa #####################")
    main()




####Los nombres está al reves

def main():
    cadena = "zeréP nauJ,01"
    print("########### Antes ###############")
    print("\n"*2)
    print(cadena)
    print("\n"*2)
    print("########### Después ###############")
    print("\n"*2)
    print(cadena[::-1])



if __name__ =='__main__':
    main()


#Ejercicio que cada ultimo registro de la matriz sume los 3 primeros.
def main():
    matriz = [
        [1, 1, 1, 3],
        [2, 2, 2, 7],
        [3, 3, 3, 9],
        [4, 4, 4, 13]
    ]
    print(matriz)
    for indice, i in enumerate(matriz):
        i[3] = sum(i[:3])

    print(matriz)

if __name__ =='__main__':
    main()

