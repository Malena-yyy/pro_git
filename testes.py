# testes
from meu_modulo.calculadora import CalculadoraBasica
from meu_modulo.calculadora import CalculadoraCientifica

calculadora= CalculadoraBasica()
cientifica= CalculadoraCientifica()

soma= calculadora.soma(1,82)
subtração= calculadora.subtracao(4,8)
multiplicação= calculadora.multiplicacao(3,78)
divisão= calculadora.divisao(30,10)
quadrado= cientifica.quadrado(3,4)
fatorial= cientifica.fatorial(6,7)
raiz= cientifica.raiz(25,16)

print('=====Testes Operações Básicas=====')
print(soma,'\n')
print(subtração,'\n')
print(multiplicação,'\n')
print(divisão,'\n')

print('=====Testes Operações Cientificas=====')
print(quadrado,'\n')
print(fatorial,'\n')
print(raiz,'\n')
