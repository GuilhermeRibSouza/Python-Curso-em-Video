#Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n = list()
for c in range(1,4):
    n.append(int(input(f'Digite o {c}ª numero: ')))
n.sort()
print(f'O menor número é {n[0]} e o maior número é {n[-1]}.')

#Esta forma foi usando coisas mais avançadas que o professor usou na aula, eu deveria usar o "if" portanto abaixo escreverei como deveria ter sido feito:

'''a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
menor == maior == a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior valor digitado é {maior} e o menor é {menor}.')'''

