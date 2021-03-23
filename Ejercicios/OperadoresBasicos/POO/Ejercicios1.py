### Definición de la Clase persona

class persona:

    def __init__(self,nombre, app, apm, edad, address):
        self.nombre = nombre
        self.app = app
        self.apm = apm
        self.edad = edad
        self.address = address
        print("Se acaba de crear una persona....")


    def imprimir(self):
        print("Nombre : {}".format(self.nombre))

persona1 = persona(nombre='Javier',app='tiburcio',apm='ortega',edad= 26, address='Los Olivos')
persona1.imprimir()

persona2 = persona('Roy','Tiburcio','Ortega',28,'Los Olivos')
persona2.imprimir()




