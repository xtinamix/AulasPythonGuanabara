# Faca um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
for c in range (0, 5):
    peso = float(input('Qual o seu peso, em kg? '))
    if c == 0:          # adicionar uma referência para o menor valor
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O menor peso é {} kg e o maior é {} kg.'.format(menor, maior))