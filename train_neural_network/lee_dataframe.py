#!/Users/laiunce/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 11:46:45 2017

@author: laiunce

como ejecutar esto en unix

python /Users/laiunce/Desktop/Entrena_red/lee_dataframe.py /Users/laiunce/Desktop/Entrena_red/

"""
import csv
import numpy as np
import pandas as pd
import sys

#directorio ='/Users/laiunce/Desktop/Entrena_red/'

directorio =''
#obtiene segundo parametro pasado, va a ser el directorio
try:
	directorio=sys.argv[1]
except:
	pass

#opcion 2, leo con pandas y transformo a matriz numpy
quimil = pd.read_excel(directorio+'Drug4.xlsx')
quimil_matrix = quimil.as_matrix()

np.save(directorio+'dataframe.npy', quimil_matrix)



