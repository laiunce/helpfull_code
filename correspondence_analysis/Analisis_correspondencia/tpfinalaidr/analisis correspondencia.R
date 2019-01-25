

#install.packages("FactoMineR")
library(FactoMineR)

#aplicacion nativa vs sistema operativo
tabla1<-table(data_categoricas$sistema_operativo_mobile,data_categoricas$client_id) 
modelo1<-CA(tabla1)


tabla2<-table(data_categoricas$provider_id ,data_categoricas$client_id) 
modelo2<-CA(tabla2)

tabla3<-table(data_categoricas$provider_id ,data_categoricas$sistema_operativo_mobile) 
modelo3<-CA(tabla3)


## HAP 

tabla_hap_tc_user <- table(data_categoricas$has_approved_payment_tc ,data_categoricas$has_approved_payment_user)
tabla_hap_tc_user_df <- data.frame(tabla_hap_tc_user)

#uno las posibilidades
#data.frame(paste('hap_tc(', tabla_hap_tc_user_df$Var1,')_hap_us(',tabla_hap_tc_user_df$Var2,')', sep = "") )


data_categoricas_haps<-ifelse(data_categoricas$has_approved_payment_tc=='Y' & data_categoricas$has_approved_payment_user == 'Y','tc(Y)us(Y)',
                              ifelse(data_categoricas$has_approved_payment_tc=='Y' & data_categoricas$has_approved_payment_user == 'N','tc(Y)us(N)',
                                     ifelse(data_categoricas$has_approved_payment_tc=='N' & data_categoricas$has_approved_payment_user == 'Y','tc(N)us(Y)',
                                            ifelse(data_categoricas$has_approved_payment_tc=='N' & data_categoricas$has_approved_payment_user == 'N','tc(N)us(N)',
                                                   ''
                                            )
                                     )
                              )
)


tabla<-table(data_categoricas_haps, data_categoricas$sistema_operativo_mobile) 
modelo<-CA(tabla)

modelo$row
modelo$col
modelo$eig

tabla<-table(data_categoricas_haps, data_categoricas$client_id) 
modelo<-CA(tabla)



#hacer por montos

tabla4<-table(data$op_dol_amount_range ,data_categoricas$sistema_operativo_mobile) 
modelo4<-CA(tabla4)

tabla5<-table(data$op_dol_amount_range ,data$sender_antiguedad_range) 
modelo5<-CA(tabla5)

tabla6<-table(data$seller_antiguedad_range ,data$sender_antiguedad_range) 
modelo6<-CA(tabla6)

#los usuarioes nuevos te operan por mobile
tabla7<-table(data_categoricas$sistema_operativo_mobile ,data$sender_antiguedad_range) 
modelo7<-CA(tabla7)

#los usuarioes nuevos te operan por client_id
tabla7<-table(data_categoricas$client_id ,data$sender_antiguedad_range) 
modelo7<-CA(tabla7)


tabla6<-table(data$seller_puntos_range ,data$sender_puntos_range) 
modelo6<-CA(tabla6)



### con varias variables usando solo las de HAP



library(FactoMineR)
library(ca)
str(data_categoricas)
library(ggplot2)
#saco nombre de variables

#data_cat <- data_categoricas[,c("sistema_operativo_mobile","profile_id","provider_id","client_id","has_approved_device","has_approved_payment_document","has_approved_payment_user","has_approved_payment_tc")]

data_cat <- data_categoricas[,c("has_approved_device","has_approved_payment_document","has_approved_payment_user","has_approved_payment_tc")]
colnames(data_cat)<- c("hap_device","hap_pay_doc","hap_pay_user","hap_pay_tc")

cats_cat = apply(data_cat, 2, function(x) nlevels(as.factor(x)))
cats_cat



mca1_cat = MCA(data_cat, graph = FALSE)
print(mca1_cat)

mca1_cat$var$contrib
summary(mca1_cat)

mca1_cat_vars_df = data.frame(mca1_cat$var$coord, Variable = rep(names(cats_cat), 
                                                                 cats_cat))
mca1_cat_obs_df = data.frame(mca1_cat$ind$coord)



# plot of variable categories
ggplot(data = mca1_cat_vars_df, aes(x = Dim.1, y = Dim.2, label = rownames(mca1_cat_vars_df))) + 
  geom_hline(yintercept = 0, colour = "gray70") + geom_vline(xintercept = 0, 
                                                             colour = "gray70") + geom_text(aes(colour = Variable)) + ggtitle("MCA plot of variables using R package FactoMineR")

summary(mca1_cat)

# MCA plot of observations and categories
ggplot(data = mca1_cat_obs_df, aes(x = Dim.1, y = Dim.2)) + geom_hline(yintercept = 0, 
                                                                       colour = "gray70") + geom_vline(xintercept = 0, colour = "gray70") + geom_point(colour = "gray50", 
                                                                                                                                                       alpha = 0.7) + geom_density2d(colour = "gray80") + geom_text(data = mca1_cat_vars_df, 
                                                                                                                                                                                                                    aes(x = Dim.1, y = Dim.2, label = rownames(mca1_cat_vars_df), colour = Variable)) + 
  ggtitle("MCA plot of variables using R package FactoMineR") + scale_colour_discrete(name = "Variable")


#####
#hago con todas las variables discretizadas del preprocess


library(FactoMineR)
library(ca)


#saco nombre de variables

#data_cat <- data_categoricas[,c("sistema_operativo_mobile","profile_id","provider_id","client_id","has_approved_device","has_approved_payment_document","has_approved_payment_user","has_approved_payment_tc")]

data_cat <- data[,c("op_dol_amount_range","sender_antiguedad_range","seller_antiguedad_range")]
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



summary(mca1_cat)

# MCA plot of observations and categories
ggplot(data = mca1_cat_obs_df, aes(x = Dim.1, y = Dim.2)) + geom_hline(yintercept = 0, 
                                                                       colour = "gray70") + geom_vline(xintercept = 0, colour = "gray70") + geom_point(colour = "gray50", 
                                                                                                                                                       alpha = 0.7) + geom_density2d(colour = "gray80") + geom_text(data = mca1_cat_vars_df, 
                                                                                                                                                                                                                    aes(x = Dim.1, y = Dim.2, label = rownames(mca1_cat_vars_df), colour = Variable)) + 
  ggtitle("MCA plot of variables using R package FactoMineR") + scale_colour_discrete(name = "Variable")



#####
#hago con antiguedad de items y dolar


library(FactoMineR)
library(ca)


#saco nombre de variables

#data_cat <- data_categoricas[,c("sistema_operativo_mobile","profile_id","provider_id","client_id","has_approved_device","has_approved_payment_document","has_approved_payment_user","has_approved_payment_tc")]

data_cat <- data[,c("sender_puntos_range","seller_puntos_range")]
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

