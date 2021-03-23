
"""
Scrapy: Es un FrameWork para realizar WebScraping.
"""

#Forma general

from scrapy.item import Field, Item
from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy.loader import ItemLoader

"""
#Ejemplo 

class Dato(Item):
    texto = Field()

class SpiderDeDatos(Spider):
    name = "MiPrimerSpider"
    start_urls = ['https://paginaparaextraerdatos.com/']

    #Reglas de Direccionamiento
    def parse(self, response):
        sel = Selector(response)
        titulo_de_pagina = sel.xpath('//h1/text()').get()

        lista = sel.xpath('//div[@id = "datos"]')
        for elemento in lista:
            item = ItemLoader(Dato(), elemento)
            item.add_xpath('texto','.//h3/a/text()')
            yield item.load_item()
"""

#Extrae información de StackOverFlow

class Pregunta(Item):
    id = Field()
    pregunta = Field()
    descripcion = Field()

class StackOverFlowSpider(Spider):
    name="MiPrimerSpider"
    #valores por defecto del encabezado
    custom_settings = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36"
    }
    start_urls = ['https://stackoverflow.com/questions/']

    def parse(self, response):
        sel = Selector(response)
        preguntas = sel.xpath('//div[@id="Questions"//div[@class = "questions-summary"]]')
        for pregunta in preguntas:
            item = ItemLoader(Pregunta(), pregunta)
            item.add_xpath('pregunta','.//h3/a/text()')
            item.add_xpath('descripcion','.//div[@class="excerpt"]/text()')
            item.add_value('id', 1)

            yield item.load_item()





