#También conocidos como Set en Python
"""

La declaración básica de este tipo de colección en Python es de la siguiente manera....
S = set{}  -- Conjunto mutable
s = frozenset()  -- Conjunto Inmutable

Los Conjuntos no pueden contener objetos como listas, conjuntos , diccionarios entre otros

"""


def name():
    #Declaración de Conjunto
    s = {'a',1,'b',2,'c',3}
    print(s)

    #Agrega elementos a la tupla
    s2 = set()
    s2.add('a')
    s2.add(1)
    s2.add(2)
    s2.add('b')
    print(s2)

    #Quita elemntos de la tupla
    s2.discard('b')
    print(s2)

    #Agrega elementos a la tupla
    s2.update( 'e','f')
    s2.update([1,2,6,7,9])
    print(s2)

if __name__ == '__main__':
    name()






####### Union de conjuntos #########

def main():

    print("##### Declaración de Conjuntos #######")
    a = {1, 2, 3, 4}
    b = {2, 4, 6, 8}

    print("Conjunto A : {}".format(a))
    print("Conjunto B : {}".format(b))

    union = a | b
    print("Union Conjunto A y B : {}".format(union))

    interseccion = a & b
    print("Intersección conjunto A y B : {}".format(interseccion))


if __name__=='__main__':
    main()
    print("############ Programa Finalizado.... ############")
