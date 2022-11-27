#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

notas = list()
t = 0
for c in range(1,3):
    notas.append(float(input(f'Qual foi a {c}ª nota? ')))
    t += 1
average = (notas[0] + notas[1])/t
if average <= 5:
    print(f'Sua média é de {average:.2f} e esta REPROVADO!!')
elif 5 < average < 7:
    print(f'Sua média é de {average:.2f} e esta de RECUPERAÇÃO!!!')
else:
    print(f'Sua média foi {average:.2f} e esta APROVADO!!!!')
