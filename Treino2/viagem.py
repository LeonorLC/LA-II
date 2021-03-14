'''

Implemente uma função que calcula o preço mais barato para fazer uma viagem de
autocarro entre duas cidades. A função recebe (para além das duas cidades) uma
lista de rotas de autocarro, onde cada rota é uma sequência de cidades por onde
passa o autocarro, intercalada com o custo para viajar entre cada par de cidades.
Assuma que cada rota funciona nos dois sentidos.

'''


#Função build dos slides (teórica 2)
def build(arestas):
    adj = {}
    for o,d,p in arestas:
        if o not in adj:
            adj[o] = {}
        if d not in adj:
            adj[d] = {}
        adj[o][d] = p
        adj[d][o] = p
    return adj

#Função Dijkstra dos slides (teórica 2)    
def dijkstra(adj,o, destino):
    pai = {}
    dist = {}
    dist[o] = 0
    orla = {o}
    while orla:
        v = min(orla,key=lambda x:dist[x])
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                pai[d] = v
                dist[d] = dist[v] + adj[v][d]
    return dist[destino]


def viagem(rotas,o,d):
    arestas=[]
    for rota in rotas:
        for i,viagem in enumerate(rota):
            if i%2 == 0 and (i+1) < len(rota) and (i+2) < len(rota):
                arestas.append((rota[i], rota[i+2], rota[i+1]))
                
    return dijkstra(build(arestas), o, d)

#Só passa 10% de 13% dos testes
