# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 11:21:13 2023

@author: nmorales
"""

from requests.auth import HTTPBasicAuth
import requests
import json
import matplotlib
import pandas as pd
import numpy as np


url_cotizacion = 'https://cloud.biva.mx/stock-exchange/BIVA/quote?isin=MX01AM050019&period=Y&quantity=5'
headers = {"x-api-key": '5tbGgJp5Bq4yGPGaLcaUE8K7dUe83uxO94GYLjIq'}

response_cotizacion = requests.get(url=url_cotizacion, headers=headers)

data_cotizacion=response_cotizacion.json()
data_cotizacion=pd.DataFrame(data_cotizacion['timeSeries']).set_index('dateInMillis')


###########################
###############################         SIMPLE RETURN
###########################

data_cotizacion['Simple_Return'] =(data_cotizacion['close']/data_cotizacion['close'].shift(1))-1 #(P1/p0)-1
print (data_cotizacion['Simple_Return'])
data_cotizacion.count(axis=1)
data_cotizacion['Simple_Return'].plot(figsize=(8,5))

avg_returns_d=data_cotizacion['Simple_Return'].mean()
print(avg_returns_d)

#####################################################
 ##this is the mean return annually (250) days
 ###############################################
avg_returns_a=data_cotizacion['Simple_Return'].mean()*250
avg_returns_a_str=str(round(avg_returns_a,5)*100)+' %'
print(avg_returns_a_str) ##aqui sale un 12% lo cual indica que se tiene un retorno anual promedio de 12%








###########################
###############################                          Logarithmic RETURN
###########################
data_cotizacion['Logarithmic_Return'] =np.log(data_cotizacion['close']/data_cotizacion['close'].shift(1)) #(P1/p0)-1

print(data_cotizacion['Logarithmic_Return'])
####se usa el precio de cierre de hoy entre el de ayer y se le resta uno ese sería el retorno simple
#print(PG['Simple_Return'])
#print(PG['Adj Close'])
data_cotizacion['Logarithmic_Return'].plot(figsize=(8,5))


#####################################################
 ##this is the mean return is a super small number lower than 1% because is daily
 ###############################################
log_returns_d=data_cotizacion['Logarithmic_Return'].mean()

#####################################################
 ##this is the mean return annually (250) days
 ###############################################
log_returns_a=data_cotizacion['Logarithmic_Return'].mean()*250
log_returns_a_str=str(round(log_returns_a,5)*100)+' %'
print(log_returns_a_str) ##aqui sale un 10% lo cual indica que se tiene un retorno anual promedio de 10%






