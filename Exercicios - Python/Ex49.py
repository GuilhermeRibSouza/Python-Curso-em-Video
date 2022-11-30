#Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

from time import sleep
n = int(input('Escolha um número inteiro e positivo qualquer: '))
for c in range(0,11):
    print(f'{n} x {c} = {n*c}')
    sleep(1)
