'''
Implemente uma função que determine qual a menor sequência de caracters que
contém n repetições de uma determinada palavra
'''
def repete(palavra,n):
    if n == 0:
        return ''
    p=palavra
    if palavra[0] == palavra[-1]:
        while n > 1:
            p += palavra[1:]
            n -= 1
    else:
        while n > 1:
            p += palavra
            n -= 1
    return p
