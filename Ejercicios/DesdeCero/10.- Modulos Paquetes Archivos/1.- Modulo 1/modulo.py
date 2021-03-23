
from datetime import datetime

class persona():

    fecha = datetime.now().strftime("%Y-%m-%d")

    def __init__(self,Nombre, ApellidoPaterno, ApellidoMaterno):
        self.Nombre = Nombre
        self.ApellidoPaterno = ApellidoPaterno
        self.ApellidoMaterno = ApellidoMaterno

    def saludar(self):
        print("Buen día {}, su ingreso es {}".format(self.Nombre, persona.fecha))



