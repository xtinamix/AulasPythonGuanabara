# Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada, o programa devera perguntar
# se o usuario quer ou nao continuar. No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens foram cadastrados.
# C) Quantas mulheres tem menos de 20 anos.
count = maior = homem = mulher = 0
sexo = idade = continuar = 'a'
while True:
    print('-'*40)
    print(' '*7,'CADASTRO DE PESSOAS')
    print('-'*40)
    while True:                 # idade é um inteiro
        try:
            idade = int(input('IDADE: '))
        except ValueError:
            continue
        else:
            break
    if idade >= 18:
        maior += 1

    sexo = ' '
    while sexo not in 'FM':                 # validacao sexo F ou M
        sexo = str(input('Sexo [F/M]: ')).strip().upper()[0]
    if sexo == 'M':
        homem += 1
    elif idade > 20:
        mulher += 1
    print('-'*40)

    continuar = ' '
    while continuar not in 'SN':                 # validacao continuar ou nao
        continuar = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
    count += 1
    if continuar == 'N':
        break
print(f'Foram cadastradas {count} pessoas.\nDessas, {maior} possuem mais de 18 anos.'
      f' {homem} são homens e {mulher} são mulheres com mais de 20 anos.')
