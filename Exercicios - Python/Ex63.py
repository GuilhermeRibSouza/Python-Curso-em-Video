#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 


t = int(input('Insira a quantidade de termos do número de ouro que você deseja: '))
n1 = 0
n2 = 1
print(f'{n1} > {n2} >', end =' ')
cont = 3
while cont <= t:
    n3 = n1 + n2
    print(f'> {n3}', end =' ')
    n1 = n2
    n2 = n3
    cont += 1
print('> Acabou')