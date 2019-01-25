# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 10:08:51 2017

@author: LAC40641
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import plotly.plotly as py
from sklearn import datasets, linear_model


                    
def agrupa_nosignificativos(x,valores_agrupar):
    if x in valores_agrupar:
        return 'agr'
    else:
        return x
    
def calcula_pearson(var,a,b):
    lista=[]
    try:
        corr=stats.pearsonr(a,b)[0]
        lista.append(var)
        lista.append(corr)
    except:
        pass
    return lista

#####################################################################################################################
# VARIABLES CONTNIUAS
#-------------------------------------------------------------------------------------------------------------------
datos_continuos1=pd.read_csv('C:\\Users\\LAC40641\\Desktop\\prueba_obj_discreto\\SET_ENTRENAMIENTO_201608_201610_2_20porc_contin.csv',encoding='latin-1',low_memory=True)
nom_objetivo=list(datos_continuos1)[-1:][0]
datos_continuos1 = datos_continuos1.drop(nom_objetivo, axis=1)
union_continuos = datos_continuos1.fillna(0)file://srfspw001i005/Riesgos_Personas/ScoreExterno/SET_ENTRENAMIENTO_201608_201610_2_20porc_contin.csv
file://srfspw001i005/Riesgos_Personas/ScoreExterno/SET_ENTRENAMIENTO_201608_201610_2_20porc_categ.csv

del datos_continuos1


#borrar
#df_sin_nulos_continuos2 = df_sin_nulos_continuos2.drop('Grupo_Segmento', axis=1)
#df_sin_nulos_continuos3 = df_sin_nulos_continuos3.drop('Grupo_Segmento', axis=1)




#-------------------------------------------------------------------------------------------------------------------
# VARIABLES CONTNIUAS
#####################################################################################################################


#####################################################################################################################
# VARIABLES CATEGORICAS
#-------------------------------------------------------------------------------------------------------------------
datos_categoricos=pd.read_csv('C:\\Users\\LAC40641\\Desktop\\prueba_obj_discreto\\SET_ENTRENAMIENTO_201608_201610_2_20porc_categ.csv',encoding='latin-1',low_memory=False)
persona_id=datos_categoricos['Persona_Id']
datos_categoricos = datos_categoricos.drop('Persona_Id', axis=1)

#datos_categoricos = datos_categoricos.drop('Auto_Moto', axis=1)
                        

#elimino variables pesadas
#try:
#    datos_categoricos=datos_categoricos.drop('Importe_Sueldo', axis=1)
#except:
#    pass

#try:
#    datos_categoricos=datos_categoricos.drop('Ind_Vto_Min_Dia_Acred_Haberes', axis=1)
#except:
#    pass

#try:
    #datos_categoricos=datos_categoricos.drop('Categoria_Laboral', axis=1)
#except:
    #pass
  #
#try:
    #datos_categoricos=datos_categoricos.drop('Convenio_Desc', axis=1) 
#except:
    #pass

#try:
    #datos_categoricos=datos_categoricos.drop('Codigo_Postal', axis=1)
#except:
    #pass

#try:
    #datos_categoricos=datos_categoricos.drop('Dependencia_Principal_Id', axis=1)
#except:
    #pass 

#try:
    #datos_categoricos=datos_categoricos.drop('Dependencia_Desc', axis=1)
#except:
    #pass



df_sin_nulos = datos_categoricos.fillna(0)

data = df_sin_nulos   
 


df_dummys=data

objetivo=df_dummys[nom_objetivo]

df_dummys = df_dummys.drop(nom_objetivo, axis=1)

nom_columnas = list(df_dummys)

#nom_columnas = ['Comportamiento_Credito_Id']

#--------------------------------------------------------------------------------------------------------------------
# crea dummys
#--------------------------------------------------------------------------------------------------------------------

for categorica in nom_columnas:
    #print(categorica)
    dummies = pd.get_dummies(df_dummys[categorica])
    print(categorica+' '+str(len(list(dummies))))
    
    if len(list(dummies)) < 50:
        lista_nom_dumm = list(dummies) 
        for v in lista_nom_dumm:
            dum_name= str(v).replace('-','_')
            dummies[str(categorica)+'_'+dum_name]=dummies[v]
            
        dummies=dummies.drop(lista_nom_dumm, axis=1)
        #add dummy variables
        df_dummys = df_dummys.join(dummies)


#dummies = pd.get_dummies(df_dummys['Sucursal_Oficial'])
    
    #drop the original column
    df_dummys = df_dummys.drop(str(categorica), axis=1)


    
    
df_dummys = df_dummys.join(objetivo)

#--------------------------------------------------------------------------------------------------------------------
# crea dummys
#--------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------------------
# hace transformaciones
#--------------------------------------------------------------------------------------------------------------------


data_dupla = data



