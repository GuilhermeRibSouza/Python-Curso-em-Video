#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
print('Escolherei um número, você ganha se adivinhar qual é ele!')
print('Pensando...')
sleep(2.5)
c = randint(1,11)
print('Pronto!')
j = int(input('Escolha seu número: '))
if c == j:
    print('Parabéns, você adivinhou!')
else:
    if c>j:
        print(f'ERROU!\nVocê chutou {c-j} a menos que eu! Eu pensei no {c}!')
    else:
        print(f'ERROU!\nVocê chutou {j-c} a mais que eu! Eu pensei no {c}!')
