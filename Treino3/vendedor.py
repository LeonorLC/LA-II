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
def aux(capacidade, produtos, p):
    if produtos == [] or capacidade == 0:
        return 0
    if produtos[0][2] > capacidade:
        return 0
    ant = p[2]
    lucro = p[1]
    vendeu = [p[0]]
    res = [(p[1], [p[0]])]
    for prod in produtos:
        if (ant + prod[2]) <= capacidade:
            ant += prod[2]
            lucro += prod[1]
            vendeu.append(prod[0])
            res.append((lucro, vendeu))
    return max(res, key = lambda x: x[0]) 

def vendedor(capacidade, produtos):
    if produtos == [] or capacidade == 0:
        return (0, [])
    produtos = sorted(produtos, key = lambda x : x[0])
    d = {}
    vendeu = []
    for p in produtos:
        if p[2] > capacidade:
            produtos.remove(p)
        else:
            d[p] = (aux(capacidade, produtos, p))
    return d[max(d.keys(), key=(lambda x: d[x]))]
