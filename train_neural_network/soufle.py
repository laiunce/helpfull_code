#!/Users/laiunce/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 11:46:45 2017

@author: laiunce

como ejecutar esto en unix

python /Users/laiunce/Desktop/Entrena_red/soufle.py /Users/laiunce/Desktop/Entrena_red/

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


dataframe = np.load(directorio+'dataframe.npy')

np.random.shuffle(dataframe)

np.save(directorio+'soufle.npy', dataframe)



