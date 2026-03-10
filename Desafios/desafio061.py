# Refaca o desafio 51, lendo o primeiro termo de uma PA, mostrando os 10 primeiros termos da progressao usando a
# estrutura while
# leia o primeiro termo e a razao de uma PA e mostre os 10 primeiros termos
a1 = float(input('Digite o primeiro termo da sequência: '))
r = float(input('Qual a razão dessa sequência? '))
i = 0
termo = a1
while i < 10:
    print('{:.1f}'.format(termo), end = '  ')
    termo += r
    i += 1
print('Fim')