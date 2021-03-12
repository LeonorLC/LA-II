##
# Main function of the Python program.
#
##

from frequencia import frequencia
from robot import robot
from cruzamentos import cruzamentos
from factoriza import factoriza
from apelidos import apelidos
from hacker import hacker
from isbn import isbn
from repete import repete
from futebol import tabela
from aloca import aloca

def main():
    
    # frequencia
    print("<h3>frequencia</h3>")
    texto = "o tempo perguntou ao tempo quanto tempo o tempo tem"
    print("in:",texto)
    print("out:",frequencia(texto))
    
    # factoriza
    print("<h3>factoriza</h3>")
    print("in:",6)
    print("out:",factoriza(6))
    
    # apelidos
    print("<h3>apelidos</h3>")
    nomes = ["Jose Carlos Bacelar Almeida",
             "Maria Joao Frade",
             "Jose Bernardo Barros",
             "Jorge Manuel Matos Sousa Pinto",
             "Manuel Alcino Pereira Cunha",
             "Xico Esperto"]
    print("in:",nomes)
    print("out:",apelidos(nomes))
    
    # robot
    print("<h3>robot</h3>")
    cs = "EEAADAAAAAADAAAADDDAAAHAAAH"
    print("in:",cs)
    print("out:",robot(cs))
    
    # cruzamentos
    print("<h3>cruzamentos</h3>")
    ruas = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]
    print("in:",ruas)
    print("out:",cruzamentos(ruas))
    
    # hacker
    print("<h3>hacker</h3>")
    log = [("****1234********","maria@mail.pt"),
           ("0000************","ze@gmail.com"),
           ("****1111****3333","ze@gmail.com")]
    print("in:",log)
    print("out:",hacker(log))

    # isbn
    print("<h3>isbn</h3>")
    livros = {
        "Todos os nomes":"9789720047572",
        "Ensaio sobre a cegueira":"9789896604011",
        "Memorial do convent":"9789720046711",
        "Os cus de Judas":"9789722036757"
    }
    print("in:",livros)
    print("out:",isbn(livros))

    # repete
    print("<h3>repete</h3>")
    print("in:","amanha",2)
    print("out:",repete("amanha",2))
    
    # tabela
    print("<h3>tabela</h3>")
    jogos = [("Benfica",3,"Porto",2),("Benfica",0,"Sporting",0),("Porto",4,"Benfica",1),("Sporting",2,"Porto",2)]
    print("in:",jogos)
    print("out:",tabela(jogos))

    # tabela
    print("<h3>aloca</h3>")
    prefs = {10885:[1,5],40000:[5],10000:[1,2]}
    print("in:",prefs)
    print("out:",aloca(prefs))
    
if __name__ == '__main__':
    main()
