# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

s = float(input('Digite seu salario: '))
if s <= 1250:
    print(f'Seu salario de {s} reais recebera um aumento de 15% passando a ser de {s*1.15:.2f} reais.')
else:
    print(f'Seu salario de {s} reais recebera um aumento de 10% passando a ser de {s*1.1:.2f} reais.')