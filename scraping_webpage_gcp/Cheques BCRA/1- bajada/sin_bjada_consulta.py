# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 14:55:54 2017

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


    
for f in range(0,len(filenames)):
    print(f)
    csv = pd.read_csv(filenames[f])
    #tmp = csv.loc[ csv['cuil_cuit_cdi'].isin([20084821285,30694382408,30709130354,33679902259,33679902259,30709130354,20042806987,20043135547,20132764787,20140274489,20173959487,20244253394,20304025086,20306395220,23240046164,27235735003,30694382408,30710352689,33679902259,33679902259,33679902259,33679902259,30710352689,30700909251,30709130354,33679902259,20042806987,20173959487,20176032619,20244973087,23240046164,27054617912,27165748323,27931551448,30694382408,30694382408,30700909251,30709130354,30709130354,30709130354,30709130354,27931551448,20407321627,20424701921,27461243202,30708752106,30709130354])]
    tmp = csv.loc[ csv['cuil_cuit_cdi'].isin([30700909251])]
    if len(tmp) > 0:
        tmp.to_csv(path+'\\match\\'+str(f)+'_match.csv', index=False)
        print(tmp)
    