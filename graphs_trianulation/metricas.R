par(mfrow=c(1,1))
library(igraph)
fg <- make_full_graph(4)
st <- make_star(5)
tr <- make_tree(20, children = 3, mode = "undirected")
rn <- make_ring(5)
er <- sample_gnm(n=30, m=40) 
sw <- sample_smallworld(dim=2, size=10, nei=1, p=0.1)
ba <-  sample_pa(n=30, power=1, m=1,  directed=F)
zach <- graph("Zachary") # the Zachary carate club


plot(fg, vertex.size=10)
closeness(fg)
plot(st, vertex.size=10, vertex.label=NA)
closeness(st)
plot(tr, vertex.size=10, vertex.label=NA)
closeness(tr)
plot(rn, vertex.size=10, vertex.label=NA)
closeness(rn)
plot(er, vertex.size=10, vertex.label=NA)
closeness(er)
plot(sw, vertex.size=10, vertex.label=NA)
closeness(sw)
plot(ba, vertex.size=10, vertex.label=NA)
closeness(ba)
plot(zach, vertex.size=10, vertex.label=NA)
closeness(zach)

closeness(fg)
eccentricity(fg)
degree(fg)


betweenness(fg)
edge_betweenness(fg)
component_distribution(fg)
cluster_edge_betweenness(fg)

degree_distribution(fg)

radius(fg)