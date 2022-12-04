#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

pa = list()

a1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
q = 0
for c in range(1, 11):
    print(f'{a1 + r*(c - 1)} ', end = '')
    q += 1
print('PAUSA')
total = 11
while True:
    t = int(input('Quer mostrar mais quantos termos?'))
    if t > 0:
        for c in range(1, t+1):
            print(f'{a1 + r*(total - 1)} ', end = '')
            q += 1
            total += 1
        print('PAUSA')
    if t == 0:
        print(f'Ao todo foram mostrados {q} termos da PA.')
        break
