"""

Implemente uma função que calula qual a subsequência (contígua e não vazia) de 
uma sequência de inteiros (também não vazia) com a maior soma. A função deve 
devolver apenas o valor dessa maior soma.

Sugere-se que começe por implementar (usando recursividade) uma função que 
calcula o prefixo de uma sequência com a maior soma. Tendo essa função 
implementada, é relativamente adaptá-la para devolver também a maior soma de toda
a lista.

"""
def somaAux(lista, d):
    if lista == []:
        return 0
    soma = 0
    for elem in lista:
        d[elem] = (soma + elem)
        soma += elem
    return d[max(d.keys(), key=(lambda x: d[x]))]

def maxsoma(lista):
    if lista == []:
        return 0
    if len(lista) == 1:
        return lista[0]
    l = []
    for i,elem in enumerate(lista):
        l.append(somaAux(lista[i:], {}))
    print(l)
    return max(l)
