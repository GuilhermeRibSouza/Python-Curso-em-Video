#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome e o primeiro nome.

nome = str(input('Escreva seu nome completo: ')).strip()
print(f'Seu nome em letras maiusculas é {nome.upper()}.')
print(f'Já em letras minusculas é {nome.lower()}.')
print('Seu nome tem {} letras.'.format(len(nome)-nome.count(' ')))
primeiro = nome.split()
print(f'Seu primeiro nome tem {len(primeiro[0])} letras e é {primeiro[0]}.')