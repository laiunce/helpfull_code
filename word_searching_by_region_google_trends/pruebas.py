#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 12:10:19 2018

@author: laiunce
"""


#
# Comeinza logica calculo de tendencia SUMAR 3 HORAS POR DIFERENCIA HORARIO CON SERVER GOOGLE
#


import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from pytrends.request import TrendReq
import numpy as np
from datetime import datetime, timedelta
import statistics


def alista(dataframe):
    lista=[]
    for i in dataframe.values.tolist():
        lista.append(i[0])
    return lista



def obtiene_tendencia(fecha,hora,marca,submarca):
    
    
    t=fecha
    fecha_hora = (t[6:10]+t[3:5]+t[0:2]+' '+hora)
    kw_list = marca+' '+submarca
    kw_list = [kw_list.replace(' ','+')]
    print(kw_list)    

    delta= 2
    pytrends = TrendReq()
    #se le agregan 3 horas por diferencia argentina con server
    datetimeobject = datetime.strptime(fecha_hora,'%Y%m%d %H:%M:%S') + timedelta(hours=3)
    
    deltatiempo =  timedelta(hours=delta)
    fecha_hora_delta_sum = datetimeobject +deltatiempo 
    fecha_hora_delta_res = datetimeobject -deltatiempo 
    
    time_range = str(fecha_hora_delta_res.isoformat())[:13]+' '+str(fecha_hora_delta_sum.isoformat())[:13]
    
    pytrends.build_payload(kw_list, cat=0, timeframe= time_range, geo='AR', gprop='')
    
    p=pytrends.interest_over_time()
    
    p['indice'] =p.index
    
    #plt.plot(p[kw_list])
    #pytrends.related_topics()
    # detectar picos
    
    
    #si media hora antes y media hora despues, la pendiente de la recta que ajusta a la regresion es positiva o mayor a x
    m20min_antes = datetimeobject - timedelta(minutes=15)
    m20min_desp = datetimeobject + timedelta(minutes=15)
    
    subdata = p[(p['indice'] > m20min_antes) & (p['indice'] < m20min_desp)]
    #plt.plot(subdata[kw_list])
    
    subdata_menor20min = subdata[ (subdata['indice'] < datetimeobject)]
    subdata_mayor20min = subdata[(subdata['indice'] >= datetimeobject)]    
    
    
    
    lista_tendencia=[]
    for i in subdata[kw_list].values.tolist():
        lista_tendencia.append(i[0])
    
    
    X = [i for i in range(0, len(lista_tendencia))]
    X = np.reshape(X, (len(X), 1))
    y = lista_tendencia
    model = LinearRegression()
    model.fit(X, y)
    # calculate trend
    trend = model.predict(X)
    
    ordenada = trend[0]
    
    pendiente = (trend[1]-ordenada)
    
    plt.plot(p[kw_list])
    plt.plot(subdata_menor20min[kw_list])
    plt.plot(subdata_mayor20min[kw_list])    
    #pendiente    
    return pendiente,subdata_menor20min[kw_list],subdata_mayor20min[kw_list]








##### prueba 1 #####



fecha='15/05/2018'
hora = '12:25:26'
marca = 'blue'
submarca = ''
pendiente,subdata_menor20min,subdata_mayor20min = obtiene_tendencia(fecha,hora,marca,submarca)

mediana_menor=statistics.median(alista(subdata_menor20min))
mediana_mayor=statistics.median(alista(subdata_mayor20min))
metrica = mediana_mayor/mediana_menor-1

print(metrica)


plt.plot(p[kw_list])
plt.plot(subdata_menor20min)
plt.plot(subdata_mayor20min) 








data=pd.read_csv('/Users/laiunce/Desktop/itera_marcas/marca_camp_acotado.csv')

lista=[]

for index, row in data.iterrows():
    
    fecha=row["Fecha"]
    hora = row["hora"]
    marca = row['Marca']
    submarca = row['SubMarca']
    try:
        pen,data = obtiene_tendencia(fecha,hora,marca,submarca)
        print(pen)    
        lista.append(pen)
    except:
        pass
