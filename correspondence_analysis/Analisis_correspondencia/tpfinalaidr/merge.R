library(cluster) 
library(prcomp)
library(devtools)
library(ggord)
library(ggbiplot)
library(corrplot)
library(ggfortify)
library(ggplot2)

library(factoextra);
library(cluster);
library(amap);
library(vegan);

multiplot <- function(..., plotlist=NULL, file, cols=1, layout=NULL) {
  library(grid)
  
  # Make a list from the ... arguments and plotlist
  plots <- c(list(...), plotlist)
  
  numPlots = length(plots)
  
  # If layout is NULL, then use 'cols' to determine layout
  if (is.null(layout)) {
    # Make the panel
    # ncol: Number of columns of plots
    # nrow: Number of rows needed, calculated from # of cols
    layout <- matrix(seq(1, cols * ceiling(numPlots/cols)),
                     ncol = cols, nrow = ceiling(numPlots/cols))
  }
  
  if (numPlots==1) {
    print(plots[[1]])
    
  } else {
    # Set up the page
    grid.newpage()
    pushViewport(viewport(layout = grid.layout(nrow(layout), ncol(layout))))
    
    # Make each plot, in the correct location
    for (i in 1:numPlots) {
      # Get the i,j matrix positions of the regions that contain this subplot
      matchidx <- as.data.frame(which(layout == i, arr.ind = TRUE))
      
      print(plots[[i]], vp = viewport(layout.pos.row = matchidx$row,
                                      layout.pos.col = matchidx$col))
    }
  }
}

#data_sample <- data[sample(nrow(data), 300), ]
data_sample <- data
#acoto universo de variables numericos solamente
data_numeric<- data_sample[1:11]
#componentes principales
Comp.pca <- prcomp(data_numeric,
                   center = TRUE,
                   scale. = TRUE)

autovectores<-data.frame(Comp.pca$rotation)
Comp_pca<-data.frame(Comp.pca$x)
data_sample <- data.frame(data_sample, Comp_pca)
#Kmeans


mydata<-data_numeric
#cluster con euclidea
gower_dist <- vegdist(data_numeric, method="euclidea")
gower_mat <- as.matrix(gower_dist)
fit <- kmeans(gower_mat, 5)

# get cluster means 
centroides<-data.frame(aggregate(data_numeric,by=list(fit$cluster),FUN=mean))
#hago bines con los datos de centroides

centroides$op_dol_amount_range<-findInterval(centroides$op_dol_amount, c(50,100,150,250,350,500,1200))

centroides$op_dol_amount_range<-
  ifelse(centroides$op_dol_amount_range==0,'<50',
         ifelse(centroides$op_dol_amount_range==1,'50-100',
                ifelse(centroides$op_dol_amount_range==2,'100-150',
                       ifelse(centroides$op_dol_amount_range==3,'150-250',
                              ifelse(centroides$op_dol_amount_range==4,'250-350',
                                     ifelse(centroides$op_dol_amount_range==5,'350-500',
                                            ifelse(centroides$op_dol_amount_range==6,'500-1200','>1200')
                                     )
                              )
                       )
                )
         )
  )


############################################################################################################


centroides$sender_antiguedad_range<-findInterval(centroides$sender_antiguedad, c(1,4,30,150,420,1000))

centroides$sender_antiguedad_range<-
  ifelse(centroides$sender_antiguedad_range==0,'<1',
         ifelse(centroides$sender_antiguedad_range==1,'1-4',
                ifelse(centroides$sender_antiguedad_range==2,'4-30',
                       ifelse(centroides$sender_antiguedad_range==3,'30-150',
                              ifelse(centroides$sender_antiguedad_range==4,'150-420',
                                     ifelse(centroides$sender_antiguedad_range==5,'420-1000','>1000')
                              )
                       )
                )
         )
  )

############################################################################################################

centroides$seller_antiguedad_range<-findInterval(centroides$seller_antiguedad, c(50000,120000))

centroides$seller_antiguedad_range<-
  ifelse(centroides$seller_antiguedad_range==0,'<50000',
         ifelse(centroides$seller_antiguedad_range==1,'50000-100000','>100000')
  )

############################################################################################################

centroides$diff_seller_sender_range<-findInterval(centroides$diff_seller_sender, c(-25000,-4000,18000,50000,100000))

centroides$diff_seller_sender_range<-
  ifelse(centroides$diff_seller_sender_range==0,'<-25000',
         ifelse(centroides$diff_seller_sender_range==1,'-25000--4000',
                ifelse(centroides$diff_seller_sender_range==2,'-4000-18000',
                       ifelse(centroides$diff_seller_sender_range==3,'18000-50000',
                              ifelse(centroides$diff_seller_sender_range==4,'50000-100000','>100000')
                       )
                )
         )
  )


############################################################################################################


centroides$sender_puntos_range<-findInterval(centroides$sender_puntos, c(10,50,100))

