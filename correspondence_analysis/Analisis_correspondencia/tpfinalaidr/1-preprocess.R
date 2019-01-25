library(ggplot2)

#leo dataset
data <- read.csv("Data/dataset3.csv")
data$client_id<-as.character(data$client_id)
data$client_id <- ifelse(data$client_id == "2568868276694852","2568",data$client_id)
data$client_id <- ifelse(data$client_id == "48638295529722","4863",data$client_id)
data$client_id<-as.factor(data$client_id)


#completo nulos con ceros
data[is.na(data)] <- 0

#elimino scoring_id ya que no se usa
data$scoring_id <-NULL
###
## OP_DOL_AMOUNT
###


#analizo distribucion de datos por kernell para ver bines dol_amount
hist(data$op_dol_amount)
plot(density(data$op_dol_amount, bw=3), main="bw=3")


#1-boxplot por op_dol_amount
p <- ggplot(data, aes(x=1,y=data$op_dol_amount)) 
p + geom_boxplot()



#2-histograma con ggplot
ggplot(data=data, aes(data$op_dol_amount)) + 
  geom_histogram(breaks=seq(1000, 5000, by =4), 
                 col="black", 
                 aes(fill=..count..))


data$op_dol_amount_range<-findInterval(data$op_dol_amount, c(50,100,150,250,350,500,1200))
#veo valores unicos 
unique(data$op_dol_amount_range)


data$op_dol_amount_range<-
  ifelse(data$op_dol_amount_range==0,'<50',
         ifelse(data$op_dol_amount_range==1,'50-100',
                ifelse(data$op_dol_amount_range==2,'100-150',
                       ifelse(data$op_dol_amount_range==3,'150-250',
                              ifelse(data$op_dol_amount_range==4,'250-350',
                                     ifelse(data$op_dol_amount_range==5,'350-500',
                                            ifelse(data$op_dol_amount_range==6,'500-1200','>1200')
                                            )
                                     )
                              )
                       )
                )
         )


unique(data$op_dol_amount_range)


#veo valores unicos 
unique(data$op_dol_amount_range)


#boxplot por rango
p <- ggplot(data, aes(op_dol_amount_range,op_dol_amount)) 
p + geom_boxplot()

#3-histograma con ggplot colores por rango
ggplot(data=data, aes(data$op_dol_amount)) + 
  geom_histogram(breaks=seq(00, 2000, by =10), 
                 col="black", 
                 aes(fill=data$op_dol_amount_range))

###
## sender_antiguedad
###

#2-boxplot por sender_antiguedad
p <- ggplot(data, aes(x=1,y=data$sender_antiguedad)) 
p + geom_boxplot()



#2-histograma con ggplot
ggplot(data=data, aes(data$sender_antiguedad)) + 
  geom_histogram(breaks=seq(0, 100, by =1), 
                 col="black", 
                 aes(fill=..count..))



data$sender_antiguedad_range<-findInterval(data$sender_antiguedad, c(1,4,30,150,420,1000))
#veo valores unicos 
unique(data$sender_antiguedad_range)


data$sender_antiguedad_range<-
  ifelse(data$sender_antiguedad_range==0,'<1',
         ifelse(data$sender_antiguedad_range==1,'1-4',
                ifelse(data$sender_antiguedad_range==2,'4-30',
                       ifelse(data$sender_antiguedad_range==3,'30-150',
                              ifelse(data$sender_antiguedad_range==4,'150-420',
                                     ifelse(data$sender_antiguedad_range==5,'420-1000','>1000')
                                                   )
                                            )
                                     )
                              )
                       )


unique(data$sender_antiguedad_range)


#boxplot por rango
p <- ggplot(data, aes(sender_antiguedad_range,sender_antiguedad)) 
p + geom_boxplot()


#boxplot excluyendo ultimo rango

data_acotada <- data[data$sender_antiguedad_range!= '>1000',]
p <- ggplot(data_acotada, aes(sender_antiguedad_range,sender_antiguedad)) 
p + geom_boxplot()

#grafico rango especifico

data_rango <- data[data$sender_antiguedad_range == '<1',]
ggplot(data=data_rango, aes(data_rango$sender_antiguedad)) + 
  geom_histogram(breaks=seq(0, 31, by =1), 
                 col="black", 
                 aes(fill=..count..))


#3-histograma con ggplot colores por rango
ggplot(data=data, aes(data$sender_antiguedad)) + 
  geom_histogram(breaks=seq(00, 500, by =2), 
                 col="black", 
                 aes(fill=data$sender_antiguedad_range))



###
## seller_antiguedad
###


#3-boxplot por seller_antiguedad
p <- ggplot(data, aes(x=1,y=data$seller_antiguedad)) 
p + geom_boxplot()



