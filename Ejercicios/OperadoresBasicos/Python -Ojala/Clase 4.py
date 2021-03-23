## Escribir en un archivo con loop que pregunte nuevamente, sobre escribirlo y colocar las fechas en la que se
## sobreescribio

from datetime import date
from datetime import time
from datetime import datetime

"""
actual = datetime.now()
fecha = date.today()
hora = time.hour
print(actual.strftime("%Y-%m-%d %H:%M  : "))
"""

def escribir():
    valor = str(input("Que desea escribir...:  "))
    cuantas = int(input("Cantidad de veces que se escribe..:  "))
    archivo = 'archivo.txt'
    narchivo = open(archivo, 'a+')
    contador = 0
    while(contador < cuantas):
        actual = datetime.now()
        formato = actual.strftime("%Y-%m-%d %H:%M  : ")
        narchivo.write(formato + "Se escribio el valor {}, el número de veces {}\n".format(valor,cuantas))
        contador += 1
    narchivo.close()

def main():

    while(True):
        valor = str(input("Desea iniciar SI/NO ....")).lower()
        if(valor == "si"):
            escribir()
            print("Se escribio Correctamente...")
        else:
            print("Programa Terminado...")
            break
    pass

if __name__ == "__main__":
    main()
