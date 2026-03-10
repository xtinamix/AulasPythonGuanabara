# Desenvolva um programa que leia o compimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
r1 = float(input('\033[1;30;45m Qual o tamanho da primeira reta: \033[m'))
r2 = float(input('Qual o tamanho da segunda reta: '))
r3 = float(input('Qual o tamanho da terceira reta: '))
if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print('As medidas PODEM formar um triângulo.')
else:
    print('As medidas NÃO PODEM formar um triângulo.')

print('Os valores \033[32m{}\033[m e \033[36m{}\033[m.'.format(r1, r2))