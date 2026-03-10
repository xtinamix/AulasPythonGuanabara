# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A media de idade do grupo
# - Qual é o nome do homem mais velho
# - Quantas mulheres têm menos de 20 anos
soma = 0
mulheres = 0
media = 0
mais_velho_idade = ''
for c in range (1, 5):
    print('--- {} PESSOA ---'.format(c))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip().lower()
    soma += idade
    media = soma/c
    if c == 1:
        mais_velho_nome = nome
        mais_velho_idade = idade
    else:
        if idade >= mais_velho_idade and sexo == 'm':
            mais_velho_nome = nome
            idade_velho = idade
        elif sexo == 'f' and idade < 20:
            mulheres +=1
print('''A média de idade do grupo é {} anos.
O homem mais velho é {} com {} anos.
Há {} mulher(es) com menos de 20 anos.'''.format(media, mais_velho_nome, idade_velho, mulheres))