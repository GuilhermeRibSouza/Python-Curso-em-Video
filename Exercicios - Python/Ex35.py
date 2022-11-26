#Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

l1 = float(input('Qual é a media do primeiro lado? '))
l2 = float(input('Qual é a medida do segundo lado? '))
l3 = float(input('Qual é a medida do terceiro lado? '))
if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2:
    print(f'As medidades de {l1}, {l2} e {l3} PODEM formar um triangulo!!!')
else:
    print(f'As medidas de {l1}, {l2} e {l3} NÃO PODEM formar um triangulo!!!')