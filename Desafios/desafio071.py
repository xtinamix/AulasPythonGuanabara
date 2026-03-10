# Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao usuario qual sera
# o valor a ser sacado (numero inteiro) e o programa vai informar quantas celulas de cada valor serao entregues.
# Obs: Considere que o caixa possui celulas de R$ 50, R$ 20, R$ 10 e R$ 1.
print('='*40)
print('{:^30}'.format('BEM VINDO AO BANCO TT'))        # comando {:^30} linha de 30 caracteres e centralizado ^
print('='*40)
while True:
    try:
        saque = int(input('Que valor você quer sacar: R$ '))
    except ValueError:
        continue
    else:
        break
total = saque
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}.')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print(f'Volte sempre! Tenha um bom dia!')