# Faça um programa que leia 5 valores numericos e guarde-os em uma lista. No final, mostre qual foi o maior
# e o menor valor digitado e suas respectivas posicoes na lista.
num = []
pos_maior = pos_menor = 0
for i in range(0,5):
    num.append(input(f'Digite o número da posição {i}: '))
print(f'O maior valor digitado foi {max(num)} na posição {num.index(max(num))}.')
print(num)