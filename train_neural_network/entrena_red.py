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
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
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

"""
Created on Tue Sep 12 11:02:48 2017

@author: auvimo

Función train
-------------
Parámetros:
       P: es una matriz con los datos de los patrones con los cuales
           entrenar la red neuronal. Los ejemplos deben estar en columnas.
       T: es una matriz con la salida esperada para cada ejemplo. Esta matriz 
           debe tener tantas filas como neuronas de salida tenga la red
       T2: clases con su valor original (0 .. n-1) (Solo es utilizado para graficar)
       ocultas: la cantidad de neuronas ocultas que tendrá la red    
       alfa: velocidad de aprendizaje
       momento: término de momento
       fun_oculta: función de activación en las neuronas de la capa oculta
       fun_salida: función de activación en las neuronas de la capa de salida
       MAX_ITERA: la cantidad máxima de iteraciones en las cuales se va a
           ejecutar el algoritmo
       cota_error: error mínimo aceptado para finalizar con el algoritmo
       dibujar: si vale True (y los datos son en dos dimensiones) dibuja los
           ejemplos y las rectas discriminantes.

Devuelve:
       w_O: la matriz de pesos de las neuronas de la capa oculta
       b_O: vector de bias de las neuronas de la capa oculta
       w_S: la matriz de pesos de las neuronas de la capa de salida
       b_S: vector de bias de las neuronas de la capa de salida
       ite: número de iteraciones ejecutadas durante el algoritmo
       error_prom: errorPromedio finalizado el algoritmo

Ejemplo de uso:
       (w_O, b_O, w_S, b_S, ite, error_prom) = train(P, T, T2, 10, 0.25, 1.2, 'logsig', 'tansig', 25000, 0.001, True);
       
"""

def train(P, T, T2, ocultas, alfa, momento, fun_oculta, fun_salida, MAX_ITE, cota_error, dibujar,fixed):
    
    (entran, CantPatrones) = P.shape   
    (salidas, CantPatrones) = T.shape
    
        
        
    #si es fixed inicia con pesos fijos sino lo hace random
    
    if fixed is None :
           w_O = np.random.rand(ocultas, entran) - 0.5
           b_O = np.random.rand(ocultas,1) - 0.5
           w_S = np.random.rand(salidas, ocultas) - 0.5
           b_S = np.random.rand(salidas,1) - 0.5
    else:         
           w_O = np.ones((ocultas, entran)) * fixed
           b_O = np.ones((ocultas,1)) * fixed
           w_S = np.ones((salidas, ocultas)) * fixed
           b_S = np.ones((salidas,1)) * fixed
    
    momento_w_S = np.zeros(w_S.shape)
    momento_b_S = np.zeros(b_S.shape)
    momento_w_O = np.zeros(w_O.shape)
    momento_b_O = np.zeros(b_O.shape)
    
    ite = 0;
    error_prom = cota_error + 1
    
    while (ite < MAX_ITE) and (error_prom > cota_error):
        suma_error = 0
        for p in range(CantPatrones): 
            neta_oculta = w_O.dot(P[:,p][np.newaxis].T) + b_O
            salida_oculta = eval(fun_oculta + '(neta_oculta)')
            neta_salida = w_S.dot(salida_oculta) + b_S
            salida_salida = eval(fun_salida + '(neta_salida)')
           
            error_ejemplo = T[:,p] - salida_salida.T[0]
            suma_error = suma_error + np.sum(error_ejemplo**2)

            delta_salida = error_ejemplo[np.newaxis].T * eval('d' + fun_salida + '(neta_salida)')
            delta_oculta = eval('d' + fun_oculta + '(neta_oculta)') * w_S.T.dot(delta_salida)
            
            w_S = w_S + alfa * delta_salida * salida_oculta.T + momento * momento_w_S
            b_S = b_S + alfa * delta_salida + momento * momento_b_S
             
            w_O = w_O + alfa * delta_oculta * P[:,p] + momento * momento_w_O
            b_O = b_O + alfa * delta_oculta + momento * momento_b_O
           
            momento_w_S = alfa * delta_salida * salida_oculta.T + momento * momento_w_S
            momento_b_S = alfa * delta_salida + momento * momento_b_S
            
            momento_w_O = alfa * delta_oculta * P[:,p].T + momento * momento_w_O
            momento_b_O = alfa * delta_oculta + momento * momento_b_O
            
        error_prom = suma_error / CantPatrones
        ite = ite + 1
        print(ite, error_prom)   
        
        if dibujar and (entran == 2):        
            plot(P, T2, w_O, b_O, 'Iteración: ' + str(ite) + ' - Error promedio: ' + str(error_prom))
        
    return (w_O, b_O, w_S, b_S, ite, error_prom)


directorio =''
#obtiene segundo parametro pasado, va a ser el directorio
try:
  directorio=sys.argv[1]
except:
  pass

X_train = np.load(directorio+'X_train.npy')
T_train = np.load(directorio+'T_train.npy')

#armo matriz de 4 clases de salida
T_matriz = np.concatenate(([T_train==0], [T_train==1], [T_train==2], [T_train==3]), axis=0).astype(int)

#defio parametros para el entrenamiento
ocultas =10
alfa= 0.1
momento = 0.02
fun_oculta = 'logsig'
fun_salida = 'logsig'
MAX_ITE= 200
cota_error = 0.05
dibujar=True
fixed=None

#Traspongo matrices para entrenamiento

X_train_traspuesto = X_train.T
T_train_traspuesto=T_train.T

#Entreno la red con X_train y T_train
(w_O, b_O, w_S, b_S, ite, error_prom) = train(X_train_traspuesto, T_matriz, T_train_traspuesto, ocultas, alfa, momento, fun_oculta, fun_salida, MAX_ITE, cota_error, dibujar,fixed)

pesos_entrada=w_O
bayas_entrada=b_O

pesos_salida=w_S
bayas_salida=b_S

np.save(directorio+'pesos_entrada.npy', pesos_entrada)
np.save(directorio+'bayas_entrada.npy', bayas_entrada)
np.save(directorio+'pesos_salida.npy', pesos_salida)
np.save(directorio+'bayas_salida.npy', bayas_salida)






