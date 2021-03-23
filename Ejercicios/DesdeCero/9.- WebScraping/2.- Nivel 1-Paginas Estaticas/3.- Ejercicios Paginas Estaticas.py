"""
Ejercicio 1:

Se realizará una WebScraping de la página web de stackoverflow, la cual debe de ser guardada en un archivo de texto
con el siguiente formato:

 Questions
 RESPONSE

El nombre del archivo debe de ser Preguntas_20201110_1920.txt

"""
from datetime import datetime
import requests
from lxml import html
import os


def Response_Html(url , encabezados):
    respuesta = requests.get(url=url, params=encabezados)
    parser = html.fromstring(respuesta.content)
    return parser


def main():
    url = "https://es.stackoverflow.com/questions/"
    cabeceras = {
         "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36"
    }
    parseador = Response_Html(url=url, encabezados=cabeceras)
    questions = parseador.xpath("//div[@id='content']//div[@id='mainbar']//div[contains(@id, 'question-summary')]//div[@class='summary']//h3/a/text()")
    responses = parseador.xpath("//div[@id='content']//div[@id='mainbar']//div[contains(@id, 'question-summary')]//div[@class='summary']//div[contains(@class, 'excerpt')]/text()")
    #diccionario = dict(zip(questions, responses))
    os.chdir(r"D:\Cursos\Python\Ejercicios\DesdeCero\9.- WebScraping\2.- Nivel 1-Paginas Estaticas")
    nombre_archivo = "3.- Preguntas_"+datetime.now().strftime("%Y%m%d_%H%M") + ".Txt"
    archivo = open(nombre_archivo, 'w+',encoding="utf-8")

    for index, question in enumerate(questions):
        archivo.write(question+"\n")
        for index2, response in enumerate(responses):
            if index == index2:
                archivo.write("\t"+response.replace("\n","").replace("\r","").replace("\t","").strip()+"\n\n")
                break
    archivo.close()


if __name__== '__main__':
    main()


