'''

Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista 
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.

'''

def build(arestas):
    adj = {}
    for o,d in arestas:
        if o not in adj:
            adj[o] = set()
        if d not in adj:
            adj[d] = set()
        adj[o].add(d)
        adj[d].add(o)
    return adj
    
def bfs(adj,o):
    pai = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                pai[d] = v
                queue.append(d)
    return pai
    
def caminhos(adj,o,d):
    pai = bfs(adj,o)
    caminho = [d]
    while d in pai:
        d = pai[d]
        caminho.insert(0,d)
    return caminho

def caminho(mapa):
    adj=[]
    compD = len(mapa[0])
    compS = len(mapa)
    visitados=[]
    for s,pontos in enumerate(mapa):
        for d,ponto in enumerate(pontos):
            if s+1 < compS and mapa[s][d] == ' ' and mapa[s+1][d] == ' ':
                adj.append(((s,d),(s+1,d)))
            if d+1 < compD and mapa[s][d] == ' ' and mapa[s][d+1] == ' ':
                adj.append(((s,d),(s,d+1)))
    
    path = caminhos(build(adj),(0,0),(len(mapa[0])-1,len(mapa)-1))
    anterior = path[0]
    pathFinal = ""
    
    for coordenada in path[1:]:
        if coordenada[0] == anterior[0] and coordenada[1] == anterior[1]+1:
            pathFinal += 'E'
        elif coordenada[0] == anterior[0] and coordenada[1] == anterior[1]-1:
            pathFinal += 'O'
        elif coordenada[0] == anterior[0]+1 and coordenada[1] == anterior[1]:
            pathFinal += 'S'
        elif coordenada[0] == anterior[0]-1 and coordenada[1] == anterior[1]:
            pathFinal += 'N'
        anterior = coordenada
    
    return  pathFinal
  
#Só passa 10% de 13% dos testes
