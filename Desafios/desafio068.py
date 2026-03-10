# Faca um programa que jogue par ou impar com o computador. O jogo so sera interrompido quando o jogador PERDER,
# mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
from random import randint
print('-='*20, end = '')
print('-')
print(' '*5, 'VAMOS JOGAR PAR OU IMPAR?')
print('-='*20, end = '')
print('-')
count = 0
while True:
    jogador = int(input('Escolha um número: '))
    pc = randint(0, 11)
    soma = jogador + pc
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print('-'*40)
    if soma%2 == 0 and (escolha in 'Pp'):             # verifica se é par
        print(f'PARABÉNS! Você jogou {jogador} e o computador {pc}. A soma dá {soma} e é PAR.')
        count += 1
    elif soma % 2 == 1 and (escolha in 'Ii'):
        print(f'PARABÉNS! Você jogou {jogador} e o computador {pc}. A soma dá {soma} e é IMPAR.')
        count += 1
    else:
        print(f'Você PERDEU! Você jogou {jogador} e o computador {pc}. A soma dá {soma}. ')
        break
print(f'ACABOU! Você venceu {count} vezes.')
