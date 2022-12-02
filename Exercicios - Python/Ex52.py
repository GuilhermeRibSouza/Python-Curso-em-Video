#Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

d = int(input('Escolha um número inteiro e positivo qualquer: '))
soma = 0
for c in range(1, d+1):
    if d % c == 0:
        print('\33[33m', end=' ')
        soma += 1
    else:
        print('\33[31m', end=' ')
    print('{}'.format(c), end=' ')
if soma == 2:
    print('\33[m\nO número {} é primo!!'.format(d))
else:
    print('O número {} não é primo!!'.format(d))
