
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
delta= 3
kw_list = ["fructis"]


pytrends = TrendReq()
#se le agregan 3 horas por diferencia argentina con server VER MX O ARG
datetimeobject = datetime.strptime(fecha_hora,'%Y%m%d %H:%M:%S') + timedelta(hours=5)
deltatiempo =  timedelta(hours=delta)
fecha_hora_delta_sum = datetimeobject +deltatiempo 
fecha_hora_delta_res = datetimeobject -deltatiempo 
time_range = str(fecha_hora_delta_res.isoformat())[:13]+' '+str(fecha_hora_delta_sum.isoformat())[:13]
pytrends.build_payload(kw_list, cat=0, timeframe= time_range, geo='MX', gprop='')
p=pytrends.interest_over_time()
p['indice'] =p.index
print(p)
