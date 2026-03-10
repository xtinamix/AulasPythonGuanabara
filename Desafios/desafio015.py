# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugaodo. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado

km = float(input('Quantos Km foram percorridos com o carro: '))
dias = int(input('Quantos dias foram alugados: '))
print('O total a ser pago pelo carro será de R$ {:.2f}.'.format(60*dias+0.15*km))
