'''
Defina uma função que recebe um número positivo
e produz a soma dos seus factores primos distintos.
'''

def factoriza(n):
    l=[]
    for num in range(1, n+1):
        if n % num == 0:
            k = 0
            for j in range(1, num+1):
                if num % j == 0:
                    k = k + 1
            if k == 2:
                l.append(num)
    
    soma=0
    for fator in l:
        soma += fator
    return soma
