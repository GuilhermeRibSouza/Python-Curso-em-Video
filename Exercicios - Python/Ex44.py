#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

p = float(input('Insira o preço do produto: R$'))
print('Qual será a forma de pagamento? Escolha uma das opções: \n[1] A VISTA NO DINHEIRO', end=' ')
print('\n[2] NO CHEQUE\n[3] A VISTA NO CARTÃO \n[4] EM DUAS VEZES NO CARTÃO \n[5] EM TRÊS VEZES NO CARTÃO')
pag = int(input('Qual será a opção de pagamento: '))
if pag == 1 or pag == 2:
    print('O produto ganhou 10% de desconto e seu valor será de {} reais!'.format(p*0.9))
elif pag == 3:
    print('O produto ganhou 5% de desconto e custará {} reais!'.format(p*0.95))
elif pag == 4:
    print('O preço não sofrerá alteração e ficará por {} reais!'.format(p))
elif pag == 5:
    parc = int(input('Em quantas parcelas você irá pagar? '))
    print('Você pagara ao todos {} reais com 10% de juros, em {} parcelas de {} reais!'.format(p*1.2, parc, (p*1.2)/parc))
else:
    print('Opção Invalida.')