#print scaterplott SIN ESTANDARIZAR
plot(data_numeric)

#convierto a matriz
Matrix_Data <-data.matrix(data_numeric)
Matrix_std <- scale(Matrix_Data)

#print scaterplott ESTANDARIZADA
data_numeric_standarizada <-data.frame(Matrix_std)
plot(data_numeric_standarizada)


corrplot(cor(Matrix_std), method="number")


#####
#####
#####



#install.packages("ggfortify")
library(ggfortify)

#tuto
#https://cran.r-project.org/web/packages/ggfortify/vignettes/plot_pca.html


#autoplot(prcomp(data_numeric), data = data, colour = 'op_dol_amount_range',loadings = TRUE)

autoplot(prcomp(data_numeric), data = data, colour = 'op_dol_amount_range')
autoplot(prcomp(data_numeric), data = data, colour = 'sender_antiguedad_range')
autoplot(prcomp(data_numeric), data = data, colour = 'seller_antiguedad_range')
autoplot(prcomp(data_numeric), data = data, colour = 'diff_seller_sender_range')
autoplot(prcomp(data_numeric), data = data, colour = 'sender_puntos_range')
autoplot(prcomp(data_numeric), data = data, colour = 'seller_puntos_range')
autoplot(prcomp(data_numeric), data = data, colour = 'sender_ult_30_dias_range')
autoplot(prcomp(data_numeric), data = data, colour = 'sender_app_ult_30_dias_range')
autoplot(prcomp(data_numeric), data = data, colour = 'seller_ult_30_dias_range')
autoplot(prcomp(data_numeric), data = data, colour = 'seller_sender_ult_30_dias_range')
autoplot(prcomp(data_numeric), data = data, colour = 'item_antiguedad_range')

#op_dol_amount_range
#sender_antiguedad_range
#seller_antiguedad_range
#diff_seller_sender_range
#sender_puntos_range
#seller_puntos_range
#sender_ult_30_dias_range
#sender_app_ult_30_dias_range
#seller_ult_30_dias_range
#seller_sender_ult_30_dias_range
#item_antiguedad_range



set.seed(1)
autoplot(kmeans(data_numeric, 10), data = data_numeric)


library(cluster)
autoplot(clara(data_numeric, 10))



