# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Qual o nome da sua cidade: ')).strip()
print(cidade[:5].lower() == 'santo')
