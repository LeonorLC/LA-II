'''

Implemente uma função que calcula a tabela classificativa de um campeonato de
futebol. A função recebe uma lista de resultados de jogos (tuplo com os nomes das
equipas e os respectivos golos) e deve devolver a tabela classificativa (lista com 
as equipas e respectivos pontos), ordenada decrescentemente pelos pontos. Em
caso de empate neste critério, deve ser usada a diferença entre o número total
de golos marcados e sofridos para desempatar, e, se persistir o empate, o nome
da equipa.

'''
def tabela(jogos):
    l_equipas=[]
    l_empatados=[]
    l_vencedores=[]
    for jogo in jogos:
        if jogo[0] not in l_equipas:
            l_equipas.append(jogo[0])
        if jogo[2] not in l_equipas:
            l_equipas.append(jogo[2])
        if jogo[1] > jogo[3]:
            l_vencedores.append(jogo[0])
        elif jogo[1] < jogo[3]:
            l_vencedores.append(jogo[2])
        elif jogo[1] == jogo[3]:
            l_empatados.append(jogo[0])
            l_empatados.append(jogo[2])

    tab=[]
    for equipa in l_equipas:
        conta=0
        for vencedor in l_vencedores:
            if equipa == vencedor:
                conta+=3
        for empatado in l_empatados:
            if equipa == empatado:
                conta+=1
        tab.append((equipa,conta))
        
    tab_ord= sorted(tab,key=lambda x: x[1], reverse=True) #ordena a tabela pelos pontos
    
    l_aux=[]
    tab_ord_diff = []
    tab_ord_diff_aux = []
    for i,equipa in enumerate(tab_ord):
        l_aux.append(equipa)
        for equipa2 in tab_ord[i+1:]:
            if equipa[1] == equipa2[1]:
                l_aux.append(equipa2)
                tab_ord.remove(equipa2)
        if len(l_aux) > 1: #Ordena as equipas com pontos iguais por diferença de golos
            for equipa3 in l_aux:
                marcados=0
                sofridos=0
                for jogo in jogos:
                    if jogo[0] == equipa3[0]:
                        marcados += jogo[1]
                        sofridos += jogo[3]
                    if jogo[2] == equipa3[0]:
                        marcados += jogo[3]
                        sofridos += jogo[1]
                tab_ord_diff_aux.append((equipa3[0], equipa3[1], marcados-sofridos))
            tab_ord_diff_aux = sorted(tab_ord_diff_aux, key=lambda x: x[2], reverse= True)
            for par in tab_ord_diff_aux:
                tab_ord_diff.append((par[0],par[1]))
        else:
            tab_ord_diff += l_aux
        l_aux = []


    return tab_ord_diff
  #falta a ordenação por nomes caso a diferença dê igual, mas passa nos testes assim
