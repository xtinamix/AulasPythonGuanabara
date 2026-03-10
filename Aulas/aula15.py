# comando break
s = n =  0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s =+ n
# print('A soma vale {}.'.format(s))
print(f'A soma vale {s}.')
s = 987.9
print(f'O salário é R$ {s:.2f}')

while True:     # validando numero inteiro
    try:
        n = int(input("Escolha um número: "))
        break
    except ValueError:
        n = int(input("Escolha um número1: "))