# Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com
# a tabela abaixo:
# - Abaixo de 18.5: Abaixo do peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input('Qual o seu peso, em kg? '))
altura = float(input('Qual a sua altura, em metros? '))
imc = peso/(altura**2)
if imc <= 18.5:
    print('Seu IMC é {:.2f} e você está abaixo do peso.'.format(imc))
elif 18.5 <= imc <= 25:
    print('Seu IMC é de {:.2f} e você está no peso ideal.'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é de {:.2f} e você está com sobrepeso.'.format(imc))
elif 30 <= imc <= 40:
    print('Seu IMC é de {:.2f} e você está obeso.'.format(imc))
else:
    print('Seu IMC é de {:.2f} e você está com obesidade mórbida.'.format(imc))
