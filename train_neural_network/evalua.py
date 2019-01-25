#!/Users/laiunce/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 11:46:45 2017

@author: laiunce
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
import sys

def purelin(x):
    return x

def dpurelin(x):
    return np.ones_like(x)
    
def logsig(x):
    return 1 / (1 + np.exp(-x))

def dlogsig(x):
    return logsig(x) * (1 - logsig(x))

def tansig(x):
    return np.tanh(x)

def dtansig(x):
    return 1.0 - np.square(tansig(x))

def crea_vector_salida(salida_salida_traspuesta):
    vector_salida=[]
    for i in salida_salida_traspuesta:    
        if i[0] == max(i):
            vector_salida.append(0)
        if i[1] == max(i):
            vector_salida.append(1)
        if i[2] == max(i):
            vector_salida.append(2)
        if i[3] == max(i):
            vector_salida.append(3)    
    return vector_salida

directorio =''
#obtiene segundo parametro pasado, va a ser el directorio
try:
    directorio=sys.argv[1]
except:
    pass


pesos_entrada = np.load(directorio+'pesos_entrada.npy')
bayas_entrada = np.load(directorio+'bayas_entrada.npy')
pesos_salida = np.load(directorio+'pesos_salida.npy')
bayas_salida = np.load(directorio+'bayas_salida.npy')


X_test = np.load(directorio+'X_test.npy')
T_test = np.load(directorio+'T_test.npy')


#traspongo matrices de Test para luego evaluar
X_test_traspuesto = X_test.T
T_test_traspuesto=T_test.T

#definir esto
fun_oculta = 'logsig'


# Para el predict tomo la misma funcion que utiliza en la funcion de entrenamiento, hay que multiplicar las matrices de pesos obtenido
# por los valores que queremos predecir

#primero multiplico los valores de entrada enX_test por los pesos de entrada y le sumo el bayas
neta_oculta = np.dot(X_test,pesos_entrada.T) + bayas_entrada.T
#para obtener la salida de la capa oculta tenemos que alicarla la funcion logsig
salida_oculta = eval(fun_oculta + '(neta_oculta)')
#luego con los valores de la salida de la capa oculta, multiplicamos con matriz de peos de capa de salida y le agregamos el bayas
neta_salida = pesos_salida.dot(salida_oculta.T) + bayas_salida
#y tambien evalualos con la funcion de salida que es logsig, dpeediendo de la funcion que apliquemos hay que cmbiar aca o no, acordarse de tansig modificar entre -1 y 1 
salida_salida = eval(fun_oculta + '(neta_salida)')

#trasponiendo los valores obtenemos el vector de las predicciones
salida_salida_traspuesta =salida_salida.T

#guarda matriz numpy por un lado y dataframe en csv por otro
np.save(directorio+'salida_salida_traspuesta.npy', salida_salida_traspuesta)


salida_vector=crea_vector_salida(salida_salida_traspuesta)


T_salida = pd.DataFrame(T_test)
T_salida.columns = ['salida_verdadera']

X_salida = pd.DataFrame(salida_vector)
X_salida.columns = ['salida_predicha']

merge = pd.concat([X_salida, T_salida], axis=1)


merge.to_csv(directorio+'salida.csv',index = False)

merge_matrix = merge.as_matrix()

np.save(directorio+'merge_matrix.npy', merge_matrix)



