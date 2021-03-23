##Funciones en python
##Son fragmentos de códigos buenos para reutilizar códigos.

def main():

    def saludar():
        print("Esta es una Función...")

    saludar()

if __name__=='__main__':
    main()


##Ejemplos tabla de multiplicar....

def Tabla(tablanum):
    contador = 0
    while(contador <= 12):
        print(" {} * {} = {}".format(tablanum, contador, tablanum * contador))
        contador += 1


def main():
    tabladel = int(input("Ingresar número de la tabla de multiplicar..... "))
    Tabla(tabladel)
    print("####Cerrando Programa#######")

if __name__=='__main__':
    main()


