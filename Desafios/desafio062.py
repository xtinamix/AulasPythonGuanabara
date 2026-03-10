# Melhore o desadio 061, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra
# quando ele disser que quer mostrar 0 termos.
a1 = float(input('Digite o primeiro termo da sequência: '))
r = float(input('Qual a razão dessa sequência? '))
i = 0           # auxiliar
opcao = 1
termo = a1      # valor do termo
n = 10          # quantidade de termos
while opcao != 0:
    print('{:.1f}'.format(termo), end = '  ')
    termo += r
    i += 1
    if (i == n):
        opcao = int(input('\nDeseja mostrar mais quantos termos? (Se quiser parar, digite 0) '))
        n = n + opcao
print('Vc calculou {} termos dessa sequência.'.format(i))
print('--- FIM ---')