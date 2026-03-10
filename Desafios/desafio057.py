# Faca um programa que leia o sexo de uma pessoa, ma so aceite os valores 'M' ou 'F'. Caso esteja errado, peca a
# digitacao novamente ate ter um valor correto
sexo = str(input('Qual o seu sexo? [F/M] ')).strip()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados inválidos. Por favor, digite F ou M: ')).strip()[0]
print('Obrigado!')