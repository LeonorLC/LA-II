##
# Tests for finder.py
#
# All tests in the folder "test" are executed
# when the "Test" action is invoked.
#
##

from Root.src.vendedor import vendedor
from Root.src.ladrao import ladrao
from Root.src.soma import maxsoma
from Root.src.validas import validas
from Root.src.espaca import espaca
from Root.src.saque import saque
from Root.src.robot import probabilidade
from Root.src.crescente import crescente
import unittest

class crescenteTest(unittest.TestCase):
    
    def test_crescente_1(self):
        with test_timeout(self,2):
            lista = [5,2,7,4,3,8]
            self.assertEqual(crescente(lista),3)

    def test_crescente_2(self):
        with test_timeout(self,2):
            lista = [15,27,14,38,26,55,46,65,85]
            self.assertEqual(crescente(lista),6)

class robotTest(unittest.TestCase):

    def test_probabilidade_1(self):
        with test_timeout(self,2):
            probs = {'U':0.25,'D':0.25,'L':0.25,'R':0.25}
            self.assertEqual(probabilidade(2,probs),0.25)
        
    def test_probabilidade_2(self):
        with test_timeout(self,2):
            probs = {'U':0.17,'D':0.33,'L':0.29,'R':0.21}
            self.assertEqual(probabilidade(6,probs),0.08)

class vendedorTest(unittest.TestCase):

    def test_vendedor_1(self):
        with test_timeout(self,2):
            produtos = [("biblia",20,2),("microondas",150,10),("televisao",200,15),("torradeira",40,3)]
            self.assertEqual(vendedor(14,produtos),(190,["biblia","biblia","microondas"]))

    def test_vendedor_2(self):
        with test_timeout(self,2):
            produtos = [("Verde",4,12),("Azul",2,2),("Cinzento",2,1),("Laranja",1,1),("Amarelo",10,4)]
            self.assertEqual(vendedor(15,produtos),(36,["Amarelo","Amarelo","Amarelo","Cinzento","Cinzento","Cinzento"]))

class ladraoTest(unittest.TestCase):

    def test_ladrao_1(self):
        with test_timeout(self,2):
            objectos = [("microondas",30,6),("jarra",14,3),("giradiscos",16,4),("radio",9,2)]
            self.assertEqual(ladrao(10,objectos),46)

    def test_ladrao_2(self):
        with test_timeout(self,2):
            objectos = [('A',10,1),('B',20,1),('C',30,1),('D',40,1),('E',50,1),('F',60,1),('G',70,1),('H',80,1),('I',90,1),('J',100,1)]
            self.assertEqual(ladrao(10,objectos),550)

class somaTest(unittest.TestCase):
    
    def test_maxsoma_1(self):
        with test_timeout(self,2):
            lista = [-2,1,-3,4,-1,2,1,-5,4]
            self.assertEqual(maxsoma(lista),6)

    def test_maxsoma_2(self):
        with test_timeout(self,2):
            lista = [1,2,3,4,-11,1,2,3,4,5]
            self.assertEqual(maxsoma(lista),15)

class validasTest(unittest.TestCase):
    
    def test_validas_1(self):
        with test_timeout(self,2):
            listas = [[8,1,7,3,3,6,3,5],[1,1,1,2,3,1,2],[3,3,3,3]]
            self.assertEqual(validas(10,listas),[[8,1,7,3,3,6,3,5],[1,1,1,2,3,1,2]])

    def test_validas_2(self):
        with test_timeout(self,2):
            listas = [[1,1,1,1,1],[2],[3,3,3,3,3,3,3],[4],[5,5,5,5,5]]
            self.assertEqual(validas(5,listas),[[1,1,1,1,1],[5,5,5,5,5]])
    
class espacaTest(unittest.TestCase):
    
    def test_espaca_1(self):
        with test_timeout(self,2):
            palavras = ["e","o","so","maior","este","curso","urso","es","maio"]
            self.assertEqual(espaca("estecursoeomaior",palavras),"este curso e o maior")
        
    def test_espaca_2(self):
        with test_timeout(self,2):
            palavras = ["o","oga","ga","gato","gatom","mia","eava","ava","e","a","va","vaca","mu","muge"]
            self.assertEqual(espaca("ogatomiaeavacamuge",palavras),"o gato mia e a vaca muge")

class saqueTest(unittest.TestCase):
    
    def test_saque_1(self):
        with test_timeout(self,2):
            mapa = [".3......",
                    "........",
                    "...5#...",
                    "...##...",
                    ".....9..",
                    "..2.....",
                    "..2.....",
                    "..2....."]
            self.assertEqual(saque(mapa),12)
        
    def test_saque_2(self):
        with test_timeout(self,2):
            mapa = ["11111",
                    "0###1",
                    "0###1",
                    "0###1",
                    "00001"]
            self.assertEqual(saque(mapa),9)

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
