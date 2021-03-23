#Trabajando con Fechas

from datetime import time
from datetime import date
from datetime import datetime

def main():
    fecha = date.today()
    print(fecha)
    print(fecha.day)
    print(fecha.year)
    print(fecha.month)
    print(str(fecha).replace("-",""))
if __name__ == "__main__":
    main()
