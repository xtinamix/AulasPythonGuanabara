# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa devera ler um numero pelo teclado (entre 0 e 200) e mostra-lo por extenso.
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Ttente novamente. ', end= '')
    print(f'O número digitado foi o {numeros[n]}.')
    continuar = str(input('Vc quer continuar? [S/N]: ')).strip()[0]
    if (continuar in 'Nn'):
        break