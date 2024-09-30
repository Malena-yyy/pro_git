# Projeto de Poo
## Índice
- [Descrição curta](#Descricão-curta)
- [Pré-Requisitos](#Pré-Requisitos)
- [Instalção](#Instalação)
- [Exemplo-de-Uso](#Exemplo-de-Uso)
- [Contato](#Contato)

## Descrição curta

Este projeto é uma simulação de uma calculadora que realiza operações matemáticas essenciais. Além das operações básicas, a calculadora também suporta algumas operações algébricas, como o cálculo de fatoriais, quadrados e raízes quadradas, oferecendo uma funcionalidade razoável e sendo fácil de usar.

## Pré-Requisitos
Este projeto requer o Python na versão 3.6 ou superior para funcionar corretamente,Além disso é preciso ter istalado na sua máquina as seguintes ferramentas:

[Git](https://git-scm.com)<br/>
[VScode](https://code.visualstudio.com/) -Editor recomendado, mas opicional

## Instalação
```
1. clone este repositorio:

git clone https://github.com/Malena-yyy/prog.git

2.Navegue até o diretório do projeto

cd prog

3.Instale o projeto e suas depedências com o pip

pip install -e .

```
## Exemplo de Uso
from calculadora_tipos import CalculadoraBasica, CalculadoraCientifica

calc_basica = CalculadoraBasica()
calc_cientifica = CalculadoraCientifica()

print(calc_basica.soma(5, 3))         
print(calc_basica.subtracao(10, 2))   
print(calc_basica.multiplicacao(6, 7))
print(calc_basica.divisao(12, 4))    

print(calc_cientifica.quadrado(4, 5))  
print(calc_cientifica.raiz(16, 25))    
print(calc_cientifica.fatorial(5, 3))  



## Contato
Conhece mais sobre esse desenvolvedor no link 
https://www.instagram.com/_malena.milani?igsh=MWNoYWV5MjBoYXIwYw==