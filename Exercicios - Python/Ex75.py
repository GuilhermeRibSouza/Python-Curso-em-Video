#Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.

n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
n3 = int(input('Insira o terceiro valor: '))
n4 = int(input('Insira o quarto valor: '))
c =(n1, n2, n3, n4)
print(f'O número 9 apareceu {c.count(9)} vezes')
if 3 in c:
    print(f'O número 3 apareceu na posição {c.index(3)+1}')
else:
    print(f'O número 3 não foi digitado nenhuma vez!')
print('Os valores pares digitados foram ',end='')
for n1 in c:
    if n1 % 2 == 0:
        print(n1, end=' ')