# Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo sera formado:

r1 = float(input('Qual o tamanho da primeira reta: '))  # primeira reta
r2 = float(input('Qual o tamanho da segunda reta: '))           # segunda reta
r3 = float(input('Qual o tamanho da terceira reta: '))             # terceira reta
if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):        # condicao de existencia de triangulos
    print('As medidas PODEM formar um triângulo ', end = '')    #  end = '' impede q pule linha
    if r1 == r2 and r2 == r3:
        print('EQUILÁTERO.')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO.')
    else:
        print('ISÓSCELES.')
else:
    print('As medidas NÃO PODEM formar um triângulo.')