centroides$sender_puntos_range<-
  ifelse(centroides$sender_puntos_range==0,'<10',
         ifelse(centroides$sender_puntos_range==1,'10-50',
                ifelse(centroides$sender_puntos_range==2,'50-100','>100')
         )
  )

############################################################################################################  

centroides$seller_puntos_range<-findInterval(centroides$seller_puntos, c(3,26,100,200,400,1000,1500))

centroides$seller_puntos_range<-
  ifelse(centroides$seller_puntos_range==0,'<3',
         ifelse(centroides$seller_puntos_range==1,'3-26',
                ifelse(centroides$seller_puntos_range==2,'26-100',
                       ifelse(centroides$seller_puntos_range==3,'100-200',
                              ifelse(centroides$seller_puntos_range==4,'200-400',
                                     ifelse(centroides$seller_puntos_range==5,'400-1000',
                                            ifelse(centroides$seller_puntos_range==6,'1000-1500','>1500')
                                     )
                              )
                       )
                )
         )
  )

############################################################################################################  

centroides$sender_ult_30_dias_range<-findInterval(centroides$sender_ult_30_dias, c(1,50,150,300,500))

centroides$sender_ult_30_dias_range<-
  ifelse(centroides$sender_ult_30_dias_range==0,'<1',
         ifelse(centroides$sender_ult_30_dias_range==1,'1-50',
                ifelse(centroides$sender_ult_30_dias_range==2,'50-150',
                       ifelse(centroides$sender_ult_30_dias_range==3,'150-300',
                              ifelse(centroides$sender_ult_30_dias_range==4,'300-500','>500')
                       )
                )
         )
  )

############################################################################################################

centroides$sender_app_ult_30_dias_range<-findInterval(centroides$sender_app_ult_30_dias, c(5))

centroides$sender_app_ult_30_dias_range<-
  ifelse(centroides$sender_app_ult_30_dias_range==0,'<5','>5')


############################################################################################################

centroides$seller_ult_30_dias_range<-findInterval(centroides$seller_ult_30_dias, c(3000,10000))

centroides$seller_ult_30_dias_range<-
  ifelse(centroides$seller_ult_30_dias_range==0,'<3000',
         ifelse(centroides$seller_ult_30_dias_range==1,'3000-10000','>10000')
  )

############################################################################################################

centroides$seller_sender_ult_30_dias_range<-findInterval(centroides$seller_sender_ult_30_dias, c(100,200,400,1500))

centroides$seller_sender_ult_30_dias_range<-
  ifelse(centroides$seller_sender_ult_30_dias_range==0,'<100',
         ifelse(centroides$seller_sender_ult_30_dias_range==1,'100-200',
                ifelse(centroides$seller_sender_ult_30_dias_range==2,'200-400',
                       ifelse(centroides$seller_sender_ult_30_dias_range==3,'400-1500','>1500')
                )
         )
  )

############################################################################################################  

centroides$item_antiguedad_range<-findInterval(centroides$item_antiguedad, c(200,4500))

centroides$item_antiguedad_range<-
  ifelse(centroides$item_antiguedad_range==0,'<200',
         ifelse(centroides$item_antiguedad_range==1,'200-4500','>4500')
  )



############################################################################################################


#con los centroides multiplicos los autovectores para luego graficarlos

#tst

#veo el autovector de PC1
PC1<-data.frame(data.frame(Comp.pca$rotation)$PC1)
#datos a corroborar



Matrix_Data <-data.matrix(data_numeric)
Matrix_std <- scale(Matrix_Data)

Matrix_std[1:3,1:11]

data_numeric[1,1:11]
Matrix_std[1,1:11] %*% as.matrix(autovectores)
data_sample[1,"PC2"]




