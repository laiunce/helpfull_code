#!/Users/laiunce/anaconda/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 11:46:45 2017

@author: laiunce
"""

import numpy as np
import pandas as pd
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
from mlxtend.plotting import plot_confusion_matrix
import sys

directorio =''
#obtiene segundo parametro pasado, va a ser el directorio
try:
	directorio=sys.argv[1]
except:
	pass

merge_matrix = np.load(directorio+'merge_matrix.npy')

merge_matrix[:,1]

mc = confusion_matrix(merge_matrix[:,0], merge_matrix[:,1])


fig, ax = plot_confusion_matrix(conf_mat=mc)
plt.show()
