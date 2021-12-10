library(igraph)

g <- erdos.renyi.game(p.or.m=0.05, n=100)
summary(g) # nie jest ważony

E(g)
V(g)

E(g)$weight <- runif(length(E(g)), 0.01, 1)
summary(g) # jest wazony

degree(g)
hist(degree(g))

cl <- clusters(g)
cl

pr <- page.rank(g)$vector
plot(g, vertex.size=pr*300, vertex.label=NA, edge.arrow.size=.2)

# ------------------------------------------------------------------------------

g <- barabasi.game(1000)
layout <- layout.fruchterman.reingold(g)
plot(g, layout=layout, vertex.size=2, vertex.label=NA, edge.arrow.size=.2)
  
V(g)[betweenness(g)==max(betweenness(g))]
betweenness(g)
diameter(g)

# Zasadniczo są one tworzone na różne sposoby: W sieci Erdos-Renyi przypisujemy 
# N węzłów, a następnie każdą parę łączymy z prawdopodobieństwem p. 
# Oznacza to, że żaden węzeł nie będzie miał znacznie wyższego stopnia niż jakikolwiek inny.
# W sieci B-A przypisujemy N węzłów, ale aby je utworzyć, zaczynamy 
# od małego zestawu połączonych węzłów. Następnie dodajemy węzły pojedynczo, 
# aż otrzymamy N węzłów. Kiedy dodajemy węzeł, łączymy go z niewielką liczbą 
# istniejących węzłów z prawdopodobieństwem proporcjonalnym do stopnia 
# istniejącego węzła. W rezultacie węzły z wyższym stopniem (wcześniejsze) 
# mają tendencję do uzyskiwania jeszcze wyższego stopnia.

# ------------------------------------------------------------------------------

dfGraph <- read.csv2("./database.csv", skip=2, sep= " ")[, 1:2]
g <- graph.data.frame(dfGraph, directed = T)
g <- simplify(g)

E(g)
V(g) # "Czy Twój graf ma 167 węzłów i 5783 krawędzie?" - TAK

V(g)$activated = F
V(g)[13]$activated = T

summary(g)

setup <- function (gr, svi) {
  V(gr)$activated = F
  V(gr)$color = 'red'
  V(gr)[svi]$activated = T
  V(gr)[svi]$color = 'green'
  return (gr)
}

activate_neighbors <- function (av, gr) {
  ac <- 0
  for(v in av) {
    nb <- neighbors(gr, v)
    ac = ac + length(nb[activated == F])
    V(gr)[nb]$activated = T
    V(gr)[nb]$color = 'green'
  }
  print(ac)
  return (gr)
}

simulate_propagation <- function (noi, gr) {
  for(i in 1:noi) {
    active <- V(gr)[activated == T]
    gr <- activate_neighbors(active, gr)
    write.csv(as_data_frame(gr, what="vertices"), sprintf("./file-%d.csv",i), row.names = FALSE)
    plot(gr, vertex.color=V(gr)$color)
  }
}

rand_indices = sample(1:100, 4)
for (r in rand_indices) {
  g <- setup(g, r)
  simulate_propagation(10, g)
}

# Centralny
g <- setup(g, betweenness(g)==max(betweenness(g)))
# simulate_propagation(10, g)