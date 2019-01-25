#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 12:32:49 2018

@author: laiunce
"""


import flask
from flask import request, jsonify
import os
import re
import bs4
import requests
import time




app = flask.Flask(__name__)
app.config["DEBUG"] = True


#directorio='/Users/laiunce/Desktop/bajada_paginas/'

directorio=''





def limpia_texto(text):
    text=text.lower()
    text = text.replace("ñ", "n")
    text = text.replace("á", "a")
    text = text.replace("é", "e")
    text = text.replace("í", "i")
    text = text.replace("ó", "o")
    text = text.replace("ú", "u") 
    text = text.replace(".", " ")
    text = text.replace(",", " ")
    text = text.replace(";", " ")        
    text = text.replace("[", " ")
    text = text.replace("]", " ")
    text = text.replace("(", " ")
    text = text.replace(")", " ")        
    text = text.replace("{", " ")
    text = text.replace("}", " ")
    text = text.replace("?", " ")        
    text = text.replace("¿", " ")        
    text = text.replace("!", " ")        
    text = text.replace("¡", " ")    
    text = text.replace(":", " ")  
    return(re.sub('[^a-zA-Z\s]', '', text))

# METODO PARA CONVERTIR URL EN TEXTO
#http://127.0.0.1:5000/api/v1/resources/get?webpage=https://www.lanacion.com.ar/
@app.route('/api/v1/resources/get', methods=['GET'])
def api_id():
    
    #reemplazar direccion html para guardar archivo
    nom_arch= re.sub('[^a-zA-Z0-9]', '', request.args['webpage'])
    
    #otiene solo texto de pagina web
    comando= 'links -dump '+request.args['webpage']+' > '+directorio+nom_arch+'.txt'
    os.system(comando)
    
    #lee el archivo
    comando3= 'cat '+directorio+nom_arch+'.txt' 
    read_arc=os.popen(comando3).read()
    
    #elimina el archivo
    comando2= 'rm '+directorio+nom_arch+'.txt'
    os.system(comando2)    
    
    return(jsonify(str(read_arc)))
    #return(str(read_arc))
    #return jsonify(str(os.system(comando)))




# METODO PARA DEVOLVER PAGINAS DEVUELTAS POR GOOGLE EN UN PERIODO Y POR PALABRA BUSQUEDA
#http://127.0.0.1:5000/api/v1/resources/get_google?busqueda=pampa+energia+argentina&fechaini=20170401&fechafin=20170401
@app.route('/api/v1/resources/get_google', methods=['GET'])
def get_google():
    
    #pagina = 'pampa+energia+argentina'
    #fechaini = '20170401'
    #fechafin = '20170401'

    busqueda = request.args['busqueda']
    fechaini = request.args['fechaini']
    fechafin = request.args['fechafin']    
    
    dia_min,mes_min,anio_min = int(fechaini[6:8]),int(fechaini[4:6]),int(fechaini[0:4])
    dia_max,mes_max,anio_max = int(fechafin[6:8]),int(fechafin[4:6]),int(fechafin[0:4])
    
    
    busqueda_dia_mes_anio = 'tbs=cdr:1,cd_min:'+str(mes_min)+'/'+str(dia_min)+'/'+str(anio_min)+',cd_max:'+str(mes_max)+'/'+str(dia_max)+'/'+str(anio_max)
    itera=["0","10"]
    #itera=["0"]
    urls=[]
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
        
        
    try:
        for cant_pag in itera:
            try:
                time.sleep(5)
                r = requests.get('https://www.google.com.ar/search?q='+busqueda+'&'+busqueda_dia_mes_anio+'&start='+cant_pag, headers=headers)
                print(r)
                #este andaba pero en ubuntu no se que le apsa que dejo de andar por lo que cambie a lxml
                #soup = bs4.BeautifulSoup(r.content, 'html5lib')
                soup = bs4.BeautifulSoup(r.content, 'lxml')
                links = soup.find_all('a', href=True)
                for i in links:
                    try:
                        if str(i)[0:13] == '<a href="http' and str(i)[17:35] != 'support.google.com':
                            urls.append(i.get('href'))
                    except:
                        print('error en devolver links')
            except:
                print('error '+str(cant_pag))
    except:
        print('error cantidad de paginas en itera')   
    
    return jsonify(urls)
    



# METODO PARA DEVOLVER PAGINAS DEVUELTAS POR GOOGLE EN UN PERIODO Y POR PALABRA BUSQUEDA
#http://0.0.0.0:5000/api/v1/resources/get_google_noticias?busqueda=pampa+energia+argentina&fechaini=20170401&fechafin=20170401
@app.route('/api/v1/resources/get_google_noticias', methods=['GET'])
def get_google_noticias():

    busqueda = request.args['busqueda']
    fechaini = request.args['fechaini']
    fechafin = request.args['fechafin']    
    
    dia_min,mes_min,anio_min = int(fechaini[6:8]),int(fechaini[4:6]),int(fechaini[0:4])
    dia_max,mes_max,anio_max = int(fechafin[6:8]),int(fechafin[4:6]),int(fechafin[0:4])
    
    #obtiene paginas de busqueda por google noticias
    busqueda_dia_mes_anio = 'tbm=nws&tbs=cdr:1,cd_min:'+str(mes_min)+'/'+str(dia_min)+'/'+str(anio_min)+',cd_max:'+str(mes_max)+'/'+str(dia_max)+'/'+str(anio_max)
    itera=["0","10","20","30","40","50","60"]
    #itera=["0"]
    
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
    
    urls=[]  
    itera=["0","10","20","30","40"]
    try:
        for cant_pag in itera:
            try:
                time.sleep(5)
                #r = requests.get('https://www.google.com.ar/search?q='+busqueda+'&'+busqueda_dia_mes_anio+'&num='+cant_pag, headers=headers)
                r = requests.get('https://www.google.com.ar/search?q='+busqueda+'&'+busqueda_dia_mes_anio+'&num=10'+'&start='+cant_pag, headers=headers)
                #este andaba pero en ubuntu no se que le apsa que dejo de andar por lo que cambie a lxml
                #soup = bs4.BeautifulSoup(r.content, 'lxml')
                soup = bs4.BeautifulSoup(r.content, 'lxml')
                links = soup.find_all('a', href=True)
                for i in links:
                    try:
                        if str(i)[0:24] == '<a class="l lLrAF" href=':
                            #la siguiente linea de codigo es para que encuentre la pagina web buscada en los links yno traiga cualqueir verdura
                            #pero se comenta ya qe ahora no estoy byscando diarios, sino cualquier palabra clave
                            #if i.get('href').find(busqueda) != -1:
                            urls.append(i.get('href'))
                    except:
                        print('error en devolver links')
            except:
                print('error '+str(cant_pag))
    except:
        print('error cantidad de paginas en itera')   

    return jsonify(urls)
    
    
    
# METODO PARA CONVERTIR URL EN TEXTO
#http://0.0.0.0:5000/api/v1/resources/return_pepe?valor=peli cara de sapo
@app.route('/api/v1/resources/return_pepe', methods=['GET'])
def return_pepe():
    return(request.args['valor'])

app.run(host='0.0.0.0', debug = False)

