# Cores no terminal
# Jeito 1
r1 = 5
r2 = 6
print('Os valores \033[32m{}\033[m e \033[36m{}\033[m.'.format(r1, r2))

# Jeito 2
nome = 'Vanessa'
print('Olá Muito prazer em te conhecer, {}{}{}!!'.format('\033[4;34m', nome, '\033[m'))

# Jeito 3
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer, {}{}{}!!!!'.format(cores['amarelo'], nome, cores['limpa']))
