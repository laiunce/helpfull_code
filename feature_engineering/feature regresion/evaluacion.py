# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:28:59 2017

@author: LAC40641
"""


    
from sklearn.metrics import confusion_matrix    
from sklearn.linear_model import LinearRegression
from pandas import read_csv
import pandas as pd

def arma_clases(lista):
    rangos = []
    var=''
    for x in lista:
        if x >=70515:
            var='A'
        if x >=50389 and x<70511:
            var='B'
        if x >=26070 and x<50389:
            var='C1'
        if x >=16396 and x<26070:
            var='C2'
        if x >=12609 and x<16396:
            var='C3'
        if x >=10270 and x<12609:
            var='D1'
        if x <10269:
            var='D2'
        rangos.append(var)
    return rangos


directorio = 'C:\\Users\\LAC40641\\Desktop\\feature\\'
df = pd.read_csv(directorio+'prueba_merge.csv',encoding='latin-1')

df_sin_nulos = df.fillna(0)


X= df_sin_nulos.iloc[:,0:-1].values
Y= df_sin_nulos.iloc[:,-1].values


# feature extraction
model = LinearRegression()
model.fit(X, Y)   




prediccion = model.predict(X)
rangos_redict = arma_clases(prediccion)
rangos_objetivo = arma_clases(Y)


m=confusion_matrix(rangos_objetivo, rangos_redict)


d1=m[0][0]+m[0][1]
d2=m[1][0]+m[1][1]+m[1][2]
d3=m[2][1]+m[2][2]+m[2][3]
d4=m[3][2]+m[3][3]+m[3][4]
d5=m[4][3]+m[4][4]+m[4][5]
d6=m[5][4]+m[5][5]+m[5][6]
d7=m[6][5]+m[6][6]

diagmasmenos=d1+d2+d3+d4+d5+d6+d7

total=sum(sum(m))

100*(diagmasmenos/total)
#100*((m[0][0]+m[1][1]+m[2][2]+m[2][2]+m[3][3]+m[4][4]+m[5][5]+m[6][6])/total)



