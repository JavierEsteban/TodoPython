
#Creación de una clase en Python
class Carro():
    color = 'Rojo'


def main():
    carro1 = Carro()
    print(carro1.color)

if __name__=='__main__':
    main()




##EJEMPLO SIN POO
def buscar_Cliente(clientes, nombre):
    estado = False
    for i, n in enumerate(clientes):
        if n['nombre'] == nombre:
            print("Cliente Encontrado: {}, con la edad : {}".format(n['nombre'], n['edad']))
            estado = True
            return estado
            break
    print("Cliente No encontrado..........")

def eliminar_Cliente(clientes, nombre):
    for i , valor in enumerate(clientes):

        if valor['nombre'] == nombre:
            print("Eliminando Cliente : {} .....".format(valor['nombre']))
            clientes.pop(i)
            #del(valor['nombre'])
    print("Cliente No encontrado..........")


def main():
    #Creación de Base de datos
    clientes = [
        {'nombre':"Javier Tiburcio", "edad" : 27, "FechaNacimiento" : "11/09/1993"},
        {'nombre':"Roy Tiburcio", "edad" : 29, "FechaNacimiento" : "15/10/1991"},
        {'nombre':"Mirian Tiburcio", "edad" : 14, "FechaNacimiento" : "20/12/2004"}
    ]

    nombre = input("Ingrese el Nombre : ")
    clienteencontrado =buscar_Cliente(clientes,nombre)

    if clienteencontrado == True:
        estatus = str(input("Desea eliminar el cliente : "))

        if estatus.upper() == "SI":
            eliminar_Cliente(clientes,nombre)
            print("Nuevo Listado..... ")
            print(clientes)
        else:
            print("Cerrando Programa..............")
            print("Nuevo Listado..... ")
            print(clientes)
    else:
        print("Cerrando Programa..............")



if __name__ == '__main__':
    main()



##Ejercicio con POO


class Cliente():

    def __init__(self, nombres, apellidos, dni):
        self.nombres = nombres
        self.apellidos = apellidos
        self.dni = dni
"""
    def __str__(self):
        return '{} {}'.format(self.nombres, self.apellidos)
"""

class Empresa():

    def __init__(self, listadocliente = []):
        self.listadocliente = listadocliente

    def buscar_clientes(self, dni = None):
        for i in self.listadocliente:
            if i.dni == dni:
                print("Encontrado correctamente : {}".format(i.nombres))
                return
                break
        print("No se encontro Cliente")

    def eliminar_clientes(self, dni = None):
        for indice, valor in enumerate(self.listadocliente):
            if valor.dni == dni:
                print("Borrado Correctamente : {}".format(valor.nombres))
                del(self.listadocliente[indice])
                return
                break
        print("No se encontro Cliente")


def main():
#Crear Objeto cliente
    cliente1 = Cliente(nombres="Javier Esteban", apellidos="Tiburcio Ortega", dni= "47970282")
    cliente2 = Cliente(nombres="Roy", apellidos="Tiburcio Ortega", dni= "47870282")
#crear objeto Empresa que tenga objetos cliente
    empresa1 = Empresa(listadocliente = [cliente1, cliente2])
    empresa1.buscar_clientes(dni='4797028')
    empresa1.eliminar_clientes(dni='4797028')


if __name__ =="__main__":
    main()
