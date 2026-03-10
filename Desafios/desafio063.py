# Escreva um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros elementos de uma
# sequencia de fibonacci (o numero seguinte é a soma dos dois anteriores)
# Ex: 0 1 1 2 3 5 8
n = int(input('Quantos elementos quer na sua sequência? '))     # qtde de termos da seq.
aux = 0
while aux < n:
    if aux == 0:
        termo = 0
        a1 = 0
        a2 = 1
        print(termo, end = ' ')
    else:
        termo = a1 + a2
        print(termo, end = ' ')
        a2 = a1
        a1 = termo
    aux += 1
