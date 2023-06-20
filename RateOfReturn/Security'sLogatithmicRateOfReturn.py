# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 10:02:34 2023

@author: nmorales
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 11:38:10 2023

@author: nmorales
"""

######################
#Logarithic return is preferable for a single security
##########################

###########################################
########for vectorization we will use the the array programming
###########################################
from pandas_datareader import data as pdr
import numpy as np
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
PG['Logarithmic_Return'] =np.log(PG['Adj Close']/PG['Adj Close'].shift(1)) #(P1/p0)-1

print(PG['Logarithmic_Return'])
####se usa el precio de cierre de hoy entre el de ayer y se le resta uno ese sería el retorno simple
#print(PG['Simple_Return'])
#print(PG['Adj Close'])
PG['Logarithmic_Return'].plot(figsize=(8,5))


#####################################################
 ##this is the mean return is a super small number lower than 1% because is daily
 ###############################################
log_returns_d=PG['Logarithmic_Return'].mean()

#####################################################
 ##this is the mean return annually (250) days
 ###############################################
log_returns_a=PG['Logarithmic_Return'].mean()*250
log_returns_a_str=str(round(log_returns_a,5)*100)+' %'
print(log_returns_a_str) ##aqui sale un 10% lo cual indica que se tiene un retorno anual promedio de 10%






