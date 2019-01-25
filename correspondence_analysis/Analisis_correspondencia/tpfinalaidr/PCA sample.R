#install.packages("devtools")
#install_github('fawda123/ggord')
#install_github("ggbiplot", "vqv")

#tener cuidado con las librarias a veces hay conflicto si cargas una sobre otra bla bal
library(prcomp)
library(ggbiplot)

#library(devtools)
#library(ggord)
#library(corrplot)
#library(ggfortify)
#library(ggplot2)

#data_sample <- data[sample(nrow(data), 3000), ]
#data_sample <- data[sample(nrow(data), 300), ]
data_sample <- data
#acoto universo de variables numericos solamente
data_numeric<- data_sample[1:11]
str(data_numeric)
#autovalores y autovectores

#5. Se mira la correlación entre variables con la función cor() 
cov(data_numeric)


#convierto a matriz
Matrix_Data <-data.matrix(data_numeric)

Matrix_std <- scale(Matrix_Data)


#Obtengo la matriz de covarianzas estandarizada
Matriz_std_cov <- cov(Matrix_std)

cor(Matrix_Data)

#miro correlaciones entre variables
corrplot(cor(Matrix_Data), method="number")

<< plot correlograma >>
  
  #Efectivamente la matriz de covarianzas de las variables estandarizadas es la misma
  # que la matriz de correlacion de las variables originales
  
  princomp(x=Matriz_std_cov, cor=TRUE)

#Los autovalores indica que porcentaje de variabilidad representa el vector correspondiente

#obtengo los autovalores y autovectores
Matrix_comp <-eigen(Matriz_std_cov)

#Autovalores por un lado
Matrix_comp$values

Matrix_comp$values[]

<<print autovalores>>
  
#Autovectores por otro
Matrix_comp$vectors




###

###
#acoto universo de variables numericos solamente

#data_sample <- data[sample(nrow(data), 300), ]
data_sample <- data
#acoto universo de variables numericos solamente
data_numeric<- data_sample[1:11]

Comp <-  data_numeric

Comp.pca <- prcomp(Comp,
                   center = TRUE,
                   scale. = TRUE)

plot(Comp.pca, type = "l")

Comp.pca$rotation

pca_prim5 <- data.frame(Comp.pca$x[,1:5])

#CON 5 VARIABLES PODEMOS EXPLOTAR EL 73 % DEL PROBLEMA
summary(Comp.pca)
<<print autovectores>>

  #Componentes 1 y 2
  #grafico tunning SINNNNN GRUPOS
g <- ggbiplot(Comp.pca, obs.scale = 1, var.scale = 1,choices = c(2,1),alpha = 0.1,ellipse = FALSE, 
                circle = FALSE,var.axes = TRUE )
#g <- g + geom_point(aes(colour=data_sample$op_dol_amount_range), size = 0.0) 
g <- g + theme(legend.direction = 'horizontal',legend.position = 'top')
g <- g + ggtitle("Componentes 1 y 2")
print(g)

#Componentes 1 y 3
#grafico tunning SINNNNN GRUPOS
g <- ggbiplot(Comp.pca, obs.scale = 1, var.scale = 1,choices = c(3,1),alpha = 0.1,ellipse = FALSE, 
              circle = FALSE,var.axes = TRUE )
#g <- g + geom_point(aes(colour=data_sample$op_dol_amount_range), size = 0.0) 
g <- g + theme(legend.direction = 'horizontal',legend.position = 'top')
g <- g + ggtitle("Componentes 1 y 3")
print(g)


#Componentes 2 y 3
#grafico tunning SINNNNN GRUPOS
g <- ggbiplot(Comp.pca, obs.scale = 1, var.scale = 1,choices = c(2,3),alpha = 0.1,ellipse = FALSE, 
              circle = FALSE,var.axes = TRUE )
