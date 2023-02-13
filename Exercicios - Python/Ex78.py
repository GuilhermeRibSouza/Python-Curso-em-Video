#Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 

# nma = 0
# nme = 0
# n = []
# for c in range(0,5):
#     j = int(input(f"Insira seu {c+1}ª número aqui: "))
#     n.append(j)
#     if c == 0 :
#         nma = j
#         nme = j
#     if c > 0:
#         if j > nma:
#             nma = j
#         if j < nme:
#             nme = j
# ima = n.index(nma)
# ime = n.index(nme)
# print(f'O maior número é {nma} e esta no lugar {ima} e o menor é {nme} e esta na posição {ime}!')

'Segunda forma de fazer'

n = [int(input(f"Insira seu {c+1}ª número aqui: "))for c in range(0,5)]
nma = max(n)
nme = min(n)
ima = n.index(nma)
ime = n.index(nme)
print(f'O maior número é {nma} e esta no lugar {ima} e o menor é {nme} e esta na posição {ime}!')