"""

Um exemplo de um problema que pode ser resolvido de forma eficiente com 
programação dinâmica consiste em determinar, dada uma sequência arbitrária de 
números não negativos, se existe uma sub-sequência (não necessariamente contígua) 
cuja soma é um determinado valor. Implemente uma função que dado um valor e uma
listas de listas de números não negativos, devolva a lista com as listas com uma
sub-sequência cuja soma é o valor dado.

"""
def somas(soma, lista):
    if lista == [] or soma == 0:
        return False
    ant = lista[0]
    for elem in lista:
        if (ant + elem) == soma:
            return True
        elif (ant + elem) < soma:
            ant += elem
        else:
            return False
def validas(soma,listas):
    if listas == [] or soma == 0:
        return []
    val = []
    for lista in listas:
        for i,elem in enumerate(lista):
            if somas(soma, lista[i:]) == True and lista not in val:
                val.append(lista)
    return val
