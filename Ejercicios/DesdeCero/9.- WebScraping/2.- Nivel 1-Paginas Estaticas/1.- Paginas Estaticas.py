"""

En este módulo se utilizarán las siguientes librerías:
1.- Request
2.- lxml
3.- beautifulsoup4
4.- Scrapy

# lxml y bs4 son herramientas para recorrer y parsear el HTML
"""


"""
Caso de estudio : Wikipedia
        Extraer los idiomas de wikipedia.
        
Utilizaremos la librería : 
    Requests ->get
    lxml ->html->fromstring
    
"""

import requests
from lxml import html

encabezados = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36"

}
url = "https://www.wikipedia.org/"

respuesta = requests.get(url, encabezados)
#print(respuesta.text)
parser = html.fromstring(respuesta.text)
parser2 = html.fromstring(respuesta.content)
print(respuesta.text)

print(parser)
print(parser2)

ingles = parser.get_element_by_id("js-link-box-en")
print(type(ingles))
print(ingles.text_content())





