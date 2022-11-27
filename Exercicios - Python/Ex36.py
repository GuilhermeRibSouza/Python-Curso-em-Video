#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

s = float(input('Qual é seu salario? '))
v = float(input('Qual é o valor da casa? '))
a = int(input('Pretende pagar em quantos anos? '))
p = v/a
c = s*0.3
if p > c:
    print(f'Sinto muito, mas seu emprestimo foi negado! A prestação não pode exceder um terço do seu salario, a prestação seria de {p:.2f} e 30% do seu salario é {c}.')
else:
    print(f'Seu emprestimo foi aceito! Sua parcela será de {p:.2f} para ser pago em {a} anos.')
