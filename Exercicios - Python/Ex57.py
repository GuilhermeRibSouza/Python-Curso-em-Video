#Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

while True:
    sexo = (str(input('Qual é o seu sexo? M para masculino e F para feminino: '))).strip().upper()
    if sexo == 'M' or sexo == 'F':
        break