# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar
# o valor da casa, o salario do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestacao mensal, sabendo que ela nao pode exceder 30% do salario ou entao o emprestimo sera negado

casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
tempo = 12*int(input('Em quantos anos você quer pagar? '))
if casa/tempo < 0.3*salario:
    print('\033[1;34mPARABÉNS\033[m, empréstimo aprovado e a prestação é de R${:.2f} mensais.'.format(casa/tempo))
else:
    print('Infelizmente o seu pedido foi \033[31mNEGADO\033[m.')
