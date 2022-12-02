#Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.


ma = me = 0
for c in range(1,6):
    p = float(input(f'O {c}ª peso: '))
    if c == 1:
        ma = me = p
    if c > 2:
        if p > ma:
            ma = p
        if p < me:
            me = p
print(f'O maior peso inserido foi {ma} Kg e o menor foi {me} Kg.')