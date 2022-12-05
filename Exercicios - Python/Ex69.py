#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos. 


i = 0
m = 0
mu = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    if idade > 18:
        i += 1
    if sexo == 'M':
        m += 1
    if sexo == 'F' and idade < 20:
        mu += 1
    c = str(input('Deseja continuar? [S/N]')).upper().strip()
    if c != 'S' and c != 'N':
        while c != 'S' and c != 'N':
            c = int(input('Valor Invalido, [S/N]: '))
    if c == 'N':
        break
print(f'Foram cadastrados {i} pessoas maiores de 18 anos, {m} homens no total e {mu} mulheres menores de 20 anos.')
