#Exercicio 4 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

while True:
    p = input('Digite qualquer coisa: ')
    print(f'O tipo primitivo do que foi digitado é {type(p)}.')
    print(f'Só há espaços no que foi escrito? {p.isspace()}')
    print(f'Só tem número? {p.isnumeric()}')
    print(f'É composto somente por letras? {p.isalpha()}')
    print(f'Por acaso é alfanúmerico? {p.isalnum()}')
    print(f'São todas as letras maiusculas? {p.isupper()}')
    print(f'Estão todas as letras minusculas? {p.islower()}')
    