# Crie um programa que leia varios numeros inteiros pelo teclado. No final da execucao, mostre a media entre todos
# os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuario se ele quer ou nao
# continuar a digitar valores.
n = soma = cont = maior = 0
opcao = 'a'
while opcao not in 'Nn':
    n = int(input('Escolha um número: '))
    if cont == 0:
        menor = n
    soma += n
    opcao = input('Deseja continuar? [S/N] ').strip()[0]
    cont += 1
    if maior < n:
        maior = n
    elif menor > n:
        menor = n
media = soma/cont
print('Você digitou {} números, a média deles é {:.2f}, o menor valor é {} e o maior {}.'.format(cont, media, menor, maior))
