#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 23:56:21 2017

@author: laiunce
"""
import matplotlib.pyplot as plt
import numpy as np
from mlxtend.plotting import plot_confusion_matrix
import sys

directorio ='/Users/laiunce/Desktop/Entrena_red/'
salida_salida_traspuesta= np.load(directorio+'salida_salida_traspuesta.npy')


plt.matshow(salida_salida_traspuesta)
