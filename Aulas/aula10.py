# Condições
# métodos possuem () no final
#

#tempo = int(input('Quantos anos tem seu carro? '))
#if tempo<=3:
#    print('Carro Novo')
#else:
#    print('Carro Velho')
#print('--FIM--')

#tempo = int(input('Quantos anos tem seu carro?'))
#print('Carro Novo' if tempo<=3 else 'Carro Velho')
#print('--FIM--')

#nome = str(input('Qual é seu nome? '))
#if nome == 'Gustavo':
#    print('Que nome lindo você tem!')
#print('Bom dia, {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6:
    print('Sua média foi boa! PARABÈNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
