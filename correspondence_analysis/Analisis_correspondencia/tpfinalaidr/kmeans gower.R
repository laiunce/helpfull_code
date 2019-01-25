

library(factoextra);
library(cluster);
library(amap);
library(vegan);

data_sample <- data
#acoto universo de variables numericos solamente
data_numeric<- data_sample[1:11]

mydata<-data_numeric
for (i in 2:22) wss[i] <- sum(kmeans(mydata,centers=i)$withinss)
plot(1:22, wss, type="b", xlab="Number of Clusters",ylab="Within groups sum of squares")





## CATEGORICAS


data_sample <- data
#acoto universo de variables numericos solamente
data_categorica<- data_sample[12:19]
data_categorica$profile_id<-NULL
data_categorica$provider_id<-NULL

str(data_categorica)
#cluster con gower
gower_dist <- daisy(data_categorica,
                    metric = "gower",
                    type = list(logratio = 3))
gower_mat <- as.matrix(gower_dist)
kfit <- kmeans(gower_mat, 4)
clusplot(data_categorica, kfit$cluster)


## CATEGORICAS CALCULADAS


data_sample <- data
#acoto universo de variables numericos solamente
data_categorica<- data_sample[20:30]
str(data_categorica)

#cluster con gower
gower_dist <- daisy(data_categorica,
                    metric = "gower",
                    type = list(logratio = 3))
gower_mat <- as.matrix(gower_dist)
kfit <- kmeans(gower_mat, 4)
clusplot(data_categorica, kfit$cluster)



## CATEGORICAS MAS CONTINUAS


data_sample <- data
#acoto universo de variables numericos solamente
data_categorica<- data_sample[1:30]
data_categorica$profile_id<-NULL
data_categorica$provider_id<-NULL
str(data_categorica)
#cluster con gower
gower_dist <- daisy(data_categorica,
                    metric = "gower",
                    type = list(logratio = 3))
gower_mat <- as.matrix(gower_dist)
kfit <- kmeans(gower_mat, 4)
clusplot(data_categorica, kfit$cluster)



## SOLO CONTINUAS GOWER


data_sample <- data
#acoto universo de variables numericos solamente
data_numeric<- data_sample[1:11]
str(data_numeric)

#cluster con gower
gower_dist <- daisy(data_numeric,
                    metric = "gower",
                    type = list(logratio = 3))
gower_mat <- as.matrix(gower_dist)
kfit <- kmeans(gower_mat, 5)
clusplot(data_numeric, kfit$cluster)



## SOLO CONTINUAS EUCLIDEA


data_sample <- data
#acoto universo de variables numericos solamente
data_numeric<- data_sample[1:11]

#cluster con euclidea
gower_dist <- vegdist(data_numeric, method="euclidea")
gower_mat <- as.matrix(gower_dist)
kfit <- kmeans(gower_mat, 5)
clusplot(data_numeric, kfit$cluster)




## SOLO CONTINUAS manhatam


data_sample <- data
#acoto universo de variables numericos solamente
data_numeric<- data_sample[1:11]

#cluster con euclidea
gower_dist <- vegdist(data_numeric, method="manhattan")
gower_mat <- as.matrix(gower_dist)
kfit <- kmeans(gower_mat, 4)
clusplot(data_numeric, kfit$cluster)


## SOLO PCA EUCLIDEA

pca_prim5 <- data.frame(Comp.pca$x)[1:5]
data_sample <- pca_prim5
#acoto universo de variables numericos solamente
data_numeric<- data_sample

#cluster con euclidea
gower_dist <- vegdist(data_numeric, method="euclidea")
gower_mat <- as.matrix(gower_dist)
kfit <- kmeans(gower_mat, 5)
clusplot(data_numeric, kfit$cluster)



##  CONTINUAS MAS PCA EUCLIDEA

data_sample <- data
#acoto universo de variables numericos solamente
data_numeric<- data_sample[1:11]

pca_prim5 <- data.frame(data.frame(Comp.pca$x)[1:8],data_numeric)

data_sample <- pca_prim5
#acoto universo de variables numericos solamente
data_numeric<- data_sample

#cluster con euclidea
gower_dist <- vegdist(data_numeric, method="euclidea")
gower_mat <- as.matrix(gower_dist)
kfit <- kmeans(gower_mat, 5)
clusplot(data_numeric, kfit$cluster)