for categorica in nom_columnas:
    
    #temporal para no hacer la transformacion que no le copo a sylvia
    data_dupla = data_dupla.drop(categorica, axis=1)
    '''
    
    print(categorica)

    #agrupa los valores que no son estadisticamente significativos
    valor_cota= 15
    
    agrupamiento=data_dupla[nom_objetivo].groupby(data_dupla[categorica]).describe()
    dc=agrupamiento['count']
    valores_agrupar = dc.loc[dc < valor_cota].index.values
    data_dupla[categorica] = data_dupla[categorica].apply(lambda x: agrupa_nosignificativos(x,valores_agrupar))
    

    nuevo_agrupamiento=data_dupla[nom_objetivo].groupby(data_dupla[categorica]).describe()
    #nuevo_agrupamiento['logica'] = (nuevo_agrupamiento['25%']+nuevo_agrupamiento['50%']+nuevo_agrupamiento['75%'] )/3
    nuevo_agrupamiento['logica'] = nuevo_agrupamiento['50%']
    

    
    indices_pd = nuevo_agrupamiento['logica'].index.values
    valores_pd = nuevo_agrupamiento['logica'].values
    
    tupla=dict(tuple(zip(indices_pd, valores_pd/min(valores_pd[valores_pd > 0]))))
    
    data_dupla[categorica+'_tran'] = data_dupla[categorica].apply(lambda x: tupla[x])
    
    #transformacion log
    #data_dupla[categorica+'_tran_lognorm'] = np.log(data_dupla[categorica+'_tran'])
    
    
    
    
    data_dupla = data_dupla.drop(categorica, axis=1)
    '''

#--------------------------------------------------------------------------------------------------------------------
# hace transformaciones
#--------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------------------------------------------------------
# VARIABLES CATEGORICAS
#####################################################################################################################



#####################################################################################################################
# UNE DATASETS
#-------------------------------------------------------------------------------------------------------------------





data_dupla_union = data_dupla
df_dummys_union = df_dummys
data_dupla_union=data_dupla_union.drop(nom_objetivo, axis=1)
df_dummys_union=df_dummys_union.drop(nom_objetivo, axis=1)


data_merge = df_dummys_union.join(data_dupla_union)
data_merge = data_merge.join(union_continuos)


del data
del data_dupla
del data_dupla_union
del datos_categoricos
del df_dummys
del df_dummys_union
del df_sin_nulos
del dummies
del union_continuos

#-------------------------------------------------------------------------------------------------------------------
# UNE DATASETS
#####################################################################################################################

#data_merge = data_dupla_union.join(objetivo)

'''
#####################################################################################################################
# crea transforamciones
#-------------------------------------------------------------------------------------------------------------------


for variable in list(data_merge)[:-1]:
    print(variable)
    try:

        y=data_merge[list(data_merge)[-1]]
        x=data_merge[variable]
        
        stats.pearsonr(x,y)[0]
        
        
        # calculate polynomial
        grado = 7
        z = np.polyfit(x, y, grado)
        f = np.poly1d(z)
          
        
        lista= []
        for valor in x:
            #print (valor)
            
            expx=grado
            texto=''
            for i in z:
                texto=texto+('+'+str(i)+'*'+str(valor)+'**'+str(expx))
                expx=expx-1
            
            lista.append(eval(texto))
            
            data_merge[variable+'_transforma_polinomio'] = pd.DataFrame(lista)
               
    except:
        pass    
    
#-------------------------------------------------------------------------------------------------------------------
# crea transforamciones
#####################################################################################################################

'''





#####################################################################################################################
# CORRELACIONES OBJETIVO
#-------------------------------------------------------------------------------------------------------------------





correlaciones_lista= []
hacer_cor = list(data_merge)[:-1]
for c in hacer_cor:
    try:
        lis_cor = calcula_pearson(c, data_merge[c],objetivo)
        if len(lis_cor)>0:
            correlaciones_lista.append(lis_cor)
    except:
        pass





#variables correlacionadas con la variable objetivo > 0.2
cota=0.15
conta=0
filtro_correlacion= []
for i in correlaciones_lista:
    if abs(i[1])>cota:
        conta+=1
        filtro_correlacion.append(i[0])
        print(i)
print(str(conta))

#variables muy correlacionadas
for i in correlaciones_lista:
    if abs(i[1])>0.2:
        print(str(i))
        
        
'''     
lista_variables_eliminar = ['Importe_Sueldo',
                            'Limite_Compra',
                            'Limite_Financiacion',
                            'Limite_Compra_VI',
                            'Limite_Compra',
                            'Limite_Financiacion_VI']
len(filtro_correlacion)


for f in filtro_correlacion:
    if f in lista_variables_eliminar:
        filtro_correlacion.remove(f)
'''



variables_correlacionadas=data_merge[filtro_correlacion]



#-------------------------------------------------------------------------------------------------------------------
# CORRELACIONES OBJETIVO
#####################################################################################################################


#####################################################################################################################
# ELIMNAR VARIABLES CORRELACIONADAS ENTRE SI
#-------------------------------------------------------------------------------------------------------------------



