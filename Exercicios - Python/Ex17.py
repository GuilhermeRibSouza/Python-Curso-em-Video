#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

from math import hypot
c1 = float(input('Qual é o primeiro cateto: '))
c2 = float(input('Qual é o segundo cateto: '))
print(f'A hipotenusa dos catetos {c1} e {c2} é igual a {hypot(c1, c2):.2f}.')
