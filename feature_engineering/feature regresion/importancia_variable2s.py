# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 13:12:24 2017

@author: LAC40641
"""

from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LinearRegression
import pandas as pd
import savReaderWriter as s
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot
from scipy import stats

def arma_clases(x):
	if x >=70515:
		return('A')
	if x >=50389 and x<70511:
		return('B')
	if x >=26070 and x<50389:
		return('C1')
	if x >=16396 and x<26070:
		return('C2')
	if x >=12609 and x<16396:
		return('C3')
	if x >=10270 and x<12609:
		return('D1') 
	if x <10269:
		return('D2') 

directorio = 'C:\\Users\\LAC40641\\Desktop\\feature\\'

df = pd.read_csv(directorio+'prueba_merge.csv',encoding='latin-1')
list(df)
df_sin_nulos = df.fillna(0)
nom_columnas=df_sin_nulos.columns.values


f,c=df_sin_nulos.shape

rango_ini= 0
rango_fin = c-1
#rango_fin = 802

df_var=df_sin_nulos.iloc[:,rango_ini:rango_fin]


X= df_var.values
Y= df_sin_nulos.iloc[:,-1].values



# feature extraction
model = LinearRegression()
rfe = RFE(model)
fit = rfe.fit(X, Y)


# fit an Extra Trees model to the data
#model2 = ExtraTreesClassifier()
#model2.fit(X, Y)
# display the relative importance of each attribute
#print(model2.feature_importances_)

#print("Num Features: %d") % fit.n_features_
#print("Selected Features: %s") % fit.support_
#print("Feature Ranking: %s") % fit.ranking_



#cota=0.2

#contador= 0
#for v in nom_columnas[:-1]:
#    try:
#        if stats.pearsonr(df_sin_nulos[v],Y)[0] > cota or stats.pearsonr(df_sin_nulos[v],Y)[0] < -cota:
#            print(v+' '+str(stats.pearsonr(df_sin_nulos[v],Y)))
#            contador+=1
#    except:
#        pass
#print('cantidad: '+str(contador))





###############################################################################################

###############################################################################################


lista_columnas_df= list(df_var)
ranking =fit.ranking_

contador= 0
variables_importantes=[]
for i in range(len(ranking)):
    if ranking[i] == 1:
        contador+=1
        variables_importantes.append(lista_columnas_df[i])
print('cantidad: '+str(contador))
        #print(nom_columnas[i])

# imprime variables mas correlacionadas

#el segundo valor es la prueba de hipotesis, la hipoteis es que las dos variables no estan correlacionadas
#si el valor es menor a 0.05 rechazamos la hipotesis nula

    
    
#stats.pearsonr(df_var['REVOLVING_TC_AM_Mean_3'],Y)[0]
#variable_scatter= 'REVOLVING_TC_AM_Mean_3'
#matplotlib.pyplot.scatter(df_var[variable_scatter],Y)
#matplotlib.pyplot.show()


nom_objetivo=list(df_sin_nulos)[-1:][0]
objetivo=df_sin_nulos[nom_objetivo]


data_salida=df_sin_nulos[variables_importantes]
data_merge_salida = data_salida.join(objetivo)

data_merge_salida.to_csv('C:\\Users\\LAC40641\\Desktop\\feature\\prueba_merge_salida.csv',index=False)

    




