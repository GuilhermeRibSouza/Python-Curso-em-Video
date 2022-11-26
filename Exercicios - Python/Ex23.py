#Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n = int(input('Insira aqui um número qualquer: '))
m = n//1000%10
c = n//100%10
d = n//10%10
u = n//1 %10
print(f'O número escolhido foi {n}.\nSeu milhar é a unidade {m}.\nSua centena é a unidade {c}.\nSua dezena é {d}.\nE sua unidade {u}.')
