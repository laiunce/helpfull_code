#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:11:56 2018

@author: laiunce
"""



#urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



#https://qbox.io/blog/python-scripts-interact-elasticsearch-examples

import requests
from elasticsearch import Elasticsearch
import json
import gmap
import pygeohash as gh
from elasticsearch_dsl import GeoPoint



ES_HOST = 'https://search-adm-35ohesxnchgmztcblylrwe3dvu.us-east-1.es.amazonaws.com'
es = Elasticsearch(ES_HOST,  verify_certs=False)



doc = {"query": {
    "bool": {
      "must": [
        {"exists" : { "field" : "geo.coordinates" }},
        {"match": { "place.country_code": "AR" }}
      ]
    }
  },
    "_source": ["geo.coordinates"]
            }
        
        
res = es.search(index="twitter_geopoint",doc_type="twitter_geopoint", body=doc,scroll='2m')

#scrollId = res['_scroll_id']
#es.scroll(scroll_id = scrollId, scroll = '300m')



sid = res['_scroll_id']
scroll_size = res['hits']['total']
final_scroll_data = []


while (scroll_size > 0):
    each_scroll = es.scroll(scroll_id = sid, scroll = '2m')
    sid = each_scroll['_scroll_id']
    scroll_size = len(each_scroll['hits']['hits'])
    final_scroll_data.append(each_scroll['hits']['hits'])
    # Getting final data in the list 
    
    

lat=[]
long=[]
for i in final_scroll_data:
    for a in i:
        print(a["_source"]["geo"]["coordinates"])
        lat.append(a["_source"]["geo"]["coordinates"][0])
        long.append(a["_source"]["geo"]["coordinates"][1])    
        
    
    
    
#####

#geohash


geohashs=[]

for l in range(0,len(lat)):
    ghash=gh.encode(lat[l],long[l], precision = 12)
    print(ghash)
    location = GeoPoint()
    location = [43, -70]
    geohashs.append(location)

number=0
for row in geohashs:
    number += 1

    go = es.index(
        index="grafica_geopoint",
        doc_type="grafica_geopoint",
        id=str(number),
        body={
            "geohash": row
        }
    )

    print (json.dumps(go))







import matplotlib.pyplot as plt
plt.plot(long,lat, 'o', markersize=1,color='black')

gmap.scatter(lat, long, '#3B0B79', size=1000, marker=True)
gmap.draw("/Users/laiunce/Desktop/map3.html")