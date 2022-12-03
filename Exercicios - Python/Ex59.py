#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

n1 = float(input('Qual é o primeiro número: '))
n2 = float(input('Qual é o segundo número: '))
while True:
    c = int(input('Escolha qual das opções você deseja:\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR DO PROGRAMA\nFAÇA AQUI SUA ESCOLHA: '))
    while c < 1 or c > 5:
        c = int(input('Escolha invalidade, faça uma escolha valida na lista citada.\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR DO PROGRAMA\nFAÇA AQUI SUA ESCOLHA: '))
    if c == 1:
        print(f'A soma dos números é igual a {n1+n2}.')
    if c == 2:
        print(f'A multiplicação dos números é igual a {n1*n2}.')
    if c == 3:
        if n1 > n2:
            print(f'{n1} > {n2}.')
        elif n2 > n1:
            print(f'{n2} > {n1}.')
        else:
            print('Os dois números são iguais.')
    if c == 4:
        n1 = float(input('Qual é o primeiro número: '))
        n2 = float(input('Qual é o segundo número: '))
        while c < 1 or c > 5:
            c = int(input('Escolha invalidade, faça uma escolha valida na lista citada.\n[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4]NOVOS NÚMEROS\n[5]SAIR DO PROGRAMA\nFAÇA AQUI SUA ESCOLHA: '))
    if c == 5:
        print('Obrigado por usar o programa.')
        break