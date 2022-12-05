#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato



soma = 0
mil = 0
barato = ('')
menor = 0
while True:
    c = str(input('Produto: ')).upper().strip()
    p = float(input('Preço: R$ '))
    t = str(input('Deseja continuar? [S/N] ')).upper().strip()
    soma += p
    if p > 1000:
        mil += 1
    if menor == 0:
        menor = p
        barato = c
    elif p < menor:
        menor = p
        barato = c
    if t != 'S' and t != 'N':
        while t != 'S' and t != 'N':
            t = str(input('Valor Invalido, [S/N]: '))
    if t == 'N':
        break
print(f'O valor total das compras é de {soma} reais, existem {mil} produtos mais caros que mil reais e o produto mais barato é {barato}.')
    
    