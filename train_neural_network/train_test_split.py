#!/Users/laiunce/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 11:46:45 2017

@author: laiunce
"""
import csv
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import sys

directorio =''
#obtiene segundo parametro pasado, va a ser el directorio
try:
	directorio=sys.argv[1]
except:
	pass


X_escalado= np.load(directorio+'X_escalado.npy')
T= np.load(directorio+'T.npy')

X_train,X_test,T_train,T_test = train_test_split(X_escalado,T,test_size=0.2)

np.save(directorio+'X_train.npy',X_train)
np.save(directorio+'X_test.npy',X_test)
np.save(directorio+'T_train.npy',T_train)
np.save(directorio+'T_test.npy',T_test)
