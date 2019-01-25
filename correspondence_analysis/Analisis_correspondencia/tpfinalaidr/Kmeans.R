
#http://www.statmethods.net/advstats/cluster.html

library(factoextra);
library(cluster);
library(amap);
library(vegan);
library(prcomp)
library(ggbiplot)


# Determine number of clusters
wss <- (nrow(mydata)-1)*sum(apply(mydata,2,var))

for (i in 2:22) wss[i] <- sum(kmeans(mydata,centers=i)$withinss)
plot(1:22, wss, type="b", xlab="Number of Clusters",ylab="Within groups sum of squares")

# K-Means Cluster Analysis

# K-Means Cluster Analysis



#cluster con euclidea
data_sample <- data
#acoto universo de variables numericos solamente
data_numeric<- data_sample[1:11]
mydata<-data_numeric
#cluster con euclidea
gower_dist <- vegdist(data_numeric, method="euclidea")
gower_mat <- as.matrix(gower_dist)
fit <- kmeans(gower_mat, 5)
clusplot(data_numeric, kfit$cluster)


# get cluster means 
aggregate(mydata,by=list(fit$cluster),FUN=mean)
# append cluster assignment
mydata <- data.frame(mydata, fit$cluster)
mydata$fit.cluster <- as.factor(mydata$fit.cluster)



# Ward Hierarchical Clustering
d <- dist(mydata, method = "euclidean") # distance matrix
fit <- hclust(d, method="ward") 
plot(fit) # display dendogram



# Cluster Plot against 1st 2 principal components
# vary parameters for most readable graph
clusplot(data_numeric, fit$cluster, color=TRUE, shade=TRUE,  labels=2, lines=0)

#obtengo los datos del cluster 3
out <- cbind(mydata, clusterNum = fit$cluster)
out[out$clusterNum ==3,]

out$clusterNum<-as.factor(out$clusterNum)

out$cluster1 <- ifelse(out$clusterNum==1,'1','no1') 
out$cluster2 <- ifelse(out$clusterNum==2,'2','no2') 
out$cluster3 <- ifelse(out$clusterNum==3,'3','no3') 
out$cluster4 <- ifelse(out$clusterNum==4,'4','no4') 
out$cluster5 <- ifelse(out$clusterNum==5,'5','no5') 
out$cluster6 <- ifelse(out$clusterNum==6,'6','no6') 

g <- ggbiplot(Comp.pca, obs.scale = 1, var.scale = 1,choices = c(2,1),alpha = 0.1, groups = out$cluster1, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=out$cluster1,), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("op_dol_amount_range");print(g)
g <- ggbiplot(Comp.pca, obs.scale = 1, var.scale = 1,choices = c(2,1),alpha = 0.1, groups = out$cluster2, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=out$cluster2,), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("op_dol_amount_range");print(g)
g <- ggbiplot(Comp.pca, obs.scale = 1, var.scale = 1,choices = c(2,1),alpha = 0.1, groups = out$cluster3, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=out$cluster3,), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("op_dol_amount_range");print(g)
g <- ggbiplot(Comp.pca, obs.scale = 1, var.scale = 1,choices = c(2,1),alpha = 0.1, groups = out$cluster4, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=out$cluster4,), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("op_dol_amount_range");print(g)
g <- ggbiplot(Comp.pca, obs.scale = 1, var.scale = 1,choices = c(2,1),alpha = 0.1, groups = out$cluster5, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=out$cluster5,), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("op_dol_amount_range");print(g)
g <- ggbiplot(Comp.pca, obs.scale = 1, var.scale = 1,choices = c(2,1),alpha = 0.1, groups = out$cluster6, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=out$cluster6,), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("op_dol_amount_range");print(g)


#el cluster 3
g <- ggbiplot(Comp.pca, obs.scale = 1, var.scale = 1,choices = c(2,1),alpha = 0.1, groups = out$cluster3, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=out$cluster3,), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("op_dol_amount_range");print(g)
g <- ggbiplot(Comp.pca, obs.scale = 1, var.scale = 1,choices = c(1,3),alpha = 0.1, groups = out$cluster3, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=out$cluster3,), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("op_dol_amount_range");print(g)
g <- ggbiplot(Comp.pca, obs.scale = 1, var.scale = 1,choices = c(2,3),alpha = 0.1, groups = out$cluster3, ellipse = FALSE,  circle = FALSE,var.axes = TRUE );g <- g + geom_point(aes(colour=out$cluster3,), size = 0.0) ;g <- g + theme(legend.direction = 'horizontal',legend.position = 'top');g <- g + ggtitle("op_dol_amount_range");print(g)



# grafico de barras por rangos o grafico de estrella para ver caracteristicas de clusters

valores3<-out[out$clusterNum ==3,]
row.names(valores3)

##seleccionar data con rownames

plot(valores3$seller_sender_ult_30_dias_range)
###
###
###
###
###



