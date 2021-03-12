'''
Pretende-se que implemente uma função que detecte códigos ISBN inválidos. 
Um código ISBN é constituído por 13 digitos, sendo o último um digito de controlo.
Este digito de controlo é escolhido de tal forma que a soma de todos os digitos, 
cada um multiplicado por um peso que é alternadamente 1 ou 3, seja um múltiplo de 10.
A função recebe um dicionário que associa livros a ISBNs,
e deverá devolver a lista ordenada de todos os livros com ISBNs inválidos.
'''

def isbn(livros):
    numeros=list(livros.values())
    l=[]
    
    for num  in numeros :
        n = ''
        lista_cada=[]
        for digito in num:
            lista_cada.append(digito)
        l.append(lista_cada)
    
    l_final=[]
    sumP=sumI=0
    for lista_cada in l:
        i=0
        sumP=sumI=0
        for digito in lista_cada:
    
            if i == 0 or i%2 == 0:
                sumP += int(digito)*1
                sumI += int(digito)*3
            else:
                sumP += int(digito)*3
                sumI += int(digito)*1
            i = i+ 1
        
        if sumP%10 != 0 and sumI%10 != 0: 
            l_final.append(''.join(lista_cada))

    res = []
    itemsList = livros.items()
    for num in l_final:
        for item in itemsList:
            if item[1] == num:
                res.append(item[0])

    return sorted(res)
