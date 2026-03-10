# Faca um programa que leia um numero qualquer e mostre o seu fatorial
# Ex: 5! = 5x4x3x2x1 = 120
n = int(input('Qual número vc quer saber o fatorial? '))
fat = 1
aux = n
print('O fatorial de {}! é: {}'.format(n, n), end = '')
while 1 < aux:
    fat *= aux
    aux -= 1
    print('x{}'.format(aux), end = '')
print('= {}.'.format(fat))