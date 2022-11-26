#Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

D = float(input('Qual foi a distancia em Km percorrida na viagem? '))
if D<=200:
    print(f'Sua viagem de {D}km terá o custo de {D*0.5} reais!')
else:
    print(f'Sua viagem de {D}km terá o custo de {D*0.45} reais!')
    