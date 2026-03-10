# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. Se o
# valor digitado for impar, desconsidere-o
soma = 0
for c in range (1,7):
    num = int(input('Digite o {}º número: '.format(c)))          # usuario coloca os numeros
    if num%2 == 0:
        soma += num
print('A soma dos números pares dessa sequência é de {}.'.format(soma))
