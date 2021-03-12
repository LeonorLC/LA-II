'''
Podemos usar um (multi) grafo para representar um mapa de uma cidade: 
cada nó representa um cruzamento e cada aresta uma rua.

Pretende-se que implemente uma função que lista os cruzamentos de uma cidade 
por ordem crescente de criticidade: um cruzamento é tão mais crítico quanto 
maior o número de ruas que interliga.

A entrada consistirá numa lista de nomes de ruas (podendo assumir que os nomes de ruas são únicos). 
Os identificadores dos cruzamentos correspondem a letras do alfabeto, e cada rua começa (e acaba) no cruzamento 
identificado pelo primeiro (e último) caracter do respectivo nome.

A função deverá retornar uma lista com os nomes dos cruzamentos por ordem crescente de criticidade, 
listando para cada cruzamento um tuplo com o respectivo identificador e o número de ruas que interliga.
Apenas deverão ser listados os cruzamentos que interliguem alguma rua, e os cruzamentos com o mesmo 
nível de criticidade deverão ser listados por ordem alfabética.
'''

def cruzamentos(ruas):
    l_letras=[]
    for rua in ruas:
        if rua[0] != rua[-1]:
            l_letras.append(rua[0])
            l_letras.append(rua[-1])
        else:
            l_letras.append(rua[0])

    l_final=[]
    letrasUsadas=[]
    for i, letra1 in enumerate(l_letras):
        conta=1
        for letra2 in l_letras[i+1:]:
            if letra2 == letra1:
                conta += 1
        if letra1 not in letrasUsadas:
            l_final.append((letra1,conta))
            letrasUsadas.append(letra1)

    l_final= sorted(l_final,key=lambda x: (x[1],x[0]))
    

    return l_final
