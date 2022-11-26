# Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Km foram rodados? '))
d = int(input('Quantos dias você ficou com o carro? '))
print(f'O preço a pagar por {km} kms rodados em {d} dias é de R${d*60 + km*0.15}.')
