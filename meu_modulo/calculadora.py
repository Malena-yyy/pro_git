# exercicio
import math
class Calculadora:
  def soma(self,a:float,b:float)->str:
    soma= a+b
    return f'a soma a mais b é {soma}'

  def subtracao(self,a:float,b:float)->str:
    subtr= a-b
    return f'a subtração a menos b é {subtr}'

  def multiplicacao(self,a:float,b:float)->str:
    mult= a*b
    return f'a multiplicao a vezes b é {mult}'

  def divisao(self,a:float,b:float)->str:
    div= a/b
    return f'a divisão a por b é {div}'

class CalculadoraBasica(Calculadora):
  pass

class CalculadoraCientifica(Calculadora):
  def quadrado(self,a:float,b:float)->str:
    quadrA= a**2
    quadrB= b**2
    return f'o quadrado de a e b são {quadrA} e {quadrB}'

  def raiz(self,a:float,b:float)->str:
    raizA= math.sqrt(a)
    raizB= math.sqrt(b)
    return f'a raiz quadrada de a e b são {raizA} e {raizB}'


  def fatorial(self,a:int,b:int)->str:
    fatA= math.factorial(a)
    fatB= math.factorial(b)
    return f'o fatorial de a e b são {fatA} e {fatB}'

# instanciando as classes
calculadora= Calculadora()
calculadora.soma(0,0)
calculadora.subtracao(0,0)
calculadora.multiplicacao(0,0)
calculadora.divisao(0,1)

cientifica= CalculadoraCientifica()
cientifica.quadrado(0,0)
cientifica.raiz(1,1)
cientifica.fatorial(0,0)
