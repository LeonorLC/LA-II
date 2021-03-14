'''

Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.
Pretende-se que implemente uma função que calcula o tamanho de uma cidade, 
sendo esse tamanho a distância entre os seus cruzamentos mais afastados.
A entrada consistirá numa lista de nomes de ruas (podendo assumir que os 
nomes de ruas são únicos). Os identificadores dos cruzamentos correspondem a 
letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

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

#Função Floyd-Warshall dos slides (teórica 2)
def fw(adj):
    dist = {}
    for o in adj:
        dist[o] = {}
        for d in adj:
            if o == d:
                dist[o][d] = 0
            elif d in adj[o]:
                dist[o][d] = adj[o][d]
            else:
                dist[o][d] = float("inf")
    for k in adj:
        for o in adj:
            for d in adj:
                if dist[o][k] + dist[k][d] < dist[o][d]:
                    dist[o][d] = dist[o][k] + dist[k][d]
    return dist
    
def tamanho(ruas):
    arestas=[]
    cruzamentos=[]
    for rua in ruas:
        if rua[0]+rua[-1] not in cruzamentos:
            arestas.append((rua[0], rua[-1], len(rua)))
            cruzamentos.append(rua[0]+rua[-1])
        else:
            for aresta in arestas:
                if rua[0] == aresta[0] and rua[-1] == aresta[1] and len(rua) < aresta[2]:
                    arestas.remove(aresta)
                    arestas.append((rua[0], rua[-1], len(rua)))
                    break

    pesosDic = fw(build(arestas))
    maior = 0
    for o in pesosDic:
        for d in pesosDic[o]:
            dist = pesosDic[o][d]
            if dist > maior:
                maior = dist

    return maior
  
  #Passa os testes todos (13%)
