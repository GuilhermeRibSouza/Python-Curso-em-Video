#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import sin, cos, tan, radians
r = float(input('Qual é o angulo desejado: '))
a = radians(r)
print(f'O angulo escolhido foi {r}, seu seno é {sin(a):.2f}, coseno equivalente a {cos(a):.2f} e tangente igual a {tan(a):.2f}.')
