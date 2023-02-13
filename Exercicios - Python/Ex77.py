#Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

# camp = ("Cho'Gath","Bel'Veth","Vel'Koz","Kha'zix","Kai'Sa","Rek'Sai","Malzahar","Kassadin")


# for c in camp:
#     print(f'O nome {c} tem ', end = '')
#     for l in c: 
#         if "a" == l:
#             print(f'{l}', end = ' ')
#         elif "e" == l:
#             print(f'{l}',end = ' ')
#         elif "i" == l:
#             print(f'{l}',end = ' ')
#         elif "o" == l:
#             print(f'{l}',end = ' ')
#         elif "u" == l:
#             print(f'{l}',end = ' ')
#     print()

#Segunda forma de fazer

camp = ("Cho'Gath","Bel'Veth","Vel'Koz","Kha'zix","Kai'Sa","Rek'Sai","Malzahar","Kassadin")
vogais = ["a", "e", "i", "o", "u"]

for c in camp:
    print(f'O nome {c} tem ', end = '')
    for l in c.lower():
        if l in vogais:
            print(f'{l}', end = ' ')
    print()