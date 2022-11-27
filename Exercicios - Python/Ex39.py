#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
t = date.today().year
y = int(input('Insira seu ano de nascimento:  '))
a = t - y
s = str(input('Insira seu sexo:\n[M] MASCULINO\n[F] FEMININO\nInsira aqui: ')).strip().upper()
while s != 'F' and s != 'M':
    s = str(input('INVALIDO, INSIRA F OU M: ')).strip().upper()
if s == 'F':
    print('Você NÃO PRECISA se alistar.')
if s == 'M':
    if a < 18:
        print(f'Você ainda não precisa se alistar, faltam {18-a} anos para isso.')
    elif a == 18:
        print('VOCÊ DEVE SE ALISTAR NESTE ANO, NÃO ESQUEÇA!!!!')
    else:
        print(f'VOCÊ JÁ DEVERIA TER SE ALISTADO!!! VOCÊ ESTA ATRASADO A {a-18} ANOS, CORRE!!!')