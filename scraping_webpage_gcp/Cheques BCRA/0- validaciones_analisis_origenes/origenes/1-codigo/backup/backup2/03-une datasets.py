# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 16:06:45 2017

@author: LAC40641
"""



import pandas as pd
import os

pgral='C:\\Users\\LAC40641\\Downloads\\'


############  al_etl

var= 'al_etl'

path = pgral+var

lista = os.listdir(path)

filenames=[]
for i in lista:
    filenames.append(path+'\\'+i)
    
combined_csv = pd.concat( [ pd.read_csv(f) for f in filenames ] )


combined_csv.to_csv(path+'\\'+var+'_merge.csv', index=False )



############  ba_etl

var= 'ba_etl'

path = pgral+var

lista = os.listdir(path)

filenames=[]
for i in lista:
    filenames.append(path+'\\'+i)

combined_csv = pd.concat( [ pd.read_csv(f) for f in filenames ] )


combined_csv.to_csv(path+'\\'+var+'_merge.csv', index=False )



############  pa_etl

var= 'pa_etl'

path = pgral+var

lista = os.listdir(path)

filenames=[]
for i in lista:
    filenames.append(path+'\\'+i)

pd.read_csv(filenames[1])

combined_csv = pd.concat( [ pd.read_csv(f,encoding='latin-1') for f in filenames ] )


combined_csv.to_csv(path+'\\'+var+'_merge.csv', index=False )