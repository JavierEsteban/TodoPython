"""
Caso de Estudio:

1.- TodopescaShop: https://www.todopescashop.com/
"""
#Paso 1: Importar las librerías
import requests
import os
from lxml import html
from datetime import datetime


#Paso 2: Declarar los valores
url = "https://www.todopescashop.com/categoria-producto/senuelos-de-pesca/"
cabeceras = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/80.0.3987.149 Safari/537.36"
}

#Paso 3: generar los archivos HTML y Parseo(Arbol de HTML)
respuesta = requests.get(url=url, params=cabeceras)
print(respuesta.status_code)
parseo = html.fromstring(respuesta.content)

nom_product = parseo.xpath("//div[@class = 'shop-container']//div[contains(@class,'product-small col has-hover product type-product post')]//div[@class='title-wrapper']//p[@class = 'name product-title']/a/text()")
price_product = parseo.xpath("//div[@class = 'shop-container']//div[contains(@class,'product-small col has-hover product type-product post')]//div[@class='price-wrapper']//span[@class = 'woocommerce-Price-amount amount']/bdi/text()")


"""
for nombre in nom_product:
    print(nombre)

for price in price_product:
    print(price)
"""
diccionario_Productos = dict(zip(nom_product, price_product))
print(diccionario_Productos)


print(os.getcwd())

os.chdir("D:\Cursos\Python\Ejercicios\DesdeCero\9.- WebScraping\9999_Ejercicios")
print(os.getcwd())

nombre_archivo = 'Productos_todopescashop_'+ str(datetime.now().strftime("%y%m%d"))+".Txt"
print(nombre_archivo)

archivo_producto = open(nombre_archivo, 'w+')
archivo_producto.write("NombreProducto|Precio\n")

for indice, valor in diccionario_Productos.items():
    #print("{}|{}".format(indice, valor))
    archivo_producto.write("{}|{}\n".format(indice, valor))

archivo_producto.close()