#obtengo dataframe con medias y desvios standars para calcular los centroides 
mean_sd<-data.frame('op_dol_amount', mean(data_numeric$op_dol_amount),sd(data_numeric$op_dol_amount))
colnames(mean_sd) <- c('var','mean','sd')
mean_sd<-data.frame('op_dol_amount', mean(data_numeric$op_dol_amount),sd(data_numeric$op_dol_amount))
colnames(mean_sd) <- c('var','mean','sd')
tem <- data.frame('sender_antiguedad', mean(data_numeric$sender_antiguedad),sd(data_numeric$sender_antiguedad))
colnames(tem) <- c('var','mean','sd')
mean_sd<-rbind(mean_sd,tem)
tem <- data.frame('seller_antiguedad', mean(data_numeric$seller_antiguedad),sd(data_numeric$seller_antiguedad))
colnames(tem) <- c('var','mean','sd')
mean_sd<-rbind(mean_sd,tem)
tem <- data.frame('diff_seller_sender', mean(data_numeric$diff_seller_sender),sd(data_numeric$diff_seller_sender))
colnames(tem) <- c('var','mean','sd')
mean_sd<-rbind(mean_sd,tem)
tem <- data.frame('sender_puntos', mean(data_numeric$sender_puntos),sd(data_numeric$sender_puntos))
colnames(tem) <- c('var','mean','sd')
mean_sd<-rbind(mean_sd,tem)
tem <- data.frame('seller_puntos', mean(data_numeric$seller_puntos),sd(data_numeric$seller_puntos))
colnames(tem) <- c('var','mean','sd')
mean_sd<-rbind(mean_sd,tem)
tem <- data.frame('sender_ult_30_dias', mean(data_numeric$sender_ult_30_dias),sd(data_numeric$sender_ult_30_dias))
colnames(tem) <- c('var','mean','sd')
mean_sd<-rbind(mean_sd,tem)
tem <- data.frame('sender_app_ult_30_dias', mean(data_numeric$sender_app_ult_30_dias),sd(data_numeric$sender_app_ult_30_dias))
colnames(tem) <- c('var','mean','sd')
mean_sd<-rbind(mean_sd,tem)
tem <- data.frame('seller_ult_30_dias', mean(data_numeric$seller_ult_30_dias),sd(data_numeric$seller_ult_30_dias))
colnames(tem) <- c('var','mean','sd')
mean_sd<-rbind(mean_sd,tem)
tem <- data.frame('seller_sender_ult_30_dias', mean(data_numeric$seller_sender_ult_30_dias),sd(data_numeric$seller_sender_ult_30_dias))
colnames(tem) <- c('var','mean','sd')
mean_sd<-rbind(mean_sd,tem)
tem <- data.frame('item_antiguedad', mean(data_numeric$item_antiguedad),sd(data_numeric$item_antiguedad))
colnames(tem) <- c('var','mean','sd')
mean_sd<-rbind(mean_sd,tem)
#

options(digits = 8)
matrix_centroides <-centroides
matrix_centroides$Group.1<-NULL

(matrix_centroides[1]-mean_sd[1,2])/mean_sd[1,3]


matrix_centroides_standar <- 
data.frame(
(matrix_centroides[1]-mean_sd[1,2])/mean_sd[1,3],
(matrix_centroides[2]-mean_sd[2,2])/mean_sd[2,3],
(matrix_centroides[3]-mean_sd[3,2])/mean_sd[3,3],
(matrix_centroides[4]-mean_sd[4,2])/mean_sd[4,3],
(matrix_centroides[5]-mean_sd[5,2])/mean_sd[5,3],
(matrix_centroides[6]-mean_sd[6,2])/mean_sd[6,3],
(matrix_centroides[7]-mean_sd[7,2])/mean_sd[7,3],
(matrix_centroides[8]-mean_sd[8,2])/mean_sd[8,3],
(matrix_centroides[9]-mean_sd[9,2])/mean_sd[9,3],
(matrix_centroides[10]-mean_sd[10,2])/mean_sd[10,3],
(matrix_centroides[11]-mean_sd[11,2])/mean_sd[11,3]
)
colnames(matrix_centroides_standar)<-c('op_dol_amount','sender_antiguedad','seller_antiguedad','diff_seller_sender','sender_puntos','seller_puntos','sender_ult_30_dias','sender_app_ult_30_dias','seller_ult_30_dias','seller_sender_ult_30_dias','item_antiguedad')

#una vez teninedo el control ok vamos a multiplicar los centroides

pca_centroides <- data.frame(as.matrix(matrix_centroides_standar)%*% as.matrix(autovectores))

centroides_pca<-data.frame(centroides,pca_centroides)

centroides_pca$Group.1<-as.factor(centroides_pca$Group.1)
gs1 <- ggplot(centroides_pca, aes(x=PC1, y=PC2, color = centroides_pca$Group.1)) + geom_point()
gs2 <- ggplot(data_sample, aes(x=PC1, y=PC2, color = data_sample$fit.cluster)) + geom_point()

multiplot(gs1,gs2, cols=2)

############################################################################################################

# append cluster assignment
data_sample <- data.frame(data_sample, fit$cluster)
data_sample$fit.cluster <- as.factor(data_sample$fit.cluster)



g1 <- ggplot(data_sample, aes(x=PC1, y=PC2, color = data_sample$fit.cluster)) + geom_point()
g2 <- ggplot(data_sample, aes(x=PC1, y=PC3, color = data_sample$fit.cluster)) + geom_point()
g3 <- ggplot(data_sample, aes(x=PC1, y=PC4, color = data_sample$fit.cluster)) + geom_point()
g4 <- ggplot(data_sample, aes(x=PC1, y=PC5, color = data_sample$fit.cluster)) + geom_point()
g5 <- ggplot(data_sample, aes(x=PC2, y=PC3, color = data_sample$fit.cluster)) + geom_point()
g6 <- ggplot(data_sample, aes(x=PC2, y=PC4, color = data_sample$fit.cluster)) + geom_point()
g7 <- ggplot(data_sample, aes(x=PC2, y=PC5, color = data_sample$fit.cluster)) + geom_point()
g8 <- ggplot(data_sample, aes(x=PC3, y=PC4, color = data_sample$fit.cluster)) + geom_point()
g9 <- ggplot(data_sample, aes(x=PC3, y=PC5, color = data_sample$fit.cluster)) + geom_point()
g10 <- ggplot(data_sample, aes(x=PC4, y=PC5, color = data_sample$fit.cluster)) + geom_point()

