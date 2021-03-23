def main():
    Nombre1 = "Javier"
    Nombre2='Esteban'
    Concatenando = Nombre1 + " " + Nombre2
    print(Concatenando)

    #caracteres especiales.
    """
    \n -> salto de línea
    \t -> Tabulación
    
    Para trabajar con cadenas crudas se coloca un "r" adelante de la cadena.
    
    """
    print("C:\nuevacarpeta\otros")
    print(r"C:\nuevacarpeta\otros")

if __name__=="__main__":
    main()






def main():
    ######## Indices y Slicing ##################
    palabra = "PYTHON"
    # P Y T H O N
    # 0 1 2 3 4 5
    print(palabra[0]) #Ver el valor de la posición cero -- Indice
    print(palabra[2:]) #Slicing
    print(palabra[:2]) #slicing
    print(palabra[-1]) #Ver el valor de la posición cero  -- Indice
    print(palabra[::-1]) #Ver la palabra al reves

if __name__ =='__main__':
    main()


