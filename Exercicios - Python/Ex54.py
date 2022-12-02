#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.


from datetime import date
h = date.today().year
ma = me = 0
for c in range(1,8):
    ano = int(input(f'Qual é o {c}ª ano de nascimento inserido? '))
    i = h - ano
    if i < 18:
        me += 1
    else:
        ma += 1
print(f'Ao todo foram {ma} pessoas de maior e {me} de menor.') 