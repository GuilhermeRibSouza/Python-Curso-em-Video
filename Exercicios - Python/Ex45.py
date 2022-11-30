#Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.

from time import sleep
from random import randint
print('Estou pensando o que irei jogar...')
c = randint(1,3)
sleep(2)
print('Pronto!')
sleep(1)
e = int(input('Faça uma escolha:\n[1] PEDRA\n[2] PAPEL\n[3] TESOURA\nFaça sua escolha: '))
print('JOOOOOO')
sleep(1)
print('KENNNNN')
sleep(1)
print('POOOOOOOO!!!!!')
sleep(1)
if c == 1 and e == 2 or c == 2 and e == 3 or c == 3 and e == 1:
    print(f'WOW, parabéns, você me venceu!!! Eu escolhi {c} e você escolheu {e}.')
elif c == e:
    print(f'AAHHH, nós empatamos!!! Eu escolhi {c} e você {e}.')  
else: 
    print(f'AAHH, EU GANHEI!!! Eu escolhi {c} e você {e}.')