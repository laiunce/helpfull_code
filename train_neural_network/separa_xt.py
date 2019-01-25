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

quimil_matrix = np.load(directorio+'soufle.npy')

#variables de entrada X y salida T
X=quimil_matrix[:,:-1]
T=quimil_matrix[:,-1]


np.save(directorio+'X.npy', X)
np.save(directorio+'T.npy', T)