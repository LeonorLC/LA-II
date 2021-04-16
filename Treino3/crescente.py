"""

Implemente uma função que dada uma sequência de inteiros, determinar o 
comprimento da maior sub-sequência (não necessariamente contígua) que se 
encontra ordenada de forma crescente.

Sugere-se que comece por implementar uma função auxiliar recursiva que determina 
o comprimento da maior sub-sequência crescente que inclui o primeiro elemento
da sequência, sendo o resultado pretendido o máximo obtido aplicando esta
função a todos os sufixos da sequência de entrada.

"""
#Versão programação dinâmica (13%)
def crescente(lista):
    if len(lista) == 0:
        return 0
    comp = len(lista)
    compCres = [1 for x in range(comp+1)]
    compCres[0] = 0
    maior = 1
    for x in range(2, comp+1):
        for y in range(x-1, 0, -1): #começa no x-1, vai até ao 0 decrementando 1
            if lista[x-1] >= lista[y-1]:
                compCres[x] = max(compCres[x], compCres[y] + 1)
        maior = max(maior, compCres[x])
    return maior

#Versão Recursiva (9%)
def maior(lista):
    if lista == []:
        return 0
    comprimento = 1
    ant = lista[0]
    for i in range(len(lista)):
        if ant <= lista[i]:
            ant = lista[i]
            comprimento += 1
    return comprimento

def crescente(lista):
    d = {}
    if lista == []:
        return 0
    for i,elem in enumerate(lista):
        d[elem] = (maior(lista[i:]) -1)
    return d[max(d.keys(), key=(lambda x: d[x]))]
