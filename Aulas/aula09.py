# Manipulando Cadeias de Textos/Caracteres
frase = 'Curso em Vídeo Python'

# Fatiamento - conseguir pegar pedaços de uma string

print('{}'.format(frase[9]))
print('{}'.format(frase[9:13]))
print('{}'.format(frase[9:21:2]))       # mostra do 9 ao 20 pulando de 2 em 2
print('{}'.format(frase[:5]))           # começa do 0 ao 5 caractere

# Análise
len(frase)      #comprimento da frase
frase.count('o')        # conta quantas 'o' tem na frase
frase.count('o', 0, 13)     # conta quantos o tem do 0 ao 12
frase.find('deo')           # quantas vezes 'deo' apareceu e mostra quando começou
'Curso'in frase              # existe curso em frase

# Transformação
frase.replace('Python', 'Android')
frase.upper()           # coloca toda a frase em maiúscula
frase.lower()           # coloca tudo em minúsculo
frase.capitalize()      # Coloca só o primeiro caractere da frase em maiuscula
frase.title()           # Coloca em maiuscula toda 1 letra da palavra
frase.strip()           # remove todos os espaços inuteis do começo e final da string
frase.rstrip()          # tira só os espaços do lado direito (final)
frase.lstrip()          # remove os espaços da esquerda (começo)

# Divisão
frase.split()           # ocorre divisão considerando os espaços e gera uma lista com os pedaços

# Junçao
'-'.join(frase)         # junta as strings e separa por '-'
