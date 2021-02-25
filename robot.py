'''
Neste problema prentede-se que implemente uma função que calcula o rectângulo onde se movimenta um robot.

Inicialmente o robot encontra-se na posição (0,0) virado para cima e irá receber uma sequência de comandos numa string.
Existem quatro tipos de comandos que o robot reconhece:
  'A' - avançar na direcção para o qual está virado
  'E' - virar-se 90º para a esquerda
  'D' - virar-se 90º para a direita 
  'H' - parar e regressar à posição inicial virado para cima
  
Quando o robot recebe o comando 'H' devem ser guardadas as 4 coordenadas (minímo no eixo dos X, mínimo no eixo dos Y, máximo no eixo dos X, máximo no eixo dos Y) que definem o rectângulo 
onde se movimentou desde o início da sequência de comandos ou desde o último comando 'H'.

A função deve retornar a lista de todas os rectangulos (tuplos com 4 inteiros)
'''
def robot(comandos):
    direcao = 0 # 0->ypos; 1->xpos; 2->yneg; 3->xneg
    xmin = 0
    xmax = 0
    ymin = 0
    ymax = 0
    l_ret=[]
    i=0
    xAtual = 0
    yAtual = 0
    while i < len(comandos):
        if comandos[i] == 'A':
            if direcao == 0:
                yAtual += 1
                if ymax < yAtual:
                    ymax = yAtual
            elif direcao == 1:
                xAtual += 1
                if xmax < xAtual:
                    xmax = xAtual
            elif direcao == 2:
                yAtual -= 1
                if ymin > yAtual:
                    ymin = yAtual
            elif direcao == 3:
                xAtual -= 1
                if xmin > xAtual:
                    xmin = xAtual
        elif comandos[i] == 'E':
            direcao = (direcao-1)%4
        elif comandos[i] == 'D':
            direcao = (direcao+1)%4
        elif comandos[i] == 'H':
            l_ret.append((xmin, ymin, xmax, ymax))
            direcao = 0
            xAtual = 0
            yAtual = 0
            xmin = 0
            xmax = 0
            ymin = 0
            ymax = 0
        i += 1
    return l_ret
