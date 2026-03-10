# Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira
from math import trunc
n = float(input('Digite um número real qualquer: '))
print ('A parte inteira dele é {}.'.format(trunc(n)))
