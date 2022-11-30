#Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

'''cont = 0
for c in range(1, 501):
    if c % 3 == 0:
        cont += c
print(f'O total dos multiplos de 3 é {cont}.')'''

#Durante o exercicio o Professor Guanabara mudou o enunciado adicionando um segundo pré requisito:
#Que fossem também impares.

cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += c
print(f'O total dos multiplos de 3 é {cont}.')
