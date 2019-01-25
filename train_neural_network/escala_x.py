#!/Users/laiunce/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 11:46:45 2017

@author: laiunce
"""
import csv
import numpy as np
import pandas as pd
import sys

directorio =''
#obtiene segundo parametro pasado, va a ser el directorio
try:
	directorio=sys.argv[1]
except:
	pass

def escalado(dataset):
    maximos_columnas =  np.max(dataset, axis=0)
    minimos_columnas =  np.min(dataset, axis=0)
    dataset_escalado = (dataset-minimos_columnas)/(maximos_columnas-minimos_columnas)
    return dataset_escalado,maximos_columnas,minimos_columnas


X = np.load(directorio+'X.npy')


#escalado de X
X_escalado,maximo,minimo = escalado(X)


np.save(directorio+'X_escalado.npy', X)