#elimino variables correlcionadas entre si mayor a 0.7, dejo la mas correlacionada con variable objetivo
lista_nombres=list(variables_correlacionadas)
lista_nombres2=list(variables_correlacionadas)

cota_cor= 0.6

for r in range(len(lista_nombres)):
    for e in range(len(lista_nombres)):
        
        corr=stats.pearsonr(variables_correlacionadas[lista_nombres[r]],variables_correlacionadas[lista_nombres[e]])[0]
        print(abs(corr))
        if abs(corr) > cota_cor and r != e:
            if stats.pearsonr(variables_correlacionadas[lista_nombres[r]],objetivo)[0] > stats.pearsonr(variables_correlacionadas[lista_nombres[e]],objetivo)[0]:
                try:
                    lista_nombres2.remove(lista_nombres[e])
                except:
                    pass
            else:
                try:
                    lista_nombres2.remove(lista_nombres[r])
                except:
                    pass

#-------------------------------------------------------------------------------------------------------------------
# ELIMNAR VARIABLES CORRELACIONADAS ENTRE SI
#####################################################################################################################


#####################################################################################################################
# EXPORTA DATASET
#-------------------------------------------------------------------------------------------------------------------
'''
#union de las variables iniciales
datam1=  union_continuos.join(df_sin_nulos)
for v in lista_nombres2:
    print(v)
    try:
        datam1=datam1.drop(v, axis=1)
    except:
        pass

del union_continuos
del df_sin_nulos

#elimino las variables que ya estan correlacioandas


try:
    datam1=datam1.drop('Sueldo_Normalizado_T', axis=1)
except:
    pass
datam1.to_csv('C:\\Users\\LAC40641\\Desktop\\feature\\prueba_merge_demas.csv',index=True)
'''


variables_correlacionadas_independientes=variables_correlacionadas[lista_nombres2]
variables_correlacionadas_independientes = variables_correlacionadas_independientes.join(objetivo)
variables_correlacionadas_independientes = variables_correlacionadas_independientes.join(persona_id)
variables_correlacionadas_independientes.to_csv('C:\\Users\\LAC40641\\Desktop\\feature\\prueba_merge_filtro.csv',index=True)







#plt.hist(objetivo)
#if objetivo>=50389 and objetivo<70511:
#Sueldo_Normalizado_T = pd.DataFrame(objetivo)
#variables_correlacionadas_independientes[variables_correlacionadas_independientes['Sueldo_Normalizado_T'] >=70515 ]
#Sueldo_Normalizado_T[Sueldo_Normalizado_T['Sueldo_Normalizado_T'] >=50389 && Sueldo_Normalizado_T['Sueldo_Normalizado_T']<70511 ]


correlaciones_lista

for v in lista_nombres2:
    for c in correlaciones_lista:
        if v == c[0]:
            print(c[0] + ','+str(abs(c[1])))


#-------------------------------------------------------------------------------------------------------------------
# EXPORTA DATASET
#####################################################################################################################



#a='RUBRO_DE_MAYOR_CONS_TC_SUPERMERCADOS'
#b='RUBRO_DE_MAYOR_CONS_TD_SUPERMERCADOS'
#stats.pearsonr(variables_correlacionadas_obejtivo[a],variables_correlacionadas_obejtivo[b])

#matriz=variables_correlacionadas.corr()



#for i in correlaciones_lista:
#    if i[0] in lista_nombres2:
#        print(i)
#
#list(data_merge)

#variables_dos_modelos = ['ANT_ANIOS_BCO_T','ANT_CLEAN_UP_CA_Min_6','ANTIGUEDAD_TC','CANT_PRODS_TIT','cantidad_PELUQUERIAS_Sum','cantidad_SALUD_Sum','Categoria_Laboral_tran','CODIGO_DESCUENTO','ConsultaMovimientosEBank_Sum_Sum','ConsultaTarjetaCoordenadasBanco_Sum_Sum','FLAG_INVERSOR__tran','FLAG_PORC_DEUDA_LIM_TC_50_Sum_6','FLAG_PORC_SDO_PROM_D_LIM_CA_90_Sum_3','GetCategoryListClubPatagonia_Sum_Sum','Max_Dia_Acred_Haberes','Mto_Extracciones_CA','PagoTarjetaDebitoCuenta_Sum_Sum','Preembozo_VI_tran','Producto_VI_MA_AM_concat_tran','Producto_VI_MA_concat_tran','Q_Acred_Haberes_12M','Q_Cotitulares','Rentabilidad_12','RUBRO_DE_MAYOR_CONS_TC_12_tran','sum__COM_Sum','UPG_MASTER_6_D','UPG_VISA_6_tran']
#variables_correlacionadas_independientes=data_merge[variables_dos_modelos]
#variables_correlacionadas_independientes = variables_correlacionadas_independientes.join(objetivo)
#variables_correlacionadas_independientes.to_csv('C:\\Users\\LAC40641\\Desktop\\feature\\prueba_merge.csv',index=False)



