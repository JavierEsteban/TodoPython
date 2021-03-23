'''
===================================================================
====               Tutorial Pandas                             ====
===================================================================
'''

'''Lamado de la librería pandas
1.- instalar el package pandas en el entorno virtual de python
2.- llamar la librería pandas.
'''

"Convertir diccionario en dataframe"
import pandas as pd
import  numpy as np
Base_datos = {'nombre':['javier', 'roy', 'mirian'], 'edad':[26, 28, 14], 'sexo': ['M', 'M', 'F']}
DataFrame = pd.DataFrame(Base_datos)
print(DataFrame)
print(DataFrame.head())

"Importar una Bd de .CSV"
Base_Mundial = pd.read_csv("D:\\Cursos\\Python\\Ejercicios\\DataSet\\futbolmundial.csv", sep=';')
Base_Mundial_final = Base_Mundial[0:3]
print(Base_Mundial.head())
print(Base_Mundial.info())
print(Base_Mundial.describe())
print(Base_Mundial[['Selección', 'Valor de mercado (mill. de €)','Edad promedio', 'Experiencia']])

print(Base_Mundial.iloc[:,:4].head())

dfBase = Base_Mundial.iloc[:, :4]
dfBase.rename(columns={
    'Selección': "Pais", 'Valor de mercado (mill. de €)': 'Valor_ME', 'Edad promedio': 'Edad_Promedio',
    'Experiencia': "Experiencia"
}, inplace=True)
dfBase

BD_FINAL = dfBase[dfBase.Pais.notnull()]

print(BD_FINAL.describe())

