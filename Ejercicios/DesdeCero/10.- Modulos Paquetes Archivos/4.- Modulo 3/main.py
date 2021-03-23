import ClasePersona as clp






def main():
    try:
        nombre = str(input("Ingrese Su nombre : "))
        app = str(input("Ingrese Su Apellido Paterno : "))
        apm = str(input("Ingrese Su Apellido Materno : "))
        ed = int(input("Ingrese su Edad : "))

        nueva_persona = clp.Persona(nombre= nombre, apellidoPaterno= app, apellidoMaterno= apm, edad= ed)
        print(nueva_persona.validaPersona())
        print(nueva_persona.validaedad())
    except ValueError:
        print("Error de valor ingresado, Por favor de ingresar el valor correcto..")
    except Exception as e:
        print (type(e).__name__)
        print (e)


if __name__ == '__main__':
    main()
