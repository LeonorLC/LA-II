'''
Neste problem pretende-se que defina uma função que, dada uma string com palavras, 
devolva uma lista com as palavras nela contidas ordenada por ordem de frequência,
da mais alta para a mais baixa. Palavras com a mesma frequência devem ser listadas 
por ordem alfabética.
'''
import operator

def frequencia(texto):
    l = []
    pal = ''
    for letra in texto:
        if letra == ' ':
            if pal != '':
                l.append(pal)
                pal = ''
        else:
            pal += letra
    if pal != '':
        l.append(pal)
        pal = ''

    d={}
    for palavra in l:
        if palavra in d:
            d[palavra]=d[palavra]+1
        else:
            d[palavra]=1

    d_ordenado=sorted(d.items(), key=operator.itemgetter(1),reverse=True)

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

    ll=[]
    for pal in lista:
        ll.append(pal[0])
        
    return ll
