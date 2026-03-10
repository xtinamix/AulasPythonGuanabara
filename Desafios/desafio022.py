# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas e minusculas
# Quantas letras ao todo (sem espaços)
# Quantas letras tem o primeiro nome

nome = input('Digite o seu nome completo: ').strip()        # strip retira os espaços do começo e fim
divide = nome.split()
print('O seu nome em letras maiúsculas é: {}'.format(nome.upper()))
print('O seu nome em letras minúsculas é: {}'.format(nome.lower()))
print('O seu nome possui {} letras.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome é {} e ele tem {} letras.'.format(divide[0], len(divide[0])))