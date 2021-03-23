import os
print(os.getcwd())

"""

Utilizar el lenguaje de Programación preferido.

Crear una base de datos con los clientes con
programación estructuradas y realizar las
siguientes opciones:

1.- Crear Clientes
2.- Buscar Clientes
3.- Listar Clientes
4.- Eliminar Clientes
5.- Exportar clientes en un archivo Txt.

 Todo con Programación Estructurada

"""

from datetime import datetime

clientes = [
    {'Dni': '47970282', 'Nombres': 'Javier Esteban', 'Apellidos': 'Tiburcio Ortega', 'Edad': 26},
    {'Dni': '33251083', 'Nombres': 'Inocenta Tomasa', 'Apellidos': 'Ortega Principe', 'Edad': 54},
    {'Dni': '46433234', 'Nombres': 'Roy Bryan', 'Apellidos': 'Tiburcio Ortega', 'Edad': 28}
]



def Buscar():
    valor = False
    dni = str(input("Ingrese el Dni : "))
    nombre = None
    for i in clientes:
        if i['Dni'] == dni:
            nombre = i['Nombres']
            valor = True
    return valor, dni, nombre



def Eliminar():
    valor, dni, nombre = Buscar()
    if(valor):
        for i, c in enumerate(clientes):
            if c['Dni'] == dni:
                print("Se Elimino Correctamente el Cliente : {}".format(c['Nombres']))
                clientes.pop(i)
    else:
        print("El Dni Ingresado no existe en la BD")
    main()


def Exportar():
    fecha = datetime.now()
    nombrearchivo = 'Clientes_' + fecha.strftime("%Y%m%d") + '.txt'
    #abrir archivo
    archivo_empleados = open(nombrearchivo, 'w+')
    #Escribiendo Archivo
    for i in clientes:
        archivo_empleados.write(i['Dni'] + ';' + i['Nombres'] + ';' + i['Apellidos'] + '\n')

    #cerrando archivo
    print("Se creó correctamente el archivo")
    archivo_empleados.close()
    main()




def agregar():
    Dni = str(input('Ingrese el Dni.... : '))
    Nombres = str(input('Ingrese los Nombres ..... : '))
    Apellidos = str(input('Ingrese los Apellidos ..... : '))
    Edad = str(input('Ingrese la Edad ..... : '))

    # Agregando Cliente Nuevo
    clientes.append({'Dni' : Dni, 'Nombres': Nombres, 'Apellidos': Apellidos , 'Edad': Edad})
    print('Se agrego Correctamente el Cliente : {} {}'.format(Nombres, Apellidos))

    # Llamando nuevamente la función Principal
    main()

def main():

    print("""


---------------------  Comienza el Programa ----------------------------
        
        1.- Agregar
        2.- Buscar
        3.- Eliminar
        4.- Exportar
        5.- Salir        
        
        
    """)

    valor = int(input("Ingrese el Valor... :  "))

    if valor == 1 :
        agregar()
    elif valor == 2:
        valor, dni, nombre = Buscar()
        if(valor):
            print("El clientes Buscado es {} ".format(nombre))
        else:
            print("El cliente No se encuentra en la BD....")
        main()
    elif valor == 3:
        Eliminar()
    elif valor == 4:
        Exportar()
    elif valor == 5:
        exit()


if __name__ == '__main__':
    main()
