# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Dolar = 3,27 reais.

d = float(input('Quanto dinheiro você tem na carteira? R$ '))
print(f'A quantia em dolar referente aos seus {d} Reais é de U$ {d/3.27:.2f}.')
