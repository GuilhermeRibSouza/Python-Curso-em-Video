#Exercício Python 037: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Escolha um número: '))
c = int(input('Escolha para qual forma você deseja converter o número:\n[1] BINARIO\n[2] OCTAL\n[3] HEXADECIMAL\nINSIRA AQUI SUA ESCOLHA: '))
while c != 1 and c != 2 and c != 3:
    c = int(input('Valor INVALIDO!! INSIRA AQUI SUA ESCOLHA [1/2/3]: '))
if c == 1:
    print(f'O número {n} em forma BINARIA é {bin(n)[2:]}.')
elif c == 2:
    print(f'O número {n} em forma OCTAL é {oct(n)[2:]}.')
elif c == 3:
    print(f'O número {n} em forma HEXADECIMAL é {hex(n)[2:]}.')

#"While não havia sido ensinado ainda, mas me adiantei e usei neste exercicio para previnir erros de digitação do usuario e para garantir que ele funcione pelo menos uma vez."