import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import plotly.plotly as py
from sklearn import datasets, linear_model

points = np.array([(1, 1), (2, 4), (4, -7),(5, -9),(7, -4), (3, 1), (9, 3)])



#points = np.array([(0, 1),  (1, 0)])
# get x and y vectors
x = points[:,0]
y = points[:,1]


# calculate polynomial
grado = 5
z = np.polyfit(x, y, grado)
f = np.poly1d(z)


np.poly1d(3)
# calculate new x's and y's
x_new = np.linspace(x[0], x[-1], 50)
y_new = f(x_new)

plt.plot(x,y,'o', x_new, y_new)
#plt.xlim([x[0]-1, x[-1] + 1 ])
plt.xlim([x[0]-1, x[-1] + 1 ])
plt.show()




--------------------------------

datos_continuos1=pd.read_csv('C:\\Users\\LAC40641\\Desktop\\prueba categorica\\prueba_importancia_continuas1.csv',encoding='latin-1')



lista_nuevas_corr= []
for variable in list(datos_continuos1):
    try:


        y=datos_continuos1['Sueldo_Normalizado_T']
        x=datos_continuos1[variable]
        
        stats.pearsonr(x,y)[0]
        
        
        # calculate polynomial
        grado = 10
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
        
        
        
        print(variable+':'+str(stats.pearsonr(x,y)[0])+'<>'+str(stats.pearsonr(lista,y)[0]))
    
        lista_nuevas_corr.append(variable+':'+str(stats.pearsonr(x,y)[0])+'<>'+str(stats.pearsonr(lista,y)[0]))
    except:
        pass    
--------------------------------

expx=grado
texto=''
for i in z:
    texto=texto+(str(i)+'x^'+str(expx)+' ')
    expx=expx-1


print(texto)    

lista= []
for valor in x:
    print (valor)
    
    expx=grado
    texto=''
    for i in z:
        texto=texto+('+'+str(i)+'*'+str(valor)+'**'+str(expx))
        expx=expx-1
    
    lista.append(eval(texto))


stats.pearsonr(lista,x)[0]
stats.pearsonr(lista,y)[0]

 