# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeio e o último nome
# separadamente
nome = str(input('Qual o seu nome completo: ')).strip()
divide = nome.split()
print('O primeiro nome é: {}.\nO último nome é: {}.'.format(divide[0].capitalize(), divide[-1].capitalize()))
