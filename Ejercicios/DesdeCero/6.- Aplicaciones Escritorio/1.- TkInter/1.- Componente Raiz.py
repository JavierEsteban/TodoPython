"""

Pasos:
    1.- Importar librería Tk
    2.- Generar un elemeto Raiz
    3.- Ejecutar periodicamente

"""
##Ejemplo 1:

# Importar la librería TKINTER
import  tkinter
import  os
from os import path
from tkinter import *

# Crear la Raíz
Raiz = tkinter.Tk()

# Colocar el Título
Raiz.title("Mi Primer Interfaz Python")
Raiz.geometry("750x450")
Raiz.resizable(0,0)
#os.chdir(r"D:\Cursos\Python\Ejercicios\DesdeCero\6.- Aplicaciones Escritorio\1.- TkInter")
#Raiz.iconbitmap("./Img/Analisis.ico")
Ruta = path.abspath('./6.- Aplicaciones Escritorio/1.- TkInter/Img/Analisis.ico')

#print(os.getcwd())
Raiz.iconbitmap(Ruta)
texto = Label(Raiz, text=Ruta)
texto.pack()

# Mostrar la ventana Principal
Raiz.mainloop()
