#Modo 1 de importar Líbrerias.
import random as rn

CantVeces = 1
while CantVeces <= 10:
    print(" Iteración {} =>  {}".format(CantVeces, rn.randint(0, 5)))
    CantVeces += 1

#Modo 2 de Importar Librería.
from  random import randint

print(randint(0,50))

#Modo 3 de Importar Librería.
from random import *
print(randint(0,80))
print(random())

