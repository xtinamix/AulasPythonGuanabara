# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
# mostre o comprimento da hipotenusa
from math import sqrt, pow, hypot
a = float(input('Digite o comprimento do cateto oposto: '))
b = float(input('Digite o comprimento do cateto adjacente: '))
# c = math.sqrt(math.pow(a, 2) + math.pow(b,2))
print('O comprimento da hipotenusa é: {:.2f}.'.format(hypot(a,b)))
