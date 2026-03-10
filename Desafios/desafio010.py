# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Sólares ela pode comprar.
# Considere US$ 1,00 = R$ 3,27
dolar = 3.27
n = float(input('Digite o quanto de dinheiro você tem: '))
print('Você pode comprar US$ {:.3f}.'.format(n/dolar))