#3-histograma con ggplot
ggplot(data=data, aes(data$seller_antiguedad)) + 
  geom_histogram(breaks=seq(0, 120000, by =100), 
                 col="black", 
                 aes(fill=..count..))



data$seller_antiguedad_range<-findInterval(data$seller_antiguedad, c(50000,120000))
#veo valores unicos 
unique(data$seller_antiguedad_range)

data$seller_antiguedad_range<-
  ifelse(data$seller_antiguedad_range==0,'<50000',
         ifelse(data$seller_antiguedad_range==1,'50000-100000','>100000')
         )


unique(data$seller_antiguedad_range)

#boxplot por rango
p <- ggplot(data, aes(seller_antiguedad_range,seller_antiguedad)) 
p + geom_boxplot()


#3-histograma con ggplot colores por rango
ggplot(data=data, aes(data$seller_antiguedad)) + 
  geom_histogram(breaks=seq(00, 150000, by =1000), 
                 col="black", 
                 aes(fill=data$seller_antiguedad_range))



###
## diff_seller_sender
###


#3-boxplot por diff_seller_sender
p <- ggplot(data, aes(x=1,y=data$diff_seller_sender)) 
p + geom_boxplot()



#3-histograma con ggplot
ggplot(data=data, aes(data$diff_seller_sender)) + 
  geom_histogram(breaks=seq(15000, 150000, by =100), 
                 col="black", 
                 aes(fill=..count..))


data$diff_seller_sender_range<-findInterval(data$diff_seller_sender, c(-25000,-4000,18000,50000,100000))
#veo valores unicos 
unique(data$diff_seller_sender_range)


data$diff_seller_sender_range<-
  ifelse(data$diff_seller_sender_range==0,'<-25000',
         ifelse(data$diff_seller_sender_range==1,'-25000--4000',
                ifelse(data$diff_seller_sender_range==2,'-4000-18000',
                       ifelse(data$diff_seller_sender_range==3,'18000-50000',
                              ifelse(data$diff_seller_sender_range==4,'50000-100000','>100000')
                                                          )
                                              )
                                       )
                                )


unique(data$diff_seller_sender_range)

#boxplot por rango
p <- ggplot(data, aes(diff_seller_sender_range,diff_seller_sender)) 
p + geom_boxplot()

#3-histograma con ggplot colores por rango
ggplot(data=data, aes(data$diff_seller_sender)) + 
  geom_histogram(breaks=seq(-100000, 100000, by =1000), 
                 col="black", 
                 aes(fill=data$diff_seller_sender_range))


###
## sender_puntos
###
         

#3-boxplot por diff_seller_sender
p <- ggplot(data, aes(x=1,y=data$sender_puntos)) 
p + geom_boxplot()



#3-histograma con ggplot
ggplot(data=data, aes(data$sender_puntos)) + 
  geom_histogram(breaks=seq(0, 100, by =1), 
                 col="black", 
                 aes(fill=..count..))


data$sender_puntos_range<-findInterval(data$sender_puntos, c(10,50,100))
#veo valores unicos 
unique(data$sender_puntos_range)


data$sender_puntos_range<-
  ifelse(data$sender_puntos_range==0,'<10',
         ifelse(data$sender_puntos_range==1,'10-50',
                ifelse(data$sender_puntos_range==2,'50-100','>100')
                       )
                )

unique(data$sender_puntos_range)

#boxplot por rango
p <- ggplot(data, aes(sender_puntos_range,sender_puntos)) 
p + geom_boxplot()

#grafico rango especifico

data_rango <- data[data$sender_puntos_range == '50-100',]
ggplot(data=data_rango, aes(data_rango$sender_puntos)) + 
  geom_histogram(breaks=seq(0, 110, by =1), 
                 col="black", 
                 aes(fill=..count..))


#3-histograma con ggplot colores por rango
ggplot(data=data, aes(data$sender_puntos)) + 
  geom_histogram(breaks=seq(0, 150, by =1), 
                 col="black", 
                 aes(fill=data$sender_puntos_range))


###
## seller_puntos
###

#3-boxplot por diff_seller_sender
p <- ggplot(data, aes(x=1,y=data$seller_puntos)) 
p + geom_boxplot()


#3-histograma con ggplot
ggplot(data=data, aes(data$seller_puntos)) + 
  geom_histogram(breaks=seq(1000, 20000, by =10), 
                 col="black", 
                 aes(fill=..count..))



data$seller_puntos_range<-findInterval(data$seller_puntos, c(3,26,100,200,400,1000,1500))
#veo valores unicos 
unique(data$seller_puntos_range)

