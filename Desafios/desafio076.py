# Crie um programa que tenha um tupla unica com nomes de produtos e seus respectivos precos, na sequencia.
# No final, mostre uma listagem de precos, organizando os dados em forma tabular.
produtos = ('Alho', 6.90, 'Margarina', 3.49, 'Batata', 1.68, 'Pimentão', 2.38, 'Cenoura', 1.98,
            'Papel Higiênico', 2.59, 'Mamão', 1.18, 'Laranja', 3.75, 'Tomate', 6.98, 'Banana', 6.38,
            'Queijo', 18.48, 'Presunto', 9.90, 'Abacaxi', 5.79, 'Cebola', 3.99)
print('-'*50)
print('LISTAGEM DE PREÇOS'.center(45))
print('-'*50)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<40}', end='')
    else:
        print(f'R$ {produtos[pos]:>7.2f}')