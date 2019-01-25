#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 11:46:45 2017

@author: laiunce
"""

################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
#### COMIENZA DEFINICION DE FUNCIONES
################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################

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

marcadores = {0:('+','b'), 1:('o','g'), 2:('x', 'y'), 3:('*', 'm')}

def plot(P, T, W, b, title):
    plt.clf()
    
    #Ejemplos
    for class_value in np.unique(T):
        x = []
        y = []
        for i in range(len(T)):
            if T[i] == class_value:
                x.append(P[0, i])
                y.append(P[1, i])
        plt.scatter(x, y, marker=marcadores[class_value][0], color=marcadores[class_value][1])
    
    #ejes
    minimos = np.min(P, axis=1)
    maximos = np.max(P, axis=1)
    diferencias = maximos - minimos
    minimos = minimos - diferencias * 0.1
    maximos = maximos + diferencias * 0.1
    plt.axis([minimos[0], maximos[0], minimos[-1], maximos[1]])
    
    #rectas discriminantes
    x1 = minimos[0]
    x2 = maximos[0]
    (neuronas, patr) = W.shape
    for neu in range(neuronas):
        m = W[neu,0] / W[neu,1] * -1
        n = b[neu] / W[neu,1] * -1
        y1 = x1 * m + n
        y2 = x2 * m + n
        plt.plot([x1, x2],[y1, y2], color='r')
    
    plt.title(title)
    
    plt.draw()
    plt.pause(0.00001) 
    
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

def escalado(dataset):
    maximos_columnas =  np.max(dataset, axis=0)
    minimos_columnas =  np.min(dataset, axis=0)
    dataset_escalado = (dataset-minimos_columnas)/(maximos_columnas-minimos_columnas)
    return dataset_escalado


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


def crea_vector_salida_2_neuronas(salida_salida_traspuesta):

#0: 00
#1: 01
#2: 10
#3: 11

    vector_salida=[]
    for i in salida_salida_traspuesta:
        if i[0] < 0.5 and i[1] < 0.5:
            vector_salida.append(0)
        if i[0] < 0.5 and i[1] >= 0.5:
            vector_salida.append(1)
        if i[0] >= 0.5 and i[1] < 0.5:
            vector_salida.append(2)            
        if i[0] >= 0.5  and i[1] >= 0.5 :
            vector_salida.append(3)            
   
    return vector_salida


################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################
#### FINALIZA DEFINICION DE FUNCIONES
################################################################################################################################################################
################################################################################################################################################################
################################################################################################################################################################



############################################################################################################################################
# Comienza lectura de datos y transformacion a matriz
############################################################################################################################################

data_drug4 = pd.read_excel('/Users/laiunce/Google Drive/redes_neuronales/Clase 5/practica/Ej1/Drug4.xlsx')
data_drug4_matrix = data_drug4.as_matrix()

############################################################################################################################################
# Finaliza lectura de datos y transformacion a matriz
############################################################################################################################################





############################################################################################################################################
#comienza separacion  X Y train Test
############################################################################################################################################

#desordenar 
np.random.shuffle(data_drug4_matrix)

#variables de entrada X y salida T
X=data_drug4_matrix[:,:-1]
T=data_drug4_matrix[:,-1]

#escalado de X
X_escalado = escalado(X)


#separo train test de X y de T
X_train,X_test,T_train,T_test = train_test_split(X_escalado,T,test_size=0.2)


############################################################################################################################################
#termina separacion  X Y train Test
############################################################################################################################################







############################################################################################################################################
#### Entrena con 4 neurondas
############################################################################################################################################



#armo matriz de 4 clases de salida
T_matriz = np.concatenate(([T_train==0], [T_train==1], [T_train==2], [T_train==3]), axis=0).astype(int)

#defio parametros para el entrenamiento
ocultas =3
alfa= 0.35
momento = 0.2
fun_oculta = 'logsig'
fun_salida = 'logsig'
MAX_ITE= 2000
cota_error = 0.05
dibujar=True
fixed=None

#Traspongo matrices para entrenamiento

X_train_traspuesto = X_train.T
T_train_traspuesto=T_train.T

#Entreno la red con X_train y T_train
(w_O, b_O, w_S, b_S, ite, error_prom) = train(X_train_traspuesto, T_matriz, T_train_traspuesto, ocultas, alfa, momento, fun_oculta, fun_salida, MAX_ITE, cota_error, dibujar,fixed)



##################################
#Comienza funcion de evaluacion

#Una vez entrenado evaluo los X_Test y T_Test

pesos_entrada=w_O
bayas_entrada=b_O

pesos_salida=w_S
bayas_salida=b_S

#traspongo matrices de Test para luego evaluar
X_test_traspuesto = X_test.T
T_test_traspuesto=T_test.T


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
# ver esta funcion que lo que hace es aplicar la logic deseada para quedarse con una prediccion, aca preguntamos cual esel maximo solamente y me quedo con este valor
#ejemplo, si teneos que para 0 da probabilidad 34%, para 1 da 12, para 2 da 50% y para 3 65% nos quedmao con que para este casola prediccion es 3
#lo ideal seria aplicar una regresion creria yo, porque esto es empirico, en cambio una regresion por ahi ve combinaciones de probabilidades mas certeras
#esta esla matriz que uso para comparar las salidas en el excel para ver si hay algun caso border por ejemplo
salida_vector=crea_vector_salida(salida_salida_traspuesta)


#Finaliza funcion de evaluacion
##################################


#ahora podemos evaluar performance
confusion_matrix(T_test, salida_vector)
accuracy_score(T_test, salida_vector)


############################################################################################################################################
#Finaliza Entrena con 4 neurondas
############################################################################################################################################



############################################################################################################################################
#Comienza entrena con 2 neurondas
############################################################################################################################################

#Nota Al usar tansig hay que reemplazar 0 por -1 asi quedan valores 1 y 1 ,si se usa lonsig usar 0 y 1.

#armo matriz de 2 clases de salida
T_matriz = np.concatenate(([T_train>=2],[T_train%2==1]), axis=0).astype(int)

#defino parametros para el entrenamiento
ocultas =3
alfa= 0.35
momento = 0.2
fun_oculta = 'logsig'
fun_salida = 'logsig'
MAX_ITE= 2000
#tener en cuenta el ajuste dependiendo del grado de error, si es muy chico por ahi se sobreajusta mucho a los datoa y si es muy grande el error generalizamas
cota_error = 0.05
dibujar=True
fixed=None

#Traspongo matrices para entrenamiento

X_train_traspuesto = X_train.T
T_train_traspuesto=T_train.T

#Entreno la red con X_train y T_train
(w_O_2, b_O_2, w_S_2, b_S_2, ite_2, error_prom_2) = train(X_train_traspuesto, T_matriz, T_train_traspuesto, ocultas, alfa, momento, fun_oculta, fun_salida, MAX_ITE, cota_error, dibujar,fixed)



##################################
#Comienza funcion de evaluacion

#Una vez entrenado evaluo los X_Test y T_Test

pesos_entrada=w_O_2
bayas_entrada=b_O_2

pesos_salida=w_S_2
bayas_salida=b_S_2

#traspongo matrices de Test para luego evaluar

X_test_traspuesto = X_test.T
T_test_traspuesto = T_test.T


neta_oculta = np.dot(X_test,pesos_entrada.T) + bayas_entrada.T
salida_oculta = eval(fun_oculta + '(neta_oculta)')
neta_salida = pesos_salida.dot(salida_oculta.T) + bayas_salida
salida_salida = eval(fun_salida + '(neta_salida)')

#En salida traspuesta tengo los valores de probabilidades.
#acordarse de que en T_Matriz definimos las combinaciones de 1 y 0 para las salidas, y en eta matriz tenems la probailidad de que 
#sea 1 el valor, si la probailidad es cercana a 0 decimos que el valor es 0 y si es mas cercana a 1 decimos que es uno,
#y en base a eso hacemos las predicciones en la funcion
salida_salida_traspuesta =salida_salida.T

salida_vector=crea_vector_salida_2_neuronas(salida_salida_traspuesta)

#Finaliza funcion de evaluacion
##################################

#ahora podemos evaluar performance
confusion_matrix(T_test, salida_vector)
accuracy_score(T_test, salida_vector)



############################################################################################################################################
#Finliza Entrena con 2 neurondas
############################################################################################################################################














