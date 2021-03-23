
import tkinter
raiz = tkinter.Tk()
raiz.title("Componente Frame")


#Componente Frame, es un componente que permite crear otros componentes dentro de el.
frame = tkinter.Frame(raiz)
frame.config(bg = "blue",widt = 500, height = 500)
frame.pack()

raiz.mainloop()




