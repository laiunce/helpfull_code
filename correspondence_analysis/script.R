

#install.packages("FactoMineR")
#install.packages("ca")
#install.packages("ggplot2")
library(ggplot2)
library(ca)
library(FactoMineR)

#lee datos
data <- read.csv("/Users/laiunce/Desktop/Analisis correspondencia/base_4_acotada.csv")

#asigna columnas
data_cat <- data[,c("item_CARRIER","palabra_busqueda","ciudad")]

# reemplaza NA values
data_cat$palabra_busqueda = data_cat$palabra_busqueda[is.na(data_cat$palabra_busqueda)] <- "None"
data_cat$ciudad = data_cat$ciudad[is.na(data_cat$ciudad)] <- "None"
data_cat$item_CARRIER = data_cat$item_CARRIER[is.na(data_cat$item_CARRIER)] <- "None"


#dimensiones a graficar
cant_dim = 2

#grafica
str(data_cat)
cats_cat = apply(data_cat, cant_dim, function(x) nlevels(as.factor(x)))
cats_cat
mca1_cat = MCA(data_cat, graph = FALSE)
mca1_cat$eig
mca1_cat_vars_df = data.frame(mca1_cat$var$coord, Variable = rep(names(cats_cat), cats_cat))
mca1_cat_obs_df = data.frame(mca1_cat$ind$coord)
# plot of variable categories
ggplot(data = mca1_cat_vars_df, aes(x = Dim.1, y = Dim.2, label = rownames(mca1_cat_vars_df))) + 
  geom_hline(yintercept = 0, colour = "gray70") + geom_vline(xintercept = 0, 
                                                             colour = "gray70") + geom_text(aes(colour = Variable)) + ggtitle("MCA plot of variables using R package FactoMineR")

