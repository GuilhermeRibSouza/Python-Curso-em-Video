#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais


n = list()
for c in range(1, 3):
    n.append(int(input(f'Insira o {c}ª número: ')))
if n[0] > n[1]:
    print(f'O primeiro número inserido é maior que o segundo: {n[0]} > {n[1]}.')
elif n[0] < n[1]:
    print(f'O segundo número inserido é maior que o primeiro: {n[0]} < {n[1]}.')
else:
    print(f'O primeiro número inserido é igual ao segundo: {n[0]} = {n[1]}.')