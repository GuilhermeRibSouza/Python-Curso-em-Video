"SIM, VOLTEI!!!"
"Depois de muuuuuito tempo volto a ti Python, vamos lá"
#Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
nma = nme = t = 0
n = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10) )
# Colocar em () transformara a variavel em uma tulpa!
# Ao adicionar a virgula e adicionar a mesma variavel, adicionara um novo número na tulpa.
print('Eu sortiei os números: ')
for r in n:
    print(f'{r}', end=' ')
print(f'\nO maior número sorteado foi o {max(n)} e o menor foi {min(n)} ')
