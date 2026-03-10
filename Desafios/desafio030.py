# Crie um progra que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('Me diga um número qualquer: '))
if n%2 == 0:
    print('{} número é par.'.format(n))
else:
    print('{} número é ímpar.'.format(n))