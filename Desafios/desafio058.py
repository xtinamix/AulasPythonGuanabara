# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um numero entre 0 e 10. So que agora o jogador vai
# tentar adivinhar ate acertar, mostrando no final quantos palpites foram necessarios para vencer.
from random import randint
print('Sou seu computador...')
print('Acabei de pensar em um número entre 0 e 10, será que vc consegue adivinhar?')
pc = randint(0, 10)
user = -1
cont = 0
while user != pc:
    user = int(input('Em qual número eu pensei? '))
    cont += 1
    if user != pc:
        if user < pc:
            a = 'MAIS'
        else:
            a = 'MENOS'
        print('Você ERROU! É {}. Tente novamente! '.format(a))
print('PARABÉNS! Vc acertou na {} tentativa!'.format(cont))
