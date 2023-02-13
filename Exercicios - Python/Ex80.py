'Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.'

# n = []
# for c in range(0, 5):
#     u = int(input(f'Digite o {c+1}º número: '))
#     if c == 0:
#         n.append(u)
#         print('Este é o primeiro número da lista!')
#     else:
#         for i, us in enumerate(n[:],1):
#             if u < us:
#                 n.insert(i-1, u)
#                 print(f'Número inserido no {i-1} da lista!')
#                 break
#         else:
#             n.append(u)
#             print('Número inserido no final da lista')
# print(n)


n = []
for c in range(0, 5):
    u = int(input(f'Digite o {c+1}º número: '))
    for i, us in enumerate(n[:],1):
        if u < us:
            n.insert(i-1, u)
            print(f'Número inserido no {i-1} da lista!')
            break
    else:
        n.append(u)
        print('Número inserido no final da lista')
print(n)
