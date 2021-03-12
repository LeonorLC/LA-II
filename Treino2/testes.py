##
#
# All tests in the folder "test" are executed
# when the "Test" action is invoked.
#
##

from Root.src.continente import maior
from Root.src.area import area
from Root.src.cidade import tamanho
from Root.src.labirinto import caminho
from Root.src.cavalo import saltos
from Root.src.viagem import viagem
from Root.src.erdos import erdos
from Root.src.travessia import travessia
import unittest

class maiorTest(unittest.TestCase):

    def test_maior_1(self):
        with test_timeout(self,1):
            vizinhos = [["Portugal","Espanha"],["Espanha","França"],["França","Bélgica","Alemanha","Luxemburgo"],["Canada","Estados Unidos"]]
            self.assertEqual(maior(vizinhos), 6)

    def test_maior_2(self):
        with test_timeout(self,1):
            vizinhos = [["Portugal","Espanha"],["Espanha","França"]]
            self.assertEqual(maior(vizinhos), 3)
        
class saltsTest(unittest.TestCase):

    def test_saltos_1(self):
        with test_timeout(self,1):
            self.assertEqual(saltos((0,0),(1,1)),2)
        
    def test_saltos_2(self):
        with test_timeout(self,1):
            self.assertEqual(saltos((0,0),(7,7)),6)

class areaTest(unittest.TestCase):

    def test_area_1(self):
        with test_timeout(self,1):
            mapa = ["..*..",
                    ".*.*.",
                    "*...*",
                    ".*.*.",
                    "..*.."]
            self.assertEqual(area((3,2),mapa),5)

    def test_area_2(self):
        with test_timeout(self,1):
            mapa = ["..*..",
                    ".*.*.",
                    "*....",
                    ".*.*.",
                    "..*.."]
            self.assertEqual(area((3,2),mapa),12)

class tamanhoTest(unittest.TestCase):
    
    def test_tamanho_1(self):
        with test_timeout(self,1):
            ruas = ["raio","central","liberdade","chaos","saovictor","saovicente","saodomingos","souto","capelistas","anjo","taxa"]
            self.assertEqual(tamanho(ruas),25)

    def test_tamanho_2(self):
        with test_timeout(self,1):
            ruas = ["ab","bc","bd","cd"]
            self.assertEqual(tamanho(ruas),4)

class caminhoTest(unittest.TestCase):

    def test_caminho_1(self):
        with test_timeout(self,1):
            mapa = ["  ########",
                    "# # #    #",
                    "# # #### #",
                    "# #      #",
                    "# # # ####",
                    "# # #    #",
                    "#   # #  #",
                    "##### ####",
                    "#        #",
                    "########  "]
            self.assertEqual(caminho(mapa),"ESSSSSSEENNNEESSSSSEEESE")
        
    def test_caminho_2(self):
        with test_timeout(self,1):
            mapa = ['   ',
                    ' # ',
                    '   ']
            self.assertIn(caminho(mapa),["EESS","SSEE"])

class viagemTest(unittest.TestCase):
    
    def test_viagem_1(self):
        with test_timeout(self,1):
            rotas = [["Porto",20,"Lisboa"],
                     ["Braga",3,"Barcelos",4,"Viana",3,"Caminha"],
                     ["Braga",3,"Famalicao",3,"Porto"],
                     ["Viana",4,"Povoa",3,"Porto"],
                     ["Lisboa",10,"Evora",8,"Beja",8,"Faro"]
                    ]
            self.assertEqual(viagem(rotas,"Caminha","Lisboa"),30)

    def test_viagem_2(self):
        with test_timeout(self,1):
            rotas = [["Porto",20,"Lisboa"],
                     ["Braga",3,"Barcelos",4,"Viana",3,"Caminha"],
                     ["Braga",3,"Famalicao",3,"Porto"],
                     ["Viana",4,"Povoa",3,"Porto"],
                     ["Lisboa",10,"Evora",8,"Beja",8,"Faro"],
                     ["Porto",15,"Lisboa",20,"Faro"]
                    ]
            self.assertEqual(viagem(rotas,"Braga","Faro"),41)

        
class erdosTest(unittest.TestCase):
    
    def test_erdos_1(self):
        with test_timeout(self,1):
            artigos = {"Adaptive register allocation with a linear number of registers": {"Carole Delporte-Gallet","Hugues Fauconnier","Eli Gafni","Leslie Lamport"},
                       "Oblivious collaboration": {"Yehuda Afek","Yakov Babichenko","Uriel Feige","Eli Gafni","Nati Linial","Benny Sudakov"},
                       "Optima of dual integer linear programs": {"Ron Aharoni","Paul Erdos","Nati Linial"}
                      }
            self.assertEqual(erdos(artigos,2),['Paul Erdos', 'Nati Linial', 'Ron Aharoni', 'Benny Sudakov', 'Eli Gafni', 'Uriel Feige', 'Yakov Babichenko', 'Yehuda Afek'])

    def test_erdos_2(self):
        with test_timeout(self,1):
            artigos = {"Specifying systems": {"Leslie Lamport"},
                       "Optima of dual integer linear programs": {"Ron Aharoni","Paul Erdos","Nati Linial"}
                      }
            self.assertEqual(erdos(artigos,1),['Paul Erdos', 'Nati Linial', 'Ron Aharoni'])

class travessiaTest(unittest.TestCase):
    
    def test_travessia_1(self):
        with test_timeout(self,1):
            mapa = ["4563",
                    "9254",
                    "7234",
                    "3231",
                    "3881"]
            self.assertEqual(travessia(mapa),(2,10))

    def test_travessia_2(self):
        with test_timeout(self,1):
            mapa = ["90999",
                    "00000",
                    "92909",
                    "94909"]
            self.assertEqual(travessia(mapa),(1,5))

if __name__ == '__main__':
    unittest.main()


import time
import signal

class TestTimeout(Exception):
    pass

class test_timeout:
  def __init__(self, test, seconds, error_message=None):
    if error_message is None:
      error_message = 'test timed out after {}s.'.format(seconds)
    self.seconds = seconds
    self.error_message = error_message
    self.test = test

  def handle_timeout(self, signum, frame):
    raise TestTimeout(self.error_message)

  def __enter__(self):
    signal.signal(signal.SIGALRM, self.handle_timeout)
    signal.alarm(self.seconds)

  def __exit__(self, exc_type, exc_val, exc_tb):
    signal.alarm(0)
    if exc_type is not None and exc_type is not AssertionError:
        self.test.fail("execution error")
