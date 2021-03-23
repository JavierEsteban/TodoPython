#Creación de Clase Carro
class Auto:

#Declaración de Variables
    marca = ""
    anio = 0
    kilometraje = 0


Nissan = Auto()
Nissan.marca = "Nissan SSS"
Nissan.anio = 2019
Nissan.kilometraje = "10 000 KM"

print(Nissan.marca)
print(Nissan.anio)
print(Nissan.kilometraje)

#Creación de Clase Curso


class Curso:




    def __init__(self, nombre, docente, numero_creditos):
        self.nombre = nombre
        self.docente = docente
        self.numero_creditos = numero_creditos
        self.listaprofesores = []

    def Agrega_Profesores(self,docente):
        pass
        #listaprofesores






def main():
    curso1 = Curso(nombre="Matematica 1", docente="Javier Tiburcio", numero_creditos= 3)
    curso1.Agrega_Profesores(curso1.docente)
    curso2 = Curso(nombre="Lenguaje 1", docente="Roy Tiburcio", numero_creditos= 5)
    curso2.Agrega_Profesores(curso1.docente)
    curso3 = Curso(nombre="Lenguaje de Programación 1", docente="Mirian Tiburcio", numero_creditos=6)
    curso3.Agrega_Profesores(curso1.docente)





if __name__ == '__main__':
    main()



