#Importar Librería nativa de python
import sqlite3
import os
import sys

print("#####################Directorio Iniciales#################")
#imprimir ubicación inicial
directorioactual = os.getcwd()
print("El Directorio actual es : {}".format(directorioactual))

os.chdir(r'D:\Cursos\Python\Ejercicios\DesdeCero\5.- Accesos a Datos\1.- SqLite\BasesDeDatos')
nuevo = os.getcwd()
print("El Directorio Nuevo es : {}".format(nuevo))
print("\n")
print("#####################Creación tabla Productos#################")
#Abre la conexión
conexion = sqlite3.connect("Retaildata.db")

#Crea el cursor
cursor = conexion.cursor()

try:
    #Ejecuta la query
    cursor.execute(" Create Table Productos ( IdProducto int, DescProducto varchar(50), PrecioVenta decimal(18,5), Costo decimal(18,5))")
except sqlite3.OperationalError:
    print("ERROR - La Tabla Productos ya se encuentra creada en la Base de Datos")
except Exception as e:
    print(type(e).__name__)
else:
    #commitea la query
    conexion.commit()
finally:
    #cierra la conexión
    conexion.close()


##; Create Table Tienda ( IdTienda int, NombreTienda varchar(50))


print("\n")
print("#####################Creación tabla Tienda#################")

conexion2 = sqlite3.connect("Retaildata.db")
cursor2 = conexion2.cursor()
query = """
        Create Table Tienda ( IdTienda int, NombreTienda varchar(50))
"""
try:
    cursor2.execute(query)
except sqlite3.OperationalError:
    print("ERROR - La Tabla Tiendas ya se encuentra creada en la Base de Datos")
except Exception as e:
    print(type(e).__name__)
    ##print(type(e).__str__())


conexion2.commit()
conexion2.close()


print("\n")
print("##################### Insertar los Datos Utilizando Execute Many #################")

conexion3 = sqlite3.connect("Retaildata.db")
cursor3 = conexion3.cursor()
quey_productos = [
    (100001,"Hielo 2.5L", 2.50000, 1.00000),
    (100002,"Empanada Pollo", 4.50000, 2.00000),
    (100003,"Pizza Familiar", 10.50000, 5.00000),
    (100004,"Inka Cola 2L", 5.50000, 4.00000)
]
cursor3.executemany('Insert into Productos (IdProducto, DescProducto, PrecioVenta, Costo) values(?,?,?,?)',quey_productos)
conexion3.commit()
conexion3.close()


print("\n")
print("##################### Insertar los Datos Utilizando Execute  Script #################")

conexion4 = sqlite3.connect("Retaildata.db")
cursor4 = conexion4.cursor()
query = """
Insert into Tienda (IdTienda, NombreTienda) Values (1, 'Comas');
Insert into Tienda (IdTienda, NombreTienda) Values (2, 'Pethit');
Insert into Tienda (IdTienda, NombreTienda) Values (3, 'Camana');
Insert into Tienda (IdTienda, NombreTienda) Values (4, 'Tda Tacna');

"""
cursor4.executescript(query)
conexion4.commit()
conexion4.close()



