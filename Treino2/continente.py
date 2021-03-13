'''

O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.

'''

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
