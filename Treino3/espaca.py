"""

Implemente uma função que, dada uma frase cujos espaços foram retirados, 
tenta recuperar a dita frase. Para além da frase (sem espaços nem pontuação), 
a função recebe uma lista de palavras válidas a considerar na reconstrução 
da dita frase. Deverá devolver a maior frase que pode construir inserindo
espaços na string de entrada e usando apenas as palavras que foram indicadas 
como válidas. Por maior entende-se a que recupera o maior prefixo da string
de entrada. Só serão usados testes em que a maior frase é única.

"""
def palavra (letraInicial, posInicial, frase, palavras, compMaior):
    if frase == "" or palavras == []:
        return ""
    pal = letraInicial
    posFinal = 0 
    l = ""
    for i,letra in enumerate(frase):
        if len(pal) < compMaior and (pal + letra) in palavras:
            l = (pal+letra)
            posFinal = i
        pal += letra
    if l == "":
        l = letraInicial
    posFinal += posInicial + 1
    return (l, posFinal)

def espaca(frase, palavras):
    if frase == "" or palavras == []:
        return ""
    compMaior = max(map(len, palavras))
    fraseFinal = ""
    i = 0
    p = ""
    while i < len(frase):
        (pal, pos) = palavra(frase[i], i+1, frase[i+1:], palavras, compMaior)
        fraseFinal += pal + " "
        if len(pal) == 1:
            (pal, pos) = palavra(frase[i+1], i+1, frase[i+1:], palavras, compMaior)
            fraseFinal += pal + " "
        i = pos
    return fraseFinal[:-1]
