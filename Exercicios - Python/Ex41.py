#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER


from datetime import date
atual = date.today().year
y = int(input('Qual é seu ano de nascimento? '))
i = atual - y
if i <= 9:
    print(f'A idade de {i} anos é categoria: MIRIM!!!')
elif i <= 14:
    print(f'A idade de {i} anos é categoria INFANTIL!!!')
elif i <= 19:
    print(f'A idade de {i} anos é categoria JÚNIOR!!!')
elif i <=25:
    print(f'A idade de {i} anos é categoria SÉNIOR!!!')
else:
    print(f'A idade de {i} anos é categoria MASTER!!!')