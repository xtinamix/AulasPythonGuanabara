# Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla. Depois disso, mostre a listagem
# de numeros gerados e tambem indique o menor e o maior valor que estao na tupla
import numpy as np
import random
n = np.random.randint(0, 101, size = 5)
print(f'Os valores sorteados foram: ', end = '')
for c in range(0, len(n)):
    print(n[c], end = '  ')
print(f'\nO menor número é o {min(n)} e o maior é o {max(n)}.')
