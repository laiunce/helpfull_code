#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 26 11:46:36 2018

@author: laiunce
"""

#interes por todo un dia 

kw_list = ["elvive"]
pytrends = TrendReq()
pytrends.build_payload(kw_list, cat=0, timeframe= '2018-03-03T03 2018-03-04T03', geo='AR', gprop='')
trend=pytrends.interest_over_time()
trend['hora'] = trend.index - timedelta(hours=3)




#interes por region



data_agg = pd.DataFrame() 

lista_prov=['AR','AR-B','AR-K','AR-H','AR-U','AR-C','AR-X','AR-W','AR-E','AR-P','AR-Y','AR-L','AR-F','AR-M','AR-N','AR-Q','AR-R','AR-A','AR-J','AR-D','AR-Z','AR-S','AR-G','AR-V','AR-T']
#lista_prov=['AR','AR-B']
for i in lista_prov:
    print(i)
    try:


        kw_list = ["elvive reparacion"]
        pytrends = TrendReq()
        pytrends.build_payload(kw_list, cat=0, timeframe= '2018-03-03T03 2018-03-04T03', geo=i, gprop='',)
        #p=pytrends.interest_by_region()
        #pytrends.related_topics()
        dataf=pytrends.interest_over_time()
        dataf['provincia']=i
        dataf['fecha_hora'] =dataf.index - timedelta(hours=3)
        
        data_aggre = dataf[['fecha_hora','provincia',kw_list[0]]]
        
        data_agg = data_agg.append(data_aggre)


    except:
        pass
