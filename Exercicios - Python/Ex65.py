#Exercício Python 065: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


n = list()
while True:
    n.append(int(input('Digite aqui um número:')))
    c = str(input('Quer continuar? [S/N]')).upper().strip()
    while c != 'S' and c != 'N':
        c = str(input('Valor Invalido. [S/N]')).upper().strip() 
        if c == 'N':
            break
    if c == 'N':
        break
m = (sum(n))/(len(n))
print(f'A média dos números digitados é {m}, o maior é {sorted(n)[-1]} e o menor é {sorted(n)[0]}.')