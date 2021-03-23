
#Creación de BD SQLITE
### Estructura de accesos a Bases de datos
"""

1.- Importa librería.
2.- Abre la conexión.
3.- abre un cursor.
4.- Ejecuta la query y aplica el commit.
5.- Cierre la conexión

"""

## Importar librería...
## Scrip para Cambiar el Directorio de Trabajo
import os

curDir = os.getcwd()
print("####### Directorio Actual #######")
print(curDir)

print("####### Directorio Nuevo #######")
os.chdir(r"D:\Cursos\Python\Ejercicios\DesdeCero\5.- Accesos a Datos\1.- SqLite\BasesDeDatos")
curDirNew = os.getcwd()
print(curDirNew)


##Conectandome y creando una tabla

import sqlite3

print("Creando la Base de Datos")
conexion = sqlite3.connect("Ejemplo.db")
print("Abriendo Cursor")
cursor = conexion.cursor()
print("Ejecutando Query")
cursor.execute("Create table Productos (IdProducto int, NombreProduct varchar(100))")
conexion.commit()
print("Cerrando Conexión")
conexion.close()

## Insertando registros a la tabla creada
import sqlite3
conn = sqlite3.connect("Ejemplo.db")
cursor = conn.cursor()
cursor.execute("insert into Productos values (1, 'Naranjas')")
conn.commit()
conn.close()


## Insertando registros a la tabla creada
import sqlite3
conn = sqlite3.connect("Ejemplo.db")
cursor = conn.cursor()
cursor.execute("insert into Productos values (3, 'Manzanas')")
conn.commit()
conn.close()


##Mostrando los registros...

import  sqlite3
conexion2 = sqlite3.connect("Ejemplo.db")
cursor = conexion2.cursor()

Productos = cursor.execute("Select * from productos ")

## print(type(Productos))
for product in Productos:
    ##print(product)
    print("El código del Producto es {} y la descripción : {}".format(product[0],product[1]))

conexion2.close()


## Insertando masivamente en la Bases de datos....

import sqlite3
conexion3 = sqlite3.connect("Ejemplo.db")
cursor = conexion3.cursor()
query = [
    (7,"Mandarina"),
    (8, "Uva"),
    (55,"Plata")]

cursor.executemany("Insert Into Productos (IdProducto, NombreProduct) Values (?,?)",query)
conexion3.commit()
conexion3.close()



