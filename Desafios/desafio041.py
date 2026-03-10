# A confederacao nacional de natacao precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER

from datetime import date
nasc = int(input('Qual o ano de nascimento do atleta: '))
atual = date.today().year
idade = atual-nasc
if idade <= 9:
    print('O(A) atleta tem {} anos e está na categoria MIRIM.'.format(idade))
elif idade <= 14:
    print('O(A) atleta tem {} anos e está na categoria INFANTIL.'.format(idade))
elif idade <= 19:
    print('O(A) atleta tem {} anos e está na categoria JUNIOR.'.format(idade))
elif idade <= 25:
    print('O(A) atleta tem {} anos e está na categoria SÊNIOR.'.format(idade))
else:
    print('O(A) atleta tem {} anos e está na categoria MASTER.'.format(idade))