multiplot(g1,g2,g3,g4,g5,g6,g7,g8,g9,g10, cols=2)
##

#grafico pca separando por profile

data_sample$PC1
g1 <- ggplot(data_sample, aes(x=PC1, y=PC2, color = data$profile_id)) + geom_point()
g2 <- ggplot(data_sample, aes(x=PC1, y=PC3, color = data$profile_id)) + geom_point()
g3 <- ggplot(data_sample, aes(x=PC1, y=PC4, color = data$profile_id)) + geom_point()
g4 <- ggplot(data_sample, aes(x=PC1, y=PC5, color = data$profile_id)) + geom_point()
g5 <- ggplot(data_sample, aes(x=PC2, y=PC3, color = data$profile_id)) + geom_point()
g6 <- ggplot(data_sample, aes(x=PC2, y=PC4, color = data$profile_id)) + geom_point()
g7 <- ggplot(data_sample, aes(x=PC2, y=PC5, color = data$profile_id)) + geom_point()
g8 <- ggplot(data_sample, aes(x=PC3, y=PC4, color = data$profile_id)) + geom_point()
g9 <- ggplot(data_sample, aes(x=PC3, y=PC5, color = data$profile_id)) + geom_point()
g10 <- ggplot(data_sample, aes(x=PC4, y=PC5, color = data$profile_id)) + geom_point()

multiplot(g1,g2,g3,g4,g5,g6,g7,g8,g9,g10, cols=2)

#grafico pca separando por profile



data_sample$PC1
g1 <- ggplot(data_sample, aes(x=PC1, y=PC2, color = data$provider_id)) + geom_point()
g2 <- ggplot(data_sample, aes(x=PC1, y=PC3, color = data$provider_id)) + geom_point()
g3 <- ggplot(data_sample, aes(x=PC1, y=PC4, color = data$provider_id)) + geom_point()
g4 <- ggplot(data_sample, aes(x=PC1, y=PC5, color = data$provider_id)) + geom_point()
g5 <- ggplot(data_sample, aes(x=PC2, y=PC3, color = data$provider_id)) + geom_point()
g6 <- ggplot(data_sample, aes(x=PC2, y=PC4, color = data$provider_id)) + geom_point()
g7 <- ggplot(data_sample, aes(x=PC2, y=PC5, color = data$provider_id)) + geom_point()
g8 <- ggplot(data_sample, aes(x=PC3, y=PC4, color = data$provider_id)) + geom_point()
g9 <- ggplot(data_sample, aes(x=PC3, y=PC5, color = data$provider_id)) + geom_point()
g10 <- ggplot(data_sample, aes(x=PC4, y=PC5, color = data$provider_id)) + geom_point()

multiplot(g1,g2,g3,g4,g5,g6,g7,g8,g9,g10, cols=2)


#grafico pca separando por client_id

data_sample$PC1
g1 <- ggplot(data_sample, aes(x=PC1, y=PC2, color = data$client_id)) + geom_point()
g2 <- ggplot(data_sample, aes(x=PC1, y=PC3, color = data$client_id)) + geom_point()
g3 <- ggplot(data_sample, aes(x=PC1, y=PC4, color = data$client_id)) + geom_point()
g4 <- ggplot(data_sample, aes(x=PC1, y=PC5, color = data$client_id)) + geom_point()
g5 <- ggplot(data_sample, aes(x=PC2, y=PC3, color = data$client_id)) + geom_point()
g6 <- ggplot(data_sample, aes(x=PC2, y=PC4, color = data$client_id)) + geom_point()
g7 <- ggplot(data_sample, aes(x=PC2, y=PC5, color = data$client_id)) + geom_point()
g8 <- ggplot(data_sample, aes(x=PC3, y=PC4, color = data$client_id)) + geom_point()
g9 <- ggplot(data_sample, aes(x=PC3, y=PC5, color = data$client_id)) + geom_point()
g10 <- ggplot(data_sample, aes(x=PC4, y=PC5, color = data$client_id)) + geom_point()

multiplot(g1,g2,g3,g4,g5,g6,g7,g8,g9,g10, cols=2)


#grafico pca separando por sistema_operativo_mobile


g1 <- ggplot(data_sample, aes(x=PC1, y=PC2, color = data$sistema_operativo_mobile)) + geom_point()
g2 <- ggplot(data_sample, aes(x=PC1, y=PC3, color = data$sistema_operativo_mobile)) + geom_point()
g3 <- ggplot(data_sample, aes(x=PC1, y=PC4, color = data$sistema_operativo_mobile)) + geom_point()
g4 <- ggplot(data_sample, aes(x=PC1, y=PC5, color = data$sistema_operativo_mobile)) + geom_point()
g5 <- ggplot(data_sample, aes(x=PC2, y=PC3, color = data$sistema_operativo_mobile)) + geom_point()
g6 <- ggplot(data_sample, aes(x=PC2, y=PC4, color = data$sistema_operativo_mobile)) + geom_point()
g7 <- ggplot(data_sample, aes(x=PC2, y=PC5, color = data$sistema_operativo_mobile)) + geom_point()
g8 <- ggplot(data_sample, aes(x=PC3, y=PC4, color = data$sistema_operativo_mobile)) + geom_point()
g9 <- ggplot(data_sample, aes(x=PC3, y=PC5, color = data$sistema_operativo_mobile)) + geom_point()
g10 <- ggplot(data_sample, aes(x=PC4, y=PC5, color = data$sistema_operativo_mobile)) + geom_point()

