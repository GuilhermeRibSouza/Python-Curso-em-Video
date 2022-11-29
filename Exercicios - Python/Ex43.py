#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida

p = float(input('Qual é seu peso em Kg?  '))
a = float(input('Qual é sua altura em m?  '))
IMC = p/(a)**2
if IMC <= 18.5:
    print(f'Seu IMC de {IMC:.2f} o classifica como ABAIXO DO PESO!!!')
elif IMC <= 25:
    print(f'Seu IMC de {IMC:.2f} o classifica como PESO IDEAL!!!')
elif IMC <= 30:
    print(f'Seu IMC de {IMC:.2f} o classifica como SOBREPESO!!!')
elif IMC <= 40:
    print(f'Seu IMC de {IMC:.2f} o classifica como OBESIDADE!!!')
else:
    print(f'Seu IMC de {IMC:.2f} o classifica como OBESIDADE MORBIDA!!!')