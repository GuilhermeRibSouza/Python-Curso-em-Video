#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes


lados = list()
for c in range(1, 4):
    lados.append(float(input(F'Qual é a medida do {c}ª lado? ')))
if lados[0] > lados [1] + lados[2] or lados[1] > lados [0] + lados[2] or lados[2] > lados [1] + lados[0]:
    print(f'Os lados {lados[0]}, {lados[1]} e {lados[2]} NÃO FORMAM UM TRIANGULO!!!')
else:
    if lados[0] == lados [1] == lados [2]:
        print(f'Os lados {lados[0]}, {lados[1]} e {lados[2]} foram um triangulo EQUILATERO!!!')
    elif lados[0] == lados[1] or lados [0] == lados[2] or lados [1] == lados [2]:
        print(f'Os lados {lados[0]}, {lados[1]} e {lados[2]} foram um triangulo ISÓSCELES!!!')
    elif lados[0] != lados[1] != lados[2]:
        print(f'Os lados {lados[0]}, {lados[1]} e {lados[2]} foram um triangulo ESCALENO!!!')

