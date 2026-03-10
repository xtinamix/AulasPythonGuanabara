# Listas
lanches = ['hamburguer', 'suco', 'pizza', 'sorvete']

# Para add um elemento usa-se a funcao .append
lanches.append('cachorro quente')           # add no final da lista o item
lanches.insert(2,'macarronada')            # add na posicao 2
print(lanches)
# del lanches[-1]                           # deleta o ultimo item da lista
a = lanches.pop(3)                          # funcao pop remove da lista e diz qual era

# funcao lanches.remove apenas exclui o valor do item
lanches.remove('suco')
print(lanches)

# valores = list(range(4,11))             # cria uma lista q varia de 4 a 10
valores = [8,2,5,4,9,3,0]
# valores.sort()                            # organiza em ordem crescente
valores.sort(reverse=True)                  # organiza em ordem descrescente
print(valores)
