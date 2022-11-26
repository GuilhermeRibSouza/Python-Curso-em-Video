#Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

from random import choice
a = list()
for c in range(1,5):
    a.append(input(f'Qual é o {c}ª aluno: '))
print(f'Vou escolher uma das pessoas informadas: {choice(a)}.')
