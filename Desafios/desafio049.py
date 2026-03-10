# Refaca o desafio 9, mostrando a tabuada de um numero que o usuario escolher, so que agora utilizando um laco for
n = int(input('Qual tabuada você quer saber: '))
for c in range (0, 11):
    print('{} x {} = {}'.format(n, c, n*c))
print('----FIM----')