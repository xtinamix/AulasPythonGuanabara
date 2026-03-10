# Escreva um programa que faça o computador "pensar" em numero entre 0 e 5 e peça para o usuário tentar descobrir qual
# foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
from time import sleep          # faz o programa dormir um pouco
n = randint(0,5)        # sorteia um numero entre 0 a 5
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
user = int(input('Em que número eu pensei? '))      # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)    # sleep 3s
if n == user:
    print('PARABÉNS! Você ACERTOU!!')
else:
    print('Você PERDEU! Eu pensei no número {} e não no {}!'.format(n, user))
