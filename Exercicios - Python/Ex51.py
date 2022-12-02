#Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.


a1 = float(input('Insira o primeiro termo da PA: '))
r = float(input('Insira a razão da PA: '))
for c in range(1, 11):
    print(f'{a1 + r*(c - 1)} ', end = '')
print('FIM!!')