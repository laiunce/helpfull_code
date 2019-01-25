# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import webbrowser
import zipfile
import pandas as pd
import os

url = 'http://www.bcra.gov.ar/cheques/actualiza.asp'
page_ext = requests.get(url)
soup_ext = BeautifulSoup(page_ext.content)
p = (soup_ext.findAll("tr"))

tmp = re.findall(r"onmousedown", str(p))

texto=[]
for i in p:
    texto.append(str(p)) 
    

tmp = re.findall(r"zips\/cheques\/\d\d\d\d\d\d\d\d.zip", str(soup_ext))

#webbrowser.open('www.bcra.gov.ar/zips/cheques/20170613.zip',autoraise=True)


path= 'C:\\Users\\LAC40641\\Downloads\\'


#establecer a google chrome como predeterminado
for i in tmp:

    #nom = 'zips/cheques/20170710.zip'
    nom = i
    
    
    with zipfile.ZipFile(path+nom[13:],"r") as zip_ref:
        zip_ref.extractall(path+nom[13:21])
    
    
    ruta_files = path+nom[13:21]+'\\cheques\\'
    
    archivo_al='al'+nom[15:21]+'.txt'
    archivo_ba='ba'+nom[15:21]+'.txt'
    archivo_pa='pa'+nom[15:21]+'.txt'
    
    #carga data frames
    
    ruta_files+archivo_al
    
    
    ##############################
    
    # lee data ba
        #reemplaza comas de archivo
    with open(ruta_files+archivo_ba, 'r+') as f:
        text = f.read()
        f.seek(0)
        f.truncate()
        f.write(text.replace(',', ''))
        
    data_ba_dataframe = pd.read_csv(ruta_files+archivo_ba, header = None)
    data_ba_dataframe.columns = ['na']
    data_ba_dataframe['mes'] = str(nom[13:21])
    
    guarda_transf = path+str('ba_etl') 
    if not os.path.exists(guarda_transf):
        os.makedirs(guarda_transf)
    
    
    data_ba_dataframe.to_csv(guarda_transf+'\\ba'+nom[13:21]+'.csv',index=False)
    
    ##############################
    
    #lee data al
    
            #reemplaza comas de archivo
    with open(ruta_files+archivo_al, 'r+') as f:
        text = f.read()
        f.seek(0)
        f.truncate()
        f.write(text.replace(',', ''))
        
    data_al = pd.read_csv(ruta_files+archivo_al,header = None)
    
    def arma_columa1(data):
        columna=[]
        for row in data[0]:
            tmp = re.findall(r"^\d{11}", str(row))
            pal=''
            for i in tmp:
                pal=pal+str(i)
            columna.append(pal)
        return pd.DataFrame(columna)
    
    
    def arma_columa2(data):
        columna=[]
        for row in data[0]:
            tmp = re.findall(r"^\d{11}\s*(\d*\s*)", str(row))
            pal=''
            for i in tmp:
                pal=pal+str(i)
            columna.append(pal)
        return pd.DataFrame(columna)
    
    def arma_columa3(data):
        columna=[]
        for row in data[0]:
            tmp = re.findall(r"^\d{11}\s*\d*\s*(\d*\s*)SF", str(row))
            pal=''
            for i in tmp:
                pal=pal+str(i)
            columna.append(pal)
        return pd.DataFrame(columna)
    
    def arma_columa4(data):
        columna=[]
        for row in data[0]:
            tmp = re.findall(r"SF(\d{11})", str(row))
            pal=''
            for i in tmp:
                pal=pal+str(i)
            columna.append(pal)
        return pd.DataFrame(columna)
    
    def arma_columa5(data):
        columna=[]
        for row in data[0]:
            tmp = re.findall(r"(\d{2}\/\d{2}\/\d{4}|IMPAGA)", str(row))
            pal=''
            for i in tmp:
                pal=pal+str(i)
            columna.append(pal)
        return pd.DataFrame(columna)
        
    
    
    columna_1 = arma_columa1(data_al)
    columna_2 = arma_columa2(data_al)
    columna_3 = arma_columa3(data_al)
    columna_4 = arma_columa4(data_al)
    columna_5 = arma_columa5(data_al)
    
    
    
    data_al_dataframe = pd.concat([columna_1,columna_2,columna_3,columna_4,columna_5], axis=1)
    data_al_dataframe.columns = ['cuil','nro_cheque','monto','SF','estado']
    data_al_dataframe['mes'] = str(nom[13:21])
    
    
    guarda_transf = path+str('al_etl') 
    if not os.path.exists(guarda_transf):
        os.makedirs(guarda_transf)
    
    
    data_al_dataframe.to_csv(guarda_transf+'\\al'+nom[13:21]+'.csv',index=False)
    
    ##############################
    
    # lee data ba pa
    

    #reemplaza comas de archivo
    with open(ruta_files+archivo_pa, 'r+') as f:
        text = f.read()
        f.seek(0)
        f.truncate()
        f.write(text.replace(',', ''))

    data_pa = pd.read_csv(ruta_files+archivo_pa, header = None,encoding='latin-1')
    
    def arma_columa_1(data):
        columna=[]
        for row in data[0]:
            tmp = re.findall(r"\d{11}", str(row))
            pal=''
            for i in tmp:
                pal=pal+str(i)
            columna.append(pal)
        return pd.DataFrame(columna)
    
    def arma_columa_2(data):
        columna=[]
        for row in data[0]:
            tmp = re.findall(r"[^0-9]+", str(row))
            pal=''
            for i in tmp:
                pal=pal+str(i.replace('  ',''))
            columna.append(pal)
        return pd.DataFrame(columna)
    
    
    columna_1 = arma_columa_1(data_pa)
    columna_2 = arma_columa_2(data_pa)
        
    
    
    data_pa_dataframe = pd.concat([columna_1,columna_2], axis=1)
    data_pa_dataframe.columns = ['cuil','nombre']
    data_pa_dataframe['mes'] = str(nom[13:21])
    
    
    guarda_transf = path+str('pa_etl') 
    if not os.path.exists(guarda_transf):
        os.makedirs(guarda_transf)
    
    
    data_pa_dataframe.to_csv(guarda_transf+'\\pa'+nom[13:21]+'.csv',index=False)
    

