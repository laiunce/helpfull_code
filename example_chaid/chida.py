# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 14:21:08 2017

@author: LAC40641
"""


#https://github.com/Rambatino/CHAID
le = preprocessing.LabelEncoder()
from CHAID import Tree
from sklearn import preprocessing
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn import tree
from sklearn.tree import _tree


df = pd.read_csv('C:\\Users\\LAC40641\\Desktop\\ejemplo arbol\\prueba_chaid.csv', encoding='latin-1')

le.fit(df['Sucursal_Oficial'].values) 
X = np.array(le.transform(df['Sucursal_Oficial']))
y = np.array(df['Sueldo_Normalizado'])

xx= np.array(X).reshape(len(X), 1)

tree = Tree.from_numpy(xx, y, split_titles=['a'], min_child_node_size=1)




df_p=pd.DataFrame(list(zip(X, y.values)),columns=['lst1_title','lst2_title'])
df_p.columns=['Sucursal_Oficial','Sueldo_Normalizado']


independent_variable_columns = ['Sucursal_Oficial']
dep_variable = 'Sueldo_Normalizado'

tree = Tree.from_pandas_df(df_p, dict(zip(independent_variable_columns, ['nominal'] * 3)), dep_variable, dep_variable_type='continuous')

tree.to_tree()




