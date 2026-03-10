# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preco normal e condico de
# pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartao: 5% de desconto
# - Em até 2x no cartão: preco normal
# - Em 3x ou mais no cartao: 20% de juros

produto = float(input('Qual o valor do produto? '))
print('''Qual a forma de pagamento: 
[1] À vista no dinheiro/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] Em 3x ou mais no cartão''')
opcao = int(input(''))
if opcao == 1:
    print('O valor final do seu produto é de R${:.2f}.'.format(produto*0.9))
elif opcao == 2:
    print('O valor final do seu produto é de R${:.2f}.'.format(produto*0.95))
elif opcao == 3:
    print('O valor do seu produto é de R${:.2f}.'.format(produto))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    print('Sua compra será parcelada em {}x de R${:.2f}.'.format(parcelas,produto*1.2/parcelas))
    print('O valor final do seu produto é de R${:.2f}.'.format(produto*1.2))
else:
    print('Não existe essa opção.')