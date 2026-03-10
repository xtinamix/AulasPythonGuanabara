# Crie um programa que leia uma frase qualquer e diga se ela e um palindromo, desconsiderando os espacos
# Palindromo: frase ou palavra que se pode ler, indiferentemente, da esquerda para a direita ou vice-versa.
frase = str(input('Digite uma palavra ou frase: ')).strip()
aux = frase.lower().replace(' ', '')
inverso = aux[::-1]
if aux == inverso:
    print('A frase "{}" É UM PALINDROMO.'.format(frase))
else:
    print('A frase "{}" NÃO é um PALINDROMO.'.format(frase))
print(inverso)
