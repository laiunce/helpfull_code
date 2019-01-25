# -*- coding: utf-8 -*-

"""
Created on Mon Jan 22 16:53:36 2018

@author: DAB97664
"""
#Este algorito calcula el lift min, lift max, y max |LIFT-1|, de todas las categorias de cada variable, con respecto 
#a las categorias del target categorico.


############################# PARAMETROS  #################################
carpeta_trabajo = '\\\\srappw001v011\\Disco D\\DAM_DESARROLLO\\SCORE EXTERNO\\MODELADO\\STREAMS\\seleccion variables\\prueba categorica\\'   # la barra invertida debe escribirse 2 veces
nombre_archivo_entrada = 'SET_ENTRENAMIENTO_201608_201610_2_20porc_categ_prueba.csv'
nombre_archivo_salida = 'ANALISIS_VAR_SET_ENTRENAMIENTO_201608_201610_2_20porc_categ_prueba2.csv'
target = 'Status'      #nombre de columna target (debe ser categorica)
min_cant_categorias = 50  # maxima cantidad de categorias que considera el análisis de lift
variables_no_consideradas = ['Persona_Id']  # si no hay campos para NO considerar, dejar vacio entre corchetes []

##############################################################################
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
import os


# define directorio de trabajo
os.chdir(carpeta_trabajo)

# carga de datos
datos_categoricos=pd.read_csv(nombre_archivo_entrada,encoding='latin-1',low_memory=False)
# imputo nulos
datos_categoricos = datos_categoricos.fillna(-99999) # completo los null con la palabra el númer -99999



#persona_id=datos_categoricos['Persona_Id'] # almaceno la Persona_Id en otra variable

# quito las columnas que no se consideraran en el analisis
if len(variables_no_consideradas) > 0:  # si tiene campos para eliminar
    datos_categoricos = datos_categoricos.drop(variables_no_consideradas, axis=1)  # quito la persona_id

### listado de variables
nom_columnas = list(datos_categoricos)  # creo una lista con los nombres de las variables
nom_columnas.remove(target) # quito de la lista al target


##### calculo la prob de ocurrencia de los valores del target ########
prob_target = pd.DataFrame( index = [0], columns= [list(set(datos_categoricos[target]))] )
count_target = pd.DataFrame( index = [0], columns= [list(set(datos_categoricos[target]))] )

for t in list(set(datos_categoricos[target])):# inicializa el vector en cero
    count_target[t][0] = 0


for t in list(set(datos_categoricos[target])):# recorre los distintos valores del target    
    for row in datos_categoricos[list([target])].iterrows(): # Recorre cada registro de la variable target
                row = list(row[1])  # separa solo los valores
                if (row[0] == t):  
                    count_target[t][0] = count_target[t][0]+1  # si el valor del registro es igual al valor del target, suma una unidad en el vector

for t in list(set(datos_categoricos[target])): # 
    if count_target[t][0] > 0:
        prob_target[t][0] = count_target[t][0] / len(datos_categoricos[target])


############## Calculo Max lift por variable #################

analisis_lift_variables =pd.DataFrame( columns= ['variable', 'dif_lift_abs', 'max_lift','min_lift' ] )


for var in nom_columnas:
    #list(set(datos_categoricos[target])) # distinct target
    #list(set(datos_categoricos[var])) # distinct variable
    if (len(list(set(datos_categoricos[var]))) < min_cant_categorias == 50):
                
        matriz = pd.DataFrame( index = list(set(datos_categoricos[var]))  , columns= [list(set(datos_categoricos[target]))] )  # crea una matriz con las distintas categorias de la variables(en filas) y los distintos valores del target (columnas)
        matriz_lift = pd.DataFrame( index = list(set(datos_categoricos[var]))  , columns= [list(set(datos_categoricos[target]))] )  # crea una matriz con las distintas categorias de la variables(en filas) y los distintos valores del target (columnas)
        
        max_lift = 1 
        min_lift = 1
        dif_lift_abs = 0
        
        # se inicializa la matriz en cero para la matriz de ocurrencia e inicializa en 1 para la matriz de lift
        for t in list(set(datos_categoricos[target])):
            for cat in list(set(datos_categoricos[var])):
                matriz[t][cat] = 0
                matriz_lift[t][cat] = 1 
                
        matriz_abs_lift = matriz.copy() # hago una copia de la matriz para posteriormente almacenar la sig formula: |LIFT-1|  ...valor absoluto
          
                        
        ##### version 2
        for cat in list(set(datos_categoricos[var])): # recorre las distintas categorias de la variable
            total_cat = 0
            for t in list(set(datos_categoricos[target])): # recorre las distintas categorias del target
                for row in datos_categoricos[list([var,target])].iterrows(): # Recorre las columnas variable y target del dataset
                    row = list(row[1])  # obtiene solo los valores
                    if (row[0] == cat and row[1] == t): # si el registro coincide con la categoria y el valor del target, seguidamente se suma un valor al vector
                        #print('hola')
                        matriz[t][cat] = matriz[t][cat] +1
                        total_cat = total_cat + 1
            for t in list(set(datos_categoricos[target])):
                #matriz_lift[t][cat] = (matriz[t][cat]  / total_cat) / prob_target[t][0]  # almaceno el lift
                matriz_lift[t][cat] = (1,(matriz[t][cat]  / total_cat) / prob_target[t][0])[(matriz[t][cat]  / total_cat) / prob_target[t][0] != 0]
                #matriz_abs_lift[t][cat] = abs( ((matriz[t][cat]  / total_cat) / prob_target[t][0])-1 )  # almaceno los sig: |LIFT-1| 
                if(matriz_lift[t][cat] > max_lift): # si el valor del lift es mayor al maximo que ya hay almacenado para esta variable, se sobre escribe con este nuevo lift
                    max_lift = matriz_lift[t][cat]
                if(matriz_lift[t][cat] < min_lift): # si el valor del lift es menor al minimo que ya hay almacenado para esta variable, se sobre escribe con este nuevo lift
                    min_lift = matriz_lift[t][cat]
                if(abs( ((matriz[t][cat]  / total_cat) / prob_target[t][0])-1 ) > dif_lift_abs and matriz[t][cat] != 0): # si el valor del |LIFT-1|  es mayor al maximo que ya hay almacenado para esta variable, se sobre escribe con este nuevo lift. Además matriz[t][cat] debe ser distinto de cero para que la formula no de 1 
                    dif_lift_abs =    abs( ((matriz[t][cat]  / total_cat) / prob_target[t][0])-1 ) 
        analisis_lift_variables = analisis_lift_variables.append(pd.DataFrame( [[var, dif_lift_abs , max_lift, min_lift] ], columns= ['variable', 'dif_lift_abs', 'max_lift','min_lift' ] ))               
        
        #DESARROLLO FUTURO:
        #se podría cargar a una variable la matriz de lift. asi en el final se lo exporta a un archivo que tenga todos los lift de las categorias de las variables con respecto a las categorias del target
        
        
    else:
        analisis_lift_variables = analisis_lift_variables.append(pd.DataFrame( [[var, None , None, None] ], columns= ['variable', 'dif_lift_abs', 'max_lift','min_lift' ] ))               
    
analisis_lift_variables.to_csv(nombre_archivo_salida, sep='\t')
