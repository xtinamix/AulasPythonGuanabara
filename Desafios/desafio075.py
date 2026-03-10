# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9
# B) Em que posicao foi digitado o primeiro valor 3
# C) Quais foram os numeros pares.
import numpy
n = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite um outro número: ')),
     int(input('Digite um último número: ')))
par = []
count = i = 0
pos = -1
for i in range(0, 4):
    if n[i]%2 == 0:
        par.append(n[i])
    i += 1
print(f'O valor 9 aparece {n.count(9)} vezes.')
if 3 in n:
    print(f'O valor 3 apareceu pela primeira vez na {n.index(3)+1}ª posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')
print(f'Os valores pares foram: {par}')