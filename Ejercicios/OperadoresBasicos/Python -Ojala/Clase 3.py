# Manejo de archivos con python

from datetime import date

def Escritura_Archivo(valor = "Defecto",NumeroRepeticiones = 2):
    nombreArchivo = "Archivo" + str(date.today()).replace("-","") +".Txt"
    archivo = open(nombreArchivo,"w+")
    for i in range(0,NumeroRepeticiones):
        archivo.write("El valor ingresado es {} y el número de la repetición es:  {} ..\n".format(valor,i+1))
    archivo.close()

def main():
    Valor = str(input("Ingrese el valor que desee que salga..."))
    NumeroRepeticiones = int(input("Ingrese el número de repeticiones...."))
    Escritura_Archivo(Valor, NumeroRepeticiones)
    print("ProgramaFinalizado.....")
    pass


if __name__ == '__main__':
    main()


"""
# Open a file in read/write mode
fo = open("archivo.txt", "r+")
print("Name of the file: ", fo.name)

# Open a file
fo = open("archivo.txt", "r")
print ("Name of the file: ", fo.name)

# Close opened file
fo.close()


##Valores importantes
'r' : usar para leer
'w' : uso para escribir  --> Elimina lo que había en el archivo y vuelve a escribir desde cero
'x' : se usa para crear y escribir en un archivo nuevo
'a' : se usa para agregar a un archivo --> Agrega información desde el último linea
'r+' : se usa para leer y escribir en el mismo archivo

"""
