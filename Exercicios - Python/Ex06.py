#Exercicio 6 - Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.

while True:
    num = int(input('Insira um número qualquer: '))
    print(f'O dobro de {num} é {num*2}.')
    print(f'O triplo de {num} é igual a {num*3}.')
    print(f'A raiz quadrada de {num} é equivalente a {num**(1/2):.2f}')
