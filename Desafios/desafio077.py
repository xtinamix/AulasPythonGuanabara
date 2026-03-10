# Crie um programa que tenha uma tupla com varias palavras (nao usar acentos). Depois disso, para cada palavra,
# quais sao as suas vogais.
palavras = ('thth', 'amor', 'valor', 'cheque', 'impressora', 'computador', 'prego', 'Caderno', 'Monitor', 'Carimbo',
            'Remédio', 'Grampeador', 'Clipe', 'Pilha', 'Ovo')
for i in palavras:
    print(f'Na palavra {i.upper()} temos ', end='')
    for letra in i:
        if letra.lower() in "aeiou":
            print(f'{letra.lower()} ', end= '')
    print('.')