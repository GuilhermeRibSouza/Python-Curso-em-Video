# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

l = float(input('Qual é a largura da parede em metros? '))
a = float(input('Qual é a altura da parede em metros? '))
print(f'A área referente a parede de dimensões de {l} m x {a} m é de {l*a:.2f} m² e será necessario {(l*a)/2:.2f} litros de tinta para pinta-la.')