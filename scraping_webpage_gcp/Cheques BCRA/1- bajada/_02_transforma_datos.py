# -*- coding: utf-8 -*-

import re
import pandas as pd
import zipfile
import os


def cuil_cuit_cdi(data):
    columna=[]
    for row in data[0]:
        columna.append(str(row[0:11]))
    return pd.DataFrame(columna)

def nro_cheque(data):
    columna=[]
    for row in data[0]:
        columna.append(str(row[12:21]))
    return pd.DataFrame(columna)

def fecha_rechazo(data):
    columna=[]
    for row in data[0]:
        columna.append(str(row[21:29]))
    return pd.DataFrame(columna)

def monto(data):
    columna=[]
    for row in data[0]:
        columna.append(str(row[29:44][:len(row[29:44])-2]+'.'+row[29:44][-2:]))
    return pd.DataFrame(columna)

def causal(data):
    columna=[]
    for row in data[0]:
        causal=''
        if str(row[44:45]) == '1':
            causal='Por vicios formales'
        if str(row[44:45]) == '2':
            causal='Sin fondos'
        columna.append(causal)
    return pd.DataFrame(columna)

def fecha_levantamiento(data):
    columna=[]
    for row in data[0]:
        columna.append(str(row[45:53]))
    return pd.DataFrame(columna)

def revision(data):
    columna=[]
    for row in data[0]:
        causal=''
        if str(row[53:54]) == 'E':
            causal='En revision'
        if str(row[53:54]) == 'S':
            causal='Fin de revision'
        columna.append(causal)
    return pd.DataFrame(columna)

def proceso_judicial(data):
    columna=[]
    for row in data[0]:
        causal=''
        if str(row[54:55]) == 'J':
            causal='En proceso judicial '
        if str(row[54:55]) == 'F':
            causal='Fin de proceso judicial '
        columna.append(causal)
    return pd.DataFrame(columna)

def cuit_relacionado(data):
    columna=[]
    for row in data[0]:
        columna.append(str(row[55:66]))
    return pd.DataFrame(columna)

def pago_multa(data):
    columna=[]
    for row in data[0]:
        columna.append(str(row[66:81]))
    return pd.DataFrame(columna)

        
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
    
def formatea_monto_dec(montofecha,fecha):
    transforma = montofecha.replace(fecha,'')
    #formato_decimal = float(transforma[:len(transforma)-3]+'.'+transforma[-3:])
    formato_decimal = str(transforma[:len(transforma)-3]+'.'+transforma[-3:])
    return formato_decimal


path= 'C:\\Users\\LAC40641\\Downloads\\'


lista_archivos=[]
for a in os.listdir(path):
    if str(a[-3:]) == 'zip':
        lista_archivos.append('zips/cheques/'+a)

#establecer a google chrome como predeterminado
for i in lista_archivos:
    
    
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
    try:
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
        
    except:
        print('archivo_ba')      
    ##############################
    
    #lee data al
    try:    
            #reemplaza comas de archivo
        with open(ruta_files+archivo_al, 'r+') as f:
            text = f.read()
            f.seek(0)
            f.truncate()
            f.write(text.replace(',', ''))
            
        data_al = pd.read_csv(ruta_files+archivo_al,header = None)
    
        #http://www.bcra.gov.ar/pdfs/texord/texord_viejos/v-ceninf_10-10-27.pdf
    
        columna_1 = cuil_cuit_cdi(data_al)
        columna_2 = nro_cheque(data_al)
        columna_3 = fecha_rechazo(data_al)
        columna_4 = monto(data_al)
        columna_5 = causal(data_al)
        columna_6 = fecha_levantamiento(data_al)
        columna_7 = revision(data_al)
        columna_8 = proceso_judicial(data_al)
        columna_9 = cuit_relacionado(data_al)        
        columna_10 = pago_multa(data_al)                
    
        
    
        data_al_dataframe = pd.concat([columna_1,columna_2,columna_3,columna_4,columna_5,columna_6,columna_7,columna_8,columna_9,columna_10], axis=1)
        data_al_dataframe.columns = ['cuil_cuit_cdi','nro_cheque','fecha_rechazo','monto','causal','fecha_pago','revision','judicial','cuit_relacionado','pago_multa']
        data_al_dataframe['anio_mes_dia'] = str(nom[13:21])
        
        
        
        guarda_transf = path+str('al_etl') 
        if not os.path.exists(guarda_transf):
            os.makedirs(guarda_transf)
        
        
        data_al_dataframe.to_csv(guarda_transf+'\\al'+nom[13:21]+'.csv',index=False)
    except:
        print('archivo_al')     
    ##############################
    
    # lee data ba pa
    
    try:
        #reemplaza comas de archivo
        with open(ruta_files+archivo_pa, 'r+') as f:
            text = f.read()
            f.seek(0)
            f.truncate()
            f.write(text.replace(',', ''))
    
        try:
            data_pa = pd.read_csv(ruta_files+archivo_pa, header = None,encoding='latin-1')
            
    
            columna_1 = arma_columa_1(data_pa)
            columna_2 = arma_columa_2(data_pa)
                
            
            
            data_pa_dataframe = pd.concat([columna_1,columna_2], axis=1)
            data_pa_dataframe.columns = ['cuil','nombre']
            data_pa_dataframe['anio_mes_dia'] = str(nom[13:21])
            
            
            guarda_transf = path+str('pa_etl') 
            if not os.path.exists(guarda_transf):
                os.makedirs(guarda_transf)
            
            
            data_pa_dataframe.to_csv(guarda_transf+'\\pa'+nom[13:21]+'.csv',index=False)
        
        except:
            print('archivo_pa csv')
    except:
        print('archivo_pa')