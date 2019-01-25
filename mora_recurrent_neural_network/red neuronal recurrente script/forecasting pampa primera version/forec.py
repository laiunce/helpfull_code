# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 12:08:19 2018

@author: LAC40641
"""


import os

from statsmodels.tsa.seasonal import seasonal_decompose
from pandas import Series
from matplotlib import pyplot
import statsmodels.api as sm
import pandas as pd

cwd = os.getcwd()
series = Series.from_csv(cwd+'\\Desktop\\forecasting mora\\data_mora.csv', header=0)
series.plot()
pyplot.show()

df = pd.read_csv(cwd+'\\Desktop\\forecasting mora\\data_mora.csv')
x = df['mora']
x_smoothed, x_trend = sm.tsa.filters.hpfilter(x, lamb=10)
fig, axes = plt.subplots(figsize=(12,4), ncols=3)

axes[0].plot(x)
axes[0].set_title('raw x')
axes[1].plot(x_trend)
axes[1].set_title('trend')
axes[2].plot(x_smoothed)
axes[2].set_title('smoothed x')

#https://machinelearningmastery.com/decompose-time-series-data-trend-seasonality/


