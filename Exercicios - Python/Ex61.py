#Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.


a1 = float(input('Insira o primeiro termo da PA: '))
r = float(input('Insira a razão da PA: '))
c = 1
while c <=10:
    print(f'{a1 + r*(c - 1)} ', end = '')
    c += 1
print('FIM!!')