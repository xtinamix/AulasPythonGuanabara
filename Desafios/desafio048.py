# Faca um programa que calcule a soma entre todos os numeros impares que sao multiplos de tres e que se encontram n
# no intervalo de 1 ate 500
soma = 0
cont = 0
for c in range (1, 501, 2):
    if c%3 == 0:
        soma += c
        cont +=1
print('O somatórios dos {} números ímpares de 1 a 500 que são multiplos de 3 é: {}.'.format(cont, soma))