multiplot(g1,g2,g3,g4,g5,g6,g7,g8,g9,g10, cols=2)

#grafico pca separando por has_approved_payment_tc

g1 <- ggplot(data_sample, aes(x=PC1, y=PC2, color = data$has_approved_payment_tc)) + geom_point()
g2 <- ggplot(data_sample, aes(x=PC1, y=PC3, color = data$has_approved_payment_tc)) + geom_point()
g3 <- ggplot(data_sample, aes(x=PC1, y=PC4, color = data$has_approved_payment_tc)) + geom_point()
g4 <- ggplot(data_sample, aes(x=PC1, y=PC5, color = data$has_approved_payment_tc)) + geom_point()
g5 <- ggplot(data_sample, aes(x=PC2, y=PC3, color = data$has_approved_payment_tc)) + geom_point()
g6 <- ggplot(data_sample, aes(x=PC2, y=PC4, color = data$has_approved_payment_tc)) + geom_point()
g7 <- ggplot(data_sample, aes(x=PC2, y=PC5, color = data$has_approved_payment_tc)) + geom_point()
g8 <- ggplot(data_sample, aes(x=PC3, y=PC4, color = data$has_approved_payment_tc)) + geom_point()
g9 <- ggplot(data_sample, aes(x=PC3, y=PC5, color = data$has_approved_payment_tc)) + geom_point()
g10 <- ggplot(data_sample, aes(x=PC4, y=PC5, color = data$has_approved_payment_tc)) + geom_point()

multiplot(g1,g2,g3,g4,g5,g6,g7,g8,g9,g10, cols=2)
#cluster con todas las variables


#imprimo solo del grupo 3

solo3 <- data_sample[data_sample$fit.cluster==3,]
solo3_data<-data[row.names(solo3),]

ggplot(solo3, aes(x=PC1, y=PC2)) + geom_point()

ggplot(solo3, aes(x=PC1, y=PC2, color = solo3_data$sistema_operativo_mobile)) + geom_point()

ggplot(solo3, aes(x=PC1, y=PC2, color = solo3_data$op_dol_amount_range)) + geom_point()

ggplot(solo3, aes(x=PC1, y=PC2, color = solo3_data$seller_puntos_range)) + geom_point()



g1 <-ggplot(solo3_data, aes(x=op_dol_amount_range, y=..count..)) + geom_bar(aes(fill = op_dol_amount_range,label = ..count..), position = "dodge")
g2 <-ggplot(solo3_data, aes(x=sender_antiguedad_range, y=..count..)) + geom_bar(aes(fill = sender_antiguedad_range,label = ..count..), position = "dodge")
g3 <-ggplot(solo3_data, aes(x=seller_antiguedad_range, y=..count..)) + geom_bar(aes(fill = seller_antiguedad_range,label = ..count..), position = "dodge")
g4 <-ggplot(solo3_data, aes(x=diff_seller_sender_range, y=..count..)) + geom_bar(aes(fill = diff_seller_sender_range,label = ..count..), position = "dodge")
g5 <-ggplot(solo3_data, aes(x=sender_puntos_range, y=..count..)) + geom_bar(aes(fill = sender_puntos_range,label = ..count..), position = "dodge")
g6 <-ggplot(solo3_data, aes(x=seller_puntos_range, y=..count..)) + geom_bar(aes(fill = seller_puntos_range,label = ..count..), position = "dodge")

multiplot(g1,g2,g3,g4,g5,g6, cols=2)

g1 <-ggplot(solo3_data, aes(x=sender_ult_30_dias_range, y=..count..)) + geom_bar(aes(fill = sender_ult_30_dias_range,label = ..count..), position = "dodge")
g2 <-ggplot(solo3_data, aes(x=sender_app_ult_30_dias_range, y=..count..)) + geom_bar(aes(fill = sender_app_ult_30_dias_range,label = ..count..), position = "dodge")
g3 <-ggplot(solo3_data, aes(x=seller_ult_30_dias_range, y=..count..)) + geom_bar(aes(fill = seller_ult_30_dias_range,label = ..count..), position = "dodge")
g4 <-ggplot(solo3_data, aes(x=seller_sender_ult_30_dias_range, y=..count..)) + geom_bar(aes(fill = seller_sender_ult_30_dias_range,label = ..count..), position = "dodge")
g5 <-ggplot(solo3_data, aes(x=item_antiguedad_range, y=..count..)) + geom_bar(aes(fill = item_antiguedad_range,label = ..count..), position = "dodge")
g6 <-ggplot(solo3_data, aes(x=sistema_operativo_mobile, y=..count..)) + geom_bar(aes(fill = sistema_operativo_mobile,label = ..count..), position = "dodge")

