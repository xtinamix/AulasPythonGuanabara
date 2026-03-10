# Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar
# o valor 999, que e a condicao de parada. No final, mostre quanto numeros foram digitados e qual foi a soma entre eles
# desconsiderando o flag)
n = count = soma = 0               # n sao os numeros e coun o contador
while n != 999:
    n = int(input('Digite um numero inteiro qualquer OU 999, caso queira parar: '))
    if n != 999:
        soma += n
        count += 1
print('Você escolheu {} e a soma deles é {}.'.format(count, soma))
