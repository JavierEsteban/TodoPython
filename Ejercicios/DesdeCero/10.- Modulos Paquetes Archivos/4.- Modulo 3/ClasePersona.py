from datetime import datetime

class Persona():
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, edad):
        self.nom = nombre
        self.app = apellidoPaterno
        self.apm = apellidoMaterno
        self.ed = int(edad)
    
    def validaPersona(self):
        return "Se creó el Objeto Persona Correctamente : {}".format(self.nom)
    
    
    def validaedad(self):
        if self.ed >= 18:
            return "La persona Creada es Mayor de edad. Su edad Actual es {}".format(self.ed)
        else:
            return "La persona es menor de Edad."
    
