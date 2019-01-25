library(FactoMineR)

data1 <- read.csv("data.csv")
print()

ac_data <-data.frame(as.factor(data1[1]), data1$Sexo,data1$Zona_Oficial)
colnames(ac_data)<-c('bad','Sexo','Zona_Oficial')


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