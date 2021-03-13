'''

O número de Erdos é uma homenagem ao matemático húngaro Paul Erdos,
que durante a sua vida escreveu cerca de 1500 artigos, grande parte deles em 
pareceria com outros autores. O número de Erdos de Paul Erdos é 0. 
Para qualquer outro autor, o seu número de Erdos é igual ao menor 
número de Erdos de todos os seus co-autores mais 1. Dado um dicionário que
associa artigos aos respectivos autores, implemente uma função que
calcula uma lista com os autores com número de Erdos menores que um determinado 
valor. A lista de resultado deve ser ordenada pelo número de Erdos, e, para
autores com o mesmo número, lexicograficamente.

'''

def tratouAutores(autores, erdos, visitados):
    for erdo in erdos:
        if erdo[0] in autores:
            for autor in autores:
                if autor not in visitados:
                    erdos.append((autor, erdo[1]+1))
                    visitados.append(autor)
                    erdos=sorted(erdos, key=lambda x: (x[1],x[0]))
            return (erdos, True)
    return (erdos, False)
    
def acabou(listaAutores, visitados):
    for autores in listaAutores:
        for autor in autores:
            if autor in visitados:
                return False
    return True

def erdos(artigos,n):
    erdos=[('Paul Erdos', 0)]
    visitados=['Paul Erdos']
    listaAutores=list(artigos.values())
    while listaAutores and not acabou(listaAutores, visitados):
        erdos, tratou = tratouAutores(listaAutores[0],erdos, visitados)
        if tratou:
            listaAutores.pop(0)
        else:
            listaAutores.append(listaAutores.pop(0))
    
    erdosF=[]
    for erdo in erdos:
        if erdo[1] <= n:
            erdosF.append(erdo[0])
        else:
            break
    
    return erdosF

#Só passa 10% de 13% dos testes
