# Crie um programa que leia o nome e o preco de varios produtos. O programa devera perguntar se o usuario vai
# continuar. No final, mostre:
# A) Qual e o total gasto na compra
# B) Quantos produtos custam mais de R$ 1000,00
# C) Qual e o nome do produto mais barato
print('-'*40)
print(' '*8, 'CADASTRO DE PRODUTO')
print('-'*40)
total = caro = barato = count = vmaisbarato= 0
nmaisbarato = 'a'
while True:
    nome = str(input('Nome do Produto: ')).strip().capitalize()
    while True:
        try:
            preco = float(input('Preço do Produto: R$ '))
        except ValueError:
            continue
        else:
            break
    if count == 0:
        vmaisbarato = preco
        nmaisbarato = nome
    if vmaisbarato > preco:
        vmaisbarato = preco
        nmaisbarato = nome
    if preco > 1000:
        caro += 1
    total += preco
    count += 1
    while True:
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
        if continuar in 'SsNn':
            break
    if continuar == 'N':
        break
    print('-' * 40)
print('-' * 40)
print(f'Você comprou {count} produtos e o total é {total:.2f}.')
print(f'Você tem {caro} produtos que custam mais de R$1000,00.')
print(f'O produto mais barato é o/a {nmaisbarato} e custou R$ {vmaisbarato:.2f}.')

