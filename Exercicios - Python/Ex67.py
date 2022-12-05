#Exercício Python 067: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    n = int(input('Qual é o número que você quer: '))
    if n >= 0:
        for c in range(0,11):
            print(f'{n} x {c} = {n*c}')
    if n < 0:
        print('Obrigado por usar o programa!')
        break