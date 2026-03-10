# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem
# de colocacao. Depois mostre:
# A) Apenas os 5 primeiros colocados.
# B) Os ultimos 4 colocados da tabela.
# C) Uma lista com os times em ordem alfabetica.
# D) Em que posicao na tabela esta o time da Chapecoense
times = ('Fortaleza', 'Athletico-PR', 'Flamengo', 'Atlético-GO', 'Atlético-MG', 'Bragantino', 'Fluminense', 'Bahia',
         'Palmeiras', 'Corinthians', 'Ceará SC', 'Santos', 'Internacional', 'Juventude', 'Cuiabá', 'Sport Recife',
         'São Paulo', 'Chapecoense', 'Grêmio', 'América-MG')
print(f'Os primeiros colocados são: {times[:5]}')
print(f'Os últimos colocados são: {times[-4:]}')
print(f'Os times em ordem alfabética fica: {sorted(times)}')
x = times.index('Chapecoense', 0)
print(f'A chapecoence encontra-se na {times.index("Chapecoense", 0)+1}ª posição.')
