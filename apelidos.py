'''
Defina uma função que, dada uma lista de nomes de pessoas, devolva essa lista ordenada 
por ordem crescente do número de apelidos (todos menos o primeiro nome). No caso de pessoas com o mesmo número de apelidos,
devem ser listadas por ordem lexicográfica do nome completo.
'''
import operator

def apelidos(nomes):
    d={}
    for nome in nomes:
        pal = ''
        apelidos=0
        for letra in nome:
            if letra == ' ':
                if pal != '':
                    apelidos += 1
                    pal = ''
            else:
                pal += letra
        if pal != '':
            apelidos += 1
            pal = ''       
        d[nome]=apelidos-1
    
    d_ordenado=sorted(d.items(), key=operator.itemgetter(1))
    
    lista=[]
    lista_aux=[]
    for elem in d_ordenado:
        if len(lista_aux) == 0:
            lista_aux.append(elem)
        elif lista_aux[0][1] == elem[1]:
            lista_aux.append(elem)
        else:
            lista_aux = sorted(lista_aux)
            lista = lista + lista_aux
            lista_aux=[]
            lista_aux.append(elem)

    lista_aux = sorted(lista_aux)
    lista = lista + lista_aux

    l_ord=[]
    for nome in lista:
        l_ord.append(nome[0])
    
    return l_ord
