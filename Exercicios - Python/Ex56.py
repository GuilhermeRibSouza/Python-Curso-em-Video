#Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

soma = 0
hvelho = 0
older = 0
men = 0
for c in range(1,5):
    nome = str(input(f'Qual é o nome da {c}ª pessoa? ')).strip().upper()
    idade = int(input(f'Qual é a idade da {c}ª pessoa? '))
    sexo = str(input(f'Qual é o sexo da {c}ª pessoa? M para masculino e F para feminino ')).strip().upper()
    if c == 1 and sexo == 'M':
        hvelho = idade
        older = nome
    if c > 1 and sexo == 'M' and hvelho < idade:
        hvelho = idade
        older = nome
    soma += idade
    if idade < 18 and sexo == 'F':
        men += 1
média = soma/c
print(f'A média das idades de todos é de {média} anos.')
print(f'O nome do homem mais velho é {older}.')
print(f'A quantidade de mulheres de menor é igual a {men}.')