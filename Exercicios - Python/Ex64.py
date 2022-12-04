#Exercício Python 064: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).


lista = list()
while True:
    n = (int(input('Digite aqui um número qualquer: ')))
    if n != 999:
        lista.append(n)
    else: 
        break
print(f'A quantidade de números inseridas é de {len(lista)} números.')
print(f'A soma entre eles é de {sum(lista)}.')
    