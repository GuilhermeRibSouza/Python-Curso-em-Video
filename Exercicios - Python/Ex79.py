'Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'

# n = []
# u = int(input("Digite um número: "))
# n.append(u)
# c = input('Deseja continuar? ').strip().upper()
# while c != "S" and c !="N":
#     c = input('Digite S ou N como escolha: ').strip().upper()
# while c == "S":
#     u = int(input("Digite um número: "))
#     if u in n:
#         print("Valor repetido, não inserido.")
#     else:
#         n.append(u)
#     c = input('Deseja continuar? ').strip().upper()
#     while c != "S" and c !="N":
#         c = input('Digite S ou N como escolha: ').strip().upper()
# n.sort()
# print(n)


'Segunda forma de fazer o exercicio'

n = []
while True:
    u = int(input("Digite um número: "))
    if u not in n:
        n.append(u)
    else:
        print('Valor já existente, não vou por.')
    c = input('Deseja continuar? ').strip().upper()
    while c != "S" and c !="N":
        c = input('Digite S ou N como escolha: ').strip().upper()
    if c =="N":
        break
n.sort()
print(n)