# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

v = float(input('Qual é sua velocidade? '))
if v <= 80:
    print('Tenha uma boa viagem, continue respeitando seu limite de velocidade!')
else:
    print('Você ultrapassou o limite de velocidade!!! Sua multa é de {} reais. Respeite o limite de velocidade!'.format((v-80)*7))
    