multiplot(g1,g2,g3,g4,g5,g6, cols=2)

g1 <-ggplot(solo3_data, aes(x=profile_id, y=..count..)) + geom_bar(aes(fill = profile_id,label = ..count..), position = "dodge")
g2 <-ggplot(solo3_data, aes(x=provider_id, y=..count..)) + geom_bar(aes(fill = provider_id,label = ..count..), position = "dodge")
g3 <-ggplot(solo3_data, aes(x=client_id, y=..count..)) + geom_bar(aes(fill = client_id,label = ..count..), position = "dodge")
g4 <-ggplot(solo3_data, aes(x=has_approved_device, y=..count..)) + geom_bar(aes(fill = has_approved_device,label = ..count..), position = "dodge")
g5 <-ggplot(solo3_data, aes(x=has_approved_payment_document, y=..count..)) + geom_bar(aes(fill = has_approved_payment_document,label = ..count..), position = "dodge")
g6 <-ggplot(solo3_data, aes(x=has_approved_payment_user, y=..count..)) + geom_bar(aes(fill = has_approved_payment_user,label = ..count..), position = "dodge")

multiplot(g1,g2,g3,g4,g5,g6, cols=2)

ggplot(solo3_data, aes(x=has_approved_payment_tc, y=..count..)) + geom_bar(aes(fill = has_approved_payment_tc,label = ..count..), position = "dodge")
ggplot(solo3_data, aes(x=sender_antiguedad_range, y=..count..)) + geom_bar(aes(fill = sender_antiguedad_range,label = ..count..), position = "dodge")

multiplot(g1,g2, cols=2)

#####

#imprimo analisis con fit cluster TODOS LOS CLUSTERS


library(FactoMineR)
library(ca)


#saco nombre de variables

#data_cat <- data_categoricas[,c("sistema_operativo_mobile","profile_id","provider_id","client_id","has_approved_device","has_approved_payment_document","has_approved_payment_user","has_approved_payment_tc")]

str(data_sample)
str(data)

data_cat <- data[,c("op_dol_amount_range","sender_antiguedad_range","seller_antiguedad_range","diff_seller_sender_range","sender_puntos_range","seller_puntos_range","sender_ult_30_dias_range","sender_app_ult_30_dias_range","seller_ult_30_dias_range","seller_sender_ult_30_dias_range","item_antiguedad_range","sistema_operativo_mobile","profile_id","provider_id","client_id","has_approved_device","has_approved_payment_document","has_approved_payment_user","has_approved_payment_tc")]
data_cat$cluster <-data_sample$fit.cluster

"op_dol_amount_range"
"sender_antiguedad_range"
"seller_antiguedad_range"
"diff_seller_sender_range"
"sender_puntos_range"
"seller_puntos_range"
"sender_ult_30_dias_range"
"sender_app_ult_30_dias_range"
"seller_ult_30_dias_range"
"seller_sender_ult_30_dias_range"
"item_antiguedad_range"
"sistema_operativo_mobile"
"profile_id"
"provider_id"
"client_id"
"has_approved_device"
"has_approved_payment_document"
"has_approved_payment_user"
"has_approved_payment_tc"
"cluster"


data_cat <- data_cat[,c("op_dol_amount_range","sender_antiguedad_range","seller_antiguedad_range","sender_puntos_range","seller_puntos_range","sistema_operativo_mobile","cluster")]

#colnames(data_cat)<- c("hap_device","hap_pay_doc","hap_pay_user","hap_pay_tc")
str(data_cat)

cats_cat = apply(data_cat, 2, function(x) nlevels(as.factor(x)))
cats_cat

mca1_cat = MCA(data_cat, graph = FALSE)

mca1_cat$eig

mca1_cat_vars_df = data.frame(mca1_cat$var$coord, Variable = rep(names(cats_cat), 
                                                                 cats_cat))
mca1_cat_obs_df = data.frame(mca1_cat$ind$coord)



# plot of variable categories
ggplot(data = mca1_cat_vars_df, aes(x = Dim.1, y = Dim.2, label = rownames(mca1_cat_vars_df))) + 
  geom_hline(yintercept = 0, colour = "gray70") + geom_vline(xintercept = 0, 
                                                             colour = "gray70") + geom_text(aes(colour = Variable)) + ggtitle("MCA plot of variables using R package FactoMineR")




# MCA plot of observations and categories
ggplot(data = mca1_cat_obs_df, aes(x = Dim.1, y = Dim.2)) + geom_hline(yintercept = 0, 
                                                                       colour = "gray70") + geom_vline(xintercept = 0, colour = "gray70") + geom_point(colour = "gray50", 
                                                                                                                                                       alpha = 0.7) + geom_density2d(colour = "gray80") + geom_text(data = mca1_cat_vars_df, 
                                                                                                                                                                                                                    aes(x = Dim.1, y = Dim.2, label = rownames(mca1_cat_vars_df), colour = Variable)) + 
  ggtitle("MCA plot of variables using R package FactoMineR") + scale_colour_discrete(name = "Variable")





