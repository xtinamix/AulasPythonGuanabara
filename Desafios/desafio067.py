# Faca um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario.
# O programa sera interrompido quando o numero solicitado for negativo.
while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    count = 0
    print('-'*41)
    if n < 0:
        break
    while count <=10:
        produto = n * count
        print(f'{n} x {count} = {produto}')
        count += 1
    print('-'*40)
print('-'*18, 'FIM', '-'*18)