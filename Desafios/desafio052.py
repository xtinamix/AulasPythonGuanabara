# Faca um programa que leia um numero inteiro e diga se ele é ou não um numero primo
n = int(input('Digite um número: '))
divisor = 0
for c in range (1, n+1):
    if n%c == 0:
        divisor += 1
if divisor == 2:
    print('O número {} É primo.'.format(n))
else:
    print('O número {} NÃO é primo.'.format(n))
print(divisor)