#####

#imprimo analisis con fit cluster SOLO UN CLUSTER CONTRA TODOS LOS OTROS
#imprimo analisis con fit cluster SOLO UN CLUSTER CONTRA TODOS LOS OTROS
#imprimo analisis con fit cluster SOLO UN CLUSTER CONTRA TODOS LOS OTROS
#imprimo analisis con fit cluster SOLO UN CLUSTER CONTRA TODOS LOS OTROS


library(FactoMineR)
library(ca)


#saco nombre de variables

#data_cat <- data_categoricas[,c("sistema_operativo_mobile","profile_id","provider_id","client_id","has_approved_device","has_approved_payment_document","has_approved_payment_user","has_approved_payment_tc")]

str(data_sample)
str(data)

data_cat <- data[,c("op_dol_amount_range","sender_antiguedad_range","seller_antiguedad_range","diff_seller_sender_range","sender_puntos_range","seller_puntos_range","sender_ult_30_dias_range","sender_app_ult_30_dias_range","seller_ult_30_dias_range","seller_sender_ult_30_dias_range","item_antiguedad_range","sistema_operativo_mobile","profile_id","provider_id","client_id","has_approved_device","has_approved_payment_document","has_approved_payment_user","has_approved_payment_tc")]
data_cat$cluster <-data_sample$fit.cluster

str(data_cat)
data_cat$cluster <- ifelse(as.character(data_cat$cluster) == '1',1,0)
data_cat$cluster <- as.factor(data_cat$cluster)
table(data_cat$cluster)

"op_dol_amount_range"
"sender_antiguedad_range"
"seller_antiguedad_range"
"diff_seller_sender_range"
"sender_puntos_range"
"seller_puntos_range"
"sender_ult_30_dias_range"
"sender_app_ult_30_dias_range"
"seller_ult_30_dias_range"
"seller_sender_ult_30_dias_range"
"item_antiguedad_range"
"sistema_operativo_mobile"
"profile_id"
"provider_id"
"client_id"
"has_approved_device"
"has_approved_payment_document"
"has_approved_payment_user"
"has_approved_payment_tc"
"cluster"


data_cat <- data_cat[,c("op_dol_amount_range","sender_antiguedad_range","seller_antiguedad_range","sender_puntos_range","seller_puntos_range","sistema_operativo_mobile","cluster")]

#colnames(data_cat)<- c("hap_device","hap_pay_doc","hap_pay_user","hap_pay_tc")
str(data_cat)

cats_cat = apply(data_cat, 2, function(x) nlevels(as.factor(x)))
cats_cat

mca1_cat = MCA(data_cat, graph = FALSE)

mca1_cat$eig

mca1_cat_vars_df = data.frame(mca1_cat$var$coord, Variable = rep(names(cats_cat), 
                                                                 cats_cat))
mca1_cat_obs_df = data.frame(mca1_cat$ind$coord)



# plot of variable categories
ggplot(data = mca1_cat_vars_df, aes(x = Dim.1, y = Dim.2, label = rownames(mca1_cat_vars_df))) + 
  geom_hline(yintercept = 0, colour = "gray70") + geom_vline(xintercept = 0, 
                                                             colour = "gray70") + geom_text(aes(colour = Variable)) + ggtitle("MCA plot of variables using R package FactoMineR")




# MCA plot of observations and categories
ggplot(data = mca1_cat_obs_df, aes(x = Dim.1, y = Dim.2)) + geom_hline(yintercept = 0, 
                                                                       colour = "gray70") + geom_vline(xintercept = 0, colour = "gray70") + geom_point(colour = "gray50", 
                                                                                                                                                       alpha = 0.7) + geom_density2d(colour = "gray80") + geom_text(data = mca1_cat_vars_df, 
                                                                                                                                                                                                                    aes(x = Dim.1, y = Dim.2, label = rownames(mca1_cat_vars_df), colour = Variable)) + 
  ggtitle("MCA plot of variables using R package FactoMineR") + scale_colour_discrete(name = "Variable")






library(FactoMineR)
library(ca)


#saco nombre de variables

#data_cat <- data_categoricas[,c("sistema_operativo_mobile","profile_id","provider_id","client_id","has_approved_device","has_approved_payment_document","has_approved_payment_user","has_approved_payment_tc")]

str(data_sample)
str(data)

data_cat <- data[,c("op_dol_amount_range","sender_antiguedad_range","seller_antiguedad_range","diff_seller_sender_range","sender_puntos_range","seller_puntos_range","sender_ult_30_dias_range","sender_app_ult_30_dias_range","seller_ult_30_dias_range","seller_sender_ult_30_dias_range","item_antiguedad_range","sistema_operativo_mobile","profile_id","provider_id","client_id","has_approved_device","has_approved_payment_document","has_approved_payment_user","has_approved_payment_tc")]
data_cat$cluster <-data_sample$fit.cluster

