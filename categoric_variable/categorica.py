#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 20:39:11 2017

@author: laiunce
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import itertools
import matplotlib.pyplot as plt
import plotly.plotly as py
from sklearn import datasets, linear_model
data=pd.read_csv('/Users/laiunce/Desktop/prueba categorica/origen.csv')

df=data

categorica='X'

# CREA DUMMIES > > > > > > > > > > > > > > > > >

dummies = pd.get_dummies(df[categorica])

#drop the original column
df = df.drop(categorica, axis=1)

#add dummy variables
df = df.join(dummies)

# CREA DUMMIES < < < < < < < < < < < < < < < < < <



# BOXPLOTS > > > > > > > > > > > > > > > > >

sns.boxplot(x='X', y='Y',data=data)

# BOXPLOTS < < < < < < < < < < < < < < < < < <


data['Y'].groupby(data['X']).describe()
v_unicos = np.unique(data[['X']].values)


stats.ttest_ind(a= data.loc[data['X'] == 'a']['Y'],
                b= data.loc[data['X'] == 'a']['Y'],
                equal_var=False)    # Assume samples have equal variance?
       
                
# HACER SANDBOX MENOR 30 OBSERVACIONES UNIRLAS TODAS EN UNA CATEOGRIA < < < < < < < < < < < < < < < < < <
# HACER SANDBOX MENOR 30 OBSERVACIONES UNIRLAS TODAS EN UNA CATEOGRIA < < < < < < < < < < < < < < < < < <

indices = []
contador=0
for v1 in v_unicos:
    l=[]
    l.append(v1)
    l.append(contador)
    indices.append(l)
    contador+=1



my_array = np.empty([len(indices), len(indices)])
for i, j in itertools.product(range(len(indices),), range(len(indices),)):
    my_array[i, j] = stats.ttest_ind(a= data.loc[data['X'] == v_unicos[i]]['Y'],
                                     b= data.loc[data['X'] == v_unicos[j]]['Y'],
                                     equal_var=False)[1]


# CLUSTER CON MATRIZ DE DISTANCIA < < < < < < < < < < < < < < < < < <
# CLUSTER CON MATRIZ DE DISTANCIA < < < < < < < < < < < < < < < < < <


# ORDENO DE MENOR A MAYOR < < < < < < < < < < < < < < < < < <




nuevo_agrupamiento=data['Y'].groupby(data['X']).describe()
#nuevo_agrupamiento['logica'] = (nuevo_agrupamiento['25%']+nuevo_agrupamiento['50%']+nuevo_agrupamiento['75%'] )/3
nuevo_agrupamiento['logica'] = nuevo_agrupamiento['50%']


indices_pd = nuevo_agrupamiento['logica'].index.values
valores_pd = nuevo_agrupamiento['logica'].values


tupla=dict(tuple(zip(indices_pd, valores_pd/min(valores_pd))))


data_dupla = data
data_dupla['X'] = data_dupla['X'].apply(lambda x: tupla[x])



# Y and Z are numpy arrays or lists of variables 
stats.pearsonr(data_dupla['X'] , data_dupla['Y'] )


# modelo < < < < < < < < < < < < < < < < < <

regr = linear_model.LinearRegression() 
# Train the model using the training sets

Xvar=data_dupla['X'].reshape(len(data_dupla['X']),1)
Yvar=data_dupla['Y'].reshape(len(data_dupla['Y']),1)

regr.fit(Xvar, Yvar)


regr.intercept_
regr.coef_

prediccion = regr.predict(Xvar)


                
                