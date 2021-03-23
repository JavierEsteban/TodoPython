
from tkinter import *

ventana = Tk()
ventana.geometry("300x300")
ventana.resizable(0,0)

texto = Label(ventana, text ="Hola Mundo")
texto.config(
    fg = "white",
    bg = "#000000",
    padx = 20,
    pady = 20
)

texto.pack()

texto = Label(ventana, text="Javier Tiburcio")
texto.pack()

ventana.mainloop()


