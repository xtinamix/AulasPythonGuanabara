# Faça um programa q leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele
n = input('Digite algo: ')
limpa = '\033[m'
print('\033[0;30mO tipo primitivo desse valor é: {}'.format(limpa), type(n))
print('\033[1;32;44mSó tem espaços? {}'.format(limpa), n.isspace())
print('É um número? ', n.isnumeric())
print('É alfabético? ', n.isalpha())
print('É alfanumérico? ', n.isalnum())
print('Está em maiúsculas? ', n.isupper())
print('Está em minúsculas? ', n.islower())
print('Está capitalizada? ', n.istitle())
