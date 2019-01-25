library(FactoMineR)
library(ca)
library(ggplot2)

data1 <- read.csv("data.csv")
print()

ac_data <-data.frame(as.factor(data1$ï..bad), data1$Sexo,data1$Zona_Oficial)
colnames(ac_data)<-c('bad','Sexo','Zona_Oficial')


mca1_cat = MCA(ac_data, graph = FALSE)
plot(mca1_cat)
