"""

Implemente uma função que determina qual a probabilidade de um robot regressar 
ao ponto de partido num determinado número de passos. Sempre que o robot dá um 
passo tem uma determinada probabilidade de seguir para cima ('U'), baixo ('D'), 
esquerda ('L') ou direita ('R'). A função recebe o número de passos que o 
robot vai dar e um dicionário com probabilidades de se movimentar em cada uma
das direcções (as chaves são os caracteres indicados entre parêntesis).
O resultado deve ser devolvido com a precisao de 2 casas decimais.

"""
def probabilidade(passos, probs):
    if passos == 0 or probs == {}:
        return 0
    pro = {}
    limiteU = passos
    limiteD = -passos
    posX = [0, 0, 1,-1]
    posY = [1, -1, 0, 0]
    movs = ['U', 'D', 'R', 'L']
    res = 0
    
    for x in range(limiteD, limiteU+1):
        for y in range(limiteD, limiteU+1): 
            for p in range(0, passos+1):
                pro[p, x, y] = 0.0
                
    pro[0,0,0] = 1.0
    
    for passo in range(1, passos+1):
        for x in range(limiteD, limiteU):
            for y in range(limiteD, limiteU):
                for i in range(4):
                    if limiteD <= (x + posX[i]) <= limiteU and limiteD <= (y + posY[i]) <= limiteU:
                        anterior = probs[movs[i]]*pro[passo-1, x + posX[i], y + posY[i]]
                        pro[passo, x, y] += anterior
                    
    
    return round(pro[passos,0,0],2)
