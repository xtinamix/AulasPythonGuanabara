# Escreva um programa que leia um numero inteiro qualquer e peca para o usuario escolher qual sera a base de conversao
# 1 para binario
# 2 para octal
# 3 para hexadecimal
numero = int(input('Escolha um número: '))
print('--=--'*20)
conv= ['binário', 'octal', 'hexadecimal']
opcao = int(input('Para qual sistema você quer convertê-lo:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\n'))
if opcao == 1 or opcao == 2 or opcao == 3:
    if opcao == 1:
        transf = bin(numero)
    elif opcao == 2:
        transf = oct(numero)
    else:
        transf = hex(numero)
    print('O número {} em {} é: {}.'.format(numero, conv[opcao-1],transf[2:]))
else:
    print('Opção {} náo é válida.'.format(opcao))