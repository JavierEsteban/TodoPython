"""
WebScraping:
    * lxml
    * beautifulsoup4
    * requests
"""


"""
caso de Estudio: StackOverflow

Utilizaremos las librerías :
    * requests
    * beautifulsoup4
"""

#Importar librerías necesarias

import requests
from lxml import html
from datetime import datetime
import os
#import beautifulsoup

url = "https://es.stackoverflow.com/questions"
encabezados = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36"
}

response = requests.get(url=url, params=encabezados)
print(response.status_code)
parser = html.fromstring(response.text)
#print(parser.text_content())

Questions = parser.xpath("//div[@id='content']//div[@id='mainbar']//div[@class='question-summary']//div[@class='summary']//h3//a/text()")

for i in Questions:
    print(i)


#####################################################
#################### Ejemplo con BS4 ################
#####################################################

#from bs4 import beautifulsoup4

