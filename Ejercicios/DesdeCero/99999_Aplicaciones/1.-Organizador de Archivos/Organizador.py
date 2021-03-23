
#Aplicación para organizar los archivos en carpetas ordenadas
import socket
import sys
import os
import shutil


def Buscar_Extension(valor_extension):
    nombres_archivos = {
        #'Word','Excel','PPT','Aplicaciones', 'Bkps', 'Comprimidos', 'Texto', 'PDF',
        'Word':['.DOC', '.DOCX'],
        'Excel':['.XLSX','.XLS','.CSV'],
        'Aplicaciones':['.EXE'],
        'Bkps':['.BAK'],
        'Comprimidos':['.ZIP', '.RAR'],
        'Texto':['.TXT'],
        'Querys':['.SQL'],
        'Reporte':['.RPT'],
        'PDF':['.PDF'],
        'KMZ':['.KML','.KMZ'],
        'CAD': ['.DWG', '.DWT','.DFX','.XML'],
        'PPT':['PPTX','PPT']
        }
    valor_extension = valor_extension.upper()
    for extensiones in (nombres_archivos):
        if valor_extension in nombres_archivos[extensiones]:
            return extensiones
            break
    else:
        return "Otros"

def Crea_Directorios(Carpetas):

    for carpeta in Carpetas:
        try:
            os.mkdir(carpeta)
        except FileExistsError:
            print("La carpeta {} Ya esxite".format(carpeta))

def Elimina_Directorios(Carpetas):
    
    for carpeta in Carpetas:
        try:
            os.rmdir(carpeta)
        except OSError:
            shutil.rmtree(os.path.join(os.getcwd(), carpeta))
        else:
            pass
        finally:
            pass

def Mueve_Directorio():      
    for archivo in os.listdir():
        if os.path.isfile(archivo): 
            valor_extension = os.path.splitext(archivo)[1]
            Carpeta_Solicitada = Buscar_Extension(valor_extension.upper())
            print(Carpeta_Solicitada)
#            print(archivo + ' Archivo : ' + os.path.splitext(archivo)[1])
#            print(os.path.splitext(archivo))
            print(archivo + "==>" + Carpeta_Solicitada + '/' + archivo)
            try:
                shutil.move(archivo, Carpeta_Solicitada + '/' + archivo)
            except FileNotFoundError:
                print("Carpeta {} No Existe".format(Carpeta_Solicitada))
            except PermissionError:
                print("El archivo {} Se encuentra Abierto o sin permisos, No se puede mover..".format(archivo))
            except Exception as e:
                print(type(e).__name__)
            print("==========")

def main():
    directorio = input(r"Ingresa la Ruta a Organizar: ")
    #print(os.getcwd())
    try:
        os.chdir(directorio)
        #print(os.listdir())
        #print(os.getcwd())
        Carpetas = ['Word','Excel','PPT','Aplicaciones', 'Bkps', 'Comprimidos', 'Texto', 'PDF','Querys','Reporte','Otros', 'KMZ']
        #Elimina_Directorios(Carpetas)
        Crea_Directorios(Carpetas)
        Mueve_Directorio()

    except FileNotFoundError:
        print("Directorio no Existe...")
    
if __name__== "__main__":
    main()
