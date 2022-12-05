#Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.


from random import randint
t = 0
print('Vamos jogar par ou impar, o jogo só acaba quando você perder.')
while True:
    c = int(input('Escolha par ou impar, pressione 1 para impar e 2 para par: [1/2] '))
    if c != 1 and c != 2:
        while c != 1 and c != 2:
            c = int(input('Valor Invalido, pressione 1 para impar e 2 para par: [1/2] '))
    a = randint(0,10)
    j = int(input('Escolha um número entre 0 e 10: '))
    if j > 10 or j < 0:
        while j > 10 or j < 0:
            j = int(input('Valor Invalido, Escolha um número entre 0 e 10: '))
    s = a + j
    if c == 1 and s % 2 == 1 or c == 2 and s % 2 == 0:
        print(f'PARABÉNS, você ganhou, eu escolhi {a} e você escolheu {j}, vamos denovo!')
        t += 1
    else:
        print(f'Que pena, você perdeu, eu escolhi {a} e você escolheu {j}, mas ganhou {t} partidas seguidas, parabéns!')
        break