#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite aqui seu nome completo: ')).strip().upper()
r = nome.split()
print(f'Seu primeiro nome é {r[0]}.')
print(f'Seu ultimo nome é {r[-1]}.')
