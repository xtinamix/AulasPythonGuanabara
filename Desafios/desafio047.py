# Crie um programa que mostre na tela todos os numeros pares que estáo no intervalo entre 1 e 50.
print('Os números pares de 1 a 50 são: ')
for c in range (2, 51, 2):
        print('{} '.format(c), end = '')
print('\n','--' *10, 'FIM', '--'*10)