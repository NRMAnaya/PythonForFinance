# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 12:30:48 2023

@author: nmorales
"""

from requests.auth import HTTPBasicAuth
import requests
import json
import matplotlib
import pandas as pd
import numpy as np

print("Escribe el nombre y serie las emisoras de  las cuales quieres obtener el ISIN, separado por comas\n Ejemplo: WALMEX *, AMX B \n ")
lista=input()


url_cotizacion = 'https://cloud.biva.mx/instruments?page=0&size=2&instrument='+lista
headers = {"x-api-key": '5tbGgJp5Bq4yGPGaLcaUE8K7dUe83uxO94GYLjIq'}

response_cotizacion = requests.get(url=url_cotizacion, headers=headers)

data_instrumento=response_cotizacion.json()
data_instrumento=pd.DataFrame(data_instrumento['content']).set_index('isin')
data_instrumento2=data_instrumento.reset_index()
data_instrumento3=data_instrumento2[['isin','securityName']]
print(data_instrumento3)
