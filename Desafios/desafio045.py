# Crie um programa que faca o computador jogar jokenpo com voce

from random import randint      # importar biblioteca pra escolha aleatoria
print('''Vamos jogar Jokenpô! Sendo: 
1 para pedra
2 para papel
3 para tesoura''')
usuario = int(input('Escolha: '))        # escolha do usuario
print('--=--'*20)
opcoes = ['pedra', 'papel', 'tesoura']          # as opcoes de escolha
computador = randint(1, 3)                   # escolha do computador
if usuario == computador:
    print('Os dois escolheram {}, EMPATOU!'.format(opcoes[computador-1]))
elif (usuario == 1 and computador == 2) or (usuario == 2 and computador == 3) or (usuario == 3 and computador == 1):
    print('O computador escolheu {} e vc {}. Você PERDEU!'.format(opcoes[computador-1], opcoes[usuario-1]))
else:
    print('O computador escolheu {} e vc {}. Você GANHOU!'.format(opcoes[computador-1], opcoes[usuario-1]))
