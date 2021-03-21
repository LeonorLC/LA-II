'''

O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.

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

def maior(vizinhos):
    fronteiras = []
    for viz in vizinhos:
        for i,v in enumerate(viz):
            if i+1 < len(viz):
                fronteiras.append((v,viz[i+1]))
    
    paises = []
    for vizinho in vizinhos:
        for pais in vizinho:
            if pais not in paises:
                paises.append(pais)
                
    contiTamanhos = []
    for pais in paises:
        tam = len(bfs(build(fronteiras),pais))
        contiTamanhos.append(tam)
    
    comp=0
    for t in contiTamanhos:
        if t > comp:
            comp = t
    return comp+1

#Só passa 8% de 13% dos testes

####Outra versão, passa menos  testes####
def maior(vizinhos):
    
    if len(vizinhos) == 0:
        return 0
    
    continentes = [vizinhos[0]]
    paisesVisitados = []
    
    for v in vizinhos[0]:
        paisesVisitados.append(v)
        
    vizinhos.pop(0)
    
    
    
    for viz in vizinhos:
        acrescenta = 0
        for pais in viz:
            if pais in paisesVisitados:
                acrescenta = 1
                for continente in continentes:
                    if pais in continente:
                        for p in viz:
                            if p not in continente:
                                continente.append(p)
                                paisesVisitados.append(p)
                break
        if acrescenta == 0:
            continentes.append(viz)
        else: 
            acrescenta = 0
                    
    continentes
    
    comp = 0
    for continente in continentes:
        if comp < len(continente):
            comp = len(continente)
    
    
    return comp
  
 #Só passa 5% de 13% dos testes
