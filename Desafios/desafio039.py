# Faca um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar.
# Se é a hora de se alistar.
# Se já passou do tempo do alistamento.
# Seu programa também devera mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input('Qual o seu ano de nascimento: '))
atual = date.today().year
idade = atual-ano
print('Quem nasceu em {} tem {} ano(s) em {}.'.format(ano, idade, atual))
if atual-ano < 18:
    print('Você ainda tem {} ano(s) para realizar seu alistamento.'.format(18-idade))
    print('Seu alistamento será em {}.'.format(atual+18-idade))
elif atual-ano == 18:
    print('Você precisa se alistar IMEDIATAMENTE.')
else:
    print('Faz {} ano(s) que você já se alistou ou deveria ter se alistado.'.format(atual-ano-18))
    print('Seu alistamento foi em {}.'.format(atual-idade+18))
