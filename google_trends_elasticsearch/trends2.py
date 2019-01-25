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
#eliminar la data 

'''
DELETE geoevolucion
'''
#eliminar el indice
#Mapear campos
'''
PUT geoevolucion
{
  "mappings": {
    "geoevolucion": {
      "properties": {
        "coordinates": {
          "type": "geo_point"
        },
        "valor": {
          "type": "float"
        }             
      }
    }
  }
}

'''
#Cargar Data
#Crear indice


ES_HOST = 'https://search-adm-35ohesxnchgmztcblylrwe3dvu.us-east-1.es.amazonaws.com'
es = Elasticsearch(ES_HOST,  verify_certs=False)



def asiga(v):
    g='0.6020736,0.4043317'
    if v == 'Autonomous City of Buenos Aires':
        g = '-34.6020736,-58.4043317'
    if v == 'Buenos Aires Province':
        g = '-34.6020736,-62.8845648,'
    if v == 'Catamarca Province':
        g = '-26.819722,-66.004682'
    if v == 'Chaco Province':
        g = '-26.819722,-66.004682'
    if v == 'Chubut Province':
        g = '-20.0300105,-67.5077583'
    if v == 'Cordoba':
        g = '-32.104840, -63.583037'
    if v == 'Corrientes Province':
        g = '-28.833780, -57.985483'
    if v == 'Entre Rios':
        g = '-31.995773, -59.143598'
    if v == 'Formosa Province':
        g = '-24.699044, -60.108693'
    if v == 'Jujuy':
        g = '-22.933315, -66.092285'
    if v == 'La Pampa Province':
        g = '-37.183086, -65.384548'
    if v == 'La Rioja Province':
        g = '-29.507927, -67.379079'
    if v == 'Mendoza Province':
        g = '-34.493486, -68.597455'
    if v == 'Misiones Province':
        g = '-26.711821, -54.183393'
    if v == 'Neuquen':
        g = '-38.449772, -69.827924'
    if v == 'Río Negro':
        g = '-40.284189, -67.542768'
    if v == 'Salta Province':
        g = '-25.031423, -64.818159'
    if v == 'San Juan Province':
        g = '-30.888616, -68.861127'
    if v == 'San Luis Province':
        g = '-33.747696, -65.872846'
    if v == 'Santa Cruz Province':
        g = '-48.631578, -69.835654'
    if v == 'Santa Fe Province':
        g = '-30.997124, -61.025170'
    if v == 'Santiago del Estero Province':
        g = '-27.569438, -63.464996'
    if v == 'Tierra del Fuego Province':
        g = '-54.438852, -67.395827'
    if v == 'Tucumán':
        g = '-27.057673, -65.262925'
    return g


for n in range(0,1000):
    kw_list = ["lancome"]
    pytrends = TrendReq()
    pytrends.build_payload(kw_list, cat=0, timeframe= 'now 1-H', geo='AR', gprop='')
    pytrends.interest_over_time()
    p=pytrends.interest_by_region()
    time.sleep(200)
    hora_ahora = datetime.datetime.now()     
    indice=0
    for index, row in p.iterrows():
        
        indice+=1
        time.sleep(1)    
    
        try:
                       
            
            
            print (index+'-'+str(row[0]))
            
            
            data='{"region": "'+index+'"}'
            #data='{"region": "A"}'
            
            datajson = json.loads(data)
            
            #coordinates ='-32.5929636,-58.4278927'
            
            #datajson['datetime'] = str(datetime.datetime.now())
            datajson['datetime_key'] = hora_ahora
            datajson['coordinates'] = asiga(index)
            datajson['valor'] = str(row[0])
            print(datajson)
            
            #print out a message to the screen that we have collected a tweet
            
            go = es.create(index="geoevolucion",
                      doc_type="geoevolucion",
                      id=str(hora_ahora)+str(indice),
                      body=datajson
                     )
            
            print (json.dumps(go)) 
          
            
   
        except:
            pass
        
    
    
    

