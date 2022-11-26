#Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
a = list()
for c in range(1,5):
    a.append(input(f'Qual o nome do {c}ª aluno: '))
shuffle(a)
print(f'A ordem de apresentação dos alunos será {a}.')