#g <- g + geom_point(aes(colour=data_sample$op_dol_amount_range), size = 0.0) 
g <- g + theme(legend.direction = 'horizontal',legend.position = 'top')
g <- g + ggtitle("Componentes 2 y 3")
print(g)

####

#grafico tunning CON GRUPOS
g <- ggbiplot(Comp.pca, obs.scale = 1, var.scale = 1,
              choices = 1:2,
              alpha = 0.4,
              groups = data_sample$op_dol_amount_range, ellipse = FALSE, 
              circle = FALSE,var.axes = TRUE )
#g <- g + geom_point(aes(colour=data_sample$op_dol_amount_range), size = 0.0) 
g <- g + theme(legend.direction = 'horizontal',legend.position = 'top')
g <- g + ggtitle("as")
print(g)

####



#op_dol_amount_range
g <- ggbiplot(Comp.pca, obs.scale = 1, var.scale = 1,choices = c(2,1),alpha = 0.1, groups = data_sample$op_dol_amount_range, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=data_sample$op_dol_amount_range), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("op_dol_amount_range");print(g)
#sender_antiguedad_range
g <- ggbiplot(Comp.pca, obs.scale = -10, var.scale = 5,choices = c(2,1), groups = data_sample$sender_antiguedad_range, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=data_sample$sender_antiguedad_range), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("sender_antiguedad_range");print(g)
#seller_antiguedad_range
g <- ggbiplot(Comp.pca, obs.scale = -10, var.scale = 5,choices = c(2,1), groups = data_sample$seller_antiguedad_range, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=data_sample$seller_antiguedad_range), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("seller_antiguedad_range");print(g)
#diff_seller_sender_range
g <- ggbiplot(Comp.pca, obs.scale = -10, var.scale = 5,choices = c(2,1), groups = data_sample$diff_seller_sender_range, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=data_sample$diff_seller_sender_range), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("diff_seller_sender_range");print(g)
#sender_puntos_range
g <- ggbiplot(Comp.pca, obs.scale = -10, var.scale = 5,choices = c(2,1), groups = data_sample$sender_puntos_range, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=data_sample$sender_puntos_range), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("sender_puntos_range");print(g)
#seller_puntos_range
g <- ggbiplot(Comp.pca, obs.scale = -10, var.scale = 5,choices = c(2,1), groups = data_sample$seller_puntos_range, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=data_sample$seller_puntos_range), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("seller_puntos_range");print(g)
#sender_ult_30_dias_range
g <- ggbiplot(Comp.pca, obs.scale = -10, var.scale = 5,choices = c(2,1), groups = data_sample$sender_ult_30_dias_range, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=data_sample$sender_ult_30_dias_range), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("sender_ult_30_dias_range");print(g)
#sender_app_ult_30_dias_range
g <- ggbiplot(Comp.pca, obs.scale = -10, var.scale = 5,choices = c(2,1), groups = data_sample$sender_app_ult_30_dias_range, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=data_sample$sender_app_ult_30_dias_range), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("sender_app_ult_30_dias_range");print(g)
#seller_ult_30_dias_range
g <- ggbiplot(Comp.pca, obs.scale = -10, var.scale = 5,choices = c(2,1), groups = data_sample$seller_ult_30_dias_range, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=data_sample$seller_ult_30_dias_range), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("seller_ult_30_dias_range");print(g)
#seller_sender_ult_30_dias_range
g <- ggbiplot(Comp.pca, obs.scale = -10, var.scale = 5,choices = c(2,1), groups = data_sample$seller_sender_ult_30_dias_range, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=data_sample$seller_sender_ult_30_dias_range), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("seller_sender_ult_30_dias_range");print(g)
#item_antiguedad_range
g <- ggbiplot(Comp.pca, obs.scale = -10, var.scale = 5,choices = c(2,1), groups = data_sample$item_antiguedad_range, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=data_sample$item_antiguedad_range), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("item_antiguedad_range");print(g)


