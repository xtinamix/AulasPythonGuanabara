# Crie um programa que leia dois valores e mostre um menu na tela:
# [1]somar [2]multiplicar [3]maior [4]novos numeros [5]sair do programa
# Seu programa devera realizar a operacao solicitada em cada caso.
opcao = 0
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
while opcao != 5:
    opcao = int(input('''O que você deseja fazer?
    [1]Somar
    [2]Multiplicar
    [3]Saber qual o maior
    [4]Inserir novos números
    [5]Sair\n'''))
    if opcao == 1:
        print('A soma de {} e {} é {}.'.format(n1, n2, n1+n2))
    elif opcao == 2:
        print('A multiplicação entre {} e {} é {}.'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {} o maior é {}.'.format(n1, n2, n1))
        elif n2 > n1:
            print('Entre {} e {} o maior é {}.'.format(n2, n1, n2))
        else:
            print('Ambos os números são iguais e valem {}.'.format(n1))
    elif opcao == 4:
        n1 = float(input('Digite o novo valor do primeiro número: '))
        n2 = float(input('Digite o novo valor do segundo número: '))
    elif opcao == 5:
        opcao = 5
    else:
        print('Não existe essa opção! Tente novamente.')
print('----- FIM -----')