str(data_cat)
data_cat$cluster <- ifelse(as.character(data_cat$cluster) == '1',1,0)
data_cat$cluster <- as.factor(data_cat$cluster)
table(data_cat$cluster)

"op_dol_amount_range"
"sender_antiguedad_range"
"seller_antiguedad_range"
"diff_seller_sender_range"
"sender_puntos_range"
"seller_puntos_range"
"sender_ult_30_dias_range"
"sender_app_ult_30_dias_range"
"seller_ult_30_dias_range"
"seller_sender_ult_30_dias_range"
"item_antiguedad_range"
"sistema_operativo_mobile"
"profile_id"
"provider_id"
"client_id"
"has_approved_device"
"has_approved_payment_document"
"has_approved_payment_user"
"has_approved_payment_tc"
"cluster"


data_cat <- data_cat[,c("op_dol_amount_range","sistema_operativo_mobile","cluster")]

#colnames(data_cat)<- c("hap_device","hap_pay_doc","hap_pay_user","hap_pay_tc")
str(data_cat)

cats_cat = apply(data_cat, 2, function(x) nlevels(as.factor(x)))
cats_cat

mca1_cat = MCA(data_cat, graph = FALSE)

mca1_cat$eig

mca1_cat_vars_df = data.frame(mca1_cat$var$coord, Variable = rep(names(cats_cat), 
                                                                 cats_cat))
mca1_cat_obs_df = data.frame(mca1_cat$ind$coord)



# plot of variable categories
ggplot(data = mca1_cat_vars_df, aes(x = Dim.1, y = Dim.2, label = rownames(mca1_cat_vars_df))) + 
  geom_hline(yintercept = 0, colour = "gray70") + geom_vline(xintercept = 0, 
                                                             colour = "gray70") + geom_text(aes(colour = Variable)) + ggtitle("MCA plot of variables using R package FactoMineR")




# MCA plot of observations and categories
ggplot(data = mca1_cat_obs_df, aes(x = Dim.1, y = Dim.2)) + geom_hline(yintercept = 0, 
                                                                       colour = "gray70") + geom_vline(xintercept = 0, colour = "gray70") + geom_point(colour = "gray50", 
                                                                                                                                                       alpha = 0.7) + geom_density2d(colour = "gray80") + geom_text(data = mca1_cat_vars_df, 
                                                                                                                                                                                                                    aes(x = Dim.1, y = Dim.2, label = rownames(mca1_cat_vars_df), colour = Variable)) + 
  ggtitle("MCA plot of variables using R package FactoMineR") + scale_colour_discrete(name = "Variable")


######


##solo con importantes




library(FactoMineR)
library(ca)


#saco nombre de variables


data_cat <- data[,c("sender_antiguedad_range","sender_puntos_range","seller_puntos_range","sender_ult_30_dias_range","sender_app_ult_30_dias_range","item_antiguedad_range","seller_ult_30_dias_range","sistema_operativo_mobile","client_id","has_approved_device")]
data_cat$cluster <-data_sample$fit.cluster

str(data_cat)
data_cat$cluster <- ifelse(as.character(data_cat$cluster) == '3',3,0)
data_cat$cluster <- as.factor(data_cat$cluster)

#me quedo solo con los del cluster 3

data_cat <- data_cat[row.names(solo3),]

cats_cat = apply(data_cat, 2, function(x) nlevels(as.factor(x)))


mca1_cat = MCA(data_cat, graph = FALSE)

mca1_cat_vars_df = data.frame(mca1_cat$var$coord, Variable = rep(names(cats_cat), 
                                                                 cats_cat))
mca1_cat_obs_df = data.frame(mca1_cat$ind$coord)



# plot of variable categories
ggplot(data = mca1_cat_vars_df, aes(x = Dim.1, y = Dim.2, label = rownames(mca1_cat_vars_df))) + 
  geom_hline(yintercept = 0, colour = "gray70") + geom_vline(xintercept = 0, 
                                                             colour = "gray70") + geom_text(aes(colour = Variable)) + ggtitle("MCA plot of variables using R package FactoMineR")




# MCA plot of observations and categories
ggplot(data = mca1_cat_obs_df, aes(x = Dim.1, y = Dim.2)) + geom_hline(yintercept = 0, 
                                                                       colour = "gray70") + geom_vline(xintercept = 0, colour = "gray70") + geom_point(colour = "gray50", 
                                                                                                                                                       alpha = 0.7) + geom_density2d(colour = "gray80") + geom_text(data = mca1_cat_vars_df, 
                                                                                                                                                                                                                    aes(x = Dim.1, y = Dim.2, label = rownames(mca1_cat_vars_df), colour = Variable)) + 
  ggtitle("MCA plot of variables using R package FactoMineR") + scale_colour_discrete(name = "Variable")

