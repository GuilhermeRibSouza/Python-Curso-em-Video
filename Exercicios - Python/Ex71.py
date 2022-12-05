#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.


d = int(input('Quanto deseja sacar? (Só temos notas de R$50, R$20, R$10 e R$1) : R$ '))
d1 = d // 50
d2 = (d - (d1*50))//20
d3 = (d - (d1*50)-(d2*20))//10
d4 = (d - (d1*50)-(d2*20)-(d3*10))//1
print(f'Foram sacados {d1} notas de 50 reais, {d2} notas de 20 reais, {d3} notas de 10 reais e {d4} notas de 1 real.')