#Exercicio 07 - Crie um programa que leia as duas notas de um aluno e forneça a média.

while True:
    nota1 = float(input('Insira aqui a primeira nota: '))
    nota2 = float(input('Insira aqui a segunda nota: '))
    print(f'A média das notas {nota1} e {nota2} é igual a {( nota1 + nota2) /2:.2f}.')
