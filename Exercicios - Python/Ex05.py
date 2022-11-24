#Exercicio 5 - Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

while True:
    num = int(input('Digite um número: '))
    print(f'O número {num} tem como antecessor o {num-1} e sucessor o {num+1}.')
    