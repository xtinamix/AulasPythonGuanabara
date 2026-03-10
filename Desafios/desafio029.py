# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80 km/h mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada Km acima do limite.
vel = float(input('Qual a velocidade do carro: '))
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print('Você foi multado em: R$ {:.2f} reais.'.format((vel - 80)*7))
print('Você está dentro da velocidade permitida!')