
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 21:28:15 2018

@author: laiunce
"""

from pytrends.request import TrendReq
import datetime
import json
import time
from elasticsearch import Elasticsearch
from pytrends.request import TrendReq
from datetime import datetime, timedelta


fecha_hora ='20180509 22:52:50'
delta= 50
kw_list = ["fructis"]


pytrends = TrendReq()
#se le agregan 3 horas por diferencia argentina con server VER MX O ARG
datetimeobject = datetime.strptime(fecha_hora,'%Y%m%d %H:%M:%S') + timedelta(hours=5)
deltatiempo =  timedelta(hours=delta)
fecha_hora_delta_sum = datetimeobject +deltatiempo 
fecha_hora_delta_res = datetimeobject -deltatiempo 
time_range = str(fecha_hora_delta_res.isoformat())[:13]+' '+str(fecha_hora_delta_sum.isoformat())[:13]
pytrends.build_payload(kw_list, cat=0, timeframe= time_range, geo='MX', gprop='')
p=pytrends.interest_by_region()
p['indice'] =p.index
print(p)


# Aguascalientes             0       Aguascalientes
# Baja California           44      Baja California
# Baja California Sur        0  Baja California Sur
# Campeche                   0             Campeche
# Chiapas                    0              Chiapas
# Chihuahua                 84            Chihuahua
# Coahuila                  54             Coahuila
# Colima                     0               Colima
# Durango                    0              Durango
# Guanajuato                43           Guanajuato
# Guerrero                   0             Guerrero
# Hidalgo                    0              Hidalgo
# Jalisco                   45              Jalisco
# Mexico City               70          Mexico City
# Michoacán                 32            Michoacán
# Morelos                    0              Morelos
# Nayarit                    0              Nayarit
# Nuevo Leon                66           Nuevo Leon
# Oaxaca                     0               Oaxaca
# Puebla                    59               Puebla
# Querétaro                  0            Querétaro
# Quintana Roo               0         Quintana Roo
# San Luis Potosi            0      San Luis Potosi
# Sinaloa                    0              Sinaloa
# Sonora                     0               Sonora
# State of Mexico           75      State of Mexico
# Tabasco                    0              Tabasco
# Tamaulipas               100           Tamaulipas
# Tlaxcala                   0             Tlaxcala
# Veracruz                  58             Veracruz
# Yucatan                    0              Yucatan
# Zacatecas                  0            Zacatecas


