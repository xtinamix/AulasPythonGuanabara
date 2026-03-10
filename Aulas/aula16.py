# Aula Tuplas
# ()tuplas []listas {}Dicionarios
lanche = ('Hambúguer', 'Suco', 'Pizza', 'Pudim')

for comida in lanche:
    print(f'Eu vou comer {comida}')

for cont in range(0, len(lanche)):
    print(lanche[cont])

for pos, comida in enumerate(lanche):           # mostra tanto o dado quanto a posição
    print(f'Eu vou comer {comida} na posição {pos}')

print(f'Comi pra caramba!')

print(sorted(lanche))           # mostra em ordem