# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:38:10 2023

@author: nmorales
"""


######################
#Simple return is preferable to use when we calculate reurns of multiple securities
##########################

from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib as plot

yf.pdr_override()
y_symbol=['PG']
from datetime import datetime
startdate=datetime(1995,1,1)
#enddate=datetime(2022,12,15)
PG= pdr.get_data_yahoo(y_symbol,start=startdate)
#####################################################
 ##these are the simple daily returns
 ###############################################
PG['Simple_Return'] =(PG['Adj Close']/PG['Adj Close'].shift(1))-1 #(P1/p0)-1
####se usa el precio de cierre de hoy entre el de ayer y se le resta uno ese sería el retorno simple
#print(PG['Simple_Return'])
#print(PG['Adj Close'])
PG['Simple_Return'].plot(figsize=(8,5))


#####################################################
 ##this is the mean return is a super small number lower than 1% because is daily
 ###############################################
avg_returns_d=PG['Simple_Return'].mean()

#####################################################
 ##this is the mean return annually (250) days
 ###############################################
avg_returns_a=PG['Simple_Return'].mean()*250
avg_returns_a_str=str(round(avg_returns_a,5)*100)+' %'
print(avg_returns_a_str) ##aqui sale un 12% lo cual indica que se tiene un retorno anual promedio de 12%






