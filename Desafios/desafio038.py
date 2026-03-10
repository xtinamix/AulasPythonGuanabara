# Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não ediste valor maior, os dois são iguais
n1 = int(input('Insira o primeiro valor: '))
n2 = int(input('Insira o segundo valor: '))
if n1 > n2:
    print('O PRRIMEIRO valor {} é o maior.'.format(n1))
elif n2 > n1:
    print('O SEGUNDO valor {} é o maior.'.format(n2))
else:
    print('Não existe valor maior, os dois são IGUAIS.')
