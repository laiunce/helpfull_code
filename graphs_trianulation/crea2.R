#install.packages("intergraph")
library(igraph)

#data_graph <- read.csv("Data/tstgraph.csv", header = TRUE)
data_graph <- read.csv("Data/246265366/data3.csv", header = TRUE)



data_graph$sender_id<-as.factor(data_graph$sender_id)
data_graph$receiver_id<-as.factor(data_graph$receiver_id)


#http://www.shizukalab.com/toolkits/sna/weighted-edgelists
el=data_graph
el[,1]=as.character(el[,1]) 
el[,2]=as.character(el[,2])
el=as.matrix(el)
g=graph.edgelist(el[,1:2],directed=TRUE)
E(g)$weight=as.numeric(el[,4]) 
E(g)$type=as.character(el[,3]) 



el[,4]<-as.numeric(el[,4])
E(g)$weight<-ifelse(as.numeric(el[,4])>1000,5,ifelse(as.numeric(el[,4])>500,4,ifelse(as.numeric(el[,4])>200,3,ifelse(as.numeric(el[,4])>100,2,ifelse(as.numeric(el[,4])>50,1,ifelse(as.numeric(el[,4])>10,0.5,0.1))))))

E(g)$color <- as.character(ifelse(data_graph$type=='money_transfer','#FF0000', #rojo
                                  ifelse(data_graph$type=='user_certification_payment','#FF0088', #rosa
                                         ifelse(data_graph$type=='account_fund','#8400FF', #violeta
                                                ifelse(data_graph$type=='pos_payment','#0000FF', #azul fuerte
                                                       ifelse(data_graph$type=='regular_payment','#0084FF', #celeste
                                                              ifelse(data_graph$type=='subscription_payment','#00FFFF', #turquesa
                                                                     ifelse(data_graph$type=='random_charge','#00FF84', #verde agua
                                                                            ifelse(data_graph$type=='recurring_payment','#84FF00', #verde fibron
                                                                                   ifelse(data_graph$type=='payment_addition','#FFFF00', '#FF8000' #naranja
                                                                                   )
                                                                            )
                                                                     )
                                                              )
                                                       )
                                                )
                                         ) 
                                  )
)
)


#hacer el in
V(g)$color_servicio <- as.character(ifelse(as.character(V(g)$name)=='246364511','red',ifelse(as.character(V(g)$name)=='226742606' | as.character(V(g)$name)=='24','orange','lightblue'))) #rojo
#paleta_colores <-c('money_transfer' = '#FF0000','user_certification_payment' = '#FF0088','account_fund' = '#8400FF','pos_payment' = '#0000FF','regular_payment' = '#0084FF','subscription_payment' = '#00FFFF','random_charge' = '#00FF84','recurring_payment' = '#84FF00','payment_addition' = '#FFFF00','cellphone_recharge'='#FF00F0')



#plot(g,layout=layout.fruchterman.reingold,edge.width=1,edge.color= E(g)$color,vertex.size=1 )
plot(g,
     vertex.color=V(g)$color_servicio ,
     layout=layout.davidson.harel(g),
     edge.width=E(g)$weight*2,
     edge.color= E(g)$color,
     vertex.size=10,
     edge.arrow.size=E(g)$weight,
     vertex.label = V(g)$names
)
closeness(g)
sum(closeness(g))
help(closeness)

1/(sumatorio de minimos saltos a nodos)

eccentricity(g)

degree(g)


transitivity(g)
transitivity(g, type="local")

sum(transitivity(g, type="local"))

1 es la cantidad de links entre vecinos de 2 en este caso entre 4,3 y 5 hay 1 solo link
dividio el grado de 2 (que es 6 como vimos anteriormente y esto) combinando tomadas de a dos como vemos en laformula


cantidad de links entre vecinos sobre combinaciones de grado del nodo tomadas de a dos


1/6