data$seller_puntos_range<-
  ifelse(data$seller_puntos_range==0,'<3',
         ifelse(data$seller_puntos_range==1,'3-26',
                ifelse(data$seller_puntos_range==2,'26-100',
                       ifelse(data$seller_puntos_range==3,'100-200',
                              ifelse(data$seller_puntos_range==4,'200-400',
                                     ifelse(data$seller_puntos_range==5,'400-1000',
                                            ifelse(data$seller_puntos_range==6,'1000-1500','>1500')
                                                   )
                                            )
                                     )
                              )
                       )
                )


#boxplot por rango
p <- ggplot(data, aes(seller_puntos_range,seller_puntos)) 
p + geom_boxplot()

#grafico rango especifico

data_rango <- data[data$seller_puntos_range == '>1500',]
ggplot(data=data_rango, aes(data_rango$seller_puntos)) + 
  geom_histogram(breaks=seq(0, 110, by =1), 
                 col="black", 
                 aes(fill=..count..))


#boxplot excluyendo ultimo rango

data_acotada <- data[data$seller_puntos_range!= '>1500',]
p <- ggplot(data_acotada, aes(seller_puntos_range,seller_puntos)) 
p + geom_boxplot()



#3-histograma con ggplot colores por rango
ggplot(data=data, aes(data$seller_puntos)) + 
  geom_histogram(breaks=seq(0, 2000, by =10), 
                 col="black", 
                 aes(fill=data$seller_puntos_range))


###
## sender_ult_30_dias
###

#3-boxplot por diff_seller_sender
p <- ggplot(data, aes(x=1,y=data$sender_ult_30_dias)) 
p + geom_boxplot()


#3-histograma con ggplot
ggplot(data=data, aes(data$sender_ult_30_dias)) + 
  geom_histogram(breaks=seq(500, 2000, by =10), 
                 col="black", 
                 aes(fill=..count..))


data$sender_ult_30_dias_range<-findInterval(data$sender_ult_30_dias, c(1,50,150,300,500))
#veo valores unicos 
unique(data$sender_ult_30_dias_range)

data$sender_ult_30_dias_range<-
  ifelse(data$sender_ult_30_dias_range==0,'<1',
         ifelse(data$sender_ult_30_dias_range==1,'1-50',
                ifelse(data$sender_ult_30_dias_range==2,'50-150',
                       ifelse(data$sender_ult_30_dias_range==3,'150-300',
                              ifelse(data$sender_ult_30_dias_range==4,'300-500','>500')
                                            )
                                     )
                              )
                       )





#boxplot por rango
p <- ggplot(data, aes(sender_ult_30_dias_range,sender_ult_30_dias)) 
p + geom_boxplot()


#boxplot excluyendo ultimo rango

data_acotada <- data[data$sender_ult_30_dias_range!= '>500',]
p <- ggplot(data_acotada, aes(sender_ult_30_dias_range,sender_ult_30_dias)) 
p + geom_boxplot()


#3-histograma con ggplot colores por rango
ggplot(data=data, aes(data$sender_ult_30_dias)) + 
  geom_histogram(breaks=seq(0, 1000, by =10), 
                 col="black", 
                 aes(fill=data$sender_ult_30_dias_range))



###
## sender_app_ult_30_dias
###


#3-boxplot por diff_seller_sender
p <- ggplot(data, aes(x=1,y=data$sender_app_ult_30_dias)) 
p + geom_boxplot()


#3-histograma con ggplot
ggplot(data=data, aes(data$sender_app_ult_30_dias)) + 
  geom_histogram(breaks=seq(00, 500, by =10), 
                 col="black", 
                 aes(fill=..count..))




data$sender_app_ult_30_dias_range<-findInterval(data$sender_app_ult_30_dias, c(5))
#veo valores unicos 
unique(data$sender_app_ult_30_dias_range)

data$sender_app_ult_30_dias_range<-
  ifelse(data$sender_app_ult_30_dias_range==0,'<5','>5')


#3-histograma con ggplot colores por rango
ggplot(data=data, aes(data$sender_app_ult_30_dias)) + 
  geom_histogram(breaks=seq(0, 2000, by =10), 
                 col="black", 
                 aes(fill=data$sender_app_ult_30_dias_range))


###
## seller_ult_30_dias
###

#3-boxplot por diff_seller_sender
p <- ggplot(data, aes(x=1,y=data$seller_ult_30_dias)) 
p + geom_boxplot()


#3-histograma con ggplot
ggplot(data=data, aes(data$seller_ult_30_dias)) + 
  geom_histogram(breaks=seq(00, 50000, by =10), 
                 col="black", 
                 aes(fill=..count..))

data$seller_ult_30_dias_range<-findInterval(data$seller_ult_30_dias, c(3000,10000))
#veo valores unicos 
unique(data$seller_ult_30_dias_range)

data$seller_ult_30_dias_range<-
  ifelse(data$seller_ult_30_dias_range==0,'<3000',
         ifelse(data$seller_ult_30_dias_range==1,'3000-10000','>10000')
                                     )


