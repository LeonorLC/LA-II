"""

Implemente uma função que dado um dicionário com as preferências dos alunos
por projectos (para cada aluno uma lista de identificadores de projecto, 
por ordem de preferência), aloca esses alunos aos projectos. A alocação
é feita por ordem de número de aluno, e cada projecto só pode ser feito
por um aluno. A função deve devolver a lista com os alunos que não ficaram
alocados a nenhum projecto, ordenada por ordem de número de aluno.

"""

def aloca(prefs):
    lista_chave_ord=sorted(prefs.keys())
    l=[]
    for chave in lista_chave_ord:
        items=prefs[chave]
        for item in items:
            if item not in l:
                l.append(item)
                del prefs[chave]
                break
    return list(prefs.keys())
