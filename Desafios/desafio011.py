# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2.

l = float(input('Qual a largura da parede, em metros: '))
h = float(input('Qual a altura da parede, em metros: '))
print('Para pintar essa parede é necessário {:.2f} litros de tinta.'.format((l*h)/2))
