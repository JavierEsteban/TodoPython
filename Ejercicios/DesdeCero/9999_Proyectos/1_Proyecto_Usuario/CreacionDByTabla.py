
import sqlite3
import os

"""
Pasos para la Conexión a una BD SQLLITE
1.- Ubicación del Archivo (db)
2.- Abrir una conexión
3.- Genera un cursor
4.- Ejecuta un query
5.- aplica los cambios con commit a la conexión.
6.- Cerrar conexión.
"""


os.chdir(r"D:\Cursos\Python\Ejercicios\DesdeCero\9999_Proyectos\1_Proyecto_Usuario")
DB_FILE = "Clientes_Data.db"
conexion = sqlite3.connect(DB_FILE)
cursor = conexion.cursor()
query = """
    Create Table Clientes(
        IdCliente INTeger PRIMARY KEY AUTOINCREMENT, 
        Nombres varchar(100), 
        ApPaterno varchar(100), 
        ApMaterno varchar(100), 
        Email varchar(100)
    );
"""


cursor.execute(query)
conexion.commit()
conexion.close()




