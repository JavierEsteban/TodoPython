
import requests
from lxml import html

url = "https://www.wikipedia.org/"
url2 = "https://www.pescaenperu.com/categoria-producto/equipos-de-pesca/canas/"

encabezados = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36"
}

respuesta = requests.get(url, encabezados)
respuesta2 = requests.get(url2, encabezados)

print(respuesta.status_code)
#print(respuesta.headers)
parser = html.fromstring(respuesta.text)


print(parser)
#print(respuesta.text)

"""
import requests
res = requests.get('https://scotch.io/c#')
print(res)

if res:
    print('Response OK')
else:
    print('Response Failed')

"""

API_KEY = 'your yandex api key'
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
res = requests.get(url)
params = dict(key=API_KEY, text='Hello', lang='en-es')

res = requests.get(url, params=params)
print(res.text)





""""
Ejemplos de WebScraping Wikipedia
-- Extrae la Información del Idioma a través de metodos de lxml.html

"""

import requests
from lxml import html

url = "https://www.wikipedia.org/"
encabezados = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36"
}
respuesta = requests.get(url=url, params=encabezados)
#print(respuesta.status_code)
parser = html.fromstring(respuesta.content)
#print(parser)

idioma = parser.get_element_by_id("js-link-box-es")
print(idioma[0].text_content())

#parser = html.fromstring(respuesta.content)
#print(parser)




"""
Ejemplos de Web Scraping

-- Extrae la información del Idioma, con metodos de xpath

"""

import requests
from lxml import html



url = "https://www.wikipedia.org/"
encabezados = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36"
}
respuesta = requests.get(url=url, params=encabezados)
#print(respuesta)
parser = html.fromstring(respuesta.text)
#print(parser.text_content())
idioma = parser.xpath("//a[@id='js-link-box-en']/strong/text()")
print("El idioma Buscado es : {}".format(idioma[0]))

##### Extrae todos los idiomas...
idiomas = parser.xpath("//a[contains(@id,'js-link-box')]/strong/text()")
for indice, idioma in enumerate(idiomas):
    print("{} -> {}".format(indice + 1,idioma))


