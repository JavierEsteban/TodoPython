"""
Proyecto :
Generar un proyecto que realicé los siguientes procesos básicos :

1- Cargar Clientes
2- Buscar Clientes
3- Listar Clientes
4- Exportar Clientes : Elegir formato (.txt, .Csv)
5- Salir

Obs: Manejar Bases de Datos SQLLITE
"""
from datetime import datetime
import os
import sqlite3


def Crear_Conexion():
    conexion = None
    try:

        os.chdir(r"D:\Cursos\Python\Ejercicios\DesdeCero\9999_Proyectos\1_Proyecto_Usuario")
        DB_FILE = "Clientes_Data.db"
        conexion = sqlite3.connect(DB_FILE)
#       print("Conexión Establecida...")
    except Exception as e:
        print(type(e).__name__)
    return conexion


def Carga_Clientes(valor):
    if valor == "MANUAL":

        Nombes = str(input("Ingrese los Nombres.... "))
        ApP = str(input("Ingrese el Apellido Paterno...."))
        ApM = str(input("Ingrese el Apellido Materno...."))
        Correo = str(input("Ingrese el Correo...."))

        #Recupera el ultimo IdCliente
        sql_var1 = """
            SELECT  IdCliente
            FROM Clientes
            ORDER BY IdCliente
            LIMIT 1;
        """
        conn = Crear_Conexion()
        cursor = conn.cursor()
        Idcliente = cursor.execute(sql_var1)
        #print(Idcliente)

        if (Idcliente is not  None):
            sql_var2 = """
                insert into Clientes
                ( Nombres, ApPaterno, ApMaterno, Email)
                values
                (?, ?, ?, ?);"""
            tupla = (Nombes, ApP, ApM, Correo)
            #print(sql_var2)
            cursor.execute(sql_var2,tupla)
            conn.commit()
            conn.close()
            print("\n")
            print("El Cliente {} ,Fue Registrado Correctamente.....".format(Nombes + ' ' + ApP))
            print("\n")
        else:
            print("\n")
            print("No Existe Clientes Registrados en la Base de Datos....")

    elif valor =="MASIVO":


        conn = Crear_Conexion()
        cursor = conn.cursor()

        os.chdir(r"D:\Cursos\Python\Ejercicios\DesdeCero\9999_Proyectos\1_Proyecto_Usuario\ImportarMasivamente")
        archivos = "Maestro_Clientes.txt"
        archivo = open(archivos,'r+')
        for indice, valor in enumerate(archivo):
         if indice != 0:
            Nombres, ApPaterno, ApMaterno, Email = valor.split("|")
            tupla = (Nombres, ApPaterno, ApMaterno, Email.replace("\n",""))
            query = """ Insert into Clientes
                ( Nombres, ApPaterno, ApMaterno, Email)
                values
                (?, ?, ?, ?); """
            cursor.execute(query, tupla)
            conn.commit()
        print("Carga masiva correctamente...")
        archivo.close()
        conn.close()

    else:
        print("Valor No definido")


def Buscar_Cliente(variable):
    valor = int(variable)
    if valor > 0 :
        conn = Crear_Conexion()
        cursor = conn.cursor()
        query = """
            SELECT IdCliente, Nombres, ApPaterno, ApMaterno, Email
            FROM CLIENTEs
            WHERE IdCliente = ?
        """

        Data_Cliente = cursor.execute(query,[valor])
        for data in Data_Cliente:
            IdCliente, Nombres, ApPaterno, ApMaterno, Email = data
            print("\nEl cliente es : {}, con el codigo {} y email {} .".format(Nombres + ' ' + ApPaterno,IdCliente,Email))
        conn.commit()
        conn.close()
    else:
        print("Error - Valor Menor que Cero...")
        print("Saliendo...")
        return

def Visualizacion_Clientes(numero_clientes):
    if 0 < numero_clientes  < 1000:
        conn = Crear_Conexion()
        cursor = conn.cursor()
        query = """
            SELECT IdCliente, Nombres, ApPaterno, ApMaterno, Email
            FROM CLIENTES
            Order by IdCliente asc
            LIMIT ? 
        """
        Usuarios =  [ str(valor[0])+ " " + valor[1] for indice, valor in enumerate(cursor.execute(query, [numero_clientes])) ]
        for i in Usuarios:
            print(i)
        conn.close()

    else:
        print("Error - No se pueden mostrar valores en negativos o mayores a 1000 Usuarios")

def Exportar_Clientes(formato):
    """
        Funcion valida para exportar clientes con los formatos txt y csv en forato de comas....
    """
    formato = int(formato)
    conn = Crear_Conexion()
    cursor = conn.cursor()
    query = """
        SELECT IdCliente, Nombres, ApPaterno, ApMaterno, Email
        FROM CLIENTES
    """

    if formato == 1:
        clientes = cursor.execute(query)
        nombrearchivo = "Exporta_Clientes_"+ str( datetime.now().strftime("%Y%m%d")) + ".TXT"
        #print(nombrearchivo)
        archivo_texto = open(nombrearchivo, 'w+')
        archivo_texto.write("IdCliente,Nombres,ApPaterno,ApMaterno,Email\n")
        for valores in clientes:
            archivo_texto.write(str(valores[0])+","+valores[1]+","+valores[2]+","+valores[3]+","+valores[4]+ "\n")
        archivo_texto.close()
        print("Exportado Correctamente.....")
    elif formato == 2:
        clientes = cursor.execute(query)
        nombrearchivo = "Exporta_Clientes_"+ str( datetime.now().strftime("%Y%m%d")) + ".CSV"
        archivo_csv = open(nombrearchivo, 'w+')
        archivo_csv.write("IdCliente,Nombres,ApPaterno,ApMaterno,Email\n")
        for valores in clientes:
            archivo_csv.write(str(valores[0])+","+valores[1]+","+valores[2]+","+valores[3]+","+valores[4]+ "\n")
        archivo_csv.close()
        print("Exportado Correctamente.....")
    else:
        print("Error - Favor de ingresar una opción correcta...")
    conn.commit()
    conn.close()


def main():
    while True:
        try:
            valor = int(input("""
            
            ######################################################
            
            Inicio de Programa:
            1.- Cargar Nuevo Cliente (Manual o Masivo)
            2.- Buscar Clientes     
            3.- Listas Clientes ( Ingresar la cantidad de clientes)
            4.- Exportar Clientes (Elegir Formato *.CSV, *.TXT) 
            5.- Salir del Programa
            
            ######################################################
            
            """))

            if valor == 1:
                tipo_carga = str(input("Elegir si desea carga másiva o carga Manual ...")).upper()
                Carga_Clientes(tipo_carga)
            elif valor == 2:
                variable = int(input("Buscar la Información del Cliente, Favor Ingrese el Código.."))
                Buscar_Cliente(variable)
            elif valor == 3:
                numero_clientes = int(input("Ingresar el número de clientes que desea visualizar..."))
                Visualizacion_Clientes(numero_clientes)
            elif valor == 4:
                formato = int(input("""
                    Elija la opción de exportación :
                    1 : formato TXT
                    2 : Formato CSV
                    Porfavor de Elegir un número
                """))
                Exportar_Clientes(formato)
            elif valor == 5:
                fecha = datetime.now().strftime("%d/%m/%y %H:%M")
                print("Siendo {}, Saliendo del Programa.....".format(fecha))
                break
            else:
                print("La Opción no corresponde a la Lista.....")

        except ValueError:
            print("Se Debe de Ingresar Valores Númericos....")
        except Exception as e:
            print(type(e).__name__)


if __name__ =='__main__':
    main()
