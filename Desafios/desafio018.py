# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import cos, sin, tan, pi
n = float(input('Digite um ângulo: '))
print('O ângulo digitado foi {} e seu seno é {:.2f}, cosseno é {:.2f} e tangente {:.2f}.'.format(n, sin(n*pi/180), cos(n*pi/180), tan(n*pi/180)))