#boxplot por rango
p <- ggplot(data, aes(seller_ult_30_dias_range,seller_ult_30_dias)) 
p + geom_boxplot()


#boxplot excluyendo ultimo rango

data_acotada <- data[data$seller_ult_30_dias_range!= '>10000',]
p <- ggplot(data_acotada, aes(seller_ult_30_dias_range,seller_ult_30_dias)) 
p + geom_boxplot()

#3-histograma con ggplot colores por rango
ggplot(data=data, aes(data$seller_ult_30_dias)) + 
  geom_histogram(breaks=seq(00, 20000, by =50), 
                 col="black", 
                 aes(fill=data$seller_ult_30_dias_range))


###
## seller_sender_ult_30_dias
###

#3-boxplot por diff_seller_sender
p <- ggplot(data, aes(x=1,y=data$seller_sender_ult_30_dias)) 
p + geom_boxplot()

#3-histograma con ggplot
ggplot(data=data, aes(data$seller_sender_ult_30_dias)) + 
  geom_histogram(breaks=seq(300, 15000, by =10), 
                 col="black", 
                 aes(fill=..count..))


data$seller_sender_ult_30_dias_range<-findInterval(data$seller_sender_ult_30_dias, c(100,200,400,1500))
#veo valores unicos 
unique(data$seller_sender_ult_30_dias_range)

data$seller_sender_ult_30_dias_range<-
  ifelse(data$seller_sender_ult_30_dias_range==0,'<100',
         ifelse(data$seller_sender_ult_30_dias_range==1,'100-200',
                ifelse(data$seller_sender_ult_30_dias_range==2,'200-400',
                       ifelse(data$seller_sender_ult_30_dias_range==3,'400-1500','>1500')
                                                   )
                                     )
                              )



#boxplot por rango
p <- ggplot(data, aes(seller_sender_ult_30_dias_range,seller_sender_ult_30_dias)) 
p + geom_boxplot()


#boxplot excluyendo ultimo rango

data_acotada <- data[data$seller_sender_ult_30_dias_range!= '>1500',]
p <- ggplot(data_acotada, aes(seller_sender_ult_30_dias_range,seller_sender_ult_30_dias)) 
p + geom_boxplot()

#3-histograma con ggplot colores por rango
ggplot(data=data, aes(data$seller_sender_ult_30_dias)) + 
  geom_histogram(breaks=seq(00, 5000, by =10), 
                 col="black", 
                 aes(fill=data$seller_sender_ult_30_dias_range))

###
## item_antiguedad
###


#3-boxplot por diff_seller_sender
p <- ggplot(data, aes(x=1,y=data$item_antiguedad)) 
p + geom_boxplot()

#3-histograma con ggplot
ggplot(data=data, aes(data$item_antiguedad)) + 
  geom_histogram(breaks=seq(00, 2000, by =5), 
                 col="black", 
                 aes(fill=..count..))


data$item_antiguedad_range<-findInterval(data$item_antiguedad, c(200,4500))
#veo valores unicos 
unique(data$item_antiguedad_range)

data$item_antiguedad_range<-
  ifelse(data$item_antiguedad_range==0,'<200',
         ifelse(data$item_antiguedad_range==1,'200-4500','>4500')
         )
                                            


#boxplot por rango
p <- ggplot(data, aes(item_antiguedad_range,item_antiguedad)) 
p + geom_boxplot()


#boxplot excluyendo ultimo rango

data_acotada <- data[data$seller_sender_ult_30_dias_range!= '>1500',]
p <- ggplot(data_acotada, aes(seller_sender_ult_30_dias_range,seller_sender_ult_30_dias)) 
p + geom_boxplot()

#3-histograma con ggplot colores por rango
ggplot(data=data, aes(data$item_antiguedad)) + 
  geom_histogram(breaks=seq(00, 7000, by =40), 
                 col="black", 
                 aes(fill=data$item_antiguedad_range))


data$op_dol_amount_range <- as.factor(data$op_dol_amount_range)
data$sender_antiguedad_range <- as.factor(data$sender_antiguedad_range)
data$seller_antiguedad_range <- as.factor(data$seller_antiguedad_range)
data$diff_seller_sender_range <- as.factor(data$diff_seller_sender_range)
data$sender_puntos_range <- as.factor(data$sender_puntos_range)
data$seller_puntos_range <- as.factor(data$seller_puntos_range)
data$sender_ult_30_dias_range <- as.factor(data$sender_ult_30_dias_range)
data$sender_app_ult_30_dias_range <- as.factor(data$sender_app_ult_30_dias_range)
data$seller_ult_30_dias_range <- as.factor(data$seller_ult_30_dias_range)
data$seller_sender_ult_30_dias_range <- as.factor(data$seller_sender_ult_30_dias_range)
data$item_antiguedad_range <- as.factor(data$item_antiguedad_range)