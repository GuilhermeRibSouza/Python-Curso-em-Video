#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o

pares = list()
for c in range(1,7):
    n = int(input(f'Digite o {c}ª número: '))
    if n % 2 == 0:
        pares.append(n)
print(f'Os números pares digitados foram: {pares} e sua soma é igual a {sum(pares)}.')