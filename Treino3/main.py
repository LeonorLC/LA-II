##
# Main function of the Python program.
#
##

from vendedor import vendedor
from ladrao import ladrao
from soma import maxsoma
from validas import validas
from espaca import espaca
from saque import saque
from robot import probabilidade
from crescente import crescente

def main():
    
    print("<h3>crescente</h3>")
    lista = [5,2,7,4,3,8]
    print("in:",lista)
    print("out:",crescente(lista))
    
    print("<h3>ladrao</h3>")
    objectos = [("microondas",30,6),("jarra",14,3),("giradiscos",16,4),("radio",9,2)]
    print("in:",10,objectos)
    print("out:",ladrao(10,objectos))
    
    print("<h3>vendedor</h3>")
    produtos = [("biblia",20,2),("microondas",150,10),("televisao",200,15),("torradeira",40,3)]
    print("in:",14,produtos)
    print("out:",vendedor(14,produtos))

    print("<h3>maxsoma</h3>")
    lista = [-2,1,-3,4,-1,2,1,-5,4]
    print("in:",lista)
    print("out:",maxsoma(lista))

    print("<h3>probabilidade</h3>")
    probs = {'U':0.25,'D':0.25,'L':0.25,'R':0.25}
    print("in:",2,probs)
    print("out:",probabilidade(2,probs))

    print("<h3>valida</h3>")
    listas = [[8,1,7,3,3,6,3,5],[1,1,1,2,3,1,2],[3,3,3,3]]
    print("in:",10,listas)
    print("out:",validas(10,listas))

    print("<h3>espaca</h3>")
    palavras = ["e","o","so","maior","este","curso","urso","es","maio"]
    print("in:","estecursoeomaior",palavras)
    print("out:",espaca("estecursoeomaior",palavras))
    
    print("<h3>saque</h3>")
    mapa = [".3......",
            "........",
            "...5#...",
            "...##...",
            ".....9..",
            "..2.....",
            "..2.....",
            "..2....."]
    print("in:")
    print('\n'.join(mapa))
    print("out:",saque(mapa))

if __name__ == '__main__':
    main()
