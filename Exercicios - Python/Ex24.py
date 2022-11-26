#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".

city = str(input('Digite a cidade em que nasceu: ')).strip().upper()
print(city[5]=='SANTO')
