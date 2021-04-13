"""

Um ladrão assalta uma casa e, dado que tem uma capacidade de carga limitada, 
tem que decidir que objectos vai levar por forma a maximizar o potencial lucro. 

Implemente uma função que ajude o ladrão a decidir o que levar.
A função recebe a capacidade de carga do ladrão (em Kg) seguida de uma lista 
dos objectos existentes na casa, sendo cada um um triplo com o nome, o valor de 
venda no mercado negro, e o seu peso. Deve devolver o máximo lucro que o ladrão
poderá  obter para a capacidade de carga especificada.

"""
def aux(capacidade, objetos):
    if objetos == [] or capacidade == 0:
        return 0
    objetos = sorted(objetos, key = lambda x : x[1], reverse = True)
    ant = objetos[0][2]
    lucro = objetos[0][1]
    lucros = [objetos[0][1]]
    for o in objetos[1:]:
        if (ant + o[2]) <= capacidade:
            ant += o[2]
            lucro += o[1]
            lucros.append(lucro)
    return max(lucros)

def ladrao(capacidade,objetos):
    if objetos == [] or capacidade == 0:
        return 0
    d = {}
    for i, o in enumerate(objetos):
        d[o] = (aux(capacidade, objetos[i:]))
    return d[max(d.keys(), key=(lambda x: d[x]))]
