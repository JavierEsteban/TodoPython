##control de bloques con IF

def main():
    if not False:
        print("Este mensaje es verdadero....")
    print("Mostrarse este mensaje tambien....")


if __name__ == "__main__":
    main()



##Ejercicios con if y else

def main():
    nota = int(input("Ingrese la nota : "))
    if nota >= 19:
        print("Excelente...")
    elif nota <= 18 and nota >= 15:
        print("Bueno.....")
    elif nota <=14 and nota >= 11:
        print("Regular....")
    else:
        print("Malo....")



if __name__=='__main__':
    main()

