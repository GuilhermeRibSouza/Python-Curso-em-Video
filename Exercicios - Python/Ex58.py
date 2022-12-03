#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.


from random import randint
from time import sleep
t = 0
while True:
    print('Escolherei um número, você ganha se adivinhar qual é ele!')
    print('Pensando...')
    sleep(2.5)
    c = randint(1,11)
    print('Pronto!')
    j = int(input('Escolha seu número: '))
    if c == j:
        print('Parabéns, você adivinhou!')
        t += 1
        print(f'Foram necessario {t} tentativas para adivinhar meu número.')
        break
    else:
        if c>j:
            print(f'ERROU!\nVocê chutou {c-j} a menos que eu! Eu pensei no {c}!')
            t += 1
        else:
            print(f'ERROU!\nVocê chutou {j-c} a mais que eu! Eu pensei no {c}!')
            t += 1