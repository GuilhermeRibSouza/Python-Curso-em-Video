#Exercicio 9 - Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

t = int(input('Escolha um número qualquer: '))
for c in range(0,11):
    print(f'{t} x {c} = {t*c}')
