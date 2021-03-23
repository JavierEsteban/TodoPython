import modulo

def main():
    Nombre = str(input("Ingrese el Nombre : "))
    App = str(input("Ingrese el Apellido Paterno : "))
    Apm = str(input("Ingrese el Apellido Materno : "))
    personas = modulo.persona(Nombre= Nombre, ApellidoPaterno= App, ApellidoMaterno = Apm)
    personas.saludar()


if __name__=='__main__':
    main()
