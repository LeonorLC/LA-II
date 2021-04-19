"""

Um vendedor ambulante tem que decidir que prod
utos levará na sua próxima viagem.
Infelizmente, tem um limite de peso que pode transportar e, tendo isso em atenção, 
tem que escolher a melhor combinação de produtos a transportar dentro desse limite 
que lhe permitirá ter a máxima receita.

Implemente uma função que, dado o limite de peso que o vendedor pode transportar, 
e uma lista de produtos entre os quais ele pode escolher (assuma que tem à sua 
disposição um stock ilimitado de cada produto), devolve o valor de receita máximo
que poderá obter se vender todos os produtos que escolher transportar, e a lista
de produtos que deverá levar para obter essa receita (incluindo repetições, 
caso se justifique), ordenada alfabeticamente.

Cada produto consiste num triplo com o nome, o valor, e o peso.

Caso haja 2 produtos com a mesma rentabilidade por peso deverá dar prioridade 
aos produtos que aparecem primeiro na lista de entrada.

"""
#Versão programação dinâmica (13%)
def vendedor(capacidade, produtos):
    if produtos == [] or capacidade == 0:
        return (0,[])
    transp = [[(0,[]) for x in range(capacidade + 1)] for y in range(len(produtos) + 1)]
    
    for i in range(len(produtos) + 1):
        for peso in range(capacidade + 1):
            if i == 0 or peso == 0:
                transp[i][peso] = (0,[])
            elif peso < produtos[i-1][2]:
                transp[i][peso] = transp[i-1][peso]
            else:
                a = transp[i-1][peso]
                b = transp[i][peso-produtos[i-1][2]]
                c = transp[i-1][peso-produtos[i-1][2]]
                b = (b[0] + produtos[i-1][1], b[1] + [produtos[i-1][0]])
                c = (c[0] + produtos[i-1][1], c[1] + [produtos[i-1][0]])
                
                transp[i][peso] = max(a, b, c, key=lambda x: x[0])
                
    transp[len(produtos)][capacidade][1].sort()
    return transp[len(produtos)][capacidade]

#Versão Recursiva (8%)
#Auxiliar
def aux(capacidade, produtos, p):
    if produtos == [] or capacidade == 0:
        return 0
    if produtos[0][2] > capacidade:
        return 0
    produtos = sorted(produtos, key = lambda x : x[0])
    ant = p[2]
    lucro = p[1]
    vendeu = [p[0]]
    res = [(p[1], [p[0]])]
    for prod in produtos:
        while ant + prod[2] <= capacidade:
            ant += prod[2]
            lucro += prod[1]
            vendeu.append(prod[0])
            vendeu = sorted(vendeu)
            res.append((lucro, vendeu))
    return max(res, key = lambda x: x[0]) 

def vendedor(capacidade, produtos):
    if produtos == [] or capacidade == 0:
        return (0, [])
    d = {}
    vendeu = []
    for p in produtos:
        if p[2] > capacidade:
            produtos.remove(p)
        else:
            d[p] = (aux(capacidade, produtos, p))
    return d[max(d.keys(), key=(lambda x: d[x]))]
