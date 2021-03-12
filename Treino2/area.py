'''

Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 

'''

def adjacentes (pos, mapa):
    adj=[]
    px=pos[0]-1
    py=pos[1]-1
    comp = len(mapa[0])
    
    if py-1 >= 0 and mapa[py-1][px] == '.':
        adj.append((px+1,py))
    if px-1 >= 0 and mapa[py][px-1] == '.':
        adj.append((px,py+1))
    if px+1 < comp and mapa[py][px+1] == '.':
        adj.append((px+2,py+1))
    if py+1 < comp and mapa[py+1][px] == '.':
        adj.append((px+1,py+2))                        
    
    return adj

def area(p,mapa):
    queue = [p]
    visitados = []
    adj = []
    listaFinal=[]
    
    while queue:
        adj = adjacentes(queue[0], mapa)
        for adjV in adj:
            if adjV not in visitados and adjV not in queue:
                queue.append(adjV)
            if adjV not in listaFinal:
                listaFinal.append(adjV)
        visitados.append(queue[0])
        queue.pop(0)
        
    

    return len(listaFinal)
