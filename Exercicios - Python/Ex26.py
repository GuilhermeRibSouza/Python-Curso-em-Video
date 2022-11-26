#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Insira uma frase qualquer: ')).strip().upper()
print('A letra A apareceu {} vezes.'.format(frase.count('A')))
print('A primeira vez que o A aparece é na posição {}.'.format(frase.find('A')+1))
print('A ultima vez que ele aparece é na posição {}.'.format(frase.rfind('A')+1))
