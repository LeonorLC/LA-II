"""
Um hacker teve acesso a um log de transações com cartões de
crédito. O log é uma lista de tuplos, cada um com os dados de uma transação,
nomedamente o cartão que foi usado, podendo alguns dos números estar
ocultados com um *, e o email do dono do cartão.

Pretende-se que implemente uma função que ajude o hacker a 
reconstruir os cartões de crédito, combinando os números que estão
visíveis em diferentes transações. Caso haja uma contradição nos números 
visíveis deve ser dada prioridade à transção mais recente, i.é, a que
aparece mais tarde no log.

A função deve devolver uma lista de tuplos, cada um com um cartão e um email,
dando prioridade aos cartões com mais digitos descobertos e, em caso de igualdade
neste critério, aos emails menores (em ordem lexicográfica).
"""

def repetidos(l_final, x):
    if len(l_final) == 0:
        return False
    for elem in l_final:
        if elem[1] == x[1]:
            return True
    return False   
    
def conta (cartao):
    conta=0
    for digito in cartao[0]:
        if digito != '*':
              conta+=1
    return conta

def hacker(log):
    i=0
    x=''
    l_aux = []
    l_final = []
    number_final = []
    for i,x in enumerate(log):
        l_aux.append(x)
        for p,e in enumerate(log[i+1:]):
            if x[1] == e[1]:
                l_aux.append(e)
        if len(l_aux) > 1 and not repetidos(l_final, l_aux[0]):
            number_final = list(l_aux[0][0])
            for number in l_aux[1:]:
                for pos, digito in enumerate(list(number)[0]):
                    if digito != '*':
                        number_final[pos] = digito
            l_final.append((''.join(number_final), l_aux[0][1]))
        else:
            if not repetidos(l_final, x):
                l_final.append(x)
        l_aux = []
    l_sorted=sorted(l_final, key=conta, reverse= True)
    l_aux2 = []
    resultado = []
    i=0
    for i,elem in enumerate(l_sorted):
        count = conta(elem)
        l_aux2.append(elem)
        for elem2 in l_sorted[i+1:]:
            if count == conta(elem2):
                l_aux2.append(elem2)
                l_sorted.remove(elem2)
        resultado += sorted(l_aux2, key=lambda x: x[1])
        l_aux2 = []

    return resultado
