# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram
# a maioridade e quantas já são maiores.
from datetime import date
maiores = 0
menores = 0
atual = date.today().year
for c in range (0, 7):
    anos = int(input('Em que ano a {} pessoa nasceu: '.format(c+1)))
    if atual-anos < 18:
        menores += 1
    else:
        maiores += 1
print('Nesse grupo há {} maiores de idade e {} menores.'.format(maiores, menores))
