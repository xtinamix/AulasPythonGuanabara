# Desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final, mostre os 10
# primeiros termos dessa progressao.
print('Vamos fazer uma sequência!')
a1 = float(input('Digite o primeiro termo da sequência: '))
r = float(input('Qual é a razão dessa sequência: '))
for c in range (0, 10):
    print('{:.1f} '.format(a1+(c*r)), end='-> ')
print('ACABOU')
