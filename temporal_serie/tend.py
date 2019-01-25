#https://machinelearningmastery.com/time-series-trends-in-python/
from pandas import read_csv
from pandas import datetime
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot
import numpy
 
def parser(x):
	return datetime.strptime('190'+x, '%Y-%m')
 
    
def normalizar(lista):
    lista_normalizada=(lista-min(lista))/(max(lista)-min(lista))
    return lista_normalizada


series = read_csv('/Users/laiunce/Downloads/serie tiempo/shampoo-sales.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
# fit linear model
X = [i for i in range(0, len(series))]
X = numpy.reshape(X, (len(X), 1))
y = series.values
model = LinearRegression()
model.fit(X, y)
# calculate trend
trend = model.predict(X)
# plot trend
pyplot.plot(y)
pyplot.plot(trend)
pyplot.show()
# detrend
detrended = [y[i]-trend[i] for i in range(0, len(series))]
# plot detrended
pyplot.plot(detrended)
pyplot.show()

trend[0]

trend[1]/trend[0]

#Ordenada al origen y pendiente


normalizados = normalizar(y)
X = [i for i in range(0, len(series))]
X = numpy.reshape(X, (len(X), 1))
model = LinearRegression()
model.fit(X, normalizados)
# calculate trend
trend_normalizados = model.predict(X)


X=35
ordenada = trend_normalizados[0]
pendiente = (trend_normalizados[1]-trend_normalizados[0])
Y = ordenada+X*pendiente
Y


trend_normalizados[0]

pyplot.plot(normalizados)
pyplot.plot(trend_normalizados)
pyplot.show()
# detrend
detrended = [normalizados[i]-trend_normalizados[i] for i in range(0, len(series))]
# plot detrended
pyplot.plot(detrended)
pyplot.show()


