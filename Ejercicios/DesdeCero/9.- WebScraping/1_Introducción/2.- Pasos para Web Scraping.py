"""
Pasos del Web Scraping

Paso 1 -> Definir URL semilla
paso 2 -> Hacer requerimiento a URL semilla
paso 3 -> Obtener respuesta HTML
paso 4 -> Extraer datos del HTML
paso 5 -> volver al PASO 2 con nuevas URLs

"""

from lxml import html
import requests
import datetime


def main ():
    """
    Paso1: Definición de Url Semilla y Encabezados
    """
    url = "https://www.wikipedia.org/"
    cabecera = {
        "user-agent":  "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36"
    }

    response = requests.get(url = url , headers= cabecera) #Hacer un Requerimiento a la URL semilla
    if response.status_code == 200:
        parser = html.fromstring(response.content) #Obtener el html del requerimiento
        #lenguaje = parser.xpath("//a[@id = 'js-link-box-es']/strong/text()") #Extraer datos del HTML
        lenguajes = parser.xpath("//div[contains(@class,'central-featured-lang')]//strong/text()")
        #print(lenguaje)
        for idioma in lenguajes:
            print(idioma)

    else:
        print("Error - Código de URL Errónea. Porfavor Ingrese la URL Nuevamente")


if __name__ == '__main__':
    main()


