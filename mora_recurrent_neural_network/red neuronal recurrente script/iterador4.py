#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 00:02:34 2018

@author: laiunce
"""
#https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/
# complementar con http://www.jakob-aungiers.com/articles/a/LSTM-Neural-Network-for-Time-Series-Prediction
from math import sqrt
import numpy as np
from numpy import concatenate
from matplotlib import pyplot
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from datetime import datetime

path='C:\\Users\\LAC40641\\Desktop\\rec\\'


# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
	n_vars = 1 if type(data) is list else data.shape[1]
	df = DataFrame(data)
	cols, names = list(), list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i))
		names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i))
		if i == 0:
			names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
		else:
			names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
	# put it all together
	agg = concat(cols, axis=1)
	agg.columns = names
	# drop rows with NaN values
	if dropnan:
		agg.dropna(inplace=True)
	return agg

# load dataset
dataset = read_csv(path+'mora_dataset_201510_201801.csv', header=0, index_col=0)

cant_evaluar=3

#for escalado in [1]:
#    for dias_entrena in [3,4,5]:
#        for batch in [1,3,6,12]:
#            for ver in [1,2,3,4,5]:
#                for epoca in [30,50,100,200]:

for dias_entrena in [12]:
    for batch in [2,3,4,5]:
        for ver in [3,4,5]:
            for epoca in [100,200,300]:    
                try:

                    values = dataset.values
                    

                    # integer encode direction
                    #encoder = LabelEncoder()
                    #values[:,4] = encoder.fit_transform(values[:,4])
                    # ensure all data is float
                    values = values.astype('float32')
                    # normalize features
                    
                    #lo de abajo para evitar el escalado si queremos saltearlo

                    scaler = MinMaxScaler(feature_range=(0, 1))
                    scaled = scaler.fit_transform(values)
                
                    
                    
                
                    #
                    #scaled = values
                    # specify the number of lag hours
                    n_dias = dias_entrena
                    # frame as supervised learning
                    reframed = series_to_supervised(scaled, n_dias, 1)
                    
                                        #el ultim registro es el a predecir
                    
                    # split into train and test sets
                    values = reframed.values
                    
                    predecir = values[len(values)-1]
                    values=values[0:len(values)-1]
                    
                    
                    n_train_dias = len(values)-cant_evaluar
                    train = values[:n_train_dias, :]
                    test = values[n_train_dias:, :]
                    
                    
                    # split into input and outputs
                    n_features = len(list(dataset))-1
                    n_obs = n_dias * n_features
                    train_X, train_y = train[:, :n_obs], train[:, -(n_features+1)]
                    test_X, test_y = test[:, :n_obs], test[:, -(n_features+1)]
                    print(train_X.shape, len(train_X), train_y.shape)
                    
                    # reshape input to be 3D [samples, timesteps, features]
                    train_X = train_X.reshape((train_X.shape[0], n_dias, n_features))
                    test_X = test_X.reshape((test_X.shape[0], n_dias, n_features))
                    print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)
                    
                    
                    
                    
                    # design network
                    model = Sequential()
                    model.add(LSTM(50, input_shape=(train_X.shape[1], train_X.shape[2])))
                    model.add(Dense(1))
                    model.compile(loss='mae', optimizer='adam')
                    # fit network
                    history = model.fit(train_X, train_y, nb_epoch=epoca, batch_size=batch, validation_data=(test_X, test_y), verbose=ver, shuffle=False)
                    # plot history
                    #pyplot.plot(history.history['loss'], label='train')
                    #pyplot.plot(history.history['val_loss'], label='test')
                    #pyplot.legend()
                    #pyplot.show()
                    
                    # make a prediction
                    yhat = model.predict(test_X)
                    test_X = test_X.reshape((test_X.shape[0], n_dias*n_features))
                    
                    pyplot.clf()
                    # grafico realidad vs predicho
                    
                    inv_yhat = concatenate((yhat, test_X[:, -(n_features):]), axis=1)
                    inv_yhat = scaler.inverse_transform(inv_yhat)
                    inv_yhat = inv_yhat[:,0]
                    #invert scaling for actual
                    test_y = test_y.reshape((len(test_y), 1))
                    inv_y = concatenate((test_y, test_X[:, -(n_features):]), axis=1)
                    inv_y = scaler.inverse_transform(inv_y)
                    inv_y = inv_y[:,0]
                    
                    
                    
                    #Prediccion de mes
                    pred_ac = (predecir[1:])[:n_obs]
                    pred_ac_reshape= pred_ac.reshape(1,len(pred_ac))
                    pred_ac_reshape_pred = pred_ac_reshape.reshape((pred_ac_reshape.shape[0], n_dias, n_features))
                    pred_modelo = model.predict(pred_ac_reshape_pred)
                    pred_ac_reshape_pred_concat = pred_ac_reshape_pred.reshape((pred_ac_reshape_pred.shape[0], n_dias*n_features))
                    inv_pred_modelo = concatenate((pred_modelo, pred_ac_reshape_pred_concat[:, -(n_features):]), axis=1)
                    inv_pred_modelo_descalado = scaler.inverse_transform(inv_pred_modelo)
                    
                    print(inv_pred_modelo_descalado[0][0])
                    
                    rmse = sqrt(mean_squared_error(inv_y, inv_yhat))

                    
                    pyplot.plot(inv_yhat, label='predicho')
                    pyplot.plot(inv_y, label='realidad')
                    pyplot.legend()
                    pyplot.savefig(path+'salidas//%.3f'%rmse+'-'+str(epoca)+'-'+str(batch)+'-'+str(ver)+'-'+str(dias_entrena)+'_pred_'+str(inv_pred_modelo_descalado[0][0])+'.png')


                    
                    print('Test RMSE: %.3f' % rmse)

                except:
                    pass

                    

