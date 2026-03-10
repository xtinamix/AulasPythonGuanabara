# Crie um programa que leia varios numeros interiros pelo teclado. O programa so vai parar quando o usuario digitar
# o valor 999, que e a condicao de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles
# (desconsiderar a flag)
soma = cont = 0
while True:
    n = int(input(f'Digite o {cont+1}º número: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'A soma dos {cont} números inseridos é {soma}.')