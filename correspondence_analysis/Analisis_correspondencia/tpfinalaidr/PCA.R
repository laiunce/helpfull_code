
library(princomp)

install.packages("prcomp")

#Funcion imprimir graficos
pcaCharts <- function(x) {
  x.var <- x$sdev ^ 2
  x.pvar <- x.var/sum(x.var)
  print("proportions of variance:")
  print(x.pvar)
  par(mfrow=c(2,2))
  plot(x.pvar,xlab="Principal component", ylab="Proportion of variance explained", ylim=c(0,1), type='b')
  plot(cumsum(x.pvar),xlab="Principal component", ylab="Cumulative Proportion of variance explained", ylim=c(0,1), type='b')
  screeplot(x)
  screeplot(x,type="l")
  par(mfrow=c(1,1))
}

#convierto hora a factor
data$hora<-as.factor(data$hora)

#acoto universo de variables numericos solamente
data_numeric<- data[1:12]
data_numeric$hora <- NULL

#print scaterplott SIN ESTANDARIZAR
plot(data_numeric)


#5. Se mira la correlación entre variables con la función cor() 
cov(data_numeric)


#convierto a matriz
Matrix_Data <-data.matrix(data_numeric)


Matrix_std <- scale(Matrix_Data)

#print scaterplott ESTANDARIZADA
data_numeric_standarizada <-data.frame(Matrix_std)
plot(data_numeric_standarizada)


#Obtengo la matriz de covarianzas estandarizada
Matriz_std_cov <- cov(Matrix_std)

cor(Matrix_Data)

#Efectivamente la matriz de covarianzas de las variables estandarizadas es la misma
# que la matriz de correlacion de las variables originales

princomp(x=Matriz_std_cov, cor=TRUE)

#Los autovalores indica que porcentaje de variabilidad representa el vector correspondiente


#obtengo los autovalores y autovectores
Matrix_comp <-eigen(Matriz_std_cov)

#Autovalores por un lado
Matrix_comp$values

#Autovectores por otro
Matrix_comp$vectors


#Directo con el Dataset analisis componentes y vectores

# guia http://www.r-bloggers.com/computing-and-visualizing-pca-in-r/
#notar que la parte del grafico se utilizo otra libreria, ggplot2


Comp <-  data_numeric

Comp.pca <- prcomp(Comp,
                   center = TRUE,
                   scale. = TRUE)

plot(Comp.pca, type = "l")

print(Comp.pca)


# Con el resumen se pueden ver las proporciones acumuladas

summary(Comp.pca)


biplot(Comp.pca,choices = 1:2, scale = 1, pc.biplot = FALSE)


#install.packages("devtools")
#install_github('fawda123/ggord')
#install_github("ggbiplot", "vqv")

library(devtools)
library(ggord)
library(ggbiplot)

#grafico tunning
g <- ggbiplot(Comp.pca, obs.scale = 10, var.scale = 5,choices = c(2,1),
              groups = data$hora, ellipse = TRUE, 
              circle = TRUE,var.axes = TRUE )
g <- g + geom_point(aes(colour=data$hora), size = 0.0) 
g <- g + theme(legend.direction = 'horizontal',legend.position = 'top')
print(g)





#se pueden ver los graficos de distintas componentes
ggord(Comp.pca,data$op_dol_amount_range, size = 1, axes = c("1", "2"),)

ggord(Comp.pca,data$op_dol_amount_range, size = 1, axes = c("1", "3"))

ggord(Comp.pca,data$op_dol_amount_range, size = 1, axes = c("1", "4"))

