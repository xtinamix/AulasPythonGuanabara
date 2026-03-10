# Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, cobrando
# R$ 0,50 por km para viagens de até 200 km e R$ 0,45 para viagens mais longas.
dist = float(input('Qual a distância da viagem? '))
if dist <= 200:
    passagem = 0.5*dist
else:
    passagem = 0.45*dist
print('O valor da passagem é de R${:.2f} reais.'.format(